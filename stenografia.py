# from stegano import lsb

# secret = lsb.hide(r"img/1.png", "привет подружка")
# secret.save(r"img/1_secret.png")

# result = lsb.reveal(r"img/1_secret.png")
# print(result)

# from stegano import exifHeader

# secret = exifHeader.hide("img/2.jpg", "img/2_secret.jpg", "привет подруга")

# result = exifHeader.reveal("img/2_secret.jpg")
# result = result.decode()
# print(result)