from fastapi import APIRouter, FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



router = APIRouter()

@router.get("/user")
def get_user():
    return {"Name": "Long"}
   
app.include_router(router)
app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )


if __name__ == "__main__": 
    uvicorn.run('app:app',
                host="localhost",
                port=3000
                )  