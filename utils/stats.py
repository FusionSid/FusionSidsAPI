import aiosqlite
import os
# import asyncio

async def get_db():
    cwd = os.getcwd()
    print(cwd)
    async with aiosqlite.connect(f"{cwd}/utils/database/stats.db") as db:
        cur = await db.execute("SELECT * FROM Stats")
        data = await cur.fetchall()

    stats = {}

    for stat in data:
        stats[stat[1]] = stat[2]

    return stats


async def update_db(name : str):
    cwd = os.getcwd()
    data = await get_db()
    if name in data:
        async with aiosqlite.connect(f"{cwd}/utils/database/stats.db") as db:
            await db.execute(f"UPDATE Stats SET used={data[name]+1} WHERE name='{name}'")
            await db.commit()
            print("Updated")
    else:
        async with aiosqlite.connect(f"{cwd}/utils/database/stats.db") as db:
            await db.execute(f"INSERT INTO Stats (name, used) VALUES ('{name}', 1)")
            await db.commit()


# async def main():
#     async with aiosqlite.connect("database/stats.db") as db:
#         await db.execute("CREATE TABLE IF NOT EXISTS Stats (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, used INTEGER)")
#         await db.commit()

#     # await update_db("test")
#     print(await get_db())


# loop = asyncio.new_event_loop()
# loop.run_until_complete(main())