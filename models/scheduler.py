# coding: utf8
import time
from gluon.scheduler import Scheduler

def demo1(*args,**vars):
    print 'you passed args=%s and vars=%s' % (args, vars)
    return args[0]

def demo2():
    1/0

def demo3():
    time.sleep(15)
    print 1/0
    return None

def demo4():
    print "I'm the demo4 task"
    time.sleep(15)
    print "I'm printing something"
    return dict(a=1, b=2)

def demo5():
    time.sleep(15)
    print "I'm printing something"
    rtn = dict(a=1, b=2)

def demo6():
    print "starting demo6, this will only work under a posix compatible os"

    def sig_fun(sig, func=None):
        time.sleep(10)

    import signal
    signal.signal(signal.SIGTERM, sig_fun)
    
    print "!clear!now that you can't terminate me I am going to sleep"
    time.sleep(20)

    print "!clear!hello again... and good bye"



scheduler = Scheduler(db)
##or, alternatively :
#scheduler = Scheduler(db,
#                      dict(
#                        demo1=demo1,
#                        demo2=demo2,
#                        demo3=demo3,
#                        demo4=demo4,
#                        foo=demo5
#                        )
#                      )
