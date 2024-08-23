import sqlalchemy as sql
import sqlalchemy.ext.declarative as declatative
import sqlalchemy.orm as orm

DATABASE_URL = "postgresql://habituser:habit1234@localhost:5432/habitdb"


engine = sql.create_engine(DATABASE_URL)
SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declatative.declarative_base()