# Create virtual environment for the NLP server and install the required dependencies.

pip3 install virtualenv
virtualenv bodi-nlp-server-venv
source bodi-nlp-server-venv/bin/activate
pip3 install -r requirements.txt

# Download the TabularSemanticParser package for the English -> SQL parsing.

git clone https://github.com/mgv99/TabularSemanticParsing
export PYTHONPATH=`pwd` && python -m nltk.downloader punkt

# Download the model checkpoint for the TabularSemanticParser (4GB size approx.)

mkdir TabularSemanticParsing/model
wget -c "https://drive.google.com/u/0/uc?id=1dlrUdGMLvvvfR3kNVy76H12rR7gr4DXI&export=download&confirm=t" -O TabularSemanticParsing/model/bridge-spider-bert-large-ems-70-1-exe-68-2.tar.gz
gzip -d TabularSemanticParsing/model/bridge-spider-bert-large-ems-70-1-exe-68-2.tar.gz
