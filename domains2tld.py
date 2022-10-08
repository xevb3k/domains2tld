import requests
import csv
from tldextract import extract

file_url = 'https://hell.sh/hosts//domains.txt'
file_object = requests.get(file_url)

with open('domains.txt', 'wb') as local_file:
    # скачиваем файл
    local_file.write(file_object.content)
with open('domains.txt') as local_file:
    # создаем список доменов, игнорируя технически и пустые строки
    domains = [row.strip() for row in local_file if row.strip() and row[0] != '#' and row[0:3] != 'www']
   
# выделяем TLD
tlds = list(map(lambda tld: '.'.join([tld.domain, tld.suffix]), map(extract, domains)))

# сохраняем в csv [домен,TLD]
with open('result.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerow(['domain', 'tld'])   # заголовок для csv, можно убрать
    for domain, tld in zip(domains, tlds):
        writer.writerow([domain, tld])
