from sqlalchemy import Integer, String, ForeignKey, create_engine, join, select, and_, or_, not_, desc, func
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, Mapped, mapped_column

engine = create_engine("sqlite:///:memory:", echo=True)  # echo показывает в консоли работу пакета
# и генерируемые sql-query
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(String(120))


class Address(Base):
    __tablename__ = 'address'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship('User')


Base.metadata.create_all(engine)  # DB creature

if __name__ == '__main__':
    n_user = User(fullname='Jack Jones')
    session.add(n_user)
    n_address = Address(email='jones@asd.asd', user=n_user)
    session.add(n_address)
    n_address = Address(email='jones_double@asd.asd', user=n_user)
    session.add(n_address)
    session.commit()

    n_user = User(fullname='Senior Pomidor')
    session.add(n_user)
    n_address = Address(email='pomidor@asd.asd', user=n_user)
    session.add(n_address)
    session.commit()

    n_user = User(fullname='Senior Muhomor')
    session.add(n_user)
    n_address = Address(email='pomidor@asd.asd', user=n_user)
    session.add(n_address)
    n_address = Address(email='pomidor_gmail@asd.asd', user=n_user)
    session.add(n_address)
    n_address = Address(email='pomidor_onemore@asd.asd', user=n_user)
    session.add(n_address)
    session.commit()

    n_user = User(fullname='Adam Smith')
    session.add(n_user)
    n_address = Address(email='pomidor@asd.asd', user=n_user)
    session.add(n_address)
    session.commit()

    statement = select(User.id, User.fullname)
    for row in session.execute(statement):
        print(row)

    statement = select(Address.id, Address.email, User.fullname).join(User)
    for row in session.execute(statement):
        print(row)

    statement = select(User)
    columns = ['id', 'fullname']
    print('_______________________scalars_________________________________')
    users = [dict(zip(columns, (row.id, row.fullname))) for row in
             session.execute(statement).scalars()]  # with scalars()
    print(users)
    print('_______________________all_____________________________________')
    users = [dict(zip(columns, (row.User.id, row.User.fullname))) for row in
             session.execute(statement).all()]  # with all()
    print(users)
    print('________________________with class object_______________________')
    users = [dict(zip(columns, (row.User.id, row.User.fullname))) for row in
             session.execute(statement)]  # without scalars()
    print(users)

    # WHERE
    statement = select(User).where(User.fullname == 'Senior Pomidor')
    r = session.execute(statement).scalar_one_or_none()
    if r:
        print(dict(zip(columns, (r.id, r.fullname))))

    # WHERE WHERE
    statement = select(User).where(User.fullname.like('Senior%')).where(User.id == 3)
    r = session.execute(statement).scalars()
    print([dict(zip(columns, (row.id, row.fullname))) for row in r])

    # WHERE AND
    statement = select(User).where(and_(User.fullname.like('Senior%'), User.id == 3))
    r = session.execute(statement).scalars()
    print([dict(zip(columns, (row.id, row.fullname))) for row in r])

    # WHERE OR
    statement = select(User).where(or_(User.fullname.like('Senior%'), User.id == 3))
    r = session.execute(statement).scalars()
    print([dict(zip(columns, (row.id, row.fullname))) for row in r])

    # WHERE NOT
    statement = select(User).where(not_(User.fullname.like('Senior%')))
    r = session.execute(statement).scalars()
    print([dict(zip(columns, (row.id, row.fullname))) for row in r])

    # ORDER BY
    statement = select(User).order_by(desc(User.fullname))
    columns = ['id', 'fullname']
    users = [dict(zip(columns, (row.User.id, row.User.fullname))) for row in session.execute(statement)]
    print(users)

    statement = (
        select(User.fullname, func.count(Address.id))
        .join(Address)
        .group_by(User.fullname)
    )
    res = session.execute(statement).mappings()
    for row in res:
        print(row)

    # res = session.execute(statement)
    # for fullname, count in res:
    #     print(f'fullname: {fullname}, emails: {count}')

    # columns = ['fullname', 'number of emails']
    # print([dict(zip(columns, (r[0], r[1]))) for r in res])

    session.close()
