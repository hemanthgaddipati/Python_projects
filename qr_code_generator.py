'''
QR CODE Generator: 
    Write a program to generate a QR code based on user input, such as text or a
    URL. The QR code should be saved as an image file that can be scanned with a
    smartphone.
    
    <TODO>
    
    Optional Enhancements
        • Add options for the user to choose the color of the QR code. This will allow
          users to generate QR codes that match their style or branding.
        • Implement a feature that lets the user generate multiple QR codes at once by
          providing a list of URLs or texts. Each QR code should be saved with a unique filename.
'''

import qrcode

data = input('Enter the Text or URL: ').strip()
filename = input('Enter the filename: ').strip()
qr = qrcode.QRCode(box_size = 10, border = 4)
qr.add_data(data)
image = qr.make_image(fill_color = 'black', back_color = 'white')
image.save(filename)
print(f'QR code saved as {filename}')
