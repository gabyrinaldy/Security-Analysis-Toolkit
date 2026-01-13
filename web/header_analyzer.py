import requests

def check_security_headers(url):
    """
    Analisa os cabeçalhos de resposta HTTP de uma URL em busca de proteções de segurança.
    """
    if not url.startswith("http"):
        url = "https://" + url

    try:
        print(f"🌐 Analisando: {url}...")
        response = requests.get(url, timeout=10)
        headers = response.headers

        # Lista de cabeçalhos que queremos verificar
        security_headers = {
            "Strict-Transport-Security": "Protege contra interceptação de dados (HSTS).",
            "Content-Security-Policy": "Previne ataques de XSS e injeção de scripts.",
            "X-Frame-Options": "Evita que o site seja colocado em um iframe (Clickjacking).",
            "X-Content-Type-Options": "Impede o navegador de adivinhar o tipo de arquivo (MIME sniffing).",
            "Referrer-Policy": "Controla quanta informação de origem é enviada para outros sites."
        }

        results = []
        for header, description in security_headers.items():
            status = "✅ PRESENTE" if header in headers else "❌ AUSENTE"
            results.append({"header": header, "status": status, "info": description})
        
        return results

    except Exception as e:
        return f"Erro ao conectar: {e}"

def display_web_results(results):
    if isinstance(results, str):
        print(results)
    else:
        print(f"\n{'Cabeçalho':<30} | {'Status':<12} | {'Descrição'}")
        print("-" * 85)
        for r in results:
            print(f"{r['header']:<30} | {r['status']:<12} | {r['info']}")