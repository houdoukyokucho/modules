def save_text(input_file_path, texts_file):
    """
    テキストファイルを保存する。
    """
    with open(input_file_path, 'w') as file:
        file.writelines(texts_file)


def get_text(input_file_path):
    """
    指定されたテキストデータの内容を返す。
    """
    with open(input_file_path) as file:
        text = file.read()
        return text


def get_text_list(input_file_path):
    """
    指定されたテキストデータの内容を改行ごとにリストで返す。
    """
    with open(input_file_path) as file:
        texts = file.read().split()
        return texts