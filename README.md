
# B.E.A.T.Z.Z v2
Cat Userbot clone with the Alan Walker tone and more features!

### The Easy Way to deploy the bot
Get APP ID and API HASH from [HERE](https://my.telegram.org) and BOT TOKEN from [BotFather](https://t.me/botfather) and then Generate string session by clicking on run.on.repl.it button!

[![Get string session](https://repl.it/badge/github/sandy1709/sandeep1709)](https://generatestringsession.sandeep1709.repl.run/)

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


[![catuserbot logo](https://telegra.ph/file/711e22e6004fe72b05cd7.png)](https://heroku.com/deploy)


### Userbot by [this legend](https://t.me/BeatsToHell913) 
### Join [this group](https://t.me/Beatzzv2) for queries and staying up to date!

### The Normal Way

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```

### UniBorg Configuration



**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**

Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`

    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.
