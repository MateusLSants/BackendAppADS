from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.infra.config import Base


class Users(Base):
    """Users Entity"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False, unique=False)
    id_produto = relationship("Produtos")

    def __rep__(self):
        return f"User [name = {self.name}]"
