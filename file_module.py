import datetime
import os
import json


def get_file_paths(input_path):
    """
    指定したディレクトリ内にあるファイルのパスをリストにしてを返す。
    """
    file_paths = []
    file_names = os.listdir(path=input_path)
    for file_name in file_names:
        file_paths.append(f'{input_path}{file_name}')
    return file_paths


def get_extension(file_name):
    """
    ファイルの拡張子を返す。
    """
    return os.path.splitext(file_name)[1][1:]


def create_directory(input_path, with_datetime=False):
    """
    指定パスのディレクトリを作成する。
    with_datetime=True の時はディレクトリの後ろに「_yyyy_mm_dd」を付与する。
    """
    if with_time:
        now_date_time = datetime.datetime.now().strftime('%Y_%m_%d')
        input_path = f'{input_path}_{now_date_time}'

    if not os.path.isdir(input_path):
        os.makedirs(input_path, exist_ok=False)
        return input_path
    else:
        return None


def get_json(input_file_path):
    """
    指定されたパスのJSONを辞書形式にして返す。
    """
    file = open(input_file_path, 'r')
    file = json.load(file)
    return file