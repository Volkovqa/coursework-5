from dbmanager.db_config import postgres_db_config
from dbmanager.db_manager import DBManager
from hhapi.hhapiengine import HHapiclient
from utils import *


def main():
    print('Загружается база данных с вакансиями с сайта hh.ru\n'
          'Не забудьте очистить таблицы после завершения работы.\n')

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

    while True:
        print("Выберите информацию для вывода:\n"
              "1 - Информация о работодателях и количестве вакансий\n"
              "2 - Получение информации о всех вакансиях в базе данных\n"
              "3 - Средняя заработная плата среди вакансий в базе\n"
              "4 - Список вакансий с зарплатой выше средней\n"
              "5 - Найти вакансии по ключевому слову\n"
              "0 - выйти из программы\n"
              "P.S. О том, как получить другие вакансии и изменить работу программы, читайте в README.")

        num = str(input('--> '))  # пользователь вводит номер нужной функции
        if num == '1':
            print(db.get_companies_and_vacancies_count())
        elif num == '2':
            vac_list_av = db.get_all_vacancies()
            for vac in vac_list_av:
                print(vac)
        elif num == '3':
            avg_salary = int(db.get_avg_salary())
            print(f"Средняя зарплата по всем вакансиям в базе данных: {avg_salary}\n")
        elif num == '4':
            vac_list_hs = db.get_vacancies_with_higher_salary()
            for vac in vac_list_hs:
                print(vac)
        elif num == '5':
            keyword = str(input("Введите ключевое слово для поиска: "))
            vac_list_kw = db.get_vacancies_with_keyword(keyword)
            for vac in vac_list_kw:
                print(vac)
        elif num == '0':
            break
        else:
            print("Неправильный код команды")

    if not db.conn.closed:
        db.conn.close()


if __name__ == '__main__':
    main()
