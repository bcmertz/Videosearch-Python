#most current version of our server that can handle streams and uploaded videos
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import requests
import cgi
import cgitb
from io import StringIO
import pycurl
import json
from io import BytesIO
import math
import numpy as np
import time
from skimage.measure import structural_similarity as ssim
import cv2
import boto3
from video import parseVideo, awsSave, arr1
# from stream import parseStream, awsSave, sendNode


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        print ("in post method")
        #boilerplate to get the data from the node post to here
        cgitb.enable()
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        videoFile = post_body.decode("utf-8")
        print('videoFile address', videoFile)

        fileType = videoFile[0]
        if fileType == 's':
            print('upload type : stream')
            videoFile = videoFile[1:len(videoFile)]
            parseStream(videoFile)

        if fileType == 'f':  #if the type is file
            print('upload type : file')
            videoFile = videoFile[1:len(videoFile)]  #the f was appended to the beginning of the string here we get rid of that
            print("videoFile:", videoFile)
            parseVideo(videoFile)  #go frame by frame and save relevant frames
            print ("Video Parsing Complete, sending data to node server")

        #POST BACK TO NODE SERVER THE LINKS FROM AWS
        payload = {
        'source': arr1,
        'url': videoFile
        }
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        res = requests.post('http://localhost:3000/predict', headers=headers, data=json.dumps(payload))
        del arr1[0:len(arr1)]
        print('Cleared data, ready to go again')
        return

def run(server_class=HTTPServer, handler_class=Handler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print ('python server running')
    httpd.serve_forever()
def main():
    print ("in main")
    run()
if __name__ == '__main__':
    # execute video parsing code
    main()
