import psutil
import datetime
from slack_bolt import Ack, Respond

def handle_who_command(ack: Ack, respond: Respond):
    ack()
    users = psutil.users()
    if not users:
        response_message = "Derzeit ist kein Benutzer angemeldet."
    else:
        response_message = "Angemeldete Benutzer:\n"
        for user in users:
            if user.host:
                masked_ip = '.'.join(user.host.split('.')[:1]) + ".x.x.x"
            else:
                masked_ip = "Unbekannt"

            login_time = datetime.datetime.fromtimestamp(user.started).strftime('%d.%m.%Y %H:%M:%S')
            response_message += (
                f"Benutzername: {user.name}\n"
                f"Terminal: {user.terminal}, Host: {masked_ip}, Anmeldezeit: {login_time}\n\n"
            )

    respond(response_message)
