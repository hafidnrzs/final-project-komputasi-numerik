from fastapi import FastAPI
from routers import derivative_routes, integral_routes

app = FastAPI(
    title="API Metode Numerik",
    description="API untuk menyelesaikan turunan dan integral menggunakan berbagai metode numerik.",
    version="0.1.0",
)
app.include_router(derivative_routes.router)
app.include_router(integral_routes.router)


# --- Endpoint Health Check ---
@app.get("/", tags=["Health Check"])
async def health_check():
    """
    Endpoint root untuk informasi API.
    """
    return {
        "message": "Selamat datang di API Metode Numerik!",
        "status": "healthy",
    }
