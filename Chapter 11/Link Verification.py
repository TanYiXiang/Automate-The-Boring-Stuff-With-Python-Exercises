# Author: Tan Yi Xiang
# Source: Automate the Boring stuff with python Ch. 11 Project
from urllib.parse import urljoin

import requests
import bs4

url = input('Type in the url you want to verify:\n')
brokenLinkNo = 0
goodLinkNo = 0
urlResponse = requests.get(url)

try:
    urlResponse.raise_for_status()
except requests.exceptions.HTTPError:
    print('Status message: ' + urlResponse.status_code)

urlResponseSoup = bs4.BeautifulSoup(urlResponse.text, 'html.parser')
urlLinks = urlResponseSoup.select('a')

for link in urlLinks:
    link_url = urljoin(url, link.get('href'))
    linkResponse = requests.get(link_url)

    try:
        linkResponse.raise_for_status()
        goodLinkNo += 1
        print('Good link:' + str(link_url))

    except requests.exceptions.HTTPError:
        print("Broken link: " + link_url)
        brokenLinkNo += 1

print("There are " + str(goodLinkNo) + " good links on this url.")
print("There are " + str(brokenLinkNo) + " broken links on this url.")
