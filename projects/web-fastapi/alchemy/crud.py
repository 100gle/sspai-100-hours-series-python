import pathlib

from sqlalchemy import Column, Integer, String, create_engine, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ROOT = pathlib.Path(__file__).parent

Base = declarative_base()
engine = create_engine(f"sqlite:///{ROOT / 'alchemy.db'}", future=True)
Session = sessionmaker(bind=engine)
fake_data = [
    dict(name="100gle", email="100gle@example.com", telephone="001-1234-5678"),
    dict(name="Steve", email="steve@example.com", telephone="011-1234-4321"),
    dict(name="John", email="john@example.com", telephone="000-8764-4321"),
]


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), nullable=False)
    email = Column(String(20))
    telephone = Column(String(11))

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}', telephone='{self.telephone}')>"


def main():
    Base.metadata.create_all(engine)
    db = Session()

    # create data
    users = [User(**data) for data in fake_data]

    # same as: db.bulk_save_objects(users)
    db.add_all(users)

    # insert expression
    stmt = insert(User).values(
        name="Tom", email="tom@example.com", telephone="000-1234-5678"
    )
    db.execute(stmt)
    db.commit()

    # select data
    print("query all data: \n", db.query(User).all())
    print(
        "query the data where name is '100gle': \n",
        db.query(User).filter(User.name == "100gle").first(),
    )
    print(
        "query the data where telephone number ends with '4321': \n",
        db.query(User).filter(User.telephone.endswith("4321")).all(),
    )

    # update data
    u = db.query(User).filter(User.name == "100gle")
    print("before updating: \n", u.first())
    u.update({"email": ""})
    db.commit()
    print(f'after updating: \n', db.query(User).filter(User.name == "100gle").all())

    # delete data
    u = db.query(User).filter(User.name == "John")
    u.delete()
    db.commit()
    print("after deleting:\n", db.query(User).all())

    db.close()
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    main()
