from collections import OrderedDict
from contextlib import closing

from django.db import connection

from api.sqlpaginator import SqlPaginator
from shop.settings import PAGINATE_PY


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_list(requests):
    params = requests.query_params.getlist("search")

    if params.getlist("search"):

        extra_sql = "where "
        for i in params.getlist("search"):
            if i == params.getlist("search")[-1]:
                extra_sql += f"(name like '%{i}%' or slug like '%{i}%' ) "
            else:
                extra_sql += f"(name like '%{i}%' or slug like '%{i}%') or "
    else:
        extra_sql = ""

    page = requests.query_params.get("page", 1)


    sql = f"""select * from sayt_product{extra_sql}
            order by id
            limit %s OFFSET %s
            """

    offset = (int(page) - 1) * PAGINATE_PY

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [PAGINATE_PY, offset])
        result = dictfetchall(cursor)

    with closing(connection.cursor()) as cursor:
        cursor.execute(f"select count(1) as cnt from sayt_product {extra_sql}" )
        root = dictfetchone(cursor)

    if root:
        cnt = root["cnt"]
    else:
        cnt = 0


    sqlpaginator = SqlPaginator(requests, page, per_page=PAGINATE_PY, count=cnt)
    pagging = sqlpaginator.get_paginated_response(per_page=PAGINATE_PY, current_page=page)

    return OrderedDict([
        ('items', result),
        ('meta', pagging),

    ])


def get_one(requests, pk):
    sql = "select * from sayt_product where id=%s"

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [pk])
        result = dictfetchone(cursor)
    return result
