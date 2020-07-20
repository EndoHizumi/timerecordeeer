import csv
from collections import OrderedDict
from io import StringIO
from typing import Dict, Iterable


def load(in_memory_buffer: StringIO, filePath: str = "") -> Iterable[OrderedDict[str, str]]:
    if len(filePath) > 0:
        with open(filePath) as f:
            reader = csv.DictReader(f)
    else:
        reader = csv.DictReader(in_memory_buffer)
    csv_dict = list(reader)
    return csv_dict


def find(attendance_datas: Iterable[Dict[str, str]], target_date: str) -> list[str]:
    target_date_attendance = [str(attendance_data.get('time')) for attendance_data in attendance_datas if attendance_data.get('date') == target_date]
    return target_date_attendance


def Emboss(time, state):
    # company_idとemp_idを取得する。

    # タイムレコーダー登録APIを叩く
    pass
