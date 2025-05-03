# TaskMaster 📋✨

A powerful, lightweight task management application built with Python and Django.

## 🚀 Features

- **Intuitive Task Management**: Create, organize, and track tasks with ease
- **Migrations System**: Seamless database schema evolution
- **RESTful API**: Full-featured API for integration with other services
- **Docker Support**: Easy deployment with containerization
- **SQLite Database**: Simple development setup with no external dependencies

## 🛠️ Tech Stack

- **Backend**: Django/Python
- **Database**: SQLite3
- **API**: Django REST Framework
- **Containerization**: Docker
- **Task Queue**: Asynchronous task processing

## 🏁 Getting Started

### Prerequisites

- Python 3.8+
- Docker (optional)
- pip

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/taskmaster.git
   cd taskmaster
   ```

2. Set up a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations
   ```bash
   python manage.py migrate
   ```

5. Start the development server
   ```bash
   python manage.py runserver
   ```

### Docker Setup

Alternatively, run with Docker:

```bash
docker-compose up
```

## 📁 Project Structure

```
TASK MANAGEMNET APPLICATION
├── task_management/         # Core application package
│   ├── __pycache__/        
│   ├── __init__.py         # Package initializer
│   ├── asgi.py             # ASGI config for async support
│   ├── settings.py         # Project settings
│   ├── urls.py             # URL routing
│   └── wsgi.py             # WSGI config
├── tasks/                  # Tasks module
│   └── __pycache__/        
├── migrations/             # Database migrations
│   ├── __pycache__/        
│   ├── __init__.py         
│   ├── 0001_initial.py     # Initial migration
├── admin.py                # Admin panel configuration
├── apps.py                 # App configuration
├── models.py               # Data models
├── serializers.py          # API serializers
├── tests.py                # Unit tests
├── urls.py                 # API endpoint definitions
├── views.py                # View controllers
├── db.sqlite3              # SQLite database
├── docker-compose.yml      # Docker Compose configuration
├── Dockerfile              # Docker container definition
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies
```

## 🧪 Running Tests

```bash
python manage.py test
```

## 🔄 API Documentation

The API endpoints are automatically documented and can be explored at:

```
http://localhost:8000/api/docs/
```

## 🙋‍♀️ Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Acknowledgements

- Django Project for the amazing web framework
- All our contributors and users

---

Made with ❤️ by Your Team