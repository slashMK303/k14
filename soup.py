import requests
from bs4 import BeautifulSoup

url = "https://github.com/Hashmmath/Python-Basic-Codes"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Temukan semua tag <p> dalam dokumen
paragraphs = soup.find_all('p')

# Untuk setiap paragraf, cetak teksnya
for paragraph in paragraphs:
    print(paragraph.text)
    with open("soup.txt", "w") as f:
        f.write(paragraph.text)
