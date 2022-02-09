"""
This is a Flask server that provides an endpoint to query a csv file with
natural language questions.
"""

from flask import Flask, request
from io import StringIO
import configparser

import text_to_table
import ca_es_to_en

ROOT_SECTION = 'root'
CONFIG_FILE_PATH = '../Bot/src/main/resources/bot.properties'


def loadConfig():
    ini_str = '[' + ROOT_SECTION + ']\n' + open(CONFIG_FILE_PATH, 'r').read()
    ini_fp = StringIO(ini_str)
    config = configparser.RawConfigParser()
    config.read_file(ini_fp)
    return config


config = loadConfig()
app = Flask(__name__)
app.config['SERVER_NAME'] = config.get(ROOT_SECTION, 'SERVER_URL')
text_to_table.setup(config.get(ROOT_SECTION, 'xls.importer.xls')[:-4], config.get(ROOT_SECTION, 'csv.delimiter').encode().decode('unicode_escape'))
ca_es_to_en.setup()


@app.route('/' + config.get(ROOT_SECTION, 'TEXT_TO_TABLE_ENDPOINT'), methods=['POST'])
def text_to_table_endpoint():
    body = request.get_json()
    return text_to_table.getTable(body)


if __name__ == '__main__':
    app.run(debug=False)
