import requests
from bs4 import BeautifulSoup
import docx2txt
import docx

# URL halaman website yang ingin disalin
url = 'https://www.scraping-bot.io/'

# Lakukan permintaan HTTP ke URL
response = requests.get(url)

# Buat objek BeautifulSoup dari respons HTTP
soup = BeautifulSoup(response.content, 'html.parser')

# Dapatkan semua teks dari halaman website
text = soup.get_text()

# Buat objek dokumen docx
doc = docx.Document()

# Tambahkan teks ke dokumen docx
doc.add_paragraph(text)

# Simpan dokumen docx
doc.save('output.docx')
