import requests
import re
import os

def access(url, headers):
    response = requests.get(url, headers=headers)
    html = response.text
    return html

def photo_url(html):
    photo_urls = re.findall(r'<li><a href="(.+)" .+<img', html)
    titles = re.findall(r'data-original=\'.+ alt=\'(.+)\' w', html)
    return zip(titles, photo_urls)

def photo_choose(group):
    for i in range(len(group)):
        print(f'{i}->',group[i][0] )
    while True:
        try:
            choose = int(input('��������ҪDownload��ͼ���ţ�'))
            if not (0 <= choose <= len(group)):
                raise ValueError
            break
        except ValueError:
            print('����������ı�ų�����Χ���������')
    try:
        os.mkdir(f'{group[choose][0]}')
    except OSError:
        pass
    os.chdir(f'{group[choose][0]}')
    return choose

def save_original(count, group, headers):
    photo_url = group[count][1]
    response = requests.get(photo_url, headers=headers).text
    page = int(max(re.findall(group[count][1] + r'/(\d+)', response)))
    for i in range(1, page + 1):
        url = photo_url + f'/{i}'
        rep = requests.get(url, headers=headers).text
        photo_urls = re.findall(r'<img src="(.+\.jpg)" alt=', rep)
        print(f'�������ص�{i}��', end='')
        save_photo(photo_urls[0], group[count][0], headers, i)
        print('���سɹ�!')
    ask = input('�Ƿ�������أ�������"Quit"�˳�����')
    return ask

def save_photo(url, title, headers, count):
    with open(title + f'{count}.jpg', 'wb') as f:
        response = requests.get(url, headers=headers)
        f.write(response.content)

def main(url, headers):
    html = access(url, headers)  
    group = list(photo_url(html))  
    while True:
        choose = photo_choose(group)  
        a = save_original(choose, group, headers)  
        if a == 'Quit' :
            break

base_url = 'https://www.mzitu.com/'
headers = {
    'Referer': 'https://www.mzitu.com/',
    'Sec-Fetch-Dest': 'image',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

if __name__ == '__main__':
    main(base_url, headers)
