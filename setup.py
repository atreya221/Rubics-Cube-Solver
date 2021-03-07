import os
import platform
if platform.system() == 'Linux':
  os.system('sudo apt-get install python3-venv')
  os.system('python3 -m pip install --upgrade pip')
  os.system('python3 -m pip install virtualenv')
  os.system('python3 -m venv .env')
  os.system('. .env/bin/activate; pip install --upgrade pip setuptools wheel')
  os.system('. .env/bin/activate; pip install -r requirements.txt')

if platform.system() == 'Windows':
  os.system('python -m pip install --upgrade pip')
  os.system('python -m pip install virtualenv')
  os.system('python -m venv .env')
  os.system('.\.env\Scripts\\activate & pip install --upgrade setuptools wheel')
  os.system('.\.env\Scripts\\activate & pip install -r requirements.txt')