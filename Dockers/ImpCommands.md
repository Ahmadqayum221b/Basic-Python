Commands that are important for dockers.
sudo docker build -t ImageName .
sudo docker run -p portnumber:3000 ImageName
sudo docker ps => lets you check the containers.
sudo docker ps -a => lets you check all the containers that are active or not.
sudo docker images => lets you check all the images.
sudo docker inspect ImageName
sudo docker inspect container_id
sudo docker compose up --build => lets you build a multi-container.
sudo docker volume create VolumeName
sudo docker run -d -p portNumber:3000 -v VolumeName:/etc/todos ImageName => this makes your data persistant.
sudo docker rm -f containerid 
instead of creating a volume you can just directly write $PWD/foldername:/etc/todos
sudo docker compose run name inside docker-compose.yml => this actually runs your project folder. 
sudo docker compose up --build is like making the build and keeping a check on the project folder tthat whether all the things are working or not.
