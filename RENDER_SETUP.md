Render deployment quick setup

1) Create a Render account at https://render.com and create a new Web Service.
   - For "Connect a repository", choose the GitHub repo: https://github.com/AshuMahar/TODO-API
   - Build Command: leave empty (Render will detect Python). Start Command: `gunicorn app:app`
   - Set the Environment to "Python" and choose the region (e.g., Oregon).

2) Add environment variables on Render:
   - `MONGO_URI` — your MongoDB connection string (do NOT include this file in the repo)
   - `JWT_SECRET_KEY` — a secure random string
   - `PORT` — set to `5000` or leave default

3) If you want automatic deploys from GitHub, enable the GitHub integration in Render and connect the repo.

4) (Optional) To trigger deploys from GitHub Actions, go to your Render Dashboard → Service → Settings → API Keys and create a "Service Key". Then add two GitHub repository secrets:
   - `RENDER_API_KEY` — the service API key value
   - `RENDER_SERVICE_ID` — the service id (found in the service URL or API)

5) Security notes:
   - Never commit `.env` with secrets. Use `.env.example` for keys only.
   - Use IP whitelisting for MongoDB Atlas in production (avoid 0.0.0.0/0 long-term).
