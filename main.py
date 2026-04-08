"""
Point d'entrée principal de l'application
"""
import uvicorn
from fastapi import FastAPI

# Créer l'application
app = FastAPI(title="ESG API", version="1.0.0")


@app.get("/")
def root():
    """Route racine"""
    return {"message": "Bienvenue sur ESG API"}

