from sqlalchemy import func, desc, select, and_

from conf.models import Grade, Teacher, Student, Subject, Group
from conf.db import session


def select_01():
    """
    SELECT
        s.id,
        s.fullname,
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 5;
    """
    result = (session
              .query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade'))
              .select_from(Student).join(Grade).group_by(Student.id).order_by(desc('average_grade')).limit(5).all())
    return result


def select_02():
    """
    SELECT
        s.id,
        s.fullname,
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM grades g
    JOIN students s ON s.id = g.student_id
    WHERE g.subject_id = 1
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 1;
    """
    result = (session
              .query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade'))
              .select_from(Grade).join(Student).filter(Grade.subjects_id == 1).group_by(Student.id).order_by(
        desc('average_grade')).limit(1).all())
    return result


def select_03():
    """
    select MAX(grade_date)
    from grades g
    join students s on s.id = g.student_id
    where g.subject_id = 1 and s.group_id = 1

    select s.id , s.fullname, s.group_id , g.grade, g.grade_date
    from grades g
    join students s on g.student_id = s.id
    where g.subject_id = 1 and s.group_id  = 1 and g.grade_date = (
        select MAX(grade_date)
        from grades g
        join students s on s.id = g.student_id
        where g.subject_id = 1 and s.group_id  = 1
    )
    """
    subquery = (select(func.max(Grade.grade_date))
                .join(Student)
                .filter(and_(Grade.subjects_id == 2, Student.group_id == 3))).scalar_subquery()

    """
    scalar_subquery() - special method to create subquery for further usage
    """

    result = session.query(Student.id, Student.fullname, Student.group_id, Grade.grade, Grade.grade_date) \
        .select_from(Grade) \
        .join(Student) \
        .filter(and_(Grade.subjects_id == 2, Student.group_id == 3, Grade.grade_date == subquery)) \
        .all()

    return result


if __name__ == '__main__':
    print(select_03(), '<<<>>>')
