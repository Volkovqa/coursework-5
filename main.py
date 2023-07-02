from dbmanager.db_config import postgres_db_config
from dbmanager.db_manager import DBManager
from hhapi.hhapiengine import HHapiclient
from utils import *


def main():
    db = DBManager(dbname=postgres_db_config.get('dbname'),
                   user=postgres_db_config.get('user'),
                   password=postgres_db_config.get('password'),
                   host=postgres_db_config.get('host'),
                   port=postgres_db_config.get('port'))

    hh_api_client = HHapiclient()
    employers_list = hh_api_client.get_employer_data()
    vacancies_list = hh_api_client.get_vacancies_data()

    insert_employer_data_into_db(employers_list, db)
    insert_vacancy_data_into_db(vacancies_list, db)

    print(db.get_companies_and_vacancies_count())
    print(db.get_all_vacancies())
    print(db.get_avg_salary())
    print(db.get_vacancies_with_higher_salary())
    print(db.get_vacancies_with_keyword('сотрудник'))

    if not db.conn.closed:
        db.conn.close()


if __name__ == '__main__':
    main()
