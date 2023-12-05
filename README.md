[![Codacy Badge](https://api.codacy.com/project/badge/Grade/259099080ca24e029a910e3249d32041)](https://app.codacy.com/gh/ch3p4ll3/QBittorrentBot?utm_source=github.com&utm_medium=referral&utm_content=ch3p4ll3/QBittorrentBot&utm_campaign=Badge_Grade)

# QBittorrentBot

With this bot telegram you can manage your qbittorrent with a few simple clicks. Thanks to QBittorrentBot you can have a list of all the files in download / upload, add torrents and magnets.  
You can add more magnets by simply placing one link per line, e.g. 
```
magnet:?xt=...  
magnet:?xt=...  
```
You can also pause, resume, delete and add/remove and modify categories.

## Configuration
### Retrieve Telegram API ID and API HASH
With the change of library to [pyrogram](https://docs.pyrogram.org/) you will need the API_ID and API_HASH. Check [here](https://docs.pyrogram.org/intro/quickstart) to find out how to recover them.
### JSON Configuration
Edit the config.json.template file and rename it to config.json. 
The config file is stored in the mounted /app/config/ volume

```
{
    "qbittorrent": {
        "ip": "192.168.178.19",
        "port": 8080,
        "user": "admin",
        "password": "admin"
    },
    "telegram": {
        "bot_token": "1111111:AAAAAAAA-BBBBBBBBB",
        "api_id": 1111,
        "api_hash": "aaaaaaaa"
    },

    "users": [
        {
            "user_id": 123456,
            "notify": false
        },
        {
            "user_id": 12345678,
            "notify": true
        }
    ]
}
```
Note: If notify is true then the user will receive a notification whenever a torrent has finished downloading

## Running
Pull and run the image with: `docker run -d -v /home/user/docker/QBittorrentBot:/app/config:rw --name qbittorrent-bot ch3p4ll3/qbittorrent-bot:latest`
### Build docker
- Clone this repo ```git clone https://github.com/Rozareoagro14/qbittorrent.git```
- Move in the project directory
- Create a config.json file
- Run `docker build -t qbittorrent-bot:latest . && docker run -d -v /home/user/docker/QBittorrentBot:/app/config:rw --name qbittorrent-bot qbittorrent-bot:latest`

### Running without docker
- Clone this repo `git clone https://github.com/Rozareoagro14/qbittorrent.git`
- Move in the project directory
- Install dependencies with `pip3 install -r requirements.txt`
- Create a config.json file
- Edit in the file /src/config.py the location of the file 'config.json'
- Start the bot with `python3 main.py`

## How to enable the qBittorrent Web UI
For the bot to work, it requires qbittorrent to have the web interface active. 
You can activate it by going on the menu bar, go to **Tools > Options** qBittorrent WEB UI

- In the new window, choose **Web UI** option
- Check the **Enable the Web User Interface (Remote control)** option
- Choose a port (by default 8080)
- Set username and password (by default username: admin / password: adminadmin)

Click on Ok to save settings.
