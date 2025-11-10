from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import uvicorn

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False


tasks: List[Task] = []


@app.get("/tasks", response_model=List[Task])
async def get_task():
    return tasks


@app.post("/tasks", response_model=List[Task])
async def create_task():
    if any(t.id == task.id for t in tasks):
        raise HTTPException(status_code=400, detail="Task already exist!")
    tasks.append(task)
    return tasks


@app.put("/tasks/{id}", response_model=Task)
async def update_task(id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == id:
            if updated_task.id != id:
                raise HTTPExceotion(
                    status_code=400, detail="Cannot change task due to invalid id")
            tasks[index] = updated_task
            return updated_task
        raise HTTPException(status_code=400, detail="Task not found")


@app.delete("/task/{id}", response_model=Task)
async def delete_id(id: int):
    for index, task in enumerate(tasks):
        if task.id == id:
            tasks.pop(index)
            return {"message": f"Task {id} has been successfully deleted!"}
    raise HTTPExceotion(
        status_code=404, detail="Task cannot be deleted.ERROR!")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
