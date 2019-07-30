import os


home_dir = os.getcwd()
# os.system('pip install virtualenv')
os.system('virtualenv -p python3 venv')
# os.system('source venv/bin/activate')
with open('requirements.txt', 'r') as requirements:
    for requirement in requirements:
        os.system('pip install --target=venv/lib/python3.7/site-packages {}'.format(requirement))


# requirements = ['requests', 're', 'urllib3', ]
# home_dir = os.getcwd()
# pip3 install -r requirements.txt