#!/usr/bin/python

import sys, getopt
from lib import notifications
import socket

def main(argv):
	command = ''
	arguments = []

	try:
		opts, args = getopt.getopt(argv, "hc:a:n:p:")
	except getopt.GetOptError:
		help()

	host = None
	port = None
	for opt, arg in opts:
		if opt == "-h":
			help()
		elif opt == "-c":
			command = arg
		elif opt == "-a":
			arguments.append(arg);
		elif opt == "-n":
			host = arg
		elif opt == "-p":
			port = arg

	if host == None:
		host = socket.gethostname()
	if port == None:
		port = 1337

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
