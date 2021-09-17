import os
import requests
import re
from bs4 import BeautifulSoup


def get_name_from_url(url):
    result = re.split(r'//', url)[1]
    result = re.sub(r'\W', '-', result)
    result += '.html'
    return result


def get_content_folder_name(file_name):
    _, ext = os.path.splitext(file_name)
    return file_name.replace(ext, '_files')


def download_content(response, content_path, base_url):
    # os.mkdir(content_path)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    urls = [img['src'] for img in img_tags]
    for url in urls:
        file_name = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
        print(file_name)
        if not file_name:
            print("Regex didn't match with the url: {}".format(url))
            continue
        with open(content_path + '/' + file_name, 'wb') as f:
            if 'http' not in url:
                url = '{}{}'.format(base_url, url)
            response = requests.get(url)
            f.write(response.content)


def download(output_path, url):
    response = requests.get(url, allow_redirects=True)
    file_name = get_name_from_url(url)
    content_folder_name = get_content_folder_name(file_name)
    content_path = output_path + '/' + content_folder_name
    download_content(response, content_path, url)
    output_path += '/' + file_name
    with open(output_path, 'w') as file_:
        file_.write(response.text)
    return output_path
