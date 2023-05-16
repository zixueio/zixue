import schedule,time,os
def job():
    path = os.getcwd()
    tranvese_folder(path)
def tranvese_folder(path):
    for file in os.listdir(path):
        if 'venv' in file:
            file.remove("venv")
        abs_path = os.path.join(path,file)
        if os.path.isdir(abs_path):
            print("dir: ",abs_path)
            tranvese_folder(abs_path)
        else:
            print("file: ",abs_path)

schedule.every(0.1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
