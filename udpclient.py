# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 06:53:49 2016

@author: waradepratik
"""
#final udp program
#import package
import socket
import sys
import time
def Main():
    
        #create socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Socket Created Successfully")
    
        #taking argument from the client 
        hostName_input,portNumber_input,command, count,delay=input("$").split()
    
        #print(hostName_input,portNumber_input,command,count,delay) &  #converting hostname to ip
        remote_ip= socket.gethostbyname(hostName_input)
        remote_port= int(portNumber_input)
        remote_delay= float(delay)
        serveraddr=(remote_ip,remote_port)    
        remote_count=int(count) 
      
        if remote_count==0:
            message = input("->->-> ")
            print("Pratik client interactive mode")
            print(message)
            start_time = time.time()
            while (time.time() - start_time) < remote_delay:                
                s.sendto(message.encode(),serveraddr)
                print("Enter in interactive mode")
            s.close()
                
        if remote_count > 0 :                      
            #join remote ip adn port number for UDP connection            
            message1=command
            message2=count
            message3=delay   
    
            # Sending the arguments in the form of message            
            s.sendto(message1.encode(),serveraddr)            
            s.sendto(message2.encode(),serveraddr)            
            s.sendto(message3.encode(),serveraddr)
            
            #count = 0 Getting the data and printing it on client time
            while remote_count:                
                data, addr = s.recvfrom(1024)
                data = data.decode('utf-8')                
                print(data)
                remote_count=remote_count-1
            s.close()   #closing socket connection

if __name__ == '__main__':
    Main()
