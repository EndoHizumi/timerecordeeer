import csv
from io import StringIO
from typing import Dict, Iterable


def handle(args) -> Iterable[str]:
    attendance_data = load(None, filePath=args.f)
    target_date_attendance = [str(date_attendance.get('time')) for date_attendance in attendance_data if date_attendance.get('date') == args.date]
    return target_date_attendance


def load(in_memory_buffer: StringIO, filePath: str = "") -> Iterable[Dict[str, str]]:
    if len(filePath) > 0:
        with open(filePath) as f:
            reader = csv.DictReader(f)
            csv_dict = list(reader)
    else:
        reader = csv.DictReader(in_memory_buffer)
        csv_dict = list(reader)
    return csv_dict
