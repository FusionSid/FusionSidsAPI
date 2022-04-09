""" (module) stats_update

This contains the Stats class and it sets it up
"""
import os
import inspect
import asyncio
import functools
from contextlib import asynccontextmanager

import asyncpg
from dotenv import load_dotenv
from fastapistats import Stats

load_dotenv()

db_url = os.environ["DATABASE_URL"]

@asynccontextmanager
async def db_conn(database_url : str):
    connection = await asyncpg.connect(database_url)
    
    yield connection

    await connection.close()

async def update_db(name:str):
    """
    Updates the stats db

    Parameters
        :param name (str): The name of the endpoint that will be updated
    """
    # connection = await asyncpg.connect(db_url)

    async with db_conn(db_url) as connection:
        data = await connection.fetch("""SELECT * FROM Stats WHERE name='{}'""".format(name))
        if len(data) == 0:
            await connection.execute("""INSERT INTO Stats (name, amount) VALUES ('{}', 1)""".format(name))
        else:
            amount = data[0][1] + 1
            await connection.execute("""UPDATE Stats SET amount={} WHERE name='{}'""".format(amount, name))
    
    # await connection.close()


def update_stats(*args, **kw_args):
    """
    Decorator to update the stats for an endpoint
    """
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
            
            loop = asyncio.get_event_loop()
            loop.create_task(update_db(name))

            if inspect.iscoroutinefunction(func):
                return await func(*args, **kwargs)
            else:
                return func(*args, **kwargs)

        return wrapped
    return wrapper


