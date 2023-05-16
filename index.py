import schedule,time
def job():
    print("I am working")
schedule.every(0.1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
