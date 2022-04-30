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