import configparser as cp

conf_file = 'conf.ini'
config = cp.ConfigParser()
config.read(conf_file)


def getConf(title: str, parameter: str):
    """return config from conf.ini"""
    return config.get(title, parameter)


def setConf(title: str, parameter: str, value: any):
    """set values to conf.ini"""
    config.set(title, parameter, value)
    with open(conf_file, 'w') as config_file:
        config.write(config_file)


def _change_conf_file(new_name: str):
    global conf_file
    conf_file = new_name