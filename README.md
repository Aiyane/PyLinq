## PyLinq

### 介绍

一个执行 SQL SELECT 语句的 Python 工具。

将 Python 中 dict 类型类比为 SQL 中数据库，使用 SQL 语句对 dict 对象进行 SELECT 操作。

例如
```python
data_sources = {
    'Teacher': [
        {'name': 'zhang', 'year': 5},
        {'name': 'li', 'year': 3}
    ],
    'Student': [
        {'number': 10, 'age': 18},
        {'number': 20, 'age': 17}
    ]
}
```

运行 `SELECT Teacher.name FROM Teacher WHERE Teacher.year = 5` 的结果为
```python
[{'name': 'zhang'}]
```

### 要求

python 3.5 及以上

pip 安装 antlr4-python3-runtime

### 使用示例

请看 `example.py` 与 `test_linq.py` 文件的示例。

### 使用索引

在 join 多张表时，相当于做多重循环。如果 join 的表数量很多，耗时会过大。如果对表的某个字段建立索引，则只进行一次循环。

新增语法 `JOIN WITH`，在该语法后可用连等号表示建立的索引。以下为例子：
```python
sql = ('(SELECT company.name, mobile.name AS mobile_name, ceo.name AS ceo_name '
       'FROM company, mobile, ceo '
       'JOIN WITH company.id = mobile.company_id = ceo.company_id)')
sql = ('(SELECT company.name, mobile.name AS mobile_name, ceo.name AS ceo_name '
       'FROM company, mobile, ceo '
       'WHERE company.name = "apple" '
       'JOIN WITH company.id = mobile.company_id = ceo.company_id)')
sql = ('(SELECT company.name, mobile.name AS mobile_name, ceo.name AS ceo_name '
       'FROM company, mobile, ceo '
       'WHERE company.name = "xiaomi" '
       'JOIN WITH mobile.id DESC '
       'INDEX BY company.id = mobile.company_id = ceo.company_id)')
sql = ('(SELECT company.name '
       'FROM company, mobile, ceo '
       'GROUP BY company.name '
       'JOIN WITH company.id = mobile.company_id = ceo.company_id)')
sql = ('(SELECT company.name '
       'FROM company, mobile, ceo '
       'GROUP BY company.name '
       'HAVING len(company.name) = 6 '
       'ORDER BY company.name DESC '
       'JOIN WITH company.id = mobile.company_id = ceo.company_id)')
sql = ('(SELECT company.name, mobile.name AS mobile_name, ceo.name AS ceo_name, mobile_price.price '
       'FROM company, mobile, ceo, mobile_price '
       'WHERE mobile_price.mobile_id = mobile.id '
       'ORDER BY mobile_price.price '
       'JOIN WITH company.id = mobile.company_id = ceo.company_id)')
```
