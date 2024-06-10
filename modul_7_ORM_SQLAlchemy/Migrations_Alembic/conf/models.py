from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, join, Date
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

Base = declarative_base()


'''
create tables dependencies "many to many" 
many teachers relates to many students and vice versa
'''


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120))
    last_name = Column(String(120))
    email = Column(String(100))
    phone = Column('cell_phone', String(100))
    address = Column(String(100))
    start_work = Column(Date, nullable=False)
    students = relationship('Student', secondary='teachers_to_students', back_populates='teachers')


'''
back_populates делает зависимости крест на крест
'''


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120))
    last_name = Column(String(120))
    email = Column(String(100))
    phone = Column('cell_phone', String(100))
    address = Column(String(100))
    teachers = relationship('Teacher', secondary='teachers_to_students', back_populates='students')


'''
all foreign keys dependencies we show in the class TeacherStudent()
'''


class TeacherStudent(Base):
    __tablename__ = 'teachers_to_students'
    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE', onupdate='CASCADE'))
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE', onupdate='CASCADE'))


