from sqlalchemy import Column, Integer, String, DateTime, Boolean
from database import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    completed = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'{self.title}'
