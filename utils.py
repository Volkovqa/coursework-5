def insert_vacancy_data_into_db(data, db):
    with db.conn.cursor() as cur:
        for vacancy in data:
            cur.execute("""
               INSERT INTO vacancies (vacancy_id, vacancy_name, employer_id, salary_from, salary_to, city, url) 
               VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
                        (
                            vacancy['vacancy_id'],
                            vacancy['vacancy_name'],
                            vacancy['employer_id'],
                            vacancy['salary_from'],
                            vacancy['salary_to'],
                            vacancy['city'],
                            vacancy['url']
                        ))


def insert_employer_data_into_db(data, db):
    with db.conn.cursor() as cur:
        for employer in data:
            cur.execute("""
                INSERT INTO employers (employer_id, employer_name, hh_url)
                VALUES (%s, %s, %s)
            """,
                        (
                            employer['employer_id'],
                            employer['employer_name'],
                            employer['url']
                        ))
