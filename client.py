#!/usr/bin/python

import sys, getopt, json
from lib import notifications
import socket

def main(argv):
	command = ''
	arguments = []

	try:
		opts, args = getopt.getopt(argv, "hc:a:n:p:")
	except getopt.GetoptError:
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
	s.send(json.dumps({'command': command, 'args': arguments}))
	message = s.recv(1024)
	notifications.notify("Brew time!", message)
	s.close()

def help():
	print 'Usage:'
	print '\tpython client.py [-h] [-n hostname] [-p port] -c command -a arg1'
	print ''
	print 'Arguments:'
	print '\t-h\tDisplays this screen'
	print '\t-n\tSets the hostname to connect to'
	print '\t-p\tSets the port to connect to'
	print '\t-c\tThe command to use, can be: \'add\', \'vote\' or \'reset\''
	print '\t-a\tAn arbitrary amount of arguments (usually just 1 required) used for the command given'
	sys.exit(1)

if __name__ == '__main__':
	main(sys.argv[1:])
