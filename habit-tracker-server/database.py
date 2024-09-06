import sqlalchemy as sql
import sqlalchemy.ext.declarative as declatative
import sqlalchemy.orm as orm
import dotenv
import os

dotenv.load_dotenv(".env")

DATABASE_URL = os.getenv("DATABASE_PUBLIC_URL") # "postgresql://habituser:habit1234@localhost:5432/habitdb"
print(DATABASE_URL)


engine = sql.create_engine(DATABASE_URL)
SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declatative.declarative_base()