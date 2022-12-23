from fastapi import FastAPI, Depends, Form, status, Response
import models
from database import engine, session_local
from sqlalchemy.orm import Session
from datetime import datetime

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    try:
        db = session_local()
        yield db
    finally:
        db.close()


@app.post("/create")
async def create_todo(db: Session = Depends(get_db), title: str = Form(...), description: str = Form(...)):
    todo = models.Todo(title=title, description=description, completed=False, created_at=datetime.now())
    db.add(todo)
    db.commit()
    return Response(status_code=status.HTTP_201_CREATED)


@app.get("/retrieve")
async def get_todo(id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == id).first()

    return Response(todo)


@app.get("/retrieve/all")
async def todo_list(db: Session = Depends(get_db)):
    todos = db.query(models.Todo).order_by(models.Todo.created_at.desc()).all()
    return Response(todos)


@app.post("/update/{id}")
async def update_todo(id: int, db: Session = Depends(get_db), title: str = Form(...),
                      description: str = Form(...), completed: bool = Form(...)):
    todo = db.query(models.Todo).filter(models.Todo.id == id).first()
    todo.title = title
    todo.completed = completed
    todo.description = description
    db.commit()
    return Response(status_code=status.HTTP_202_ACCEPTED)


@app.get("/delete/{id}")
async def delete(id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == id).first()
    db.delete(todo)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
