🛡️ Security Analysis Toolkit V1.1
Este repositório é um canivete suíço de segurança cibernética desenvolvido em Python. Ele foi construído com uma arquitetura modular, permitindo que cada área da segurança (Rede, Forense, Web e Autenticação) tenha seu próprio espaço organizado.

🚀 Funcionalidades
O toolkit oferece quatro módulos principais acessíveis através de um menu interativo:

Rede (network/):

ARP Scanner: Identifica dispositivos ativos na rede local e seus endereços MAC. (Requer privilégios de administrador/sudo).

Forense Digital (forensics/):

Metadata Extractor: Analisa arquivos de imagem (JPEG/PNG) para extrair dados EXIF, incluindo modelo do dispositivo, data e localização (link direto para Google Maps).

Segurança Web (web/):

Header Analyzer: Verifica se um site possui cabeçalhos de segurança essenciais como HSTS, CSP e X-Frame-Options.

Autenticação (auth/):

Password Checker: Avalia a força de senhas usando critérios de complexidade (comprimento, símbolos, números e letras).

📂 Estrutura do Repositório
Plaintext

Security-Analysis-Toolkit/
├── toolkit.py           # Script Mestre (Menu Principal)
├── requirements.txt     # Dependências (Scapy, Pillow, Requests)
├── .gitignore           # Filtro para ignorar o ambiente virtual (.venv)
├── auth/                # Módulo de Autenticação
├── forensics/           # Módulo de Perícia Digital
├── network/             # Módulo de Análise de Rede
└── web/                 # Módulo de Auditoria Web

🛠️ Como Instalar e Rodar

Clone este repositório:

Bash
git clone https://github.com/seu-usuario/Security-Analysis-Toolkit.git
cd Security-Analysis-Toolkit
Crie e ative seu ambiente virtual (recomendado):

Bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou .venv\Scripts\activate no Windows

Instale as bibliotecas:

Bash
pip install -r requirements.txt
Execute o Toolkit:

Bash
python toolkit.py

⚠️ Aviso Legal (Disclaimer)
Este projeto foi criado para fins educacionais e de estudo de segurança ética. O autor não se responsabiliza pelo uso indevido destas ferramentas em sistemas sem autorização prévia. Hacking sem permissão é ilegal.

📝 Licença
Este projeto está sob a licença MIT - veja o arquivo LICENSE para detalhes.

Linkedin da criadora: https://www.linkedin.com/in/gabrielarinaldi02/