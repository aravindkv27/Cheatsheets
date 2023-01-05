# Azure DevOps

https://dev.azure.com/

## What is Azure DevOps?

* It is and DevOps Platform
* Saas Platform from Microsoft
* To implement all our DevOps processes.
* Extended from existing services and tools.


## What is a DevOps Platform?

#### DevOps
    DevOps is an combination of Concepts, Tools and Practices.
        - Anything that makes developing and releasing applications.

Azure Devops is an technological implentation of DevOps precess which covers whole softwate development life cycle.

### Azure Boards

    - Azure Boards is used for planning the software
    - Agile, Scrum and so many

### Azure Reops
    - Host your code in private git repo
    - Similar to GitLab, GitHub, BitBucket etc,..
    - It is not just for hosting the code it is also part of Azure DevOps tool
    - Collaborate on the code
    - Enables to use any Git workflow
    - Azure Repos commit, pull request or branch can be linked to the work items.

### Azure Pipelines

    - Write the pipeline in a YAML file
    - Host this pipeline config with the rest of your app code in your git project.

#### Pipeline Syntax
* Smallest building block of a pipeline.
* A step can either be a Script or a task.
    - A task is a pre-created script, which can use as a convenience.   
    - We can use the task with a set of inputs. We don't have to know the commands exactly.

#### Jobs

- A job represents an execution boundary of a set of steps
- Each job runs on an agent.
- All the steps in a job run on the same agent.

#### Agent

- An agent is computing infrastructure with agent software installed on it.
- We can pull the vmimages using pool command
- Define on which os and version to run your tasks

### Azure Artifacts

    Artifacts differ based on the programming language used for writing the application
