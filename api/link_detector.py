from urllib.parse import urlparse
from os.path import splitext
import magic

mimes = ["video", "image"]  # Note, only checks five characters! - for now, hardcoded, maybe put in a config?
mime = magic.Magic(mime=True)


def getType(url):  # Used to find the file and extention
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    root = root.replace('/', '')  # remove slashes
    ext = ext.replace('/', '')
    return root, ext


def checkType(path):  # Uses magic to get a base mime type, then checks it
    typemime = mime.from_file(path)  #get mime
    for x in mimes:
        if typemime[0:5].lower() == x[0:5]:  
            return typemime  # Whatever typemine is, it will be truthy
    return False


def getName(url):
    return ".".join(getType(url))  # separated because I am too lazy to put them together
