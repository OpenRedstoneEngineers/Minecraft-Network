import os
import pkg_resources
import yaml
from ore_network import servers


def network_setup():
    # Make shared folder
    try:
        os.mkdir('./shared')
    except FileExistsError:
        pass

    # Fetch or create config
    print("Preparing a new network instance")
    config = create_main_config()
    server_config = create_servers_config()
    plugin_config = create_plugins_config()


def create_plugins_config():
    config = yaml.safe_load(
        pkg_resources
            .resource_string(__name__, "config/global_plugins.yml")
            .decode("utf-8"))

    with open('./plugins.yml', 'w') as conf_yaml:
        yaml.safe_dump(config, conf_yaml)
    return config

def create_servers_config():
    config = yaml.safe_load(
        pkg_resources
            .resource_string(__name__, "config/servers.yml")
            .decode("utf-8"))

    servers.appendPluginsConfig(config["servers"])
    with open('./servers.yml', 'w') as conf_yaml:
        yaml.safe_dump(config, conf_yaml)
    return config


def create_main_config():
    config = {
        "ready": False,
        "create_servers": True,
        "install_plugins": True,
    }

    with open('./config.yml', 'w') as conf_yaml:
        yaml.safe_dump(config, conf_yaml)
    return config
