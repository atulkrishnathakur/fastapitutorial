from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

# Product Model
class Product(Base):
    __tablename__='product'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    def __repr__(self):
        return f"<Product id={self.id} name={self.name}>"