import psutil
import platform

def handle_netstat_command(ack, respond, command):
    ack()

    if platform.system() in ["Linux", "Darwin"]:
        port = int(command['text']) if 'text' in command and command['text'].isdigit() else None
        connections = psutil.net_connections(kind='inet')

        if port:
            active_connections = [
                conn for conn in connections
                if conn.laddr.port == port and conn.status == psutil.CONN_ESTABLISHED and conn.raddr
            ]
            if active_connections:
                message = f"Verbindungen für Port {port}:\n"
                for conn in active_connections:
                    message += f"- Remote IP: {conn.raddr.ip}, Status: {conn.status}\n"
            else:
                message = f"Keine aktiven Verbindungen für Port {port} gefunden."
        else:
            port_count = {}
            for conn in connections:
                if conn.status == psutil.CONN_ESTABLISHED and conn.raddr:
                    port = conn.laddr.port
                    port_count[port] = port_count.get(port, 0) + 1

            sorted_ports = sorted(port_count.items(), key=lambda x: x[1], reverse=True)
            message = "Verbindungen pro Port:\n"
            for port, count in sorted_ports:
                message += f"- Port {port}: {count} Verbindungen\n"
    else:
        message = "Dieser Befehl ist nur auf Debian/Unix-Systemen verfügbar."

    respond(message)
