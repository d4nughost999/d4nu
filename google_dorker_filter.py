# google_dorker_filter_color.py
import time
import random
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# List User-Agent biar ga ketauan bot
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; rv:109.0) Gecko/20100101 Firefox/117.0"
]

print(Fore.CYAN + r"""
   ____                   _      
  / _| _   _    _| | ___ 
 | |  _ / _ \ / _ \ / _` | |/ _ \
 | |_| | (_) | (_) | (_| | |  __/
  \__|\_/ \_/ \, |_|\___|
                    |___/        
""" + Style.RESET_ALL)

print(Fore.YELLOW + "   Google Dorker v2 - Filter Mode" + Style.RESET_ALL)
print(Fore.MAGENTA + "   Author: d4nu-ghost 🕶️" + Style.RESET_ALL)

query = input(Fore.CYAN + "\n[?] Masukkan dork query: " + Style.RESET_ALL)
pages = int(input(Fore.CYAN + "[?] Ambil berapa halaman (1 halaman ≈ 10 hasil): " + Style.RESET_ALL))
domain_filter = input(Fore.CYAN + "[?] Filter domain (misal: .id / .go.id / .sch.id) atau kosong untuk semua: " + Style.RESET_ALL)

urls = []

for page in range(pages):
    start = page * 10
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    url = f"https://www.google.com/search?q={query}&start={start}"

    print(Fore.YELLOW + f"[+] Fetching page {page+1} -> {url}" + Style.RESET_ALL)
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    for link in soup.select("a"):
        href = link.get("href")
        if href and href.startswith("/url?q="):
            clean = href.split("/url?q=")[1].split("&")[0]
            if "google.com" not in clean:
                if domain_filter == "" or domain_filter in clean:
                    urls.append(clean)
                    print(Fore.GREEN + "  -> " + clean + Style.RESET_ALL)

    # Delay random biar aman
    time.sleep(random.uniform(2, 5))

save = input(Fore.CYAN + "\nSimpan hasil ke file? (y/n): " + Style.RESET_ALL)
if save.lower() == "y":
    fname = "google_dork_results.txt"
    with open(fname, "w") as f:
        for u in urls:
            f.write(u + "\n")
    print(Fore.GREEN + f"[+] Hasil tersimpan di {fname}" + Style.RESET_ALL)
