import os
from enum import StrEnum

# constants.py
APP_TITLE = 'Clair Obscur Save Loader'
DEFAULT_PROFILE_NAME = 'new Profile'
CONFIG_LOCATION = os.path.join(os.environ['HOME'], '.clair_obscur_save_loader')
CONFIG_FILE_NAME = 'config.json'
PROFILES_FOLDER_NAME = 'Save'


class Color(StrEnum):
    ERROR = 'red'
    INFO = '#eeeeee'


# Messages
class Messages(StrEnum):
    SELECT_PROFILE = 'Select a profile first'
    PROFILE_EXISTS = 'Profile already exists'
    INVALID_CARACTER = "you can't use / or \\ in the name"
    SAVESTATE_EXIST = 'Savestate already exists'
