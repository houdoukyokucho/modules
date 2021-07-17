import moviepy.editor as mp


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