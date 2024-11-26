from PIL import Image, ImageTk
import os
import datetime

def get_image_info(image_path):
    img = Image.open(image_path)
    
    resized_img = img.resize((560, 650))
    photo = ImageTk.PhotoImage(resized_img)
    
    return photo, resized_img, img.size

def get_image_details(image_path, resized_img, original_size):
    file_size = os.path.getsize(image_path)
    file_size_mb = file_size / (1024*1024)
    if file_size_mb >= 1:
        file_size_str = f"{file_size_mb:.2f} MB"
    else:
        file_size_str = f"{file_size / 1024:.2f} KB"
    
    image_width, image_height = original_size
    creation_date = datetime.datetime.fromtimestamp(os.path.getctime(image_path)).strftime('%Y-%m-%d %H:%M:%S')
    
    info_text = f"Размер файла: {file_size_str}\nРазмер изображения: {image_width}x{image_height} (Оригинал)\nДата создания: {creation_date}"
    return info_text