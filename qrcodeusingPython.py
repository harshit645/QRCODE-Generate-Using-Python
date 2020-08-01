#pip install pyqrcode
import pyqrcode

#pip install pypng
import png

#any url
url="https://www.google.com"

#it creates our qrcode
qr=pyqrcode.create(url)

#it converts our qr into png format
#scale decides the size of qrcode
#more the value of scale more the size of image
#qrGoogle is name of our qrcode image
#G:\\, it is the location at which our qrcode download
qr.png("G:\\qrGoogle.png",scale=6)
