from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict


url = 'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'
conn = urlopen(url)

raw_data = conn.read()
html_content = raw_data.decode('utf-8')

with open('abc.html','wb') as f:
    f.write(raw_data)

soup = BeautifulSoup(html_content,'html.parser')
table = soup.find('table', id='tableContent')

tr_list = table.find_all('tr')
tbl_list = []
for tr in tr_list:
    trs = tr.find_all('td')
    dic = {}
    for i in range(len(trs)):
        if trs[i].string != None:
            if i == 0:
                dic['Các danh mục'] = trs[i].string.strip()
            elif i == 1 :
                dic['Quý 4 - 2016'] = trs[i].string.strip()
            elif i == 2 :
                dic['Quý 1 - 2017'] = trs[i].string.strip()
            elif i == 3 : 
                dic['Quý 2 - 2017'] = trs[i].string.strip()
            elif i == 4 :
                dic['Quý 3 - 2017'] = trs[i].string.strip()
            elif i == 5 :
                dic['Tăng Trưởng'] = trs[i].string.strip()
    if dic != {}:
        tbl_list.append(dic)

pyexcel.save_as(records = tbl_list,dest_file_name='btk.xlsx')
