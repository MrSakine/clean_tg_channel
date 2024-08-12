# Configurations

Get your API_ID & API_HASH [here](https://my.telegram.org/auth). After you are logged in, click on `API development tools` then copy them there

Copy and paste the contents of `config.example.json` into a new file named `config.json`

Replace `<API_ID>` & `<API_HASH>` in `config.json` respectively by their values

Replace `<CHANNEL_ID>` by the ID of the channel you wanna remove contents. If channel ID has `-` sign, this means its private, otherwise its public

Replace `<BOT_TOKEN>` by the token of your bot from bot father. Also, make sure to add the same bot to the channel you are gonna clean and make it admin

Example
```json
{
    "api_id": "16*****",
    "api_hash": "0f*********",
    "bot_token": "68*********",
    "channel_id": "-14*******"
}
```

# How to use

Run the script by using `python3 main.py` & enter your phone number. They will ask you a confirmation code, copy it from your telegram app & paste it in the terminal
You will have to enter a password if your account has 2fa enabled (by password)

After your first login, you won't have to go over all these processes again. Pyrogram will store your session for you