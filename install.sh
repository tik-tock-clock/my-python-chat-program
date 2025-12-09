python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install textual pyinstaller

pyinstaller -F --add-data="style.tcss:./"
deactivate

mv ./dist/client ./