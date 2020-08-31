import configparser
config = configparser.ConfigParser()


def add_configure(key, value, section_name='DEFAULT'):
    if section_name in config:
        config[section_name][key] = value
    else:
        config[section_name] = {
            key: value
        }
    config[section_name][key] = value
    with open('configurations.ini', 'w') as configfile:
        config.write(configfile)
