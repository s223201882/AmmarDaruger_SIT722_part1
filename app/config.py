import os

class Settings:
    DATABASE_URL: str = os.getenv("postgresql://sit722_part1_db_32nf_user:82hFDixW65kmS40VgupdxYXaRy7tnJK3@dpg-cr0tvsbqf0us73ffsqlg-a.oregon-postgres.render.com/sit722_part1_db_32nf")

settings = Settings()
