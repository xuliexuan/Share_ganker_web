import qrcode
import Image

qr = qrcode.QRCode(
    version=10,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1
)
qr.add_data("http://weibo.com/234892007")
qr.make(fit=True)

img = qr.make_image()
img = img.convert("RGBA")

icon = Image.open("/home/ganker/lxxu/Web_lxxu/Blog_lxxu/static/icon/twitter.ico")

img_w, img_h = img.size
factor = 4
size_w = int(img_w / factor)
size_h = int(img_h / factor)

icon_w, icon_h = icon.size
if icon_w > size_w:
    icon_w = size_w
if icon_h > size_h:
    icon_h = size_h
icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

w = int((img_w - icon_w) / 2)
h = int((img_h - icon_h) / 2)
img.paste(icon, (w, h), icon)

img.save("/home/ganker/lxxu/Web_lxxu/Blog_lxxu/static/images/lxxu.png")
