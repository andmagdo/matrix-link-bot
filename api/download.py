import urllib.request
from api.link_detector import getName

folder = "Downloads"


def download(url):
    urllib.request.urlretrieve(url, f"{folder}/{getName(url)}")

