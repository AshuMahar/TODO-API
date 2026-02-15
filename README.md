# JWT TODO API

Simple Flask TODO API with JWT authentication and MongoDB.

**🌐 Live Demo**: https://todo-api-zf6r.onrender.com

## API Endpoints

## New endpoints

- **Update Todo**
	- `PUT /api/v1/todos/<todo_id>`
	- Requires `Authorization: Bearer <access_token>` header
	- Body (JSON): `{ "title": "...", "desc": "...", "is_complete": true|false }`

- **Delete Todo**
	- `DELETE /api/v1/todos/<todo_id>`
	- Requires `Authorization: Bearer <access_token>` header

- **Refresh Access Token**
	- `POST /api/v1/auth/refresh`
	- Requires `Authorization: Bearer <refresh_token>` header
	- Response: `{ "access_token": "..." }`

- **Logout (revoke refresh token)**
	- `POST /api/v1/auth/logout`
	- Requires `Authorization: Bearer <refresh_token>` header
	- Stores the token's `jti` in the `token_blacklist` collection so it cannot be reused

Example curl to refresh:

```
curl -X POST \
	-H "Authorization: Bearer <REFRESH_TOKEN>" \
	https://your-host/api/v1/auth/refresh
```

Example curl to logout:

```
curl -X POST \
	-H "Authorization: Bearer <REFRESH_TOKEN>" \
	https://your-host/api/v1/auth/logout
```

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|----------------|
| POST | `/api/v1/auth/register` | User signup | ❌ No |
| POST | `/api/v1/auth/login` | JWT login | ❌ No |
| GET | `/api/v1/auth/profile` | Get user profile | ✅ Yes |
| POST | `/api/v1/todos` | Create todo | ✅ Yes |
| GET | `/api/v1/todos?page=1&limit=5` | List todos with pagination | ✅ Yes |

**Base URL**: https://todo-api-zf6r.onrender.com

### Quick Test (Postman)
1. Register: `POST /api/v1/auth/register` with `{"name":"User","email":"user@example.com","password":"pass123"}`
2. Login: `POST /api/v1/auth/login` with `{"email":"user@example.com","password":"pass123"}` → copy `access_token`
3. Use token: Add header `Authorization: Bearer <token>` to protected endpoints

Setup (local):

1. Create and activate virtualenv:

```powershell
py -3 -m venv myvenv
.\myvenv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and fill values (especially `MONGO_URI` and `JWT_SECRET_KEY`).

4. Run locally:

```powershell
python app.py
```

Prepare for deployment:

- `Procfile` included for use with services like Render/Heroku: `web: gunicorn app:app`.
- `.env.example` lists required environment variables; do not commit secrets.

Recommended deployment flow (GitHub + Render):

1. Initialize a git repo locally and push to GitHub (see commands below).  
2. Create a MongoDB Atlas cluster, database user, and obtain the connection string.  
3. On Render (or Railway), create a new Web Service from the GitHub repo and set env vars (`MONGO_URI`, `JWT_SECRET_KEY`, `PORT`).  
4. Use `gunicorn app:app` as the start command (Procfile already set this).

Commands to push to GitHub (replace `<repo-url>`):

```powershell
git remote add origin <repo-url>
git push -u origin main
```

If you have `gh` (GitHub CLI) installed and authenticated you can run:

```powershell
gh repo create <repo-name> --public --source=. --remote=origin --push
```

MongoDB Atlas quick steps:

1. Sign into https://cloud.mongodb.com and create a free cluster.  
2. Create a database user with a password and give it `Read and write` access to the database.  
3. In Network Access add your deployment IP (or 0.0.0.0/0 for testing).  
4. Copy the connection string and set `MONGO_URI` in your Render/GitHub secrets.

What I created/changed: see `ashu.txt` for a short changelog.
