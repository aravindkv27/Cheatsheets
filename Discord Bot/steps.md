# Creating A Bot

## Create a bot account 

```
https://discord.com/developers/
```

* Create a application and give a bot name

* Navigate to "Bot" tab, click "Add Bot" and click "yes, do it".

* Copy the token and keep it safely.

* Now, go to bot page click "OAuth2" tick "Bot" and "Application.commands".

* Tick the required permissions and copy the redirect link and paste it in browser.

* The link will redirect and now select the discord server where the bot want to be invited.



# Install node.js

After installing node follow the below steps

## Open terminal or powershell

Go to the required folder, Open the terminal and Run the command 

```
npm init -y
```

## Install the required module

```
npm i discord.js
```
## Create a json file

Create a **config.json** and insert your token 

```
{
    "token": "Token"
}
```

## Create a Main file

Create a **index.js**

```
const { Client, Intents } = require('discord.js');
const { token } = require('./config.json');

// Create a new client instance
const client = new Client({ intents: [Intents.FLAGS.GUILDS] });

// When the client is ready, run this code (only once)
client.once('ready', () => {
	console.log('Ready!');
});

// Login to Discord with your client's token
client.login(token);
```
