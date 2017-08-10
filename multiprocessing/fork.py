import os

print('Process (%s) start...' % os.getpid())

pid = os.fork()

if pid == 0 :
	print('Child process, %s is son of %s' % (os.getpid(), os.getppid()))
else :
	print('%s created %s' % (os.getpid(), pid))

pid = os.fork()

if pid == 0 :
        print('Child process, %s is son of %s' % (os.getpid(), os.getppid()))
else :
        print('%s created %s' % (os.getpid(), pid))


