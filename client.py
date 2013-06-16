#!/usr/bin/python

import sys, getopt
from lib import notifications
import socket

host = socket.gethostname()
port = 1337

def main(argv):
	command = ''
	arguments = []

	try:
		opts, args = getopt.getopt(argv, "hc:a:")
	except getopt.GetOptError:
		help()

	for opt, arg in opts:
		if opt == "-h":
			help()
		elif opt == "-c":
			command = arg
		elif opt == "-a":
			arguments.append(arg);

	s = socket.socket()
	s.connect((host, port))
	s.send(command + '|' + '#'.join(arguments))
	message = s.recv(1024)
	notifications.notify("Brew time!", message)
	s.close()

def help():
	print 'Help goes here...';
	sys.exit(1)

if __name__ == '__main__':
	main(sys.argv[1:])
