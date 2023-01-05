from sqlalchemy import Column, Integer, String, create_engine, insert, select
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine("sqlite://", echo=True, future=True)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(10), nullable=False)
    email = Column(String(20))
    telephone = Column(String(11))

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}', telephone='{self.telephone}')>"


def main():
    Base.metadata.create_all(engine)
    db = engine.connect()
    stmt = (
        insert(User)
        .values(name="100gle", email="100gle@example.com", telephone="001-1234-5678")
        .compile()
    )

    db.execute(stmt)
    db.commit()

    query = select(User)
    data = db.execute(query).all()
    for row in data:
        print(row)

    db.close()


if __name__ == '__main__':
    main()
