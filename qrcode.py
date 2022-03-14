#Install the required packages 
pip install qrcode
pip install image

#Import the installed packages 
import qrcode
import image

#version -> Higher the number, more the complexity in QRCode
#box_size -> Size of the box where the QRCode will be displayed
#boreder -> The white borders surrounding all four sides of the QRCode
qr=qrcode.QRCode( version=15, box_size=10, border=5)
data="https://twitter.com/Raja_Kathireshh" # the content that has to converted into a QRCode

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black", back_color="white")
img.save("qrcode.png") #saving the QRCode as an image
