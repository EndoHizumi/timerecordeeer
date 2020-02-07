import csv
from io import StringIO
from typing import Dict, Iterable, List

import requests


def load(in_memory_buffer: StringIO = None, filePath: str = "") -> List[Dict[str, str]]:
    if len(filePath) > 0:
        with open(filePath) as f:
            reader = csv.DictReader(f)
            csv_dict = list(reader)
    else:
        reader = csv.DictReader(in_memory_buffer)
        csv_dict = list(reader)
    return csv_dict


def find(attendance_dict: Iterable[Dict[str, str]], target_date: str) -> List[str]:
    target_date_attendance = [str(attendance_data.get('time')) for attendance_data in attendance_dict if attendance_data.get('date') == target_date]
    return target_date_attendance

