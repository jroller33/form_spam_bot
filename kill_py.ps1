# sometimes this bot can get hung up and start causing errors. If that happens, run this powershell script, which kills all Python processes and will also kill the bot

taskkill /im python.exe /F
taskkill /im python3.9.exe /F
