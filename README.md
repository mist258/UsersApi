
## INSTALLATION AND LAUNCHING GUIDE


```bash
    1) git clone https://github.com/mist258/UsersApi.git

    2) poetry shell  (#initaialize environment)

    3) poetry install  (#install dependencies)

    4) Create a .env file and set the variables according to .env.example.

    5) psql -h [your-host] -p [your-port] -U [your-username] (#execute current cmd in console to create db (example: psql -h localhost -p 5432 -U postgres))

    6) CREATE DATABASE [your-db-name];

    7) exit;

    8) alembic upgrade head  (#apply existing migration)

    


```
## If you are using PyCharm, after creating the database you can connect to it by entering the data from the .env file into the appropriate fields.
<img width="1008" height="860" alt="image" src="https://github.com/user-attachments/assets/10c0c938-a51f-4d41-98be-2f652059534b" />

