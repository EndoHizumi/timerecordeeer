from time_recordeeer.freee import freee


def handle(state):
    # company_idとemp_idを取得する。
    api = freee()
    emp_info = api.me()['companies'][0]
    company_id = emp_info['id']
    employee_id = emp_info['employee_id']
    # タイムレコーダー登録APIを叩く
    res = api.register_time_clocks(company_id, employee_id, state)
    return res
