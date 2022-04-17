# pylint: disable=E1101

from src.infra.config import DBconnectionHeadler
from src.infra.entites import Users


class FakerRepo:
    """A simple Repository"""

    @classmethod
    def insert_use(cls):
        """Something"""

        with DBconnectionHeadler() as db_conection:
            try:
                new_user = Users(name="João", password="123")
                db_conection.session.add(new_user)
                db_conection.session.commit()
            except:
                db_conection.session.rollback()
                raise
            finally:
                db_conection.session.close()
