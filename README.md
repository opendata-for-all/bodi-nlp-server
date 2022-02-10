# bodi-nlp-server

This repository contains a server used in the [bodi-generator](https://github.com/opendata-for-all/bodi-generator)
project to answer questions not implemented in a chatbot. This is done by running NLP tools in the server that can be
accessed through server endpoints.

These are the current provided functionalities:

- **Text-to-table**: the input is a natural language query and the output is the provided tabular answer. This is done by
  [TabularSemanticParsing](https://github.com/mgv99/TabularSemanticParsing). Note that this language model translates
  English to SQL statements. So, when the input is not in English, a translation to English must be performed.
  Currently, supported languages are Spanish, Catalan and English.

### Deploy the server

Before deploying the server, you may want to edit some variables for your purpose.

#### run_server.sh

- **checkpoint_path**: the path to the model checkpoint
- **csv_dir**: the directory where the csv files (i.e. the database) are stored

#### flask_server.py

- **CONFIG_FILE_PATH**: the path to a .properties file that contains properties used within the server. These 
  properties 
  are:
  - **xls.importer.xls**: the name of the csv file used as a database
  - **csv.delimiter**: the delimiter or separator of the tabular data file cells (e.g. `,`, `\t` (tab))
  - **SERVER_URL**: the URL where the server is deployed
  - **TEXT_TO_TABLE_ENDPOINT**: the endpoint of the server used to make requests to query the database with natural 
    language sentences

```
./run_server.sh
```