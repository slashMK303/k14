import requests
from bs4 import BeautifulSoup
import pandas as pd


class WebAnalyzer:
    def __init__(self, url):
        self.url = url

    def get_headers(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")

        headers = []

        for header in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
            text = header.text.strip()
            level = header.name
            headers.append((text, level))

        return headers

    def save_to_file(self, headers, output_file):
        with open(output_file, "w") as f:
            for text, level in headers:
                f.write(f"Text: {text}\nLevel: {level}\n\n")


url = input("Masukkan URL yang ingin Anda analisis: ")
analyzer = WebAnalyzer(url)
headers = analyzer.get_headers()

df = pd.DataFrame(headers, columns=["Text", "Level"])
df.index += 1
print(df)

# mengambil nama untuk nama file dari akhir sampai bertemu "/"
name = url.split("/")[-1]

output_file = f"output/{name}.txt"
analyzer.save_to_file(headers, output_file)