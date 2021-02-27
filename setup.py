import os
os.system('python3 -m pip install --upgrade pip')
os.system('python3 -m pip install virtualenv')
os.system('python3 -m venv .env')
os.system('. .env/bin/activate; pip install --upgrade pip setuptools wheel')
os.system('. .env/bin/activate; pip install -r requirements.txt')