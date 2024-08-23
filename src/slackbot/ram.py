import psutil

def handle_ram_command(ack, respond):
    ack()

    ram_info = psutil.virtual_memory()
    usage_percentage = ram_info.percent
    total_memory = ram_info.total
    
    used_memory = round(total_memory * (usage_percentage / 100))

    if total_memory >= 1024 ** 3:
        total_memory_str = f"{total_memory / (1024 ** 3):.2f} GB"
        used_memory_str = f"{used_memory / (1024 ** 3):.2f} GB"
    else:
        total_memory_str = f"{total_memory / (1024 ** 2):.0f} MB"
        used_memory_str = f"{used_memory / (1024 ** 2):.0f} MB"

    message = (
        f"RAM Usage:\n"
        f"Total: {total_memory_str}\n"
        f"Used: {used_memory_str}\n"
        f"Usage: {usage_percentage}%"
    )

    respond(message)
