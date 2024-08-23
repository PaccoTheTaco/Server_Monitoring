import psutil
from slack_bolt import Ack, Respond

def handle_processes_command(ack: Ack, respond: Respond):
    ack()
    processes = [(p.info["name"], p.info["cpu_percent"]) for p in psutil.process_iter(["name", "cpu_percent"])]
    processes = sorted(processes, key=lambda x: x[1], reverse=True)

    response_message = "Laufende Prozesse:\n"
    for i, (name, cpu) in enumerate(processes[:10], start=1):  # Zeigt die ersten 10 Prozesse
        response_message += f"{i}. {name} - CPU-Auslastung: {cpu}%\n"

    respond(response_message)
