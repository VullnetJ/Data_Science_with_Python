import urllib
from urllib import request
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = request.urlopen('http://py4e-data.dr-chuck.net/comments_875541.html').read()
my_list = list()
count_tags = 0

soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
for tag in tags:
    count_tags = count_tags + 1
    content = int(tag.contents[0])
    my_list.append(content)
    print('Counting: ', count_tags)
    print('Sum is: ', sum(my_list))

    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)