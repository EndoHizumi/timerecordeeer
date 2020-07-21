import csv
from io import StringIO
from typing import Dict, Iterable


def load(in_memory_buffer: StringIO, filePath: str = "") -> Iterable[Dict[str, str]]:
    if len(filePath) > 0:
        with open(filePath) as f:
            reader = csv.DictReader(f)
            csv_dict = list(reader)
    else:
        reader = csv.DictReader(in_memory_buffer)
        csv_dict = list(reader)
    return csv_dict


def find(attendance_data: Iterable[Dict[str, str]], target_date: str) -> Iterable[str]:
    target_date_attendance = [str(date_attendance.get('time')) for date_attendance in attendance_data if date_attendance.get('date') == target_date]
    return target_date_attendance


def Emboss(time, state):
    # company_idとemp_idを取得する。

    # タイムレコーダー登録APIを叩く
    pass
