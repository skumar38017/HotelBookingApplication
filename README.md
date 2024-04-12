Navigte to run Project HotelBookin

1. BackEnd / Database ( mysql )

  # 1.( Install MYSQL DATABASE, )
     sudo apt update
     sudo apt install mysql-server
     sudo systemctl status mysql
     sudo mysql -u root -p 
  
  # 2. ( Create Database, )
      CREATE DATABASE <name of project database>
  # 3. ( Create User In MYSQL ( With Grant All privileges on databse ) )
       GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'host';
       GRANT ALL PRIVILEGES ON demo.* TO 'myuser'@'localhost';
       GRANT ALL PRIVILEGES ON demo.* TO 'myuser'@'%';

   
2. Django Project
3. 
    # 1. Create Virtual Env ( if you are running of local machine / virtual Folder)
            Python -m Venv HotelBookingSite
            source/(Folder)/bin/activate
    # 2. Clone Project from GitHub 
            git clone https://github.com/sumitkumar74604/HotelBooking.git
    # 3. Install Django
            pip install django
    # 4. Install mysqlclient
            pip install mysqlclient
    # 5. Run makemigrations, Migrate
            python manage.py makemigrations
            python manage.py migrate
    # 6. Create A super User ( optional )
            python manage.py createsuperuser <enter>
            username :admin
            email :
            password:admin
            
    # 7. Run server
            python manage.py runserver 0.0.0.0:8000      
