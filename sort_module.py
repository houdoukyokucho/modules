def sort_dicts_by_key(dicts, keys, reverse=False):
    """
    第一引数に並び替え対象の配列を指定する。
    第二引数に並び替える属性名が入った配列を指定する。
    第三引数に昇順か降順を指定する。
    """
    dicts.sort(key=lambda x: ([x[key] for key in keys]), reverse=reverse)
    return dicts