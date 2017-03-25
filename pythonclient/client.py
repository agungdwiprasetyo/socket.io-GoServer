#!/usr/bin/env python3
from socketIO_client import SocketIO, LoggingNamespace

import numpy as np
from random import uniform

socketIO = SocketIO("http://localhost", 1993, LoggingNamespace)

def getData(*args):
	print(args[0])

if __name__ == '__main__':
	print ("Listening server...")
	socketIO.on('chat message', getData)
	socketIO.wait()
