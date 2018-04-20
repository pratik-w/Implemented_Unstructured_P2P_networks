
import socket
import subprocess
import time
import datetime as dt

def Main():    
    #create socket
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        port=input("$Enter port number :- ")    #port number validation
        temp=int(port)
        if temp<=0:
            raise ValueError
        else:
            port=temp       
        
    except ValueError:
         print("Oops!  That was no valid number.  Try again...")
         s.close()
         
    #bind port number with ip address     
    s.bind(('',int(port)))    
    print("Server Started")
    while True:
        
        #getting command from client
        data,addr=s.recvfrom(1024)
        command=data.decode('utf-8')        
        print("Command Run :" + command)
        print("Server connected to [ip,port]  :" , str( addr) )        
        
        #getting number of count
        data,addr=s.recvfrom(1024)
        count=data.decode('utf-8')
        #print("From connected user count is :" + count)
        exe_count= int(count)
        
        #Getting delay time
        data,addr=s.recvfrom(1024)
        d=data.decode('utf-8')
       # print("From connected user count is :" + d)
       # s.sendto(count.encode('utf-8'),addr)
        delay= float(d)
        
        if (exe_count>0) :         
        
            for run_pgram in range(exe_count):
                start_time=dt.datetime.now()    #getting real time of pc
                op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                end_time=dt.datetime.now()   #getting time after execution of command
                exe_time=(end_time-start_time).microseconds    #final execution time in microseconds
                #print ("Current date & time " + time.strftime("%c"))
                print("Execution Time in microsecond: " ,exe_time)
                time.sleep(delay)
                #print ("After Delay current date & time " + time.strftime("%c"))
                if op:
                    output=str(op.stdout.read())
                    #print ("Output:", (output))
                    print("sending to ",addr)
                    s.sendto(output.encode('utf-8'),addr)

                else:
                    error=str(op.stderr.read())
                    #print ("Error:",str(error))
                    s.sendall(error)      
        
        
    s.close()#closing while
    if exe_count==0:
           print("Server interactive:")
            

if __name__=='__main__':
    Main()