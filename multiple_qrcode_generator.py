import qrcode
import json
data={'dalle':'https://dalle.com.np/', 'daddys':'https://daddys-kitchen-the-cafe-and-restaurant.business.site/'}

#with open('data.txt') as json_file:
    #data = json.load(json_file)
save_path=r'C:\Users\Aarati\Documents\GitHub\multiple_qrcode_generator\media/'
for keys in data:
        qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=5,

        )
        qr.add_data(data[keys])
        qr.make(fit=True)
        img = qr.make_image(fill_color='red', back_color='white')
        name = save_path + 'qr'+keys + '.png'
        img.save(save_path+'qr'+keys+'.png')
        #file1 = open(name, "w")
        #file1.write(name)