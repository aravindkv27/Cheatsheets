# Azure Compute Services

Azure compute is an on-demand computing service for cloud applications.

It provides computing resources such as, <br>
- Disk 
- Memory
- Networking
- Operating Systems
- Processors

### Azure Computing Service Supports

- Linux
- Windows Server
- SQL server
- Orcale
- IBM
- SAP

### Most Prominent Servies are:
- Azure Virtual Machine
- Azure Container Instances
- Azure App Service
- Azure Functions(serverless computing)

### Azure Virtual Machines:
- Infrastructure as a Service(IaaS)
- customize all the software running on the vm.
- vm is software emulation of physical computer
- Need to configure, update and maintain the software that runs on the vm.
- Image is a template used to create a VM.
- Examples of when to use VMs.
  - During testing and development
  - When running application in the cloud.
  - When extending your datacenter to the cloud.
  - During disaster recovery.
- Scale Vms in the Azure.
  - Run single vm for testing, development, or minor tasks.
  - Group VMs to provide high scalability, availability, and redundancy.
    - Virual Machine scale sets
    - Azure Batch.


### VM scale set
- Use to deploy and manage set of identical, load balanced vms.
- support true autoscale.
- Demand is high vm instances is added, if demand goes down vm instances is removed.
- Process can be manual or automated.
- Allows you to manage, configure, and update large number of VMs in minutes to provide highly available application.

### Azure Batch
- Enables large-scale parallel and high-performance computing(HPC) batch jobs ability to scale to 10, 100, 1000 of VMs.


### Containers and Kubernetes
- Use to deploy and manage containers.
- Containers are lightweight, virtualized application environment.
- Run multiple instance of a containerized application in a single host machine.

### App Service
- Platform as a Service(Paas).
- Quickly build, deploy and scale any application(web,app) on any platform.
- offers autmatic scaling and availability.
- Supports windows and linux.
- Types of App services
  - Host most common app services like
    - Web apps
    - API apps
    - WebJobs
    - Mobile apps
- It handles most of the infrastructure decisions.
    - Deployment and management are integrated into the platform.
    - Endpoints are secured.
    - Scaled quickly to handle high traffic loads.
    - Built-in load balancing and traffic manager provide high avaiability.

### Functions
- Suitable when you concerned about code running your service.
