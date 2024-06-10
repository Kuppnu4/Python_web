from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, join
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

engine = create_engine("sqlite:///:memory:", echo=True)  # echo показывает в консоли работу пакета
# и генерируемые sql-query
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column('id', Integer, primary_key=True)
    fullname = Column('fullname', String)


class Address(Base):
    __tablename__ = 'address'
    id = Column('id', Integer, primary_key=True)
    email = Column('email', String(50), nullable=False)
    user_id = Column('user_id', Integer, ForeignKey('user.id'))
    user = relationship('User')


Base.metadata.create_all(engine)  # DB creature

if __name__ == '__main__':
    n_user = User(fullname='Jack Jones')
    session.add(n_user)
    n_address = Address(email='jones@asd.asd', user=n_user)
    session.add(n_address)
    session.commit()

    users = session.query(User).all()
    for row in users:
        print(row.id, row.fullname)

    user = session.query(User).filter_by(id=1).first()
    print(user.fullname)

    address = session.query(Address).filter_by(user_id=1).first()
    print(address.email, address.user.fullname)

    session.close()
