import qrcode

def generate_image(data):
    img = qrcode.make(data)
    img.save("qr_image.png")

if __name__ == "__main__":
    url = input("Input the url: ")
    generate_image(url)