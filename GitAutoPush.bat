:loop
	:: 到指定地址下载hosts文件
	curl -o C:\Windows\System32\drivers\etc\hosts https://raw.hellogithub.com/hosts
	copy /y C:\Windows\System32\drivers\etc\hosts C:\Windows\System32\drivers\etc\hosts.old
	copy /y C:\path\to\downloaded\hosts C:\Windows\System32\drivers\etc\hosts
	
	:: 使用以下命令刷新DNS缓存	
	git config --global --unset http.proxy
	git config --global --unset https.proxy
	ipconfig/flushdns

	:: Navigate to the directory you wish to push to GitHub
	::修改路径为您需要自动push的路径. Eg. C:\Users\rich\Desktop\Writings
	cd C:\Users\Administrator\Desktop\zixue
	
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