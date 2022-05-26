# Azure Fundamentals (AZ-900)

## Cloud Computing

It is delivery model for services like Storage(Filesm,DB),Compute power. 
Storage means not only like storing data. It also provides various services like VM, SQL etc.,
Cloud means creating a application whatever like web, AI, ML, Devops. Cloud provides good networking and good analytics for delivering.

## Key Characteristics

- Scalability
    - It is the process of allocating or deallocating resourses. 

- Elasticity
    - It is the ability to scale dynamically

- Agility
    - It is the ability to allocate and deallocate resources quickly.

- Fault Tolerance
    - It is the ability to remain up and running durning component and service failures.

- Disaster Recovery
    - Simply, creating a copy of your resources. It is the ability to recover from an event that has taken down the service.

- High Availability
    - It is a measure of system uptime for users/services. It is the ability to keep services running for extended periods of time with very little downtime.


### Azure Portal

- Self service
- Public web-based interface for mangaement of azure platform
- Customizable
- Simple tasks

### Azure powershell

- First tool allow us to deploy automation
- Powershell and module
- Multi-platform with powershell core
- Simple to use

### Azure CLI

- Designed for automation
- Mutli-platform (python)
- simple to use
- Native OS terminal scripting

### Azure Cloud Shell

- Cloud based scripting env
- completely free
- Support both azure powershell and azure cli
- Dozen of additional tools

## Azure Advisor

- Service that created to continuously scan those service.
- Personalized consultant service
- Designed to provide recommendations and best practive for
    - cost
    - security
    - Reliability
    - Performance
    - Operational Excellence

## Azure Security Group

- Designed to filter traffic to and from azure resources located in azure virtual network

- Filtering controlled by rules

- Ability to have multiple inbound and outbound rules

- Rules are created by specifying
    - Protocol(TCP/Ip)
    - Port
    - Direction
    - Priority
    - Source and Destination

### Application security Group

    - Feature allows grouping of vm located in az virtual network
    - Designed to reduce the maintenance effort