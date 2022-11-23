# HexOcean-DRF-Task

# Running the Project Locally (Windows 10)

## Installation

First, clone the repository to your local machine (SSH example):

```bash
git clone git@github.com:Rantoryu/HexOcean-DRF-Task.git
```

Move to drf_project folder that contains manage.py file (using terminal from IDE):
```bash
cd .\drf_project\
```

Activate virtual environment:
```bash
.\Scripts\activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at 127.0.0.1:8000.
