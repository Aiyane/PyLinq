## PyLinq

### 介绍

开发中。

计划实现一个执行 SQL SELECT 语句的 Python 工具。

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
