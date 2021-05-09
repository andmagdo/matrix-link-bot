from urllib.request import urlretrieve
from api.link_detector import getName, checkType
from os.path import isdir
from os import mkdir, remove

folder = "Downloads"  # for now, the folder is hardcoded


def download(url):  # Downloads url to folder
    if not isdir(folder):  # Makes sure folder exists
        mkdir(folder)
    path = f"{folder}/{getName(url)}"
    if path == f"{folder}/.":  # Makes sure not to have "[Errno 21] Is a directory"
        path = f"{folder}/noName"
    try:
        urlretrieve(url, path)
    except Exception as e:  # Prints exception to terminal and stops
        print(f"{url} - {e}")
        return False
    return path


def checkUrl(url):  # downloads url to check if mime type matches the listed
    path = download(url)
    if not path:  # If download(url) returns false, return that the url is not part of the mime types
        return False
    if not checkType(path):  # Checks if the mime type is listed, if not, it deletes and stops
        remove(path)
        return False
    return path  # If it makes it through the checks, checkurl returns where the caller can find it
