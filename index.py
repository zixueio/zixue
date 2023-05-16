import schedule,time,os
def job():
    path = os.getcwd()
    tranvese_folder(path)
    os.path.join(path,'index.html')
    with open('index.html','w') as f:
        f.write('')

unlist= ['venv','.idea','.git']
unfile = ['index.py','GitAutoPush.bat']
def tranvese_folder(path,d=None,index_file='index.html'):
    for root,dirs,files in os.walk(path):
        dirs[:]=[d for d in dirs if d not in unlist]
        files[:]=[file_name for file_name in files if file_name not in unfile]
        if d not in unlist:
            for file_name in files:
                if file_name.endswith('.html'):
                    relative_path=os.path.relpath(os.path.join(root,file_name),os.path.dirname(index_file))
                    with open(index_file,'a') as f:
                        f.write(f"{relative_path}\n")

schedule.every(0.1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
