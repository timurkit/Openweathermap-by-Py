import requests, xml.etree.ElementTree as ET
res=requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
root=ET.fromstring(res)
one_nok=float(root[18][4].text.replace(',','.'))/int(root[18][2].text)  
one_huf=float(root[7][4].text.replace(',','.'))/int(root[7][2].text)
nok_in_sol=one_nok*(1/one_huf)
print('1 NOK =',round(nok_in_sol,4),'HUF')