from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
import os
import ram
import cpu
import diskusage
import netstat

load_dotenv()

app = App(token=os.getenv("SLACK_TOKEN"))

@app.command("/test")
def handle_test_command(ack, respond):
    ack()
    respond("Test erfolgreich")

app.command("/ram")(ram.handle_ram_command)
app.command("/cpu")(cpu.handle_cpu_command)
app.command("/diskusage")(diskusage.handle_disk_command)
app.command("/netstat")(netstat.handle_netstat_command)

if __name__ == "__main__":
    handler = SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN"))
    handler.start()
