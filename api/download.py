from urllib.request import urlretrieve
from api.link_detector import getName, checkType, checkContent
from os.path import isdir
from os import mkdir, remove
import youtube_dl


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


def checkUrl(url):  # checks if mime type matches the allowed
    if not isdir(folder):  # Makes sure folder exists
        mkdir(folder)

    if not checkContent(url):  # Checks first if the url headers return a correct type, if not, passes to youtube_dl 
        return youtube(url)
    
    path = download(url)
    if not path:  # If download(url) returns false, stop, as the download failed
        return False
    
    if not checkType(path):  # Checks if the mime type is listed, if not, it deletes and stops
        remove(path)
        return False
    
    return path  # If it makes it through the checks, checkurl returns where the caller can find it


def youtube(url):
    if url[0:32] == 'https://www.youtube.com/watch?v=':  # Naming the file by its youtube id
        urlName = url[32:43]
    elif url[0:17] == 'https://youtu.be/':  
        urlName = url[17:28]
    else:  # Else, not part of a youtube link, but still may be supported, naming by url
        urlName = url[:8]
        urlName = f'{urlName}'.replace('/', '')
    
    ydl = youtube_dl.YoutubeDL({'outtmpl': f'{folder}/{urlName}', 
                                'noplaylist': True,
                                'merge-output-format': 'mp4',
                                'format': "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]"})

    try:
        with ydl:
            ydl.extract_info(url)
        ydl.download(url)
        return f'{folder}/{urlName}'
    except youtube_dl.utils.DownloadError:
        return False

