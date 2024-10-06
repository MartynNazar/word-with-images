from PIL import Image, ImageEnhance, ImageFilter

image = Image.open("images.jfif")


while True:
    print("1. Показати зображення")
    print("2. Зберегти зображення")
    print("3. Зробити ч/б")
    print("4. Поворот зображення")
    print("5. Відзеркалення зображення")
    print("6. Збільшення яскравості")
    print("7. Розмивання зображення")
    print("8. Накладення контурів")
    print("9. Тиснення зображення")
    print("10. Накладання контурів")
    print("11. Збільшення деталізації зображення")
    operation = input("Введіть операцію")
    if operation == "1":
        image.show()
    elif operation == "2":
        name = input("введіть назву файлу")
        image.save(name)
    elif operation == "3":
        image = image.convert("L")
    elif operation == "4":
        image = image.transpose(Image.ROTATE_90)
    elif operation == "5":
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
    elif operation == "6":
        image = ImageEnhance.Brightness(image).enhance(1.5)
    elif operation == "7":
        image = image.filter(ImageFilter.BLUR)
    elif operation == "8":
        image = image.filter(ImageFilter.CONTOUR)
    elif operation == "9":
        image = image.filter(ImageFilter.EMBOSS )
    elif operation == "10":
        image = image.filter(ImageFilter.CONTOUR)
    elif operation == "11":
        image = image.filter(ImageFilter.DETAIL  )









