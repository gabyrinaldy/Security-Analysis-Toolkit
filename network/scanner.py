import socket

def scan_local_network(ip_range):
    print(f"🔎 Escaneando portas comuns no range: {ip_range}...")
    # Exemplo simplificado: escaneando apenas o IP final .1 até .10 na porta 80
    base_ip = ".".join(ip_range.split(".")[:-1])
    found = []
    
    for i in range(1, 11): # Testa os primeiros 10 IPs
        ip = f"{base_ip}.{i}"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((ip, 80)) # Tenta conectar na porta 80 (HTTP)
        if result == 0:
            found.append({'ip': ip, 'mac': "Apenas root pode ver o MAC"})
        sock.close()
    return found

def display_results(clients):
    print("\nDispositivos com porta 80 aberta:")
    for c in clients:
        print(f"IP: {c['ip']}")