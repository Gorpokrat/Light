import pytest
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select, delete, insert, update

# Строка подключения к базе данных
CONN_STR = 'postgresql://qa:skyqa@5.101.50.27:5432/x_clients'

# Создаем движок SQLAlchemy
engine = create_engine(CONN_STR)

# Определение таблицы students (без поля age)
metadata = MetaData()

students = Table(
    'students', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String)
)

@pytest.fixture(scope='function')
def setup_and_teardown():
    yield
    # Очистка данных после каждого теста
    with engine.connect() as conn:
        conn.execute(delete(students).where(students.c.name == 'Test Student'))

def test_add_student():
    with engine.connect() as conn:
        # Добавляем студента
        conn.execute(insert(students).values(name='Test Student'))
        # Проверяем добавление
        result = conn.execute(select(students).where(students.c.name == 'Test Student')).fetchone()
        assert result is not None
        assert result['name'] == 'Test Student'

def test_update_student():
    with engine.connect() as conn:
        # Добавляем студента для обновления
        conn.execute(insert(students).values(name='Test Student'))
        # Обновляем имя (или другие поля при наличии)
        conn.execute(update(students).where(students.c.name == 'Test Student').values(name='Updated Student'))
        # Проверяем обновление
        result = conn.execute(select(students).where(students.c.name == 'Updated Student')).fetchone()
        assert result is not None
        assert result['name'] == 'Updated Student'

def test_delete_student():
    with engine.connect() as conn:
        # Добавляем студента для удаления
        conn.execute(insert(students).values(name='Test Student'))
        # Удаляем студента
        conn.execute(delete(students).where(students.c.name == 'Test Student'))
        # Проверяем удаление
        result = conn.execute(select(students).where(students.c.name == 'Test Student')).fetchone()
        assert result is None
