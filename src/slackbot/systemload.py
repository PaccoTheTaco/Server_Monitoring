import platform
import os
from slack_bolt import Ack, Respond

def handle_systemload_command(ack: Ack, respond: Respond):
    ack()
    if platform.system() in ["Linux", "Darwin"]:
        load1, load5, load15 = os.getloadavg()
        response_message = (
            f"Systemauslastung:\n"
            f"1 Minute: {load1:.4f}\n"
            f"5 Minuten: {load5:.4f}\n"
            f"15 Minuten: {load15:.4f}\n"
        )
    else:
        response_message = "Dieser Befehl ist nur auf Debian/Unix-basierten Systemen verfügbar."

    respond(response_message)
