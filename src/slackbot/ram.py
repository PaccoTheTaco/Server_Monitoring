import psutil

def handle_ram_command(ack, respond):
    ack()

    ram_info = psutil.virtual_memory()
    if ram_info.total < 1024 ** 3:
        total_ram = ram_info.total / (1024 ** 2)
        used_ram = ram_info.used / (1024 ** 2)
        free_ram = ram_info.available / (1024 ** 2)
        unit = "MB"
    else:
        total_ram = ram_info.total / (1024 ** 3)
        used_ram = ram_info.used / (1024 ** 3)
        free_ram = ram_info.available / (1024 ** 3)
        unit = "GB"
    
    usage_percentage = ram_info.percent

    message = (
        f"RAM Usage:\n"
        f"Total: {total_ram:.2f} {unit}\n"
        f"Used: {used_ram:.2f} {unit}\n"
        f"Free: {free_ram:.2f} {unit}\n"
        f"Usage: {usage_percentage}%"
    )

    respond(message)
