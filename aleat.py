#!/usr/bin/python
#-*- coding:utf-8 -*-


import webapp
import random


class aleat (webapp.webApp):

    def process (self, parsedRequest):

        resource = parsedRequest[2]		
        nextPage = str (random.randint (0,10000))
        nextUrl = "http://" + "localhost" + ":" + "1234" +'/aleat/' + nextPage
        htmlBody = '<p>Quieres mas: <a href="' \
            + nextUrl + '">'+ nextPage + "</a></p>"
        return ("HTTP/1.1 200 OK\r\n\r\n", "<html><body><h1>" + htmlBody +"</h1></body></html>")

if __name__ == "__main__":
	testAleat = aleat("localhost", 1234)
