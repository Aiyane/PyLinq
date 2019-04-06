from PyLinq.api import sql_run


def main(sql_expr: str, data_sources: dict):
    print(sql_run(sql_expr, data_sources))


if __name__ == '__main__':
    test_sql_expr = "(SELECT Teacher.name FROM Teacher WHERE Teacher.year = 5)"
    test_data = {
        'Teacher': [
            {'name': 'zhang', 'year': 5},
            {'name': 'li', 'year': 3}
        ],
        'Student': [
            {'number': 10, 'age': 18},
            {'number': 20, 'age': 17}
        ]
    }
    main(test_sql_expr, test_data)
