
from psycopg2 import sql


class CursorByName():
    def __init__(self, cursor):
        self._cursor = cursor
    
    def __iter__(self):
        return self

    def __next__(self):
        row = self._cursor.__next__()
        return { description[0]: row[col] for col, description in enumerate(self._cursor.description) }


class UserQueries:

    user_personal_info_query = sql.SQL("select {fields} from {table} where {pkey} = %s").format(
        fields=sql.SQL(',').join([
            sql.Identifier('email'),
            sql.Identifier('phone'),
            sql.Identifier('first_name'),
            sql.Identifier('last_name'),
            sql.Identifier('postal_code'),
            sql.Identifier('city'),
            sql.Identifier('country_code'),
            sql.Identifier('state_input'),
            sql.Identifier('country_input'),
            sql.Identifier('address_1'),
            sql.Identifier('address_2'),
            sql.Identifier('short_state_input'),
    ]),
    table=sql.Identifier('users'),
    pkey=sql.Identifier('id'))

    user_cart_detail_query = sql.SQL("select {fields} from {table} where {pkey} = %s").format(
        fields=sql.SQL(',').join([
            sql.Identifier('url'),
            sql.Identifier('form_type'),
            sql.Identifier('form_data')
        ]),
        table=sql.Identifier('cart_form_details'),
        pkey=sql.Identifier('userid')
    )

