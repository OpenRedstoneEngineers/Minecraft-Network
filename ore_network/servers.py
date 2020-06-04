import pkg_resources
import os
import csv


class Server:
    FOLDER = "./mcserver-{servername}"

    def __init__(self, config):
        """A class representing info about a server and how to set it up with plugins.
        It will be represented by it's name and what plugins are on it. also it may
        contain info about any unique differences in a plugin

        :param config: configuration details about the server.
        """
        self.config = config

    def prep_directory(self):
        try:
            os.mkdir(Server.FOLDER.format(servername=self.config["name"]))
        except FileExistsError:
            pass
        try:
            os.mkdir(Server.FOLDER.format(servername=self.config["name"])+"/plugins")
        except FileExistsError:
            pass

    def __compile(self):
        pass

    def install(self):
        pass

    def getPluginsFolder(self):
        return Server.FOLDER.format(servername=self.config["name"])+"/plugins"

    def needsPlugin(self, name):
        return name in self.config["plugins"]


def load_servers(servers):
    server_objects = []
    for config in servers.values():
        server_objects.append(Server(config))

    print(str(len(server_objects)) + " servers loaded")

    return server_objects


def appendPluginsConfig(servers):
    for server in servers.values():
        server["plugins"] = []

    serverplugins_csv = pkg_resources.resource_string(__name__, "config/serverplugins.csv").decode("utf-8")
    reader = csv.reader(serverplugins_csv.split("\n"), delimiter=',')
    pluginnames = next(reader)[1:]
    for row in reader:
        print(row)
        servername = row[0]
        for item, pluginname in zip(row[1:], pluginnames):
            # If the server is configured to have this plugin, add it to the server configs
            if item == "TRUE":
                servers[servername]["plugins"].append(pluginname)
