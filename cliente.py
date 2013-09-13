#encoding:utf-8
import socket  
  
s = socket.socket()   
s.connect(("localhost", 8000))  
  
while True:  
      mensaje = raw_input("> ")  
      s.send(mensaje)  
      if mensaje == "salir":  
         break  
  
print "adios"  
  
s.close() 