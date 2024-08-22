English version below

Um den Bot selber nutzen zu können müssen folgende Schritte befolgt werden:
- kopiere dir den kompletten Ordner "src" auf deinen Server 
- erstelle in dem Ordner eine Datei namens ".env" und schreibe in diese "DISCORD_TOKEN=" und dann dahinter deinen Discordbot Token
- stelle sicher das auf deinem Server Python installiert ist (python --version oder python3 --version)
- --> wenn Python nicht installiert ist, installiere python via "sudo apt-get install python3"
- Nun installiere die dazugehöhrigen bibliothek "sudo apt-get install python3-pip"
- installiere nun über pip einmal discord.py (pip install discord.py) dann noch dotenv (pip install python-dotenv) und noch psutil (pip install psutil)
- Nun navigiert du in das Verzeichnis src und führt dann in diesem python3 bot.py aus und dann solltest du auf Discord die Befehle ausführen können

---------------------

English version:
To be able to use the bot yourself, the following steps must be followed:
- copy the complete folder ‘src’ to your server 
- create a file called ‘.env’ in the folder and write ‘DISCORD_TOKEN=’ and then your Discordbot token behind it
- if you want your bot to do the output in your language, please adapt the code yourself. Translate from German/Deutsch into your desired language 
- make sure that Python is installed on your server (python --version or python3 --version)
--> if Python is not installed, install python via ‘sudo apt-get install python3’
- Now install the corresponding library ‘sudo apt-get install python3-pip’
- Now install discord.py via pip (pip install discord.py), then dotenv (pip install python-dotenv) and psutil (pip install psutil)
- Now navigate to the src directory and then execute python3 bot.py in this directory and then you should be able to execute the commands on Discord
