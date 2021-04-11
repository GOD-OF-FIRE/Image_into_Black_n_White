from PIL import Image
img=Image.open("C:\\Users\\kusha\\Desktop\\IMG_20210228_115545.jpg")
blackAndWhite = img.convert("L")
blackAndWhite.save('bw_kushagra.png')
blackAndWhite.show()