import asyncpg
import asyncio
from config import data


class Database():
    def __init__(self):
        loop = asyncio.get_event_loop()
        self.pool : asyncio.pool.Pool = loop.run_until_complete(
            asyncpg.create_pool(
                user = data.PGUSER,
                database = data.DBNAME,
                password = data.PGPASSWORD,
                host = data.IP,
                port = data.DBPORT,
                loop = loop
            )
        )

    async def new_user(self,user_id, user_name):
        try:
            sql = "INSERT INTO users (user_id, user_name) VALUES($1,$2)"
            await self.pool.execute(sql,user_id,user_name)
        except:
            pass


    async def get_users(self):
        sql = "SELECT user_id FROM users"
        res = await self.pool.fetch(sql)
        return res

    async def get_tel_book(self):
        sql = "select user_name, user_id from users order by user_name ASC"
        res = await self.pool.fetch(sql)
        return res