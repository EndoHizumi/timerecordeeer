from time_recordeeer.freee import freee


def handle(args):
    # company_idとemp_idを取得する。
    api = freee()
    # 打刻可能種別の取得APIを叩く
    res = api.get_available_type()
    return res
