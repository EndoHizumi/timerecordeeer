import csv
from io import StringIO
from typing import Dict, Iterable
from src.freee import freee
import argparse


def load(in_memory_buffer: StringIO, filePath: str = '') -> Iterable[Dict[str, str]]:
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


def emboss(state):
    # company_idとemp_idを取得する。
    api = freee()
    emp_info = api.me()['companies'][0]
    company_id = emp_info['id']
    employee_id = emp_info['employee_id']
    # タイムレコーダー登録APIを叩く
    res = api.register_time_clocks(company_id, employee_id, state)
    return res


def find_handler(args):
    attendance_data = load(args.f)
    return find(attendance_data, args.date)


def emboss_handler(args):
    return emboss(args.state)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers()

    find_parser = sub_parser.add_parser('find', help='Display specify date attendance data.')
    find_parser.add_argument('date')
    find_parser.add_argument('-f', default='./worktime.csv', help='attendance file path')
    find_parser.set_defaults(func=find_handler)

    emboss_parser = sub_parser.add_parser('emboss', help='Register the stamping information of the specified employee.')
    emboss_parser.add_argument('state', type=str, choices=['clock_in', 'break_begin', 'break_end', 'clock_out'])
    emboss_parser.set_defaults(func=emboss_handler)

    args = parser.parse_args()
    print(args.func(args))
