from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import criteria
from backend.routes import upload
from backend.routes import weights
from backend.routes import scores

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # explicit list only
    allow_credentials=False,         # only if you really need cookies/auth
    allow_methods=["*"],            # GET, POST, etc.
    allow_headers=["*"],            # Content-Type, Authorization, etc.
)

# then mount your routers…
app.include_router(criteria.router)
app.include_router(upload.router)
app.include_router(weights.router)
app.include_router(scores.router)

@app.get("/")
def health_check():
    return {"status": "API is running"}
