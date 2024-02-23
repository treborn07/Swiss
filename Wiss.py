import requests
import socket
import time
import subprocess
import os
import whois
from scapy.all import ARP, Ether, srp

def localizar_ip(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = response.json()
        
        if data["status"] == "success":
            print(f"IP: {data['query']}")
            print(f"País: {data['country']}")
            print(f"Cidade: {data['city']}")
            print(f"ISP: {data['isp']}")
            print(f"Latitude: {data['lat']}")
            print(f"Longitude: {data['lon']}")
        else:
            print("Falha ao localizar o IP.")
    except requests.RequestException as e:
        print(f"Erro na requisição HTTP: {e}")
    except KeyError as e:
        print(f"Dados inválidos recebidos da API: {e}")
    except Exception as e:
        print(f"Erro ao processar a solicitação: {e}")

        
def encontrar_endereco_ip(ip):
    try:
        endereco = socket.gethostbyaddr(ip)
        print(f'O endereço IP {ip} está associado ao domínio: {endereco[0]}')
    except socket.herror:
        print(f'Não foi possível encontrar o domínio associado ao endereço IP {ip}')
    except Exception as e:
        print(f"Erro ao processar a solicitação: {e}")        
        
def chamar_programa():
    # Substitua 'ia.py' pelo nome do programa que deseja chamar
    subprocess.run(["python3", "ia.py"])   

def consultar_whois():
    dominio = input("Insira o domínio que deseja consultar: ")
    try:
        info = whois.whois(dominio)
        print(info)
    except Exception as e:
        print(f"Erro ao consultar WHOIS: {e}")
         
def verificar_portas_abertas(ip, verbose=False):
    try:
        print(f"Verificando portas abertas em {ip}...")
        for porta in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Define um timeout de 1 segundo para cada tentativa de conexão
            resultado = sock.connect_ex((ip, porta))
            if resultado == 0:
                print(f"A porta {porta} está aberta")
            elif verbose:
                print(f"A porta {porta} está fechada")
            sock.close()
    except Exception as e:
        print(f"Erro ao verificar portas abertas: {e}")
        
def listar_usuarios_wifi(ip_ranges=["192.168.0.1/24"]):
    clientes = []
    for ip_range in ip_ranges:
        arp = ARP(pdst=ip_range)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether / arp

        result = srp(packet, timeout=3, verbose=False)[0]

        for sent, received in result:
            clientes.append({'ip': received.psrc, 'mac': received.hwsrc})

    return clientes

if __name__ == "__main__":
    print("Clientes conectados à rede Wi-Fi:")
    # Exemplo de uso com duas faixas de IP diferentes
    faixas_ip = ["192.168.0.1/24", "192.168.2.0/20", "10.0.0.1/24"]
    clientes = listar_usuarios_wifi(ip_ranges=faixas_ip)
    for cliente in clientes:
        print(f"IP: {cliente['ip']}, MAC: {cliente['mac']}")

        
def exibir_menu():
    arte_ascii = """
__________________¶________________¶
_________________¶¶________________¶¶               =========RobertSCE=========
_______________¶¶¶__________________¶¶¶      	1. Localizar IP
_____________¶¶¶¶____________________¶¶¶¶    	2. Host/Associada
____________¶¶¶¶¶____________________¶¶¶¶¶   	3. IA
___________¶¶¶¶¶______________________¶¶¶¶¶  	4. Seu endereço Público
__________¶¶¶¶¶¶______________________¶¶¶¶¶¶    5. Consulta WHOIS
__________¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶    6. Varredura/PORTAS
__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶	7. Listar Clientes/WIFI
___________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶	8.
____________¶¶¶¶¶¶¶¶____¶¶¶¶¶¶____¶¶¶¶¶¶¶¶	9.	
___¶________¶¶¶¶¶¶¶______¶¶¶¶______¶¶¶¶¶¶¶
___¶_______¶¶¶¶¶¶¶¶___O_¶¶¶¶¶__O__¶¶¶¶¶¶¶¶
__¶¶¶______¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶
__¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
_¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶
_¶¶¶¶¶____¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶
___¶¶_____¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶
___¶¶______¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶
____¶¶______¶¶________¶¶¶¶¶¶¶¶¶¶_______¶¶
_____¶¶______¶¶¶_______________________¶
_____¶¶________¶¶____¶¶¶¶¶¶¶¶¶¶¶______¶
______¶¶________¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶__¶
_______¶¶__________¶¶¶_____¶¶¶¶¶¶¶¶¶¶
_________¶¶___________¶¶¶¶¶__¶¶¶¶¶¶¶¶¶
_____________________________¶¶¶¶¶¶¶¶¶¶
______________________________¶¶¶¶¶¶¶¶¶
_______________________________¶¶¶¶¶¶¶ 
"""
    print(arte_ascii)

    # Adicione outras partes do seu menu abaixo
exibir_menu() 

escolha = False
escolha1 = False
escolha2 = False
escolha3 = False
escolha4 = False	

while escolha == False:
    nivel = int(input("Escolha uma opção: \n"))
    if nivel == 1:
        ip = input("Insira o endereço IP que deseja localizar: \n")
        localizar_ip(ip)
    elif nivel == 2:
        host = input("Insira o IP que deseja analisar: \n")
        encontrar_endereco_ip(host)
    elif nivel == 3:
        print("Aguarde, estamos chamando o chatbot para você...")
        chamar_programa()
    elif nivel == 4:
        print("Seu endereço público é: \n")
        os.system("curl ifconfig.me")
    elif nivel == 5:
        consultar_whois()
    elif nivel == 6:
        host = input("Insira o endereço IP ou o nome do host que deseja verificar: ")
        verbose = input("Deseja ativar o modo verbose? (S/N): ").upper() == "S"
        verificar_portas_abertas(host, verbose)
        exibir_menu()  # Mostra o menu novamente após a verificação
    elif nivel == 7:
        print("Clientes conectados à rede Wi-Fi:")
        faixas_ip = ["192.168.0.1/24", "192.168.2.0/20", "10.0.0.1/24"]
        clientes = listar_usuarios_wifi(ip_ranges=faixas_ip)
        for cliente in clientes:
            print(f"IP: {cliente['ip']}, MAC: {cliente['mac']}")
        exibir_menu()  # Mostra o menu novamente após listar os clientes conectados
