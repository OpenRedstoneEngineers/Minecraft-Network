import plugins
import servers


def install():
    plugin_objects = plugins.load_plugins()
    server_objects = servers.load_servers()

    # This is where the servers may be set up

    for server in server_objects:
        target = server.getPluginsFolder()
        for plugin in plugin_objects:
            if server.needsPlugin(plugin.name):
                plugin.installPlugin(target)
