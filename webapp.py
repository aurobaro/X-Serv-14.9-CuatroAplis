#!/usr/bin/python -tt
# -*- coding: UTF-8 -*-

import sys
import socket


class app:
	def parse(self, request, port):

		method = request.split()[0]
		resource = request.split()[1]
		parsedRequest = (method,resource)
		return parsedRequest

	def process(self, parsedRequest):

		return ("200 OK", "<html><body><h1>""webApp""<p></body></html>")


class webApp:
    """Root of a hierarchy of classes implementing web applications

    This class does almost nothing. Usually, new classes will
    inherit from it, and by redefining "parse" and "process" methods
    will implement the logic of a web application in particular.
    """

    def select(self, request):
        """Selects the application (in the app hierarchy) to run.

        Having into account the prefix of the resource obtained
        in the request, return the class in the app hierarchy to be
        invoked. If prefix is not found, return app class
        """

        resource = request.split(' ', 2)[1]
        for prefix in self.apps.keys():
            if resource.startswith(prefix):
                print "Running app for prefix: " + prefix + \
                    ", rest of resource: " + resource[len(prefix):] + "."
                return (self.apps[prefix], resource[len(prefix):])
        print "Running default app"
        return (self.myApp, resource)

    def __init__(self, hostname, port, apps):
        """Initialize the web application."""

        self.apps = apps
        self.myApp = app()

        # Create a TCP objet socket and bind it to a port
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mySocket.bind((hostname, port))

        # Queue a maximum of 5 TCP connection requests
        mySocket.listen(5)

        # Accept connections, read incoming data, and call
        # parse and process methods (in a loop)

        while True:
            print 'Waiting for connections'
            (recvSocket, address) = mySocket.accept()
            print 'HTTP request received (going to parse and process):'
            request = recvSocket.recv(2048)
            print request
            (theApp, rest) = self.select(request)
            parsedRequest = theApp.parse(request, rest)
            (returnCode, htmlAnswer) = theApp.process(parsedRequest)
            print 'Answering back...'
            recvSocket.send("HTTP/1.1 " + returnCode + " \r\n\r\n"
                            + htmlAnswer + "\r\n")
            recvSocket.close()

if __name__ == "__main__":
	hola = app()
	adios = app()
	aleat = app()
	suma = app()
	testWebApp = webApp("localhost", 1234, {'/hola': hola,
                                            '/adios': adios,
											'/aleat/': aleat,
											'/suma/': suma})


'''class webApp:

	def parse(self, request):

		method = request.split()[0]
		resource = request.split()[1]
		parsedRequest = (method,resource)
		return parsedRequest

	def process(self, parsedRequest):

		return ("200 OK", "<html><body><h1>""webApp""<p></body></html>")

	def select(self, request):
		for prefix in self.apps:
			if resource.startswith (prefix):
				print "En funcionamiento la aplicacion con prefijo: " + prefix + \
                    ", resto de recurso: " + resource[len(prefix):]
				return (self.apps[prefix])
		print "No existe la aplicacion introducida, en funcionamiento la aplicacion por defecto"
		return (self.defaultapp)


	def __init__(self, hostname, port):


        # Create a TCP objet socket and bind it to a port
		mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		mySocket.bind((hostname,port))

        # Queue a maximum of 5 TCP connection requests
		mySocket.listen(5)

        # Accept connections, read incoming data, and call
        # parse and process methods (in a loop)

		try:        
			while True:
				print 'Waiting for connections'
				(recvSocket, address) = mySocket.accept()
				print 'HTTP request received (going to parse and process):'
				request = recvSocket.recv(1024)
				print request
				parsedRequest = self.parse(request)
				[returnCode, htmlAnswer] = resource.parse (parsedRequest)
				print 'Answering back...'
				recvSocket.send("HTTP/1.1 " + returnCode + " \r\n\r\n"
								+ htmlAnswer + "\r\n")
				recvSocket.close()

		except KeyboardInterrupt:
			print "Closing binded socket"
			mysocket.close()

  
if __name__ == "__main__":

	dic = {'/hola', '/adios', '/aleat/', '/suma/'}	
	testWebApp = webApp("localhost", 1234)'''


