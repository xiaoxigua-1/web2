from flask import Flask
import flask
import os
import random
import subprocess
import zipfile
import shutil
app = Flask(__name__)
@app.route("/spotify/")
def spotify():
    url=flask.request.args.get("url")
    dl=os.listdir("dl")
    filename=flask.request.args.get("filename")
    if filename in dl :
        return '重新輸入名稱'
    #下載spotift歌曲
    if str(url).startswith("https://open.spotify.com/track/"):
        cmd="spotdl -f dl/%s.{output-ext} --song %s"%(filename,url)
        subprocess.call(cmd, shell=True) 
        w=flask.send_file(f"dl\\{filename}.mp3")
        return  w
    elif str(url).startswith("https://open.spotify.com/playlist"):
        cmd=f"spotdl --write-to dl/{filename}.txt --playlist {url}"
        subprocess.call(cmd, shell=True)
        os.mkdir(f'dl/{str(filename)}')
        cmd="spotdl -f dl/%s/{track-name}.{output-ext} --list dl/%s.txt"%(filename,filename)
        subprocess.call(cmd, shell=True)
        os.remove(f"dl/{filename}.txt")
        zipf=zipfile.ZipFile(f"dl\\{filename}.zip","w")
        dlp=os.listdir(f"dl/{filename}")
        for p in dlp :
            zipf.write('dl/%s/%s'%(filename,p))
        shutil.rmtree(f"dl/{filename}")
        w=flask.send_file(f"dl/{filename}.zip")
        return w
def main():
    if __name__ == "__main__":
        print("開啟中")
        app.run()
main()
