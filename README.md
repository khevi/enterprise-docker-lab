# Enterprise Docker Lab

A production-style DevOps lab built on Ubuntu using Docker Compose, Nginx, Flask, MySQL, persistent storage, and custom Docker networking.

## Architecture

```text
User Browser
     |
     v
Nginx Reverse Proxy :8091
     |
     v
Flask Application :5000
     |
     v
MySQL Database :3306
     |
     v
Persistent Host Storage
/opt/devops/enterprise-app/mysql/data

How to Run
git clone https://github.com/khevi/enterprise-docker-lab.git
cd enterprise-docker-lab
docker network create enterprise-app-net
docker compose up -d --build
Test the Application
curl http://localhost:8081
curl http://localhost:8081/health
curl http://localhost:8091
Services
Service	Container	Port	Purpose
Nginx	app-nginx	8091:80	Reverse proxy
Flask	flask-app	8081:5000	Web application
MySQL	mysql-db	3306	Database
Key DevOps Concepts Demonstrated
Multi-container application deployment
Docker Compose orchestration
Custom Docker bridge network
Container-to-container communication by service name
MySQL persistent storage using bind mounts
Nginx reverse proxy configuration
Dockerfile-based image build
Health checks and dependency ordering
GitHub version control workflow
Useful Commands
docker compose ps
docker compose logs -f
docker compose down
docker compose up -d --build
docker network inspect enterprise-app-net
docker exec -it mysql-db mysql -uappuser -pAppPass123 devopsdb
Persistence

MySQL data is stored outside the container at:

/opt/devops/enterprise-app/mysql/data

This allows the database container to be removed and recreated without losing data.
EOF
