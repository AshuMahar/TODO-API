# JWT TODO API

Simple Flask TODO API with JWT authentication and MongoDB.

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
