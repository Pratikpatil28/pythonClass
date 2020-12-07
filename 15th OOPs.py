#Mutli-threading
#define - To breake one task into multiple process and then again break it into threading

#Where we use threading?
#We use threafing beacuse we can run different threads
#on diffrent cores to wrork efficiently rather than put a work load on single thread

from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello()  #Suppose as t1 thread

t2 = Hi()    #Suppose as t2 thread

#Start function internally calls [Run] function
#we used start beacuse it separate threads t1 & t2 from main thread
t1.start()
sleep(0.2)   #sleep time to break the schedular sync...and grant only one function to perform complete
t2.start()

#Join is used as to stop main thread perform function, and let threads to exucte the program and then main thread run the program
t1.join()
t2.join()

print('Bye')#Main thread program