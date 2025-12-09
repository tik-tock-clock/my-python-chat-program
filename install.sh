mkdir chat-program-client
cd chat-program-client

git clone https://github.com/tik-tock-clock/my-python-chat-program.git git-repo
cd git-repo
python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install textual pyinstaller

pyinstaller -F --add-data="style.tcss:./"
deactivate

cd ..
mv ./git-repo/dist/client ./
mv ./git-repo/style.tcss ./