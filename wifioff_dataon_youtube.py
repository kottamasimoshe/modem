import os,time,datetime

def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	cmdr='adb logcat -b radio  > sms_log'+'&'
	os.system(cmdr)
def wifi_off():
             cmd= "adb -s "+div+" shell svc wifi disable"
             rc=os.system(cmd)
             print "wifii disabled"
             time.sleep(5)
             return rc
def data_on():
             cmd= "adb -s "+div+" shell svc data enable"
             rc=os.system(cmd)
             print "data enabled"
             time.sleep(10)
             return rc

def youtube():
             cmd= "adb -s "+div+" shell am start -a android.intent.action.VIEW -d http://www.youtube.com/watch?v=xko3vld5Wds"
             rc=os.system(cmd)
             print "youtube opened"
             time.sleep(10)
             return rc
def iter_status(iterations,div):
        collect_logs()
        for i in range(iterations):
                print i+1
                off=wifi_off()
                on=data_on()
                open1= youtube()
div = "ZX1D64GJW6"
iterations=3
iter_status(iterations,div)
