import requests
from hh_api_config import hh_config


class HHapiclient:

    def __init__(self, page: int = 0) -> None:
        self.url = "https://api.hh.ru/vacancies"
        self.params = {
            "page": page,
            "employer_id": hh_config.get("employer_ids"),
            "only_with_salary": hh_config.get("only_with_salary"),
            "per_page": hh_config.get("vacancies_per_page"),
            "area": hh_config.get("area")
        }

    def get_vacancies_data(self) -> list[dict]:
        response = requests.get(self.url, params=self.params)
        return response.json()['items']

    def get_employer_data(self) -> list[dict]:
        emp_list = [
            {
                'id': uid,
                'name': requests.get(f"https://api.hh.ru/employers/{uid}").json().get('name'),
                'url': requests.get(f"https://api.hh.ru/employers/{uid}").json().get('alternate_url')
            }
            for uid in self.params.get('employer_id') if uid is not None
        ]

        return emp_list
