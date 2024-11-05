import qrcode
import image

qr = qrcode.QRCode(
    version = 15, # the higher the number, the bigger, complexer the image
    box_size = 10, # size of the window where qr code will be displayed
    border = 5, # the white part of the image
)

data = "https://github.com/Manuel-Sarkisjan" # where do you want to redirect / just write text between quotations marks if you want to display text

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black", back_color="white")
img.save("test.png")

