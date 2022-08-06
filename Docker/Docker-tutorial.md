# Docker

## What is Container?

- A way to package application with all the necessary Dependainces and configuration.
- It is Portable, easily shared and moved around.
- Make devlopment and deployment efficient.

 ## Problems Without Docker
-  Installation process different on each OS.
-  Many steps goes wrong. 

 ## Why containers is used
 
-  Own isloated environment.
-  Packaged with all needed configuration.
-  One command to install the requirements and Dependainces.

## Container
- Container is made up of images.
- Layer mostly Linux base image, because small in size.
- Application image on top.

## Image and Container

**Image**
- It is the actual package where it contains all dependainces.
- Artifact, It can be moved around.

**Container**
- Container is a running environment for Image. It contain port which is used to talk between them.
- It contain file system, application image and environment configuration. 
- Images or stored in our local machine and start the application.
- Here, the container environment is created in our machine.

## Docker vs VM

 Docker has run only on application layer but VM contains both  Application and OS Kernel layer. Which means if we download VM in our machine it will create a Own Kernel and Application layer.

- Docker Image is much smaller than VM.
- Speed- Docker container start and run much fast but if we start VM it need to start kernel first so it take times.
- Compatibility: VM of any os can run on any OS host but we cant do that in docker. Docker wont run on windows. But Docker Toolbox can run in windows.cd 