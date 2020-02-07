import csv
from io import StringIO
from unittest import TestCase

import time_recordeeer as recorder


class TestLoad(TestCase):
    def setUp(self):
        self.test_data = [
            'date,time,state',
            '2020/01/31,09:10:51,begin',
            '2020/01/31,09:11:58,login',
            '2020/01/31,17:55:42,logout',
            '2020/01/31,17:55:46,fin'
        ]
        self.expect_data = list(csv.DictReader(self.test_data))

    def test_データから勤怠データが読み込みができる(self):
        actual_data = recorder.load(self.test_data)
        self.assertEqual(actual_data, self.expect_data)

    def test_ファイルから勤怠データが読み込みができる(self):
        with open("temp.csv", "w") as f:
            f.write("\r".join(self.test_data))
        actual_data = recorder.load(filePath="temp.csv")
        self.assertEqual(actual_data, self.expect_data)

