# Configurations

Get your API_ID & API_HASH [here](https://my.telegram.org/auth). After you are logged in, click on `API development tools` then copy them there

Copy and paste the contents of `config.example.json` into a new file named `config.json`

Replace `<API_ID>` & `<API_HASH>` in `config.json` respectively by their values

Replace `<CHANNEL_ID>` by the ID of the channel you wanna clean. If channel ID has `-` sign, this means its private, otherwise its public

Create a new bot from bot father and make sure to add it to the admin list of the channel you are gonna clean

Example
```json
{
    "api_id": "16*****",
    "api_hash": "0f*********",
    "channel_id": "-14*******"
}
```

# How to use

Run the script by using `python3 main.py` & enter your phone number. They will ask you a confirmation code, copy it from your telegram app & paste it in the terminal
You will have to enter a password if your account has 2fa enabled (by password)

After your first login, you won't have to go over all these processes again. Pyrogram will store your session for you

Finally, run the `/delete` command in your channel to start the cleaning

# Library

Pyrogram - [Pyrogram](https://docs.pyrogram.org/)