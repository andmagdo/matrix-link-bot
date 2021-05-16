from urllib.parse import urlparse
from os.path import splitext
import magic
import requests

mimes = ["video", "image"]  # Note, only checks five characters! - for now, hardcoded, maybe put in a config?
mime = magic.Magic(mime=True)


def getType(url):  # Used to find the file and extension
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    root = root.replace('/', '')  # remove slashes
    ext = ext.replace('/', '')
    return root, ext


def checkType(path):  # Uses magic to get a base mime type, then checks it
    typemime = mime.from_file(path)  # get mime
    return checkMIME(typemime)


def checkContent(url):
    r = requests.get(url, stream=True)
    contentType = r.headers['Content-Type'].split(';')[0]
    return checkMIME(contentType)


def checkMIME(mimeType):
    for x in mimes:
        if mimeType[0:5].lower() == x[0:5]:
            return mimeType  # Whatever mimeType is, it will be truthy
    return False


def getName(url):
    return ".".join(getType(url))  # separated because I am too lazy to put them together
