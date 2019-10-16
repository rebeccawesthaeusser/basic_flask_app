# Basic Flask App

This is a basic Flask App.  
What I used:  
 -Python & Flask  
 -MySQL  
 -Jenkins  
 -Docker  
 -Tox   
       
Docker commands to start the Docker Image:  
 - 
 -check out the Docker Hub Page https://hub.docker.com/r/rw044/flask_tutorial     
 -docker pull rw044/flask_tutorial:latest  
 -docker run -e PYTHONUNBUFFERED=0 -d -p 5000:5000 rw044/flask_tutorial:latest (returns container ID)    
 -open browser and go to http://127.0.0.1:5000/   
 
Docker commands to change & push the Image:
 - 
 -docker build -t flask_tutorial:latest .  
 -docker push flask_tutorial:latest  
 
Docker command for logging:
 -
 docker logs container_id -f
    
  