# import threading
# from threading import *
# from time import sleep

# class First_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 1st Thread")
# class Second_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 2nd Thread")
# t1=First_Thread()
# t2=Second_Thread()
# t1.run()
# t2.run()




# import threading
# from threading import *
# from time import sleep

# class First_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 1st Thread")
# class Second_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 2nd Thread")
# t1=First_Thread()
# t2=Second_Thread()
# t1.start()
# t2.start()



# import threading
# from threading import *
# from time import sleep

# class First_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 1st Thread")
#             sleep(1)
# class Second_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 2nd Thread")
#             sleep(1)
# t1=First_Thread()
# t2=Second_Thread()
# t1.start()
# t2.start()




# import threading
# from threading import *
# from time import sleep

# #create a global lock
# lock=threading.Lock()

# class First_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             with lock:
#                 print(i,"This is 1st Thread")
            
# class Second_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             with lock:
#                 print(i,"This is 2nd Thread")
            
# t1=First_Thread()
# t2=Second_Thread()
# t1.start()
# t2.start()




# import threading
# from threading import *
# from time import sleep

# #create a global lock
# lock=threading.Lock()

# class First_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             with lock:
#                 print(i,"This is 1st Thread")
#                 sleep(1)
            
# class Second_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             with lock:
#                 print(i,"This is 2nd Thread")
#                 sleep(1)
            
# t1=First_Thread()
# t2=Second_Thread()
# t1.start()
# t2.start()





# import threading
# from threading import *
# from time import sleep

# #create a global lock
# lock=threading.Lock()

# class First_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             with lock:
#                 print(i,"This is 1st Thread")
#                 sleep(1)
            
# class Second_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             with lock:
#                 print(i,"This is 2nd Thread")
#                 sleep(1)
# class Third_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             with lock:
#                 print(i,"This is 3rd Thread")
#                 sleep(1)
            
# t1=First_Thread()
# t2=Second_Thread()
# t3=Third_Thread()
# t1.start()
# t2.start()
# t3.start()


# import threading
# from threading import *
# from time import sleep

# class First_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 1st Thread")
#             sleep(1)
            
# class Second_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 2nd Thread")
#             sleep(1)
# class Third_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 3rd Thread")
#             sleep(1)
            
# t1=First_Thread()
# t2=Second_Thread()
# t3=Third_Thread()
# t1.start()
# t2.start()
# t3.start()






# import threading
# from threading import *
# from time import sleep

# class First_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 1st Thread")
#             sleep(1) #prints every 1sec-fastest
            
# class Second_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 2nd Thread")
#             sleep(2)#print every 2sec -medium
# class Third_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 3rd Thread")
#             sleep(3) #print every 3sec -slowest
            
# t1=First_Thread()
# t2=Second_Thread()
# t3=Third_Thread()
# t1.start()
# t2.start()
# t3.start()



# import threading
# from threading import *
# from time import sleep

# class First_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 1st Thread")
#             sleep(1) 
            
# class Second_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 2nd Thread")
#             sleep(1)
# class Third_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 3rd Thread")
#             sleep(1) 
            
# t1=First_Thread()
# t2=Second_Thread()
# t3=Third_Thread()
# t1.start()
# t2.start()
# t3.start()
# t1.join()#Main thread waits for t1 to finish
# t2.join()#main thread waits for t2 to finish
# t3.join()#main thread waits for t3 to finish
# print("All threads have finished executing...")
# #The main thread is the thread that runs when you start your python program




# import threading
# from threading import *
# from time import sleep

# class First_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 1st Thread")
#             sleep(1) 
            
# class Second_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 2nd Thread")
#             sleep(1)
# class Third_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 3rd Thread")
#             sleep(1) 
            
# t1=First_Thread()
# t2=Second_Thread()
# t3=Third_Thread()
# t1.start() #starts first thread
# t1.join()#Main thread waits for t1 to finish
# t2.start() #starts second thread
# t2.join()#main thread waits for t2 to finish
# t3.start() #starts third thread
# t3.join()#main thread waits for t3 to finish
# print("All threads have finished executing...")




# import threading
# from threading import *
# from time import sleep

# class First_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 1st Thread")
#             sleep(1)
# class Second_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 2nd Thread")
#             sleep(1)
# t1=First_Thread()
# t2=Second_Thread()
# t1.start()
# print(t1.is_alive())
# t2.start()
# print(t2.is_alive())




# import threading
# from threading import *
# from time import sleep

# class First_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 1st Thread")
#             sleep(1)
# class Second_Thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 2nd Thread")
#             sleep(1)
# t1=First_Thread()
# t2=Second_Thread()
# t1.start()
# print(t1.is_alive())
# t2.start()
# print(t2.is_alive())
# t1.join()
# t2.join()
# print(t1.is_alive())
# print(t2.is_alive())


# import threading
# print(threading.current_thread().getName())



# import threading
# print(threading.current_thread().name)