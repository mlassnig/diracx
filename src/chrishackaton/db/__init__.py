# import databases

# from .jobs import Base as JobsBase

# def setup_db(url, Base):
#     database = databases.Database(url)
#     engine = sqlalchemy.create_engine(
#         url, connect_args={"check_same_thread": False}
#     )
#     Base.create_all(engine)
#     return database


# jobs_db = setup_db("sqlite:///:memory:", JobsBase)

# job_db_url = "sqlite:///:memory:"


# engine = sqlalchemy.create_engine(job_db_url)