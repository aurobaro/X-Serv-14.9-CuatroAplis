#!/usr/bin/python
#-*- coding:utf-8 -*-


import webapp



class suma (webapp.webApp):

    def process(self, parsedRequest):

        if len(parsedRequest.split('/'))== 4:
            op1=parsedRequet.split('/')[2]
            op2=parsedRequest.split('/')[3]
            resultado=int(op1)+int(op2)
            return ("HTTP/1.1 200 OK\r\n\r\n", "<html><body><h1>Resultado:"+ str(resultado)+"</h1></body></html>")
        else:
            return ("HTTP/1.1 200 OK\r\n\r\n", "<html><body><h1>Faltan operandos para realizar la operacion</h1></body></html>")

    '''def process (self, parsedRequest):
        
        resource = parsedRequest[1]
        operacion = resource.split('/')[2]
        operando1 = operacion.split('&')[0]
        operando2 = operacion.split('&')[1]
            
        if operando1.isdigit() and operando2.isdigit():

            resultado = int(operando1) + int(operando2)
            htmlbody ="<h1>Sumador Simple</h1>" + \
                "<p>La suma es: " + str(resultado) + \
                "</p>"
            return ("200 OK", "<html><body>" + htmlbody + "</body></html>")'''


if __name__ == "__main__":
	suma = suma("localhost", 1234)




