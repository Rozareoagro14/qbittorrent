from src.qbittorrent_bot import app, scheduler

if __name__ == '__main__':
    scheduler.start()
    print("Bot started")
    app.run()
