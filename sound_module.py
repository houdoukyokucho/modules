from google.cloud import texttospeech
from pydub import AudioSegment


def get_sound_length(input_file_path):
    """
    指定した音声ファイルの再生秒数を返す。
    """
    sound = AudioSegment.from_file(input_file_path)
    time = sound.duration_seconds
    return time


def connect_sounds(input_file_paths, output_file_path):
    """
    複数の音声ファイルのパスを配列で渡すと全て結合して保存する。
    """
    for index, input_file_path in enumerate(input_file_paths):
        if index==0:
            base_sound_file = AudioSegment.from_file(input_file_path, format="mp3")
            continue
        sound_file = AudioSegment.from_file(input_file_path, format="mp3")
        base_sound_file += sound_file
    base_sound_file.export(output_file_path, format="mp3")


def stack_sound_on_sound(input_base_file_path, input_additional_file_path, output_file_path):
    """
    音声ファイルに音声ファイルを合成して保存する。
    """
    base_sound = AudioSegment.from_file(input_base_file_path, format="mp3")
    additional_sound = AudioSegment.from_file(input_additional_file_path, format="mp3")
    # 追加音声を再生 0 秒時点に重ねる。
    start_time_ms = 0 * 1000
    additional_sound = additional_sound -20
    result_sound = base_sound.overlay(additional_sound, start_time_ms)
    result_sound.export(output_file_path, format="mp3")


def text_to_speech(text_content, output_file_path):
    """
    文字列を渡すと音声ファイルを作成して保存する。
    """
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text_content)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="ja-JP",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
        name="ja-JP-Wavenet-B"
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open(output_file_path, "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)