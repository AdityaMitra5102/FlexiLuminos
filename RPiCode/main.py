import threading
import os

def task1():
    os.system("./run.sh")
def task5():
    os.system("./runweb.sh")
def task2():
    os.system("java Main")
def task3():
    os.system("python3 discordbot.py")
def task4():
    os.system("python3 telegrambot.py")
t1=threading.Thread(target=task1, name='t1')
t2=threading.Thread(target=task2, name='t2')
t3=threading.Thread(target=task3, name='t3')
t4=threading.Thread(target=task4, name='t4')
t5=threading.Thread(target=task5, name='t5')
t2.start()
t1.start()
t3.start()
t4.start()
t5.start()
while True:
	if t1.is_alive() is False:
		t1.join()
		t1=threading.Thread(target=task1, name='t1')
		t1.start()
	if t2.is_alive() is False:
		t2.join()
		t2=threading.Thread(target=task2, name='t2')
		t2.start()
	if t3.is_alive() is False:
		t3.join()
		t3=threading.Thread(target=task3, name='t3')
		t3.start()
	if t4.is_alive() is False:
		t4.join()
		t4=threading.Thread(target=task4, name='t4')
		t4.start()
	if t5.is_alive() is False:
		t5.join()
		t5=threading.Thread(target=task5, name='t5')
		t5.start()
