import yaml

from ore_network import plugins, servers


def install():
    # NB: Assumes setup has been run beforehand

    # Check if there is an installation ready
    with open('./config.yml', 'r') as yaml_main_config:
        main_config = yaml.safe_load(yaml_main_config)
    if not main_config["ready"]:
        print("Error: set ready to true in config.yml to start installation")
        return

    ### Servers ###
    # Load servers
    with open('./servers.yml', 'r') as yaml_server_config:
        server_config = yaml.safe_load(yaml_server_config)

    server_objects = servers.load_servers(server_config)
    # Install servers
    if main_config["create_servers"]:
        print("Installing servers")
        for server in server_objects:
            server.install()

    ### Plugins ###
    # Load plugins
    with open('./plugins.yml', 'r') as yaml_plugin_config:
        plugin_config = yaml.safe_load(yaml_plugin_config)

    plugin_objects = plugins.load_plugins(plugin_config)
    # Install plugins
    if main_config["install_plugins"]:
        print("Installing plugins")
        for plugin in plugin_objects:
            plugin.retrievePlugin()
            for server in server_objects:
                server.prep_directory()
                target = server.getPluginsFolder()
                if server.needsPlugin(plugin.getID()):
                    plugin.installPlugin(target)
