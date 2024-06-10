from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.models import Student, Contact


def remove_contacts():
    remove_contact_s = session.query(Contact).filter(Contact.id < 28)

    for c in remove_contact_s:
        session.delete(c)


if __name__ == '__main__':
    try:
        remove_contacts()
        session.commit()
    except SQLAlchemyError as err:
        print(err)
        session.rollback()
    finally:
        session.close()