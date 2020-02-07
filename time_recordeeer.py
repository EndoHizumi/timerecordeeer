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

