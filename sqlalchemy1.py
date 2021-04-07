from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import Session

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Classroom(Base):
    __tablename__ = 'classroom'
    id = Column(Integer,primary_key=True)
    teacher_name = Column(String(255))

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    hobby = Column(String(255))
    classroom_id = Column(Integer, ForeignKey(Classroom.id))

class Grade(Base):
    __tablename__ = 'grade'
    id = Column(Integer,primary_key=True)
    exam_id = Column(Integer)
    student_id = Column(Integer, ForeignKey(Student.id))
    exam_score = Column(Integer)