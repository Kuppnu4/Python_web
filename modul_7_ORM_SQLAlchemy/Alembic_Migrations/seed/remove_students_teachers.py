from sqlalchemy import and_, or_
from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.models import Teacher, Student, TeacherStudent


def remove_students():
    students = session.query(Student).all()

    for student in students:
        session.delete(student)


def remove_teachers():
    teachers = session.query(Teacher).all()

    for teacher in teachers:
        session.delete(teacher)


# def remove_teach_stud():
#     teach_stud_s = (session.query(TeacherStudent).filter(and_(
#         Teacher.id > 6, Student.id > 10
#         ))
#                     .join(Student)
#                     .join(Teacher)
#                     .all())
#
#     for ts in teach_stud_s:
#         session.delete(ts)


if __name__ == '__main__':
    try:
        # remove_teach_stud()
        remove_students()
        remove_teachers()
        session.commit()
    except SQLAlchemyError as err:
        print(err)
        session.rollback()
    finally:
        session.close()
