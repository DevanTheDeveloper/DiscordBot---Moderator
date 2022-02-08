# DiscordBot---Moderator


SETUP

- pip install requirements.txt
- create .env file with bot api token as "bot_secret"
- assign channel id for channel to be monitored for new participant introductions


FUNCTION

- Provides discord quild details and channels on loadup. Also creates/access SQLITE3 DB to log activation.
- Monitors all messages on guild to ensure all posters have introduced themselves. Posts from unintroduced members are deleted
and a dm is sent to them with instructions on how to introduce.
- Once introduced, sql entry is made for user and user sent dm welcoming them to guild.
- Displays message and user details for all messages sent within guild while active.
