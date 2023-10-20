import requests
from bs4 import BeautifulSoup

# URL halaman website yang ingin disalin
url = 'https://example.com'

# Lakukan permintaan HTTP ke URL
response = requests.get(url)

# Buat objek BeautifulSoup dari respons HTTP
soup = BeautifulSoup(response.content, 'html.parser')

# Dapatkan semua konten halaman website
content = soup.get_text()

# Salin konten halaman website ke file
with open('page_content.txt', 'w') as f:
    f.write(content)
