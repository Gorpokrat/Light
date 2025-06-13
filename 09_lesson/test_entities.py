import pytest
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select, delete, insert, update

CONN_STR = 'postgresql://qa:skyqa@5.101.50.27:5432/x_clients'


engine = create_engine(CONN_STR)
metadata = MetaData()

students = Table(
    'students', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)
)

@pytest.fixture(scope='function')
def setup_and_teardown():
    yield
  
    with engine.connect() as conn:
        conn.execute(delete(students).where(students.c.name == 'Test Student'))

def test_add_student(setup_and_teardown):
    # Добавление студента
    with engine.connect() as conn:
        conn.execute(insert(students).values(name='Test Student', age=20))
        # Проверка добавления
        result = conn.execute(select([students]).where(students.c.name == 'Test Student')).fetchone()
        assert result is not None
        assert result['name'] == 'Test Student'

def test_update_student(setup_and_teardown):
    # Сначала добавим студента для обновления
    with engine.connect() as conn:
        conn.execute(insert(students).values(name='Test Student', age=20))
        # Обновляем его возраст
        conn.execute(update(students).where(students.c.name == 'Test Student').values(age=21))
        # Проверяем обновление
        result = conn.execute(select([students]).where(students.c.name == 'Test Student')).fetchone()
        assert result['age'] == 21

def test_delete_student(setup_and_teardown):
    # Добавляем студента для удаления
    with engine.connect() as conn:
        conn.execute(insert(students).values(name='Test Student', age=20))
        # Удаляем его
        conn.execute(delete(students).where(students.c.name == 'Test Student'))
        # Проверяем удаление
        result = conn.execute(select([students]).where(students.c.name == 'Test Student')).fetchone()
        assert result is None
