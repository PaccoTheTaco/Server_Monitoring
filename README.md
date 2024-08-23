English version below

Discordbot setup:
Um den Bot selber nutzen zu können müssen folgende Schritte befolgt werden:
- kopiere dir den kompletten Ordner "discordbot" auf deinen Server 
- erstelle in dem Ordner eine Datei namens ".env" und schreibe in diese "DISCORD_TOKEN=" und dann dahinter deinen Discordbot Token
- stelle sicher das auf deinem Server Python installiert ist (python --version oder python3 --version)
- --> wenn Python nicht installiert ist, installiere python via "sudo apt-get install python3"
- Nun installiere die dazugehöhrigen bibliothek "sudo apt-get install python3-pip"
- installiere nun über pip einmal discord.py (pip install discord.py) dann noch dotenv (pip install python-dotenv) und noch psutil (pip install psutil)
- Nun navigiert du in das Verzeichnis discordbot und führt dann in diesem python3 bot.py aus und dann solltest du auf Discord die Befehle ausführen können

Slack App setup
- Wenn du noch keine Slack App hast, kannst du dir eine unter https://api.slack.com/apps erstellen. 
- Füge in deiner Slack App die Slash Commands "/test", "/cpu", "/diskusage", "/netstat", "/processes", "/ram", "/systemload", "/uptime" und "/serverwho" ein.
- Füge deine Slack-App zu deinem Workspace hinzu.
- Kopiere den kompletten Ordner "discordbot" auf deinen Server. 
- erstelle in diesem Ordner eine Datei namens ".env" und schreibe in diese "SLACK_TOKEN=" hinter den Token deiner Slack App.
- Schreibe nun in die gleiche Datei (.env) "SLACK_APP_TOKEN" dahinter den App Token.
- Stelle sicher, dass Python auf deinem Server installiert ist (python --version oder python3 --version).
- Wenn Python nicht installiert ist, installiere es mit "sudo apt-get install python3".
- Installiere nun die zugehörige Bibliothek "sudo apt-get install python3-pip".
- Installiere nun über pip einmal slack-bolt (pip install slack-bolt), dann noch dotenv (pip install python-dotenv) und noch psutil (pip install psutil).
- Navigiere nun in das Verzeichnis slackbot und führe python3 bot.py aus, dann sollten die Commands in deinem Workspace funktionieren.

---------------------

English version:

Discordbot setup:
To be able to use the bot yourself, the following steps must be followed:
- copy the complete folder ‘src’ to your server 
- create a file called ‘.env’ in the folder and write ‘DISCORD_TOKEN=’ and then your Discordbot token behind it
- if you want your bot to do the output in your language, please adapt the code yourself. Translate from German/Deutsch into your desired language 
- make sure that Python is installed on your server (python --version or python3 --version)
--> if Python is not installed, install python via ‘sudo apt-get install python3’
- Now install the corresponding library ‘sudo apt-get install python3-pip’
- Now install discord.py via pip (pip install discord.py), then dotenv (pip install python-dotenv) and psutil (pip install psutil)
- Now navigate to the src directory and then execute python3 bot.py in this directory and then you should be able to execute the commands on Discord

Slack app setup
- If you don't have a Slack app yet, you can create one at https://api.slack.com/apps. 
- Add the slash commands ‘/test’, ‘/cpu’, ‘/diskusage’, ‘/netstat’, ‘/processes’, ‘/ram’, ‘/systemload’, ‘/uptime’ and ‘/serverwho’ to your Slack app.
- Add your Slack app to your workspace.
- Copy the complete folder ‘discordbot’ to your server. 
- Create a file called ‘.env’ in this folder and write ‘SLACK_TOKEN=’ after the token of your Slack app.
- Now write ‘SLACK_APP_TOKEN’ after the app token in the same file (.env).
- Make sure that Python is installed on your server (python --version or python3 --version).
- If Python is not installed, install it with ‘sudo apt-get install python3’.
- Now install the associated library ‘sudo apt-get install python3-pip’.
- Now install slack-bolt via pip (pip install slack-bolt), then dotenv (pip install python-dotenv) and psutil (pip install psutil).
- Now navigate to the slackbot directory and execute python3 bot.py, then the commands should work in your workspace.