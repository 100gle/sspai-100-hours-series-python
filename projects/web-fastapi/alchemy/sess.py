from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine("sqlite://", echo=True, future=True)
Session = sessionmaker(bind=engine)


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
    with Session() as db:
        user = User(
            name="100gle", email="100gle@example.com", telephone="001-1234-5678"
        )

        db.add(user)
        db.commit()

        data = db.query(User).all()
        for row in data:
            print(row)


if __name__ == '__main__':
    main()
