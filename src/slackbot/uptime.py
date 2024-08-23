import psutil
import datetime
from slack_bolt import Ack, Respond

def handle_uptime_command(ack: Ack, respond: Respond):
    ack()
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime_duration = datetime.datetime.now() - boot_time
    days, seconds = uptime_duration.days, uptime_duration.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    response_message = (
        f"Server Uptime:\n"
        f"Seit: {boot_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"Laufzeit: {days} Tage, {hours} Stunden, {minutes} Minuten, {seconds} Sekunden\n"
    )

    respond(response_message)
