import requests
import re


def get_name_from_url(url):
    result = re.split(r'//', url)[1]
    result = re.sub(r'\W', '-', result)
    result += '.html'
    return result


def download(output_path, url):
    page_obj = requests.get(url, allow_redirects=True)
    output_path += '/' + get_name_from_url(url)
    with open(output_path, 'w') as file_:
        file_.write(page_obj.text)
    return output_path
