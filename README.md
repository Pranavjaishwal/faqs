# FAQ Management System

This is a Django-based FAQ management system that supports multi-language translations, a WYSIWYG editor, and a REST API for managing FAQs. It also includes caching for improved performance and a user-friendly admin interface.

---

## Features

- _Multi-language Support:_ FAQs can be translated into multiple languages (e.g., English, Hindi, Bengali).
- _WYSIWYG Editor:_ Answers can be formatted using a rich text editor (CKEditor).
- _REST API:_ A Django REST API is provided for managing FAQs.
- _Caching:_ Translations are cached using Redis for improved performance.
- _Admin Panel:_ A user-friendly admin interface for managing FAQs.

---

## Installation

Follow these steps to set up the project locally.

### Prerequisites

- Python 3.8+
- Redis (for caching)

### Steps

1. Clone the repository:
   git clone (https://github.com/ArmanKhan1522/faqs_project.git)
   cd faq_project

2. Create a virtual environment:
   python -m venv myenv
   myenv\Scripts\activate # On Windows
   source myenv/bin/activate # On macOS/Linux

3. Install dependencies:
   pip install -r requirements.txt

4. Run migrations:
   python manage.py migrate

5. Create a superuser:
   python manage.py createsuperuser

6. Start the development server:
   python manage.py runserver

7. Access the application:
   Home Page: http://127.0.0.1:8000/
   Admin Panel: http://127.0.0.1:8000/admin/
   API Endpoint: http://127.0.0.1:8000/api/faqs/

Usage
Admin Panel

1. Log in to the admin panel at http://127.0.0.1:8000/admin/.
2. Add FAQs with translations for questions and answers.

API Endpoints

1. Fetch FAQs in English (default):
   curl http://localhost:8000/api/faqs/

2. Fetch FAQs in Hindi:
   curl http://localhost:8000/api/faqs/?lang=hi

3. Fetch FAQs in Bengali:
   curl http://localhost:8000/api/faqs/?lang=bn

Technologies Used
Backend: Django, Django REST Framework
Database: SQLite (default)
Caching: Redis
Frontend: HTML, CSS
WYSIWYG Editor: CKEditor
Translation: Google Translate API (via googletrans)

Contributing
Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
   git checkout -b feature/your-feature-name

3. Commit your changes:
   git commit -m "Add your feature"

4. Push to the branch:
   git push origin feature/your-feature-name

5. Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Developer
Developed by: ARMAN KHAN

Key Sections in the README 1. Project Overview: A brief description of the project.

    2. Features: Highlights the key features of the project.

    3. Installation: Step-by-step instructions to set up the project locally.

    4. Usage: Examples of how to use the application.

    5. Technologies Used: Lists the technologies and tools used in the project.

    6. Contributing: Guidelines for contributing to the project.

    7. License: Information about the project's license.

    8. Developer: Your name as the developer.
