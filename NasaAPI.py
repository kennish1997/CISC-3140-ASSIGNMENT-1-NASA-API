import urllib.request
from urllib.request import urlopen
import json
import requests
import ssl
from flask import Flask,render_template
import webbrowser

app=Flask(__name__)
myContext = ssl.SSLContext()

apodurl= 'https://api.nasa.gov/planetary/apod?'
mykey= 'api_key=FaBTaAnCYyPyLrXYkbiUjyBPJRJQmsgDPcsLRMM1'
urlcom= apodurl + mykey
link = urllib.request.urlopen(urlcom, context=myContext)
apodread= link.read()
decodeapod= json.loads(apodread.decode('utf-8'))
myurl=decodeapod['hdurl']

@app.route('/')
def nasaapi():
    return render_template('page.html',APOD= myurl)+ "<b>Title:</b>" + decodeapod['title'] + "<br>" +"<b>Date:</b>"  +decodeapod['date']+"<br>" "<b>Explanation:</b> " + "<br>" + decodeapod['explanation']
    
    
app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True)
