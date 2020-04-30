import os

import yaml
import sys


class Plugin:
    def __init__(self, config):
        """A class representing info about a plugin resource and how to retrieve it.
        It can exist on spigot where retrieval will be done through the spigetAPI, or
        it will be on github where retrieval (and potentially compilation) is defined
        per plugin

        :param config: configuration details about the plugin.
        """
        self.config = config

    def __compile(self):
        pass

    def __retrieveSpigot(self, id):
        pass

    def check_version(self):
        pass

    def installPlugin(self, target):
        # TODO
        pass


class PluginSpigot(Plugin):
    def __init__(self, config):
        super().__init__(config)

    def retrieve(self):
        return self.retrieveSpigot(self.config.id)


def load_plugins():
    global_plugins = yaml.safe_load(open('config/global_plugins.yml'))

    print(global_plugins)

    plugin_objects = []
    for config in global_plugins.values():

        if config["source"] == "spigot":
            plugin_objects.append(PluginSpigot(config))

    print(str(len(plugin_objects)) + " plugins loaded")
    return plugin_objects

