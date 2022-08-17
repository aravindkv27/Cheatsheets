## Run Docker 

```
docker run container_name:version
```

## Lists All The Running Container

```
docker ps
```

## Show All The Running and Exited Containers

```
docker ps -a
```

## Docker Installation

**Installtion for ubuntu**
 [https://docs.docker.com/engine/install/ubuntu/](https://docs.docker.com/engine/install/ubuntu/)
 
                                        (or)
										
```
sudo apt update
sudo apt install snapd
sudo snap install docker
```

## Docker Basic Commands

**Docker pull**

	This is used to pull the images from the docker repository

```
docker pull image_name
```

**Docker run**

	This command is used to create a container from an image.
	
```
docker run image_name 
#Run a create a container.
docker run -d (or) --detach image_name 
#It run the container in background and print container ID.
```
**Docker Remove**

	This command is used to remove one or more containers.

```
docker rm container_id
```

**Docker start**

	To start the container 
	
```
docker start container_id
```

**Docker Stop**

	To stop the container use command docker stop with container id.
	
```
docker stop container_ID
```

**To list running and stopped container**

	It will show every container no matter it will run or not.
```
docker ps -a
```

**Port Container**

	Port of the host 6000 and the port we are binding which is container port. We can't use same port for different container.
	 
```
docker run -pHP:BP
```

**Debugging Container**

	To list the logs of the container
	
```
docker logs container_ID (or) NAMES
```

**Change the name of the container**

While we running the container, container will give some random names. We can change the name while running the container.

```
docker run -d -pHP:BP --name <Name> <Image>
```

**Docker Exec**

```
docker exec -it container_id (or) Name /bin/bash
#it - interactive terminal
```

**Docker Network**

### To create a own docker network

```
docker network create <network_name>
```

**Docker Image**

### To remove the docker image

```
docker image rmi <image-id>

docker image rmi image_name:new_tag

docker rmi -f <Image ID>
```