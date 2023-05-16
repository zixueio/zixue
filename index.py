import schedule,time,os
def job():
    path = os.getcwd()
    tranvese_folder(path)

unlist= ['venv','.idea','.git','GitAutoPush.bat','index.py']
def tranvese_folder(path,d=None):
    for root,dirs,files in os.walk(path):
        dirs[:]=[d for d in dirs if d not in unlist]
        if d not in unlist:
            for file_name in files:
                print(os.path.join(root,file_name))
schedule.every(0.1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
