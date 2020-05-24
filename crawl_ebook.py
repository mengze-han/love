import requests
from bs4 import BeautifulSoup
import re
from tqdm import tqdm
from PIL import Image
import os
import img2pdf



def get_request(url):
    a = requests.get(url)
    a.encoding='utf-8'
    soup = BeautifulSoup(a.text,"html.parser")
    div = soup.select('.article')
    img_list = []
    for img in div:
        p = img.select('p')
        if len(p):
            im = img.select('img')
            for j in im:
                jpg = re.findall(r'\bhttp\S*?jpeg\b',str(j))
                img_list.append(jpg)
    return img_list

def save_img(img_list):
    os.mkdir("./src") if not os.path.exists("./src") else None
    for index, img in tqdm(enumerate(img_list)):
        f = requests.get(img[0])
        file_name = "./src/{}.jpg".format(index)
        with open(file_name, 'wb') as file:
             file.write(f.content)

def generate_pdf():
    os.mkdir("./pdf") if not os.path.exists("./pdf") else None
    jpgs = os.listdir('./src')
    jpg = [jpg for jpg in jpgs if 'jpg' in jpg]

    ss = [int(i.split('.')[0]) for i in jpg]
    ss.sort()
    ss = ["./src/{}.jpg".format(i) for i in ss]
    print(ss)
    pdf_file = img2pdf.convert(ss)
    with open("./pdf/name.pdf","wb") as f:
         f.write(pdf_file)



url = "https://www.sohu.com/a/235865982_796524"

imgs = get_request(url)
save_img(imgs)
generate_pdf()