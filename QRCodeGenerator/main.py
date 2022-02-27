import qrcode

feat=qrcode.QRCode(version=1,box_size=10,border=4)
feat.add_data(input("Enter the link for which QR is to be generated: "))
feat.make(fit=True)
gen_image=feat.make_image(fill_color="black",back_color="white")
gen_image.save('My_QRCODE.png')