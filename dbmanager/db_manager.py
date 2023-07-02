import psycopg2


class DBManager:
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
            database=dbname,
            user=user,
            password=password,
            host=host,
            port=port)

    def get_companies_and_vacancies_count(self):
        with self.conn.cursor() as cur:
            cur.execute("""
            SELECT employers.employer_name, COUNT(vacancies.vacancy_id)
            FROM employers
            JOIN vacancies ON vacancies.employer_id = employers.employer_id
            GROUP BY employers.employer_name
            """)

            return cur.fetchall()

    def get_all_vacancies(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                    SELECT vacancy_name, employer_name, (salary_from + salary_to) / 2 AS salary, url 
                    FROM vacancies
                    JOIN employers USING(employer_id)
                    ORDER BY salary DESC
                    """)
            return cur.fetchall()

    def get_avg_salary(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                    SELECT AVG(salary_from + salary_to) / 2
                    FROM vacancies
            """)
            return cur.fetchone()[0]

    def get_vacancies_with_higher_salary(self):
        with self.conn.cursor() as cur:
            cur.execute(f"""
                    SELECT vacancy_name, (salary_from + salary_to) / 2 AS salary, url 
                    FROM vacancies
                    WHERE (salary_from + salary_to) / 2 > {self.get_avg_salary()}
                    ORDER BY salary DESC
            """)
            return cur.fetchall()

    def get_vacancies_with_keyword(self, keyword: str):
        with self.conn.cursor() as cur:
            cur.execute(
                f"""
                SELECT vacancy_name, salary_from, salary_to, url FROM vacancies 
                WHERE vacancy_name ILIKE '%{keyword}%'
                """
            )
            result = cur.fetchall()
            return result
