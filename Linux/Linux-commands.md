# Linux Commands

## List
</br>

#### To List the files in the directory.

``` 
ls  
```
#### To enlist the every files in the directory including hidden files.

```
ls -a 
```

#### Display the files in long format.
```
ls -l 
```

## Print Working Directory
</br>

#### Print the path of current working directory 
```
pwd 
```
</br>

## Change Directory
</br>

```
cd <path>
```

#### To return to the root directory
```
cd /
```
#### Other CD flags
```
cd - # Switch back to previous directory where you working earlier.
cd .. # Go back to previous dir
cd -- # Show the previous dir where you worked.
cd ~ # Home directory
cd 'Anime movie' - used to change dir which contains whitespaces.
cd ../ ../ # Move two dir up from where you are.
```



## Make/Create a Directory

</br>

```
mkdir <Directory Name>
```
**Note:** In Linux Directory is called as a folder.


</br>

## Remove a file of Directory

</br>

#### To remove a empty directory:
```
rmdir <Directory Name>
```

#### To remove a file:
```
rm <File Name>
```
#### To Remove a files regrusively:
```
rm -r <file-name/dir>
```

#### To remove by force:
```
rm -f <file-name/dir>
rm -rf <file-name/dir>
```
**Note:** Be caution with these command.

</br>

## Copy

Copy a file from one location to another.
```
cp <source> <destination>
```

## move

Move or rename a file or directory.
```
mv doc document
```

</br>

## Grep

Used to find or search a regular expression or a string in a text file.
```
grep "string" filename
    (or)
filename grep "string"
```
--color used to color the string

</br>

## Touch

Create a new file.
```
touch <path>
```
</br>

## tar and zip and unzip

Tar and Zip used for compressing and archiving files.
```
tar cvf filename.tar <path>
```

```
zip filename.zip files
```

```
unzip file.zip
```

## Echo
Used to print and write to a file.
```
echo "string" > <path>

echo -e "\n" >> filename
```

</br>

## Wget

</br>

**Wget will download the resource/content from the url which is specified in the command.**

#### Syntax:

```
wget <options> <url>
```

#### Saving downloaded file under different name

```
wget -O <file-name> <url>
```
#### To specific directory

```
wget -P <path-to-directory> <url>
```
#### Downloading in background

```
wget -b <url>
```

#### To Download multiple files

</br>

**To Download multiple files create a text file with list of links to be download.**

```
wget -i <file-name>
```

</br>

## Print Environment

</br>

#### printenv prints the environment variables.

</br>

#### Syntax:

```
printenv <option> <variable>
```

#### To print all environment variables:
```
printenv
```

#### To print the location of specific directory:
```
printenv <variable> 
Eg: printenv USER // Print the user.
```

</br>

## Hostnamectl
</br>

The **hostnamectl** command is used to set the hostname using terminal without opening the **etc/hostname** file.

</br>

#### To display the current status of the hostname:
```
hostnamectl
```

</br>

## CHSH

</br>

#### To change the a login shell 

```
chsh -s /bin/zsh
```

The above command change default shell in zsh.

## To clear the DNS cache

```
sudo systemd-resolve --flush-caches
```

## Chmod

Allow us to change the read(4), write(2), and execute(1) permission of files and directories.
</br>
Owner | User | Group </br>
(rwx)   (r--)   (r--)

```
chmod +x demo.txt
```

</br>

## Ping

Test the connectivity between two computers.
```
ping reddit.com
```

## UFW

Uncomplicated Firewall is a user-friendly front-end for managing iptables firewall rules and its main goal is to make managing iptables easier or as the name says uncomplicated.

```
sudo ufw app list
```

https://linuxize.com/post/how-to-setup-a-firewall-with-ufw-on-ubuntu-18-04/


## Other commands
- head (to print first 10 lines)
- tail (to print a last 10 lines)