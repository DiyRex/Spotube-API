from flask import Flask, request, send_file, render_template, redirect
from io import BytesIO
import logging
import sys
import os
import json
import gunicorn
import uvicorn
import spotify
import ytdl

print("Server is running :)")
print(".....................")

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

APP_NAME = os.environ.get('APP_NAME')
host_url = "https://" + APP_NAME + ".herokuapp.com"


app = Flask(__name__)

@app.before_first_request
def initialize():
  print("Initializing...")

@app.route("/")
def runner():
  info =  {"Stats":"Server Running !!!","Owned by":"DiyRex :)","Usage":[{"Get Data from Spotify":host_url+"/spotube?url=[url]"},{"Download Audio from YT": host_url+"/audio?url=[url]"}]}
  return info

@app.route('/spotube',methods=['GET'])
def spotube():
    audio = request.args.get('url')
    json_data = spotify.spotify_dl(url=audio,ytdl_url=host_url+"/audio?url="+audio)
    return json_data

@app.route("/audio", methods=['GET', 'POST'])
def download_audio():
    youtube_url = request.args.get('url')
    print(youtube_url)
    audio = ytdl.download_audio(youtube_url)
    file_bytes = b""
    with open(audio[1], "rb") as f:
        file_bytes = f.read()
    return send_file(
         audio[1], 
         mimetype="audio/mpeg", 
         as_attachment=True, 
         attachment_filename=audio[0])


if __name__ == "__main__":
    app.run(threaded=True, port=5000, debug=True, use_reloader=False)
