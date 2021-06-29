'''
Multitasking: Execute multiple task at the same time
Processed based multitasking: Executing multi task at same time where each task is a separate independent program(process)
Thread based multitasking: Executing multiple task at the same time where each task is a separate independent part of the same program(process). Each independent part is called thread.
Thread: is a separate flow of execution. Every thread has a task
Multithreading: Using multiple thread in a prhram
once a thread is created, it should be started by calling start method: t= Thread(target=fun, args=())  then t.start()
'''
from threading import Thread
def display(user):
    print('hello', user)
th=Thread(target=display, args=('uma',))
th.start()

#Example: thread in loop
def show(a,b):
    print('hello number', a,b)

for i in range(3):
    t=Thread(target=show, args=(10,20))
    print('hey')
    t.start()