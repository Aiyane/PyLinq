import unittest

from PyLinq.api import sql_run as run


class SQLRuleTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(SQLRuleTest, self).__init__(*args, **kwargs)

        self.data_sources = {
            "company": [
                {
                    "id": 1,
                    "name": 'apple',
                },
                {
                    "id": 2,
                    "name": 'huawei',
                },
                {
                    "id": 3,
                    "name": 'xiaomi',
                },
                {
                    "id": 4,
                    "name": 'xiaomi',
                },
            ],
            "mobile": [
                {
                    "id": 1,
                    "name": "xiaomi2",
                    "company_id": 3,
                },
                {
                    "id": 2,
                    "name": "xiaomi3",
                    "company_id": 3,
                },
                {
                    "id": 3,
                    "name": "Mix2",
                    "company_id": 4,
                },
                {
                    "id": 3,
                    "name": "Mix2S",
                    "company_id": 4,
                },
                {
                    "id": 4,
                    "name": "iphone4",
                    "company_id": 1,
                },
                {
                    "id": 5,
                    "name": "iphone5",
                    "company_id": 1,
                },
                {
                    "id": 6,
                    "name": "Mate20",
                    "company_id": 2,
                }
            ],
            "ceo": [
                {
                    "id": 1,
                    "name": "Tim Cook",
                    "company_id": 1,
                },
                {
                    "id": 2,
                    "name": "renzhengfei",
                    "company_id": 2,
                },
                {
                    "id": 3,
                    "name": "leijun",
                    "company_id": 3,
                },
                {
                    "id": 4,
                    "name": "leijun",
                    "company_id": 4,
                }
            ],
            "mobile_price": [
                {
                    "id": 1,
                    "mobile_id": 1,
                    "type": 0,
                    "price": 1000,
                },
                {
                    "id": 2,
                    "mobile_id": 2,
                    "type": 0,
                    "price": 2000,
                },
                {
                    "id": 3,
                    "mobile_id": 3,
                    "type": 1,
                    "price": 2000,
                },
                {
                    "id": 4,
                    "mobile_id": 4,
                    "type": 1,
                    "price": 5000,
                },
                {
                    "id": 5,
                    "mobile_id": 5,
                    "type": 1,
                    "price": 6000,
                },
                {
                    "id": 6,
                    "mobile_id": 6,
                    "type": 1,
                    "price": 7000,
                }
            ]
        }

    def is_same_val(self, sort_key, one_val, other_val):
        one_val = sorted(one_val, key=lambda x: x[sort_key])
        other_val = sorted(other_val, key=lambda x: x[sort_key])
        self.assertListEqual(one_val, other_val)

    def test_index_sql(self):
        sql = ('(SELECT company.name, mobile.name AS mobile_name, ceo.name AS ceo_name '
               'FROM company, mobile, ceo '
               'INDEX BY company.id = mobile.company_id = ceo.company_id)')
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source, [{'name': 'apple', 'mobile_name': 'iphone4', 'ceo_name': 'Tim Cook'},
                                           {'name': 'apple', 'mobile_name': 'iphone5', 'ceo_name': 'Tim Cook'},
                                           {'name': 'huawei', 'mobile_name': 'Mate20', 'ceo_name': 'renzhengfei'},
                                           {'name': 'xiaomi', 'mobile_name': 'xiaomi2', 'ceo_name': 'leijun'},
                                           {'name': 'xiaomi', 'mobile_name': 'xiaomi3', 'ceo_name': 'leijun'},
                                           {'name': 'xiaomi', 'mobile_name': 'Mix2', 'ceo_name': 'leijun'},
                                           {'name': 'xiaomi', 'mobile_name': 'Mix2S', 'ceo_name': 'leijun'}])

    def test_index_sql2(self):
        sql = ('(SELECT company.name, mobile.name AS mobile_name, ceo.name AS ceo_name '
               'FROM company, mobile, ceo '
               'WHERE company.name = "apple" '
               'INDEX BY company.id = mobile.company_id = ceo.company_id)')
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source, [{'name': 'apple', 'mobile_name': 'iphone4', 'ceo_name': 'Tim Cook'},
                                           {'name': 'apple', 'mobile_name': 'iphone5', 'ceo_name': 'Tim Cook'}])

    def test_index_sql3(self):
        sql = ('(SELECT company.name, mobile.name AS mobile_name, ceo.name AS ceo_name '
               'FROM company, mobile, ceo '
               'WHERE company.name = "xiaomi" '
               'ORDER BY mobile.id DESC '
               'INDEX BY company.id = mobile.company_id = ceo.company_id)')
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source, [{'name': 'xiaomi', 'mobile_name': 'Mix2', 'ceo_name': 'leijun'},
                                           {'name': 'xiaomi', 'mobile_name': 'Mix2S', 'ceo_name': 'leijun'},
                                           {'name': 'xiaomi', 'mobile_name': 'xiaomi3', 'ceo_name': 'leijun'},
                                           {'name': 'xiaomi', 'mobile_name': 'xiaomi2', 'ceo_name': 'leijun'}])

    def test_index_sql4(self):
        sql = ('(SELECT company.name '
               'FROM company, mobile, ceo '
               'GROUP BY company.name '
               'INDEX BY company.id = mobile.company_id = ceo.company_id)')
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source, [{'name': 'apple'},
                                           {'name': 'huawei'},
                                           {'name': 'xiaomi'}])

    def test_index_sql5(self):
        sql = ('(SELECT company.name '
               'FROM company, mobile, ceo '
               'GROUP BY company.name '
               'HAVING len(company.name) = 6 '
               'ORDER BY company.name DESC '
               'INDEX BY company.id = mobile.company_id = ceo.company_id)')
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source, [{'name': 'xiaomi'},
                                           {'name': 'huawei'}])

    def test_cale_sql(self):
        sql = ('(SELECT company.id+2*3 AS id '
               'FROM company '
               'WHERE company.name = "apple")')
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source, [{'id': 7}])

    def test_simple_sql1(self):
        sql = ('(SELECT * '
               'FROM mobile '
               'WHERE mobile.company_id = 1 OR mobile.id = 1)')
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source, [{'id': 1, 'name': 'xiaomi2', 'company_id': 3},
                                           {'id': 4, 'name': 'iphone4', 'company_id': 1},
                                           {'id': 5, 'name': 'iphone5', 'company_id': 1}])

    def test_simple_sql2(self):
        sql = ("(SELECT * "
               "FROM mobile "
               "WHERE mobile.company_id + mobile.id > 5)")
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source, [{'id': 3, 'company_id': 4, 'name': 'Mix2'},
                                           {'id': 3, 'company_id': 4, 'name': 'Mix2S'},
                                           {'id': 5, 'company_id': 1, 'name': 'iphone5'},
                                           {'id': 6, 'company_id': 2, 'name': 'Mate20'}])

    def test_simple_sql3(self):
        sql = ("(SELECT * "
               "FROM mobile "
               "WHERE mobile.company_id - mobile.id < 3 "
               "AND mobile.company_id - mobile.id > 0)")
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source, [{'company_id': 3, 'name': 'xiaomi2', 'id': 1},
                                           {'company_id': 3, 'name': 'xiaomi3', 'id': 2},
                                           {'company_id': 4, 'name': 'Mix2', 'id': 3},
                                           {'company_id': 4, 'name': 'Mix2S', 'id': 3}])

    def test_join_sql2(self):
        sql = ("(SELECT company.name AS company_name, mobile.name AS mobile_name "
               "FROM mobile, company "
               "WHERE mobile.company_id = company.id "
               "AND mobile.name = 'xiaomi3')")
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source, [{'company_name': 'xiaomi', 'mobile_name': 'xiaomi3'}])

    def test_join_sql3(self):
        sql = ("(SELECT mobile.name AS mobile_name, company.name AS company_name, ceo.name AS ceo_name "
               "FROM mobile, company, ceo "
               "WHERE mobile.company_id = company.id "
               "AND company.id = ceo.company_id "
               "AND ceo.name = 'renzhengfei')")
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source,
                             [{'company_name': 'huawei', 'mobile_name': 'Mate20', 'ceo_name': 'renzhengfei'}])

    def test_simple_sum_sql(self):
        sql = ("(SELECT SUM(mobile.id) AS sum_mobile_id, SUM(mobile.company_id) AS sum_company_id "
               "FROM mobile)")
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source, [{'sum_company_id': 18, 'sum_mobile_id': 24}])

    def test_simple_count_sql(self):
        sql = "(SELECT COUNT(*) AS count1 FROM mobile)"
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source, [{'count1': 7}])

    def test_group_sql4(self):
        sql = ("(SELECT mobile.company_id, icount(*) AS count1 "
               "FROM mobile "
               "GROUP BY mobile.company_id)")
        data_source = run(sql, self.data_sources)
        self.is_same_val('company_id', data_source, [{'company_id': 3, 'count1': 2},
                                                     {'company_id': 4, 'count1': 2},
                                                     {'company_id': 1, 'count1': 2},
                                                     {'company_id': 2, 'count1': 1}])

    def test_having_sql1(self):
        sql = ("(SELECT mobile.company_id, icount(*) AS count1 "
               "FROM mobile GROUP BY mobile.company_id "
               "HAVING COUNT(*) >= 2 AND mobile.company_id != 4)")
        data_source = run(sql, self.data_sources)
        self.is_same_val('company_id', data_source, [{'count1': 2, 'company_id': 3},
                                                     {'count1': 2, 'company_id': 1}])

    def test_select_sql2(self):
        sql = ("(SELECT mobile.name AS mobile_name, company.name AS company_name, ceo.name AS ceo_name "
               "FROM mobile, company, ceo "
               "WHERE mobile.company_id = company.id "
               "AND company.id = ceo.company_id "
               "AND mobile.name = 'Mate20')")
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source,
                             [{'company_name': 'huawei', 'mobile_name': 'Mate20', 'ceo_name': 'renzhengfei'}])

    def test_select_sql3(self):
        sql = ("(SELECT mobile.name AS mobile_name, company.name AS company_name, ceo.name AS ceo_name "
               "FROM mobile, company, ceo "
               "WHERE mobile.company_id = company.id "
               "AND company.id = ceo.company_id "
               "AND mobile.name = 'Mate20')")
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source,
                             [{'company_name': 'huawei', 'mobile_name': 'Mate20', 'ceo_name': 'renzhengfei'}])

    def test_select_sql4(self):
        sql = ("(SELECT mobile.name AS mobile_name, company.name AS company_name, ceo.name AS ceo_name "
               "FROM mobile, company, ceo "
               "WHERE mobile.company_id = company.id "
               "AND company.id = ceo.company_id "
               "AND '1' = 'Mate20')")
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source, [])

    def test_sum_sql3(self):
        sql = "(SELECT SUM(mobile.id) AS sum1 FROM mobile)"
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source, [{'sum1': 24}])

    def test_asc_order(self):
        sql = ("(SELECT mobile.company_id "
               "FROM mobile "
               "ORDER BY mobile.company_id ASC)")
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source, [{'company_id': 1},
                                           {'company_id': 1},
                                           {'company_id': 2},
                                           {'company_id': 3},
                                           {'company_id': 3},
                                           {'company_id': 4},
                                           {'company_id': 4}])

    def test_desc_order(self):
        sql = ("(SELECT mobile.company_id "
               "FROM mobile "
               "ORDER BY mobile.company_id DESC)")
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source, [{'company_id': 4},
                                           {'company_id': 4},
                                           {'company_id': 3},
                                           {'company_id': 3},
                                           {'company_id': 2},
                                           {'company_id': 1},
                                           {'company_id': 1}])

    def test_group_order(self):
        sql = ("(SELECT mobile.company_id "
               "FROM mobile "
               "GROUP BY mobile.company_id "
               "ORDER BY mobile.company_id)")
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source, [{'company_id': 1},
                                           {'company_id': 2},
                                           {'company_id': 3},
                                           {'company_id': 4}])

    def test_in_order(self):
        sql = ("(SELECT mobile.company_id, mobile.name "
               "FROM mobile "
               "WHERE mobile.name IN ('xiaomi2', 'xiaomi3', 'Mate20'))")
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source, [{'name': 'xiaomi2', 'company_id': 3},
                                           {'name': 'xiaomi3', 'company_id': 3},
                                           {'name': 'Mate20', 'company_id': 2}])

    def test_not_in_order(self):
        sql = ("(SELECT mobile.company_id, mobile.name "
               "FROM mobile "
               "WHERE mobile.name NOT IN ('xiaomi2', 'xiaomi3', 'Mate20'))")
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source, [{'name': 'Mix2', 'company_id': 4},
                                           {'name': 'Mix2S', 'company_id': 4},
                                           {'name': 'iphone4', 'company_id': 1},
                                           {'name': 'iphone5', 'company_id': 1}])

    def test_sub_select_order(self):
        sql = ("(SELECT mobile.company_id, mobile.name "
               "FROM mobile "
               "WHERE mobile.company_id IN "
               "(SELECT company.id FROM company))")
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source, [{'name': 'xiaomi2', 'company_id': 3},
                                           {'name': 'xiaomi3', 'company_id': 3},
                                           {'name': 'Mix2', 'company_id': 4},
                                           {'name': 'Mix2S', 'company_id': 4},
                                           {'name': 'iphone4', 'company_id': 1},
                                           {'name': 'iphone5', 'company_id': 1},
                                           {'name': 'Mate20', 'company_id': 2}])

    def test_when_case_order(self):
        sql = ("(SELECT "
               "CASE WHEN company.name = 'xiaomi' THEN '小米' "
               "WHEN company.name ='huawei' THEN '华为' "
               "WHEN company.name ='apple' THEN '苹果' "
               "ELSE '' END AS company_name "
               "FROM company)")
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source, [{'company_name': '苹果'},
                                           {'company_name': '华为'},
                                           {'company_name': '小米'},
                                           {'company_name': '小米'}])

    def test_rename_funcs(self):
        sql = "(SELECT rename('公司,ID', company.name, company.id) FROM company)"
        data_source = run(sql, self.data_sources)
        self.assertListEqual(data_source, [{'公司': 'apple', 'ID': 1},
                                           {'公司': 'huawei', 'ID': 2},
                                           {'公司': 'xiaomi', 'ID': 3},
                                           {'公司': 'xiaomi', 'ID': 4}])

    def test_nested_funcs(self):
        sql = ("(SELECT int(SUM(mobile.id)) AS sum1, mobile.company_id "
               "FROM mobile "
               "GROUP BY mobile.company_id)")
        data_source = run(sql, self.data_sources)
        self.is_same_val('company_id', data_source, [{'sum1': 3, 'company_id': 3},
                                                     {'sum1': 6, 'company_id': 4},
                                                     {'sum1': 9, 'company_id': 1},
                                                     {'sum1': 6, 'company_id': 2}])

    def test_deflate(self):
        sql = ("(SELECT deflate(ceo.name, 'ceo_name', mobile_price.type, SUM(mobile_price.price), '0:普通,1:旗舰', 0) "
               "FROM mobile, company, ceo, mobile_price "
               "WHERE mobile.id = mobile_price.mobile_id "
               "AND mobile.company_id = company.id "
               "AND company.id = ceo.company_id "
               "GROUP BY ceo.name, mobile_price.type)")

        data_source = run(sql, self.data_sources)
        data_source = sorted(data_source, key=lambda x: x['ceo_name'])
        self.assertListEqual(data_source, [{'旗舰': 11000, '普通': 0, 'ceo_name': 'Tim Cook'},
                                           {'旗舰': 4000, '普通': 3000, 'ceo_name': 'leijun'},
                                           {'旗舰': 7000, '普通': 0, 'ceo_name': 'renzhengfei'}])

    def test_deflate2(self):
        self.data_sources['company'] = []
        sql = ("(SELECT deflate(ceo.name, 'ceo_name', mobile_price.type, SUM(mobile_price.price), '0:普通,1:旗舰', 0) "
               "FROM mobile, company, ceo, mobile_price "
               "WHERE mobile.id = mobile_price.mobile_id "
               "AND mobile.company_id = company.id "
               "AND company.id = ceo.company_id "
               "GROUP BY ceo.name, mobile_price.type)")

        data_source = run(sql, self.data_sources)
        data_source = sorted(data_source, key=lambda x: x['ceo_name'])
        self.assertListEqual(data_source, [])
