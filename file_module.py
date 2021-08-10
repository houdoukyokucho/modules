import datetime
import json
import os
import shutil
import zipfile


def get_file_paths(input_path, filter_extension=None):
    """
    指定したディレクトリ内にあるファイルのパスをリストにしてを返す。
    """
    file_paths = []
    file_names = os.listdir(path=input_path)
    for file_name in file_names:
        if filter_extension:
            if filter_extension == get_extension(file_name):
                file_paths.append(f'{input_path}{file_name}')
            else:
                continue
        else:
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
    if with_datetime:
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


def create_zip_file(input_file_paths, output_file_path):
    with zipfile.ZipFile(output_file_path, 'w', compression=zipfile.ZIP_DEFLATED) as new_zip:
        for input_file_path in input_file_paths:
            file_name_in_zip = os.path.basename(input_file_path)
            new_zip.write(input_file_path, arcname=file_name_in_zip)


def put_index_on_file_name_if_exist(file_name_path):
    """
    受け取ったファイルのパスが存在する場合、ファイル名の最後に () で囲んだインデックスを付与して返す。
    ./path/file.txt も ./path/file(1).txt も存在する場合 ./path/file(2) を返す。
    インデックスは　100 を上限とする。
    """
    if os.path.exists(file_name_path):
        dirpath, file_name = os.path.split(file_name_path)
        name, ext = os.path.splitext(file_name)
        for i in range(2, 100):
            new_file_name = f'{name}({i}){ext}'
            new_file_path = os.path.join(dirpath, new_file_name)
            file_name_path = new_file_path
            if not os.path.exists(new_file_path):
                break
    return file_name_path


def delete_file(input_file_path):
    os.remove(input_file_path)


def attach_index_to_file_name_if_exist(file_name_path):
    """
    受け取ったファイルのパスが存在する場合、ファイル名の最後に () で囲んだインデックスを付与して返す。
    ./path/file.txt も ./path/file(1).txt も存在する場合 ./path/file(2) を返す。
    インデックスは　100 を上限とする。
    """
    if os.path.exists(file_name_path):
        dirpath, file_name = os.path.split(file_name_path)
        name, ext = os.path.splitext(file_name)
        for i in range(2, 100):
            new_file_name = f'{name}({i}){ext}'
            new_file_path = os.path.join(dirpath, new_file_name)
            file_name_path = new_file_path
            if not os.path.exists(new_file_path):
                break
    return file_name_path


def copy_file(input_file_path, output_file_path):
    shutil.copyfile(input_file_path, output_file_path)