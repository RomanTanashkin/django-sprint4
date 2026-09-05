# Blogicum

Blog platform on Django: authors publish posts in categories and locations, readers comment, every user has a public profile page.

Built during the *Python Developer* course at Yandex Practicum (2025–2026). Every project was reviewed and accepted by a course mentor. Final stage of the Django module (four sprints: project setup → ORM and admin → forms and authentication → testing).

## Features

- Posts with category, location, cover image, scheduled publication date
- Unpublished and future-dated posts are hidden from readers, visible to the author
- Comments with edit/delete for the comment author
- User registration, login, profile page with pagination, profile editing
- Static pages (About, Rules), custom 403/404/500 pages
- Bootstrap 5 templates

## Tech stack

Python 3 · Django · django-bootstrap5 · SQLite · pytest

## Run locally

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
cd blogicum
python manage.py migrate
python manage.py loaddata ../db.json    # demo data
python manage.py runserver
```

Optional: set `DJANGO_SECRET_KEY` in the environment; a development default is used otherwise.

## Tests

```bash
pytest          # 26 tests
```

## Author

Roman Tanashkin — [github.com/RomanTanashkin](https://github.com/RomanTanashkin)
