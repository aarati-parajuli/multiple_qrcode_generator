import qrcode

data={'dalle':'https://dalle.com.np/', 'daddys':'https://daddys-kitchen-the-cafe-and-restaurant.business.site/'}
for keys in data:
        qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=5,

        )
        qr.add_data(data[keys])
        qr.make(fit=True)
        img = qr.make_image(fill_color='red', back_color='white')
        img.save('qr'+keys+'.png')