import os
from pathlib import Path
from datetime import datetime, timezone

def convert_time2secs(time):
    return sum(x * int(t) for x, t in zip([3600, 60, 1], time.split(":")))
#print(convert_time2secs('0:06:40'))
#225 400

def check_exists_file(yt_video_title, path_check, type_file='.mp4'):
    str_path = f"{path_check}\\{yt_video_title}{type_file}"
    str_path = str_path.replace('#', '')
    path_w10 = Path(str_path)
    print(str_path)
    exists = os.path.exists(path_w10)
    return exists

def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
    dt = datetime(year, month, day, hour, minute, 0).isoformat() + '.000Z'
    return dt


def utcformat(dt, timespec='milliseconds'):
    """convert datetime to string in UTC format (YYYY-mm-ddTHH:MM:SS.mmmZ)"""
    iso_str = dt.astimezone(timezone.utc).isoformat('T', timespec)
    return iso_str.replace('+00:00', 'Z')


def fromutcformat(utc_str, tz=None):
    iso_str = utc_str.replace('Z', '+00:00')
    return datetime.fromisoformat(iso_str).astimezone(tz)


