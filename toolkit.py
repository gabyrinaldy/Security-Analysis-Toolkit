import os
from network.scanner import scan_local_network, display_results
from forensics.metadata_extractor import get_image_metadata, display_metadata
from web.header_analyzer import check_security_headers, display_web_results
from auth.password_checker import check_password_strength # <-- Importação Nova

def main():
    while True:
        print("\n" + "="*45)
        print(" 🛡️  CYBERSECURITY TOOLKIT V1.1 - COMPLETO  🛡️")
        print("="*45)
        print("1. [REDE]    Escaneamento ARP")
        print("2. [FORENSE] Metadados de Imagem")
        print("3. [WEB]     Analisar Cabeçalhos de Segurança")
        print("4. [AUTH]    Testar Força de Senha") # <-- Opção Nova
        print("0. Sair")
        print("="*45)
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            target = input("Range da rede (ex: 192.168.1.0/24): ")
            display_results(scan_local_network(target))
        
        elif opcao == "2":
            path = input("Caminho da imagem (ex: foto.jpg): ")
            display_metadata(get_image_metadata(path))
            
        elif opcao == "3":
            url = input("URL do site (ex: google.com): ")
            display_web_results(check_security_headers(url))

        elif opcao == "4": # <-- Lógica Nova
            print("\n--- ANALISADOR DE SENHAS ---")
            pwd = input("Digite a senha para testar: ")
            rating, tips = check_password_strength(pwd)
            print(f"\nAvaliação: {rating}")
            if tips:
                print("Dicas para melhorar:")
                for tip in tips: print(tip)
            
        elif opcao == "0":
            print("Encerrando... Até a próxima!")
            break
        else:
            print("[!] Opção inválida.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()