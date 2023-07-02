def insert_vacancy_data_into_db(data, db):
    with db.conn.cursor() as cur:
        for vacancy in data:
            if vacancy['salary']['from'] is None:
                from_zero = 0
            else:
                from_zero = vacancy['salary']['from']
            if vacancy['salary']['to'] is None:
                to_zero = 0
            else:
                to_zero = vacancy['salary']['to']
            cur.execute("""
               INSERT INTO vacancies (vacancy_id, vacancy_name, employer_id, salary_from, salary_to, city, url) 
               VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
                        (
                            vacancy['id'],
                            vacancy['name'],
                            vacancy['employer']['id'],
                            from_zero,
                            to_zero,
                            vacancy['area']['name'],
                            vacancy['alternate_url']
                        ))
        db.conn.commit()


def insert_employer_data_into_db(data, db):
    with db.conn.cursor() as cur:
        for employer in data:
            cur.execute("""
                INSERT INTO employers (employer_id, employer_name, hh_url)
                VALUES (%s, %s, %s)
            """,
                        (
                            employer['id'],
                            employer['name'],
                            employer['url']
                        ))
        db.conn.commit()
