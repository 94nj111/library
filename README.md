
# Django Catalog Application

This project is a Django-based catalog of books.

## Installation Steps

### 1. Clone the Repository
Clone the repository to your local machine:

```bash
git clone <REPOSITORY_URL>
cd <REPOSITORY_FOLDER_NAME>
```

### 2. Create and Activate a Virtual Environment
Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment:

- **Linux/MacOS:**
  ```bash
  source .venv/bin/activate
  ```

- **Windows:**
  ```bash
  .venv\Scripts\activate
  ```

### 3. Install Dependencies
Install the required libraries from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations
Run migrations to set up the database:

```bash
python manage.py migrate
```

### 5. Load Fixture Data
Populate the database using the provided fixture file:

```bash
python manage.py loaddata fixtures.json
```

### 6. Start the Development Server
Run the Django development server:

```bash
python manage.py runserver
```

You can now access the project in your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Notes
- Make sure you have Python 3.8 or later installed.
- The `django-debug-toolbar` requires the server to run in debug mode (`DEBUG = True` in Django settings).
