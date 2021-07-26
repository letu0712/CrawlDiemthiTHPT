from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
import re

f1 = open("ToHopTuNhien.csv","a")
f2 = open("ToHopXaHoi.csv","a")


header1 = "SBD, Toan, Van, Ly, Hoa, Sinh, Anh,\n"
f1.write(header1)

header2 = "SBD, Toan, Van, Su, Dia, GDCD, Anh,\n"
f2.write(header2)



#Fake trình duyệt tránh bị ktra robot
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

brower = webdriver.Chrome(executable_path='chromedriver.exe')

link = 'https://diemthi.tuyensinh247.com/diem-thi-tot-nghiep-thpt/bac-ninh-59.html'
brower.get(link)


for i in range(19000101,19016389):
    sbd = brower.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div[3]/div[2]/div[1]/div[2]/div/input')
    sbd.clear()
    sbd.send_keys(str(i))

    btxem = brower.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div[3]/div[2]/div[1]/div[3]/input[2]')
    btxem.click()

    resp = requests.get(link, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')

    result = brower.find_elements_by_id('result')

    result_data = result[0].text
    print(result_data)
    try:
        x = re.search(r'[0-9]{8}', result_data)
        sbd = x.group(0)
        print(sbd)
    except:
        continue

    diem_data = result_data.split(';')
    print(diem_data)
    try:
        try:
            toan = diem_data[0].split('Môn Toán: ')[1]
            van = diem_data[1].split('Môn Văn: ')[1]
            ly = diem_data[2].split('Môn Lý: ')[1]
            hoa = diem_data[3].split('Môn Hóa: ')[1]
            sinh = diem_data[4].split('Môn Sinh: ')[1]
            anh = diem_data[5].split('Môn Ngoại ngữ: ')[1]
            dsdiem = f'{sbd},{toan}, {van}, {ly}, {hoa}, {sinh}, {anh},\n'
            f1.write(dsdiem)

        except:
            toan = diem_data[0].split('Môn Toán: ')[1]
            van = diem_data[1].split('Môn Văn: ')[1]
            su = diem_data[2].split('Môn Sử: ')[1]
            dia = diem_data[3].split('Môn Địa: ')[1]
            gdcd = diem_data[4].split('Môn Giáo dục công dân: ')[1]
            anh = diem_data[5].split('Môn Ngoại ngữ: ')[1]
            dsdiem = f'{sbd},{toan}, {van}, {su}, {dia}, {gdcd}, {anh},\n'
            f2.write(dsdiem)

    except:
        continue

f1.close()
f2.close()

