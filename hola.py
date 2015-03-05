#!/usr/bin/python -tt
# -*- coding: UTF-8 -*-


import webapp



class hola (webapp.webApp):

    def process (self, parsedRequest):
        
        return ("200 OK", "<html><body><h1>Hola</h1></body></html>")


class adios (webapp.webApp):

    def process (self, parsedRequest):
        
        return ("200 OK", "<html><body><h1>Adios</h1></body></html>")

if __name__ == "__main__":

    testhola = hola("localhost", 1234, "/hola")
    testadios = adios("localhost", 1234, "/adios")

