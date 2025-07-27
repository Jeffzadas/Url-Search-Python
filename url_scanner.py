import requests

URLS_TO_TEST = [
    "admin", "login", "dashboard", "wp-admin", "user/profile",
    "config", "backup", "test", "dev", "robots.txt",
    ".env", ".git/", "phpinfo.php", "backup.zip", "uploads/",
    "404-error", "area-51", "this-page-does-not-exist"
]

def test_url(base_url):
    # Adiciona 'http://' se não tiver e garante a barra final
    if not base_url.startswith(("http://", "https://")):
        base_url = "http://" + base_url
    if not base_url.endswith("/"):
        base_url += "/"

    print(f"\n🔍 Testando URLs em: {base_url}\n")

    for path in URLS_TO_TEST:
        full_url = base_url + path
        try:
            response = requests.get(full_url, timeout=5, allow_redirects=False)
            
            if response.status_code == 200:
                print(f"[✅] ENCONTRADA: {full_url}")
            elif response.status_code == 403:
                print(f"[🔒] ACESSO NEGADO: {full_url}")
            elif response.status_code in (301, 302):
                print(f"[↪️] REDIRECIONA: {full_url} -> {response.headers.get('Location')}")
            elif response.status_code == 404:
                print(f"[❌] NÃO EXISTE: {full_url}")
            else:
                print(f"[⚠️] CÓDIGO {response.status_code}: {full_url}")

        except requests.exceptions.RequestException:
            print(f"[🚫] ERRO AO ACESSAR: {full_url}")

if __name__ == "__main__":
    print("🛠️  DIGITE A URL BASE (ex: site.com ou http://site.com)")
    user_url = input(">>> ").strip()
    test_url(user_url)
    print("\n✔️ Busca concluída!")