#Many are not needed I think...
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
#Basically the url stored in a simple variable
urlcom= apodurl + mykey
link = urllib.request.urlopen(urlcom, context=myContext)

apodread= link.read()
decodeapod= json.loads(apodread.decode('utf-8'))
#The url of the jpeg
myurl=decodeapod['hdurl']

@app.route('/')
def nasaapi():
    #Taking the small details from the api such as the title, explanation, and date
    return render_template('page.html',APOD= myurl)+ "<b>Title:</b>" + decodeapod['title'] + "<br>" +"<b>Date:</b>"  +decodeapod['date']+"<br>" "<b>Explanation:</b> " + "<br>" + decodeapod['explanation']
    
#When you save any changes on your file, you just have to refresh your page for changes to take place

if __name__ == '__main__':
    app.run(debug=True)
