:: 使用`%~dp0`获取当前批处理文件的路径（包括驱动器和目录），并将其存储在名为`script_path`的变量中
set "script_path=%~dp0"

:loop
	:: 删除现有hosts文件
	del /f C:\Windows\System32\drivers\etc\hosts

	:: 到指定地址下载hosts文件
	curl -o C:\Windows\System32\drivers\etc\hosts https://raw.hellogithub.com/hosts
	
	:: 使用以下命令刷新DNS缓存	
	git config --global --unset http.proxy
	git config --global --unset https.proxy
	ipconfig/flushdns

	:: Navigate to the directory you wish to push to GitHub
	::获取当前文件路径
	cd "%script_path%"
	
	::Initialize GitHub
	git init
	
	::Pull any external changes (maybe you deleted a file from your repo?)
	git pull
	
	::Add all files in the directory
	git add --all
	
	::Commit all changes with the message "auto push". 
	::Change as needed.
	git commit -m "auto push"
	
	::Push all changes to GitHub 
	git push
	
	::Alert user to script completion and relaunch.
	echo Complete. Relaunching...
	
	::Wait 300 seconds until going to the start of the loop.
	::Change as needed.
	TIMEOUT 300
	
::Restart from the top.
goto loop