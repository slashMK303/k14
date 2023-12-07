import requests
from bs4 import BeautifulSoup
import pandas as pd  # analisi data

# url = "https://id.wikipedia.org/wiki/Windah_Basudara"
url = input("Masukan url yang anda ingin analisis : ")
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

headers = []

for header in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
    text = header.text.strip()
    level = header.name
    headers.append((text, level))

df = pd.DataFrame(headers, columns=["Text", "Level"])
df.index += 1
print(df)

# mengambil nama untuk nama file dari akhir sampai bertemu "/"
name = url.split("/")[-1]

output_file = f"output/{name}.txt"

with open(output_file, "w") as f:
    for index, row in df.iterrows():
        f.write(f"Text: {row['Text']}\nLevel: {row['Level']}\n\n")
