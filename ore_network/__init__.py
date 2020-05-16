from ore_network import servers, plugins


def install():
    print("retrieving plugins")
    plugin_objects = plugins.load_plugins()
    print("retrieving servers")
    server_objects = servers.load_servers()

    # This is where the servers may be set up

    print("installing plugins")
    for server in server_objects:
        server.prep_directory()
        target = server.getPluginsFolder()
        for plugin in plugin_objects:
            if server.needsPlugin(plugin.getID()):
                plugin.installPlugin(target)


if __name__ == "__main__":
    install()
