from fastapi import FastAPI

from routes.load import router as load_router

from routes.query import router as query_router

app = FastAPI(
    title="AI Data Extraction System"
)

app.include_router(load_router)

app.include_router(query_router)