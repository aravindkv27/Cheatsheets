# Create a Linux virtual machine in the Azure portal

## Create an Virtual machine
 
1. Open a azure protal. 
2. Under service, select Virtual Machines.
3. In the Virtual machines page, select Create and then Virtual machine. The Create a virtual machine page opens.
4. Create a new resource group and enter the vm name.

## What I did

1. Created a Ubuntu VM(azvm) using Azure portal.
2. Connected the my azvm using ssh in my local linux machine.
3. azvm is successfully connected. 
4. I created a new user called surat and switched it into that user and I tried some basic linux commands.
5. Then, I install nginx using cli.
    - sudo apt-get -y update
    - sudo apt-get -y install nginx
6. After nginx installation, Checked Nginx is active or not.
    -systemctl status nginx.


Resources:

https://docs.microsoft.com/en-in/azure/virtual-machines/linux/quick-create-portal
https://docs.microsoft.com/en-in/azure/virtual-machines/linux/tutorial-manage-vm
https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04
