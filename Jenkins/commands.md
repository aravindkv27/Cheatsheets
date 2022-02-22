# Jenkins

## Jenkins Installation

Paste this in terminal
```
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
```

Next

```
nano /etc/apt/sources.list
```

Then, Add the following entry, save and close the file

```
deb https://pkg.jenkins.io/debian-stable binary/
```

After that, 

```
sudo apt-get update
sudo apt-get install jenkins
```

After the installation completes, run this command and copy the password

```
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

