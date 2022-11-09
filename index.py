from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Entidades import Tabela1, Tabela2
from datetime import date

engine = create_engine('mysql://root:root@localhost/test')
db_session = sessionmaker(bind=engine)()


def getAll(db_session, obj):
    return db_session.query(obj).all()


def add(db_session, obj):
    db_session.add(obj)
    db_session.commit()


def delete(db_session, obj, id):
    obj = db_session.query(obj).filter_by(id=id).first()
    db_session.delete(obj)
    db_session.commit()

