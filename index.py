import schedule,time,os
def job():
    breakpoint()

def tranvese_folder(path):
    for file in os.listdir(path):
        abs_path = os.path.join(path,file)
        

schedule.every(0.1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
