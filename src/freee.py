import requests
import json
import webbrowser
from datetime import date
from typing import Dict


class freee:
    access_token = ''
    headers = {'Authorization': f'Bearer {access_token}', 'accept': 'application/json'}

    def __init__(self):
        with open('config.json') as f:
            config = json.load(ｆ)
            if config.get('access_token'):
                self.access_token = config.get('access_token')
            else:
                print('config.jsonにアクセストークンが登録されていません。認証ページにログインしてアクセストークンを取得してください')
                token_url = f"{config['token_url']}?client_id={config['client_id']}&redirect_uri={config['redirect_uri']}&response_type={config['response_type']}"
                webbrowser.open(token_url)

    def me(self):
        # curl -X GET "https://api.freee.co.jp/hr/api/v1/users/me" -H  "accept: application/json" -H  "Authorization: Bearer 2ef4f5578946860370d8f3d8358f53bf0d0d56807bd3e640ff02b020ea3b68d8"
        return requests.get("https://api.freee.co.jp/hr/api/v1/users/me", headers=self.headers).json()

    def register_time_clocks(self, company_id: str, emp_id: str, state: str):
        payload: Dict[str, str] = {'company_id': company_id, 'type': state, 'emp_id': emp_id, 'base_date': date.today().strftime('%Y-%m-%d')}
        return requests.post(f"https://api.freee.co.jp/hr/api/v1/employees/{emp_id}/time_clocks", headers=self.headers, data=payload).json()
