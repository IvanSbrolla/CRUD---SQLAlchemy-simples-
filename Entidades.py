from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_utils import database_exists, create_database

database_name = 'test'
engine = create_engine(f'mysql://root:root@localhost/{database_name}')
Base = declarative_base()

if not database_exists(engine.url):
    create_database(engine.url)


class Tabela1(Base):
    __tablename__ = 'tabela1'  # campo obrigatorio
    id = Column(Integer, primary_key=True)
    texto = Column(String(20))
    valor_decimal = Column(DECIMAL(10, 2))
    valor_inteiro = Column(Integer)
    data = Column(Date) # recebe um tipo datetime.date


class Tabela2(Base):
    __tablename__ = 'movimentacoes'
    id = Column(Integer, primary_key=True) # usar o __tablename__ da outra tabela
    id_tabela1 = Column(Integer, ForeignKey('tabela1.id'))
    tabela1 = relationship('Tabela1') # usar o nome da classe


Base.metadata.create_all(bind=engine)
