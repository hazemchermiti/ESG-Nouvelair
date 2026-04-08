# Architecture REST API - ESG Nouvelair

## Structure du projet

```
ESG-Nouvelair/
├── main.py                 # Point d'entrée de l'application
├── requirements.txt        # Dépendances Python
├── .env.example           # Exemple de configuration
├── .env                   # Configuration (git ignored)
└── app/
    ├── __init__.py
    ├── config.py          # Configuration globale
    ├── api/
    │   ├── __init__.py
    │   ├── api.py         # Configuration FastAPI
    │   └── endpoints/
    │       ├── __init__.py
    │       ├── health.py  # Endpoints de santé
    │       └── users.py   # Endpoints utilisateurs
    ├── models/
    │   ├── __init__.py
    │   └── user.py        # Schémas Pydantic
    ├── services/
    │   ├── __init__.py
    │   └── user_service.py # Logique métier
    ├── database/
    │   ├── __init__.py
    │   ├── db.py          # Configuration BD
    │   └── models.py      # Modèles ORM
    └── utils/
        ├── __init__.py
        └── responses.py   # Utilitaires de réponse
```

## Principes architecturaux

### 1. **Séparation des responsabilités**
- **Models**: Schémas Pydantic pour la validation des données
- **Services**: Logique métier et opérations complexes
- **Endpoints**: Handlers HTTP simples et directs
- **Database**: Configuration et modèles ORM

### 2. **Structure en couches**
```
HTTP Request
     ↓
API Endpoint (api/endpoints/)
     ↓
Service (services/)
     ↓
Database (database/ + ORM models)
     ↓
Data Storage
```

### 3. **Configuration centralisée**
- Toutes les settings dans `app/config.py`
- Support des variables d'environnement (.env)
- Configuration facile à modifier

## Installation

### 1. Créer un environnement virtuel
```bash
python -m venv venv
```

### 2. Activer l'environnement
**Windows:**
```bash
.\venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Créer le fichier .env
```bash
cp .env.example .env
```

## Lancer l'application

### Développement
```bash
python main.py
```

L'API sera disponible à `http://localhost:8000`

### Documentation interactive
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints disponibles

### Health Check
- `GET /health` - Vérifier la santé de l'API
- `GET /` - Page d'accueil

### Utilisateurs (v1)
- `GET /api/v1/users` - Lister tous les utilisateurs
- `GET /api/v1/users/{id}` - Récupérer un utilisateur
- `POST /api/v1/users` - Créer un utilisateur
- `PUT /api/v1/users/{id}` - Modifier un utilisateur
- `DELETE /api/v1/users/{id}` - Supprimer un utilisateur

## Exemple de requête

### Créer un utilisateur
```bash
curl -X POST "http://localhost:8000/api/v1/users" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "full_name": "John Doe",
    "password": "securepassword123"
  }'
```

### Réponse
```json
{
  "success": true,
  "message": "User created successfully",
  "data": {
    "id": 1,
    "email": "user@example.com",
    "full_name": "John Doe",
    "is_active": true,
    "created_at": "2024-01-15T10:30:00",
    "updated_at": null
  },
  "errors": null
}
```

## Prochaines étapes

1. **Authentification**: Ajouter JWT authentication
2. **Validation**: Améliorer la validation des emails
3. **Hashing**: Utiliser bcrypt pour les passwords
4. **Tests**: Créer des tests unitaires et d'intégration
5. **Logging**: Configurer un système de logging robuste
6. **Documentation**: Ajouter des docstrings détaillées
7. **Migrations**: Utiliser Alembic pour les migrations BD

## Technologies utilisées

- **FastAPI**: Framework web moderne et performant
- **SQLAlchemy**: ORM powerful pour la base de données
- **Pydantic**: Validation robuste des données
- **Uvicorn**: Serveur ASGI haute performance
