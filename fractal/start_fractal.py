from fractal import paint_koch


depth = int(input("Вкажіть глибину промальовки сніжинки Коха: "))
length = int(input("Вкажіть розмір у пікселях сегмента сніжинки Коха: "))

paint_koch(length=length, depth=depth)