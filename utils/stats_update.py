""" (module) stats_update

This contains the Stats class and it sets it up
"""
import os
import inspect
import functools

import asyncpg
from dotenv import load_dotenv
from fastapistats import Stats

load_dotenv()

db_url = os.environ["DATABASE_URL"]

async def update_db(name):
    connection = await asyncpg.connect(db_url)
    data = await connection.fetch("""SELECT * FROM Stats WHERE name='{}'""".format(name))
    if len(data) == 0:
        await connection.execute("""INSERT INTO Stats (name, amount) VALUES ('{}', 1)""".format(name))
    else:
        amount = data[0][1] + 1
        await connection.execute("""UPDATE Stats SET amount={} WHERE name='{}'""".format(amount, name))
    
    await connection.close()


def update_stats(*args, **kw_args):
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            try:
                name = kw_args["name"]
            except KeyError:
                name = None

            try:
                if name is None:
                    name = str(func.__name__)
            except UnboundLocalError:
                name = str(func.__name__)

            await update_db(name)    

            if inspect.iscoroutinefunction(func):
                return await func(*args, **kwargs)
            else:
                return func(*args, **kwargs)

        return wrapped
    return wrapper


