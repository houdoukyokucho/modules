import cv2
import numpy as np
import moviepy.editor as mp
from PIL import ImageFont, ImageDraw, Image


def combine_video_with_sound(input_video_path, input_sound_path, output_path):
    """
    指定したパスの動画ファイルと音声ファイルを合成し保存する。
    """
    clip = mp.VideoFileClip(input_video_path).subclip()
    clip.write_videofile(output_path, audio=input_sound_path)


def connect_videos(input_file_paths, output_path):
    """
    指定したパスの複数の動画ファイルを結合して保存する。
    """
    clips = []
    for input_file_path in input_file_paths:
        clip = mp.VideoFileClip(input_file_path)
        clips.append(clip)
    final_clip = mp.concatenate_videoclips(clips)
    final_clip.write_videofile(output_path, fps=30)


def separate_video(input_file_path, output_file_path, start_seconds, end_seconds):
    """
    始まりの時間と終わりの時間を秒数で指定し、その間の動画を抽出し保存する。
    """
    cap = cv2.VideoCapture(input_file_path)
    cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    writer = cv2.VideoWriter(output_file_path, fourcc, fps, (cap_width, cap_height))

    for i in range(int(end_seconds * fps)):
        ret, frame = cap.read()
        if ret:
            if int(start_seconds * fps) < i:
                writer.write(frame)
    writer.release()
    cap.release()


def capture_video(input_file_path, output_file_path, capture_seconds, target_frame_in_second='last'):
    """
    時間を秒で指定して動画のキャプチャを保存する。
    target_frame_in_second で 1 秒の内の最初のフレームか、
    最後のフレームかキャプチャの対象を選択できる。
    """
    cap = cv2.VideoCapture(input_file_path)
    cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    last_frame = int(capture_seconds * fps)
    first_frame = int(last_frame - (fps-1))
   
    if target_frame_in_second == 'last':
        target_frame = last_frame
    else:
        target_frame = first_frame

    for i in range(last_frame+1):
        ret, frame = cap.read()
        if ret:
            if i == target_frame:
                cv2.imwrite(output_file_path, frame)


def stack_video_on_video(input_file_path_1, input_file_path_2, output_file_path, end_time):
    """
    動画を合成して保存する。
    """
    # 本体をロードする。
    base_video = mp.VideoFileClip(input_file_path_1)
    # 動画サイズを取得を取得する。
    w,h = moviesize = base_video.size
    #ワイプ動画をロードする。
    wipe_video = (mp.VideoFileClip(input_file_path_2).
            resize((w/3,h)).
            set_pos(('right','bottom')) )
    # 本体とワイプを合成する。
    final_clip = mp.CompositeVideoClip([base_video, wipe_video])
    # 0～x 秒間で書き出す。
    final_clip.subclip(0, end_time).write_videofile(output_file_path, fps=30)


def insert_text_on_video(input_file_path, output_file_path, text, text_rgb, font_size, x, y, stroke_fill, stroke_width):
    """
    動画にテキストを挿入して保存する。
    text_rgb: テキストの色を指定
    font_size: テキストの大きさを指定
    x: 横軸の座標を指定
    y: 縦軸の座標を指定
    stroke_fill: 文字の縁の色を指定
    stroke_width: 文字の縁の大きさを指定
    """
    cap = cv2.VideoCapture(input_file_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    out = cv2.VideoWriter(output_file_path, fourcc, fps, (width, height))
    
    while True:
        ret, frame = cap.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(frame_rgb)
            draw = ImageDraw.Draw(pil_image)
            font = ImageFont.truetype('/usr/share/fonts/ipa-gothic/ipag.ttf', font_size)
            draw.text((x, y), text, fill=text_rgb, font=font, stroke_width=stroke_width, stroke_fill=stroke_fill)
            rgb_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
            out.write(rgb_image)
        else:
            break
    cap.release()
    out.release()


def get_video_length(input_file_path):
    """
    指定した動画ファイルの再生秒数を返す。
    """
    cap = cv2.VideoCapture(input_file_path)
    video_frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    video_second_length = video_frame_count / video_fps
    return video_second_length