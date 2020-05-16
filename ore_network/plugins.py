import os
import requests
import yaml
import sys
import shutil
import pkg_resources

headers = {"User-Agent": "ORENetwork/1.0.0"}


class Plugin:
    VERSION_GET_URL = "https://api.spiget.org/v2/resources/{resource}/versions/{version}/download"
    PLUGIN_CONFIGS = pkg_resources.resource_filename("ore_network", "config/plugin_configs")

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
        # response = requests.head(Plugin.VERSION_GET_URL.format(resource=spigotid, version=spigotversion), headers=headers)
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

        print("installing "+self.config["name"])
        if "config_folder" in self.config:
            print("contains configfolder... installing into "+target)
            shutil.copytree(Plugin.PLUGIN_CONFIGS+"/"+self.config["config_folder"], target+"/"+self.config["config_folder"])


def load_plugins():
    plugins_yaml = pkg_resources.resource_string(__name__, "config/global_plugins.yml").decode("utf-8")
    global_plugins = yaml.safe_load(plugins_yaml)

    print(global_plugins)

    plugin_objects = []
    for id, config in global_plugins.items():
        plugin_objects.append(Plugin(id, config))

    print(str(len(plugin_objects)) + " plugins loaded")
    return plugin_objects
