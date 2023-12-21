from HarleyMusic.core.bot import Lipps
from HarleyMusic.core.dir import dirr
from HarleyMusic.core.git import git
from HarleyMusic.core.userbot import Userbot
from HarleyMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Lipps()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
