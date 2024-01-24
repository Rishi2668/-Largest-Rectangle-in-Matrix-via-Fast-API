# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from rectangle_logic import largest_rectangle
from database import Base, engine, SessionLocal, Log
from typing import List
from datetime import datetime


app = FastAPI()

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Pydantic model for input matrix
class MatrixRequest(BaseModel):
    matrix: List[List[int]]



# FastAPI endpoint
@app.post("/largest_rectangle")
async def get_largest_rectangle(matrix_request: MatrixRequest):
    matrix = matrix_request.matrix
    log_entry = Log(request=str(matrix))
    result = largest_rectangle(matrix)
    
    

    with SessionLocal() as db:
        # Calculate turnaround time
        start_time = datetime.utcnow()

        
        # Calculate turnaround time
        end_time = datetime.utcnow()
        turnaround_time = (end_time - start_time).total_seconds() * 1000  # in milliseconds

        log_entry.response = str(result)
        log_entry.turnaround_time = int(turnaround_time)
        db.add(log_entry)
        db.commit()
        db.close()

    return result


# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000)
