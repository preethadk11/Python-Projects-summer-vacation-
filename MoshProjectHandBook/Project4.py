#OR Code Generator
import qrcode
qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
text=input("Enter the text or URL for the QR code: ")
file=input("Enter the filename: ")
color,back=input("Enter fill_color and back color: ").split()
qr.add_data(text)
qr.make(fit=True)
img=qr.make_image(fill_color=color,back_color=back)
img.save(file)
print(f'QR code saved as {file}')