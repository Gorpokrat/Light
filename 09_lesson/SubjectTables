import pytest
from SubjectTable import SubjectTable


db_subject = SubjectTable("postgresql+psycopg2://postgres:12345@localhost:5432/postgres")

@pytest.mark.parametrize("subject_title", [
    "Art",
    "Applied Math",
    "PE",
    "Literature - 2"
])
def test_add_subject(subject_title):
    db_subject.create_subject(db_subject.get_max_id() + 1, subject_title)
    new_id = db_subject.get_max_id()
    new_subject = db_subject.get_subject(new_id)
    db_subject.delete_subject(new_id)
    assert new_subject[0][1] == subject_title


@pytest.mark.parametrize("subject_title, new_subject_title", [
    ("Art", "Motion Art"),
    ("Applied Math", "Applied Math II"),
    ("PE", "Physical Education"),
     ("Literature - 2", "Literature for experts")
])
def test_update_subject(subject_title, new_subject_title):
    db_subject.create_subject(db_subject.get_max_id() + 1, subject_title)
    new_id = db_subject.get_max_id()
    db_subject.update_subject(new_subject_title, new_id)
    new_subject = db_subject.get_subject(new_id)
    db_subject.delete_subject(new_id)
    assert new_subject[0][1] == new_subject_title


def test_delete_subject():
    subject_title = 'Chemistry'
    db_subject.create_subject(db_subject.get_max_id() + 1, subject_title)
    new_id = db_subject.get_max_id()
    db_subject.delete_subject(new_id)
    rows = db_subject.get_subject(new_id)
    assert len(rows) == 0
