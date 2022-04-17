import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from src.infra.config import Base


class ProdutosTypes(enum.Enum):
    """Defining Produtos Type"""

    eletronico = "eletronico"
    automovel = "automovel"


class Produtos(Base):
    """Produtos Entity"""

    __tablename__ = "Produtos"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=False)
    typeP = Column(Enum(ProdutosTypes, nullable=False))
    description = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        out_name = f"Produto [name = {self.name}]"
        out_type = f"Produto [name = {self.name}]"
        out_desc = f"Produto [name = {self.name}]"
        out_userid = f"Produto [name = {self.name}]"
        return out_name, out_type, out_desc, out_userid
