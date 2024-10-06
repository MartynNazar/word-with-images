from PIL import Image

image = Image.open("images.jfif")
image.show()

rotated_image = image.rotate(90)
rotated_image.show()
rotated_image.save("rotated_image.png")

