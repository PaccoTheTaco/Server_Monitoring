import psutil

def handle_cpu_command(ack, respond):
    ack()

    cpu_usage = psutil.cpu_percent(interval=1)

    response_message = f"Current CPU Usage: {cpu_usage}%"

    respond(response_message)
