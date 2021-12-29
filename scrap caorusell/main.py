from bs4 import BeautifulSoup
import requests

html_doc = requests.get(' https://id.carousell.com/categories/electronics-cameras-and-gadgets-7/')
# print(html_doc.text)

soup = BeautifulSoup(html_doc.text, 'html.parser')
laptop_terpopuler = soup.find(attrs={'class':'D_o'})

titles = laptop_terpopuler.findAll(attrs={'class':'D_qp'})

for title in titles:
    print(title.find('p',attrs={'class':'D_eS D_eC D_eT D_eW D_eZ D_fb D_fe D_eP'}))
# titles = laptop_terpopuler.findAll(attrs={'class':'D_qp'})
#
# for title in titles:
#     print(title.text)
