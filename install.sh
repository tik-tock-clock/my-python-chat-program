python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install textual pyinstaller

pyinstaller -F --add-data="style.tcss:./" client.py
deactivate

mv ./dist/client ./sudo apt install -f