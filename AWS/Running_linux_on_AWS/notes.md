### Why Linux?
    - Customization and Flexibility
    - Stability and Reliability
    - Security
    - Cost Savings
    - Scalability
    - Integration with Cloud Services

### Use Case Scenarios
    - Compliance
    - Legacy Application(broke into microservices)
    - Container Transition

### Distribution Offered on AWS
    - Amazon Linux (Offered and maintained by AWS)
    - Red Hat Enterprise Linux (Focus on enterprise market)
    - Ubuntu (Robust user interface and based on Debian)
    - SUSE (Focus on enterprise market)
    - Kali Linux (Focused on Security purposes)
    - Debian (Free and Open Source)
    - CentOS (Community driven Distribution)
    

## Amazon Elastic Compute Cloud
### What is Amazon EC2?

    Amazon Elastic Compute Cloud
    Provide scalable compute on AWS

### Types of EC2 Instances

1) General purpose
    - Provides a balance of compute, memory and networking.
    - Useful for a variety of workloads.

2) Compute Optimized
    - Appropriate for workloads requiring high-performance processors or 
        are compute bound.
    - Good for video encoding and CPU-based machine Learning.

3) Memory Optimized
    - Provide Instances with lots of fast memory

4) Accelerated Computing

5) Storage Optimized

## Amazon Machine Images(AMI)

### What is AMI?

- AMI provides the info req to launch an instance. 
- [Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)

### AMI Components

1) Root Device
    - Amazon Elastic Block Store(EBS) snapshot
    - Instance store volume

2) Launch Permissions
    - The AWS accounts that use ami.

3) Block Device Mapping
    - Specifies which volumes to attach to the instance.

### Finding an AMI

1) Community AMI
2) Amazon MarketPlace AMIs
3) My AMIs

