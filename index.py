import schedule,time,os


def job(path):
    for file in os.listdir(path):
        abs_path = os.path.join(path,file)
        if os.path.isdir(abs_path):
            print("dir: ",abs_path)
            job(abs_path)
        else:
            print("file: ",abs_path)

schedule.every(0.1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
