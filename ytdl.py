import subprocess
import time
import os
import temp_folder

def download_audio(url):
    path = temp_folder.tmpf()
    time.sleep(3)
    command = r"yt-dlp -f 'ba' -x --audio-format mp3 {0}  -o '{1}/%(title)s.%(ext)s'"
    comm = str(command.format(url,path))
    print(comm)
    process = subprocess.call(comm,shell=True)
    file_name = os.listdir(path) 
    print(file_name)
    file_path = os.path.join(path,file_name[0])
    return file_name[0] , file_path

#download_audio(url="https://www.youtube.com/watch?v=6q6Vh1ZhB8Q")
