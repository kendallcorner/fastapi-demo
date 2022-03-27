from sqlalchemy import text
from typing import Iterable

from sqlalchemy.sql.expression import true
from backend.dao import engine
from backend.model.demo_model import Demo


class DemoDao(object):
    select_clause = text(
        """
        SELECT * FROM demo
        """
    )

    def find_all(self) -> Iterable[str]:
        with engine.connect() as conn:
            results = conn.execute(self.select_clause)
            for row in results:
                yield Demo(**dict(row))

    insert_clause = text(
        """
        INSERT INTO demo (info)
        VALUES (:info)
        RETURNING *
        """
    )

    def insert(self, info: str) -> Demo:
        with engine.begin() as conn:
            row = conn.execute(
                self.insert_clause.bindparams(info=info)
            ).fetchone()
            return Demo(**dict(row))

demo_dao_instance = DemoDao()
