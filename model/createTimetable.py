
from datetime import datetime
#compare the time
def comepare_time(start,end):
    """
    :param start:
    :param end:
    :return:
                    0: start = end
                    1:start < end
                    2:start > end
    """
    # 日期格式话模版
    format_pattern = "%H:%M"
    # 将 'str' 时间通过格式化模式转化为 'datetime.datetime' 时间戳, 然后在进行比较
    difference = (datetime.strptime(end, format_pattern) - datetime.strptime(start, format_pattern))
    # 可以获取天(days), 或者秒(seconds)
    if difference.seconds == 0 and difference.days == 0:
        return 0
    elif difference.seconds  > 0 and difference.days == 0:
        return 1
    elif difference.seconds  > 0 and difference.days < 0:
        return 2


