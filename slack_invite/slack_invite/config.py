import os
import configparser

def get_env_variable(var_name):
    if var_name in os.environ:
        return os.environ.get(var_name)
    else:
        return config['SLACK-SETTINGS'][var_name]

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
config = configparser.ConfigParser()
config.read(path + '/settings.cfg')

slack_url = get_env_variable('SLACK_URL')
slack_team = get_env_variable('SLACK_TEAM')
slack_token = get_env_variable('SLACK_TOKEN')
