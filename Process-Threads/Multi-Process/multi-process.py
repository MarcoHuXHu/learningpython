from multiprocessing import Process
import os
import time

def run_proc(name):
	print('Run child process %s(%s)' % (name,os.getpid()))
	time.sleep(2)

if __name__=='__main__':
	print('Parent process %s' % os.getpid())
	p=Process(target=run_proc,args=('test',))
	p.start()
	print('Started')
	p.join()	# will wait for child-process p to finish
	print('End')

