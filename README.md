# Hospital Management  

A simple **Django-based Hospital Management System** with features like appointment scheduling, user registration, blogs, and more.

## Setup  
1. Clone the repository:  
   ```bash
   git clone https://github.com/FADHILI-Josue/Hospital-Management-System  
   ```
2. Create and activate a virtual environment:  
   ```bash
   python -m venv env  
   env\Scripts\activate
   ```
3. Install dependencies:  
   ```bash
   pip install -r requirements.txt  
   ```
4. Apply migrations and run server:  
   ```bash
   cd app
   python manage.py migrate  
   python manage.py runserver  
   ```
5. Access the app at [http://localhost:8000](http://localhost:8000). 

## seeding dummy data
```bash
python manage.py loaddata seed/categories.json 
python manage.py loaddata seed/specialities.json
python manage.py loaddata seed/status.json
python manage.py loaddata seed/time.json
```