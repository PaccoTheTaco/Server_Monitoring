import psutil

def handle_disk_command(ack, respond):
    ack()

    disk_info = psutil.disk_usage('/')
    total_disk = disk_info.total / (1024 ** 3)
    used_disk = disk_info.used / (1024 ** 3)
    free_disk = disk_info.free / (1024 ** 3)
    usage_percentage = disk_info.percent

    message = (
        f"Disk Usage:\n"
        f"Total: {total_disk:.2f} GB\n"
        f"Used: {used_disk:.2f} GB\n"
        f"Free: {free_disk:.2f} GB\n"
        f"Usage: {usage_percentage}%"
    )

    respond(message)
