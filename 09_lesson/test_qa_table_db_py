from sqlalchemy import create_engine
from sqlalchemy.sql import text


class SubjectTable:
    __scripts = {
        "insert subject": text("insert into subject (subject_id, subject_title) values (:id, :new_title)"),
        "get max id": "select max(subject_id) from subject",
        "select by id": text("select * from subject where subject_id =:select_id"),
        "delete by id": text("delete from subject where subject_id = :select_id"),
        "update title": text("update subject set subject_title = :new_title where subject_id = :id")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def create_subject(self, subject_id, title):
        self.__db.execute(self.__scripts["insert subject"], id=subject_id, new_title=title)

    def get_max_id(self):
        return self.__db.execute(self.__scripts["get max id"]).fetchall()[0][0]

    def get_subject(self, subject_id):
        return self.__db.execute(self.__scripts["select by id"], select_id=subject_id).fetchall()

    def delete_subject(self, subject_id):
        self.__db.execute(self.__scripts["delete by id"], select_id=subject_id)

    def update_subject(self, title, actual_id):
        self.__db.execute(self.__scripts["update title"], new_title=title, id=actual_id)
