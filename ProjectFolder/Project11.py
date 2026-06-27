#qrcode generator
import qrcode
num=int(input("Enter the number of url or text to generate: "))
temp=num
while temp:
    data=input("Enter the text or URL for the OR code: ")
    filename=f'qr_{num-(temp-1)}.png'
    qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )#object.we need diff object each time to store diff qrcodes
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black",back_color="white")
    img.save(filename)
    print(f'QR code saved as {filename}')
    temp-=1
