alembic init alembic

#docker usage
docker-compose run app alembic revision --autogenerate -m "migration" 
docker-compose run app alembic upgrade head

#normal usage
alembic revision --autogenerate -m "migration" 
alembic upgrade head


#docker commands

DATABASE_URL=mysql+pymysql://root:root@db:3306/lms
# postgres credentials
DB_ROOT_PASSWORD=root
# DB_USER=root
DB_PASSWORD=root
DB_NAME=lms

