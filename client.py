import socket
import threading
import os
import sys
import textual
from textual import on, events
from textual.app import App, ComposeResult
from textual.widgets import Input, Log
from textual.containers import Container
from textual.screen import Screen

HOST = input("Enter the host you would like to connect to:\n")
PORT = int(input("Enter the port you would like to connect to:\n"))
ADDR = (HOST, PORT)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDR)

textual.CSS_PATH = os.path.join("./", "style.tcss")

class TextualUIapp(App):

    CSS_PATH = "style.tcss"

    def compose(self) -> ComposeResult:

        self.chat = Log(id="chat", classes="chats")
        self.user_input = Input(id="user", placeholder="Enter message here: If you want to quit, type '/quit'", validate_on="submitted", classes="user_a")

        yield Container(
            self.chat,
            self.user_input
        )

    def recieve(self):
        while True:
            try:
                chat_log = self.query_one("#chat", Log)
                data = client_socket.recv(1024)
                chat_log.write(f"{data.decode()}\n")

            except OSError:
                break

    @on(Input.Submitted, "#user")
    def message_submitted(self, event: Input.Submitted):
        if event.value:
            client_socket.send(event.value.encode())

        if event.value == "/quit":
            sys.exit()

        self.query_one("#user", Input).clear()

    def on_mount(self) -> None:
        self.recieve_thread = threading.Thread(target=self.recieve, daemon=True)
        self.recieve_thread.start()

if __name__  == "__main__":
    app = TextualUIapp()
    app.run()
    client_socket.close()