import tkinter
import qrcode

window = tkinter.Tk()
window.title("QR-Generator")
window.geometry("300x100")

def generate_image():
    input = tebox.get(1.0, "end-1c")
    if input != "":
        img = qrcode.make(input)
        img.save("qr_image.png")

label = tkinter.Label(window,text="Ingrese la URL:")
label.pack()
tebox = tkinter.Text(window, height=1, width=30)
genbutton = tkinter.Button(window, text="Generar", command=generate_image)
tebox.pack()

genbutton.pack()
window.mainloop()