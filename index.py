import schedule,time,os
def job():
    path = os.getcwd()
    tranvese_folder(path)
def tranvese_folder(path):
    for root,dirs,files in os.walk(path):
        dirs[:]=[d for d in dirs if d not in ['venv','.idea']]
        if d not in ['venv','.idea']:
            for file_name in files:
                print(os.path.join(root,file_name))
schedule.every(0.1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
