Navigte to run Project HotelBookin

1. BackEnd / Database ( mysql )

   Install MYSQL DATABASE, 
   Create Database, 
   Create User In MYSQL ( With Grant All privileges on databse )
   
2. Django Project 
    # 1. Create Virtual Env ( if you are running of local machine / virtual Folder)
            Python -m Venv HotelBookingSite
            source/(Folder)/bin/activate
    # 2. Clone Project from GitHub 
            git clone https://github.com/sumitkumar74604/HotelBooking.git
    # 3. Install Django
            pip install django
    # 4. Install mysqlclient
            pip install mysqlclient
    # 4. Run makemigrations, Migrate
            python manage.py makemigrations
            python manage.py migrate
    # 5. Run server
            python manage.py runserver 0.0.0.0:8000      
