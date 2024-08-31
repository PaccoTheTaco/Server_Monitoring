English version below

## Deutsche Version:

### Discordbot setup:

Ein paar Einblicke von dem Discordbot erhälst du hier: 

/ram: 

[RAM](example_pics/RAM.png)

/cpu:

[CPU](example_pics/CPU.png)

/uptime

[uptime](example_pics/uptime.png)

Um den Bot selber nutzen zu können müssen folgende Schritte befolgt werden:
- lade die die Discord Bot zip Datei von der [Releases-Seite](https://github.com/PaccoTheTaco/Server_Monitoring/releases) herunter
- entpacke diese und schiebe sie auf deinen Server in einen Ordner deiner Wahl
- stelle sicher das auf deinem Server Python installiert ist (python --version oder python3 --version) --> wenn Python nicht installiert ist, installiere python via "sudo apt-get install python3"
- installiere die dazugehörige Bibliothek "sudo apt-get install python3-pip"
- navigiere in das Verzeichnis und installiere über pip die benötigten Pakete "pip install -r requirements.txt"
- in dem gleichen Verzeichnis musst du nun die Datei .env erstelllen und in dieser "DISCORD_TOKEN=" reinschreiben. Hinter dem "DISCORD_TOKEN=" fügst du den Token ein den du dir vom [Discord Developer Portal](https://discord.com/developers/applications) holen kannst
- wieder in dem gleichen Verzeichnis führst du "python3 bot.py" und dein Bot sollte laufen 

PS: vergiss nicht deinen Discordbot auf deinen Discord Server zu adden :D

### Slack App setup:

Hier sind ein paar Einblicke zu der Slack App: 

/ram: 

[RAM](example_pics/slack_RAM.png)

/cpu:

[CPU](example_pics/slack_CPU.png)

/diskusage

[uptime](example_pics/diskusage.png)

- lade die die Slack App zip Datei von der [Releases-Seite](https://github.com/PaccoTheTaco/Server_Monitoring/releases) herunter
- entpacke diese und schiebe sie auf deinen Server in einen Ordner deiner Wahl
- stelle sicher das auf deinem Server Python installiert ist (python --version oder python3 --version) --> wenn Python nicht installiert ist, installiere python via "sudo apt-get install python3"
- installiere die dazugehörige Bibliothek "sudo apt-get install python3-pip"
- navigiere in das Verzeichnis und installiere über pip die benötigten Pakete "pip install -r requirements.txt"
- in dem gleichen Verzeichnis musst du nun die Datei .env erstelllen und in dieser "SLACK_TOKEN=" reinschreiben. Hinter dem "SLACK_TOKEN=" fügst du den Token ein den du dir vom [Slack App Portal](https://api.slack.com/apps) geholt hast
- bleibe in dem Verzeichnis und führe python3 bot.py aus, dann sollten die Commands in deinem Workspace funktionieren.

---------------------

## English version:

### Discordbot setup:

You can get a few insights into the Discordbot here: 

/ram: 

[RAM](example_pics/RAM.png)

/cpu:

[CPU](example_pics/CPU.png)

/uptime

[uptime](example_pics/uptime.png)

To be able to use the bot yourself, the following steps must be followed:
- download the Discord Bot zip file from the [Releases page](https://github.com/PaccoTheTaco/Server_Monitoring/releases)
- unzip it and move it to your server in a folder of your choice
- make sure that Python is installed on your server (python --version or python3 --version) --> if Python is not installed, install python via ‘sudo apt-get install python3’
- install the corresponding library ‘sudo apt-get install python3-pip’
- navigate to the directory and install the required packages via pip ‘pip install requirements.txt’
- in the same directory you now have to create the file .env and write ‘DISCORD_TOKEN=’ in it. After the ‘DISCORD_TOKEN=’ you insert the token that you can get from the [Discord Developer Portal](https://discord.com/developers/applications)
- again in the same directory you run ‘python3 bot.py’ and your bot should run 

PS: don't forget to add your discordbot to your discord server :D

### Slack App setup:

Here are a few insights into the Slack app: 

/ram: 

[RAM](example_pics/slack_RAM.png)

/cpu:

[CPU](example_pics/slack_CPU.png)

/diskusage

[uptime](example_pics/diskusage.png)

- download the Slack App zip file from the [releases page](https://github.com/PaccoTheTaco/Server_Monitoring/releases)
- unzip it and move it to your server in a folder of your choice
- make sure that Python is installed on your server (python --version or python3 --version) --> if Python is not installed, install python via ‘sudo apt-get install python3’
- install the corresponding library ‘sudo apt-get install python3-pip’
- navigate to the directory and install the required packages via pip ‘pip install -r requirements.txt’
- In the same directory, you must now create the .env file and write ‘SLACK_TOKEN=’ in it. After the ‘SLACK_TOKEN=’ you insert the token you got from the [Slack App Portal](https://api.slack.com/apps)
- stay in the directory and execute python3 bot.py, then the commands should work in your workspace.