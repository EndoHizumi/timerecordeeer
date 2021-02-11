from time_recordeeer.freee import freee


def handle(args):
    # company_idとemp_idを取得する。
    api = freee()
    # タイムレコーダー登録APIを叩く
    res = api.register_time_clocks(args.state)
    return res
