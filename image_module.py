import cv2
import math
from PIL import Image


def save_image(input_file_path, image_file):
    """
    イメージファイルを保存する。
    """
    with open(input_file_path, 'wb') as file:
        file.write(image_file)


def image_to_video(input_file_path, output_file_path, time):
    """
    イメージファイルから指定の秒数の動画を作成する。
    """
    video_time = time
    img = cv2.imread(input_file_path)
    width = img.shape[1]
    height = img.shape[0]
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    video = cv2.VideoWriter(output_file_path, fourcc, 20.0, (width, height))

    frame_count = math.ceil(video_time * 20)
    for _ in range(frame_count):
        video.write(img)
    video.release()


def resize_image(input_file_path, output_file_path, width, height):
    """
    ファイルサイズを強制的に width×height に変更する。
    アスペクト比は崩れるので注意する。
    """
    img = Image.open(input_file_path).convert("RGB")
    img_resize = img.resize((width, height))
    img_resize.save(output_file_path)


def check_image_size(input_file_path):
    """
    ファイルサイズを返す。
    """
    image = cv2.imread(input_file_path)
    h, w, _ = image.shape
    image_size = {
        'height': h,
        'width': w,
    }
    return image_size


def trim_image(input_file_path, output_file_path, left, upper, right, lower):
    """
    left, upper, right, lower
    640, 0, 1280, 1280
    """
    image = Image.open(input_file_path)
    croped_image = image.crop((left, upper, right, lower))
    croped_image.save(output_file_path, quality=95)