import os
import requests
import yaml
import sys
import shutil

headers = {"User-Agent": "ORENetwork/1.0.0"}


class Plugin:
    VERSION_GET_URL = "https://api.spiget.org/v2/resources/{resource}/versions/{version}/download"

    def __init__(self, pid, config):
        """A class representing info about a plugin resource and how to retrieve it.
        It can exist on spigot where retrieval will be done through the spigetAPI, or
        it will be on github where retrieval (and potentially compilation) is defined
        per plugin

        :param config: configuration details about the plugin.
        """
        self.pid = pid
        self.config = config

    def __compile(self):
        pass

    def __retrieveSpigot(self, target):
        spigotid = self.config["id"]
        spigotversion = self.config["version"]
        response = requests.head(Plugin.VERSION_GET_URL.format(resource=spigotid, version=spigotversion), headers=headers)
        # TODO: The head contains a url behind cf DDoS protection. Need to bypass this
        # Deprecated:
        # filename, headers = request.urlretrieve(Plugin.VERSION_GET_URL.format(resource=spigotid, version=spigotversion), headers={"User-Agent":"OmarProgram"})
        # shutil.move(filename, target)

    def getName(self):
        return self.config["name"]

    def getID(self):
        return self.pid

    def check_version(self):
        pass

    def installPlugin(self, target):
        # TODO
        if self.config["source"] == "spigot":
            self.__retrieveSpigot(target)
        elif self.config["source"] == "git":
            pass
        elif self.config["source"] == "bukkit":
            pass

        if "configfolder" in self.config:
            shutil.copytree("config/plugin_configs/"+self.config["configfolder"], target+self.config["configfolder"])


def load_plugins():
    global_plugins = yaml.safe_load(open('config/global_plugins.yml'))

    print(global_plugins)

    plugin_objects = []
    for id, config in global_plugins.items():
        plugin_objects.append(Plugin(id, config))

    print(str(len(plugin_objects)) + " plugins loaded")
    return plugin_objects
