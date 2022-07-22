from datetime import datetime
import schedule
import time


def emailjob():
    now = datetime.now()
    print("send email job - Time:"+now.strftime("%H:%M:%S"))
    
def buildreport():
    now = datetime.now()
    print("buildreport job. - Time:"+now.strftime("%H:%M:%S"))

def buildimage():
    now = datetime.now()
    print("buildimage job.- Time:"+now.strftime("%H:%M:%S"))        
    
schedule.every(5).seconds.do(emailjob)    
schedule.every(2).seconds.do(buildreport)    

schedule.every().day.at("11:54").do(buildimage)    

while True:
    schedule.run_pending()
    time.sleep(1)