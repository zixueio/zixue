import schedule,time,os

unlist= ['venv','.idea','.git']
unfile = ['index.py','GitAutoPush.bat']
def job():
    current_foler_path = os.getcwd()
    index_file_path= os.path.join(current_foler_path,'index.html')
    os.path.join(current_foler_path,'index.html')
    with open('index.html','w') as f:
        f.write("\n\n")
    tranverse_folder(current_foler_path,index_file_path)
    with open(index_file_path,'a') as f:
        f.write("\n")

def tranverse_folder(path,d=None,index_file='index.html'):
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
