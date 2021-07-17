import datetime


def convert_time_structure_to_seconds(time):
    """
    「:」が使用されている時間形式を「秒に」変換して返す。
    """
    ts = time.split(':')
    if len(ts) == 1:
        time = datetime.timedelta(seconds=int(ts[-1]))
    if len(ts) == 2:
        time = datetime.timedelta(minutes=int(ts[-2]), seconds=int(ts[-1]))
    if len(ts) == 3:
        time = datetime.timedelta(hours=int(ts[-3]), minutes=int(ts[-2]), seconds=int(ts[-1]))
    return time.seconds
    