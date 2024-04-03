import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# WebDriver'ı yapılandırma ve web sayfasını açma
service = Service('/path/to/chromedriver')  # ChromeDriver'ın konumunu belirtin
driver = webdriver.Chrome(service=service)
driver.get('')  # Veri kazıyacağınız web sayfasının URL'sini belirtin

# Tabloyu bulma ve verileri çekme
table = driver.find_element(By.CLASS_NAME, 'dataframe')
table_data = []
headers = []

# Tablodaki başlıkları alın
header_elements = table.find_elements(By.TAG_NAME, 'th')
for header in header_elements:
    headers.append(header.text)

# Tablodaki satırları alın
rows = table.find_elements(By.TAG_NAME, 'tr')
for row in rows:
    row_data = []
    cells = row.find_elements(By.TAG_NAME, 'td')
    for cell in cells:
        row_data.append(cell.text)
    table_data.append(row_data)

# CSV dosyasına yazma
with open('population_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(table_data)

# WebDriver'ı kapatma
driver.quit()
