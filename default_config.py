import json
import sys

DEFAULT_JSON_FILE_LOCATION = "/home/lukas/Nextcloud/Programming/i3GroupStart/config/config.json"
I3_CONFIG_FILE = "/home/lukas/.config/i3/config"
I3_BACKUP_CONFIG_FILE_LOCATION = "/home/lukas/.config/i3/config.from-groups.backup"

json_config_location = sys.argv[0]
with open(json_config_location, 'r') as json_file:
    json_config = json.load(json_file)
    DEFAULT_JSON_FILE_LOCATION = json_config_location
    I3_CONFIG_FILE = json_config["i3ConfigFile"]
    I3_BACKUP_CONFIG_FILE_LOCATION = json_config["i3BackupFileLocation"]
