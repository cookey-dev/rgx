# Kociemba TwoPhase API

from threading import Thread
from twophase import solver, start_server, client_gui, computer_vision

srv = Thread(target=start_server.start, args=(8080, 20, 2))
srv.start()
