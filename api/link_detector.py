from urllib.parse import urlparse
from os.path import splitext

extensions = ["jpg", "jpeg", "png", "tif", "tiff", "gif", "mp4", "bmp", "mkv", "webp", "heif", "svg", "txt",
              "md", "mp3"]


def getType(url):
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    return root[1:], ext[1:]


def checkType(url):
    extension = getType(url)[1].lower()
    for x in extensions:
        if extension == x:
            return True
    return False


def getName(url):
    return ".".join(getType(url))


def checkAndGet8Link(url):
    if checkType(url):
        return getName(url)
    return None
