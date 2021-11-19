import qrcode
import image

qr = qrcode.QRCode(
    version=40,  # shows the complexity, higher the number greater the complexity(between 1 to 40 )
    box_size=10,  # size of the box
    border=5  # the white border around the image
)
data = "https://www.youtube.com/watch?v=onHPipeASdk&list=PLpp8-k7G_6Y3Wj1suZQ-9lATFzFuGw93x6"
# the data can be anything from url to normal text or special code


qr.add_data(data)  # adding data to the qr object
qr.make(fit=True)  # creating the code
img = qr.make_image(fill="blue", back_color="red")  # creating the qr image, color can be of any choice
img.save("test1.jpg")  # saving the image in a file
