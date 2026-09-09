async def photo():
    from PIL import Image
    import os
    from pathlib import Path
    import imagehash
    # Укажите путь к вашей папке
    folder = Path("./obuch")
    # Ищем файлы с расширением .jpg
    image_paths = [str(p) for p in folder.glob("*.jpg") if p.is_file()]
    for path in image_paths:
        img=Image.open(f"{path}")
        hash1200=imagehash.phash(img)
        print(hash1200)
        resized=img.resize((800,800))
        hash800 = imagehash.phash(resized)
        print(hash800)
        resized2 = img.resize((400, 400))
        hash400 = imagehash.phash(resized2)
        print(hash400)

