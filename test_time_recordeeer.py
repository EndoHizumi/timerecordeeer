import csv
import tempfile
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


class TestFind(TestCase):
    def setUp(self):
        self.test_data = [
            'date,time,state',
            '2020/01/31,09:10:51,begin',
            '2020/01/31,09:11:58,login',
            '2020/01/31,17:55:42,logout',
            '2020/01/31,17:55:46,fin',
            '2020/02/03,09:41:19,begin',
            '2020/02/03,09:41:48,login',
            '2020/02/03,18:53:49,logout',
            '2020/02/03,18:53:54,fin',
        ]
        self.test_data = list(csv.DictReader(self.test_data))

    def test_指定した日付の勤怠データを取得できる(self):
        expect_data = ["09:10:51", "09:11:58", "17:55:42", "17:55:46"]
        actual_data = recorder.find(self.test_data, "2020/01/31")
        self.assertEqual(actual_data, expect_data)


class TestEmboss(TestCase):
    def test_Freeeへ打刻できる(self):
        pass

    def test_Slackへ投稿できる(self):
        pass
