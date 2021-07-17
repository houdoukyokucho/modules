import moviepy.editor as mp
import cv2


def combine_video_with_sound(input_video_path, input_sound_path, output_path):
    """
    指定したパスの動画ファイルと音声ファイルを合成し保存する。
    """
    clip = mp.VideoFileClip(input_video_path).subclip()
    clip.write_videofile(output_path, audio=input_sound_path)


def connect_videos(video_with_sound_file_name_paths, output_path):
    """
    指定したパスの複数の動画ファイルを結合して保存する。
    """
    clips = []
    for video_with_sound_file_name_path in video_with_sound_file_name_paths:
        clip = mp.VideoFileClip(video_with_sound_file_name_path)
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
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    writer = cv2.VideoWriter(output_file_path, fourcc, fps, (cap_width, cap_height))

    for i in range(end_seconds * fps):
        ret, frame = cap.read()
        if ret:
            if start_seconds * fps < i:
                writer.write(frame)
    writer.release()
    cap.release()


def capture_video(input_file_path, output_file_path, capture_seconds, target_frame_in_second='first'):
    """
    時間を秒で指定して動画のキャプチャを保存する。
    target_frame_in_second で 1 秒の内の最初のフレームか、
    最後のフレームかキャプチャの対象を選択できる。
    """
    cap = cv2.VideoCapture(input_file_path)
    cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    last_frame = capture_seconds * fps
    first_frame = last_frame - (fps-1)

    if target_frame_in_second == 'first':
        target_frame = first_frame
    else:
        target_frame = last_frame

    for i in range(capture_seconds * fps):
        ret, frame = cap.read()
        if ret:
            if i == target_frame:
                cv2.imwrite(output_file_path, frame)


def stack_video_on_video(input_file_path_1, input_file_path_2, output_file_path, end_time):
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

