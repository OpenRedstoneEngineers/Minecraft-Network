import yaml
import os
import csv


class Server:
    def __init__(self, config):
        """A class representing info about a server and how to set it up with plugins.
        It will be represented by it's name and what plugins are on it. also it may
        contain info about any unique differences in a plugin

        :param config: configuration details about the server.
        """
        self.config = config

    def prep_directory(self):
        try:
            os.mkdir("./mcserver-"+self.config.name)
        except FileExistsError:
            pass
        try:
            os.mkdir("./mcserver-"+self.config.name+"/plugins")
        except FileExistsError:
            pass

    def __compile(self):
        pass

    def install(self):
        pass

    def getPluginsFolder(self):
        return "./mcserver-"+self.config["name"]+"/plugins"

    def needsPlugin(self, name):
        return name in self.config["plugins"]


def load_servers():
    servers = yaml.safe_load(open('config/servers.yml'))
    appendPluginsConfig(servers)

    server_objects = []
    for config in servers.values():
        server_objects.append(Server(config))

    print(str(len(server_objects)) + " plugins loaded")

    return server_objects


def appendPluginsConfig(servers):
    for server in servers:
        server["plugins"] = []
    with open("config/serverplugins.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        pluginnames = next(reader)[1:]
        for row in reader:
            servername = row[0]
            for item, pluginname in zip(row[1:], pluginnames):
                # If the server is configured to have this plugin, add it to the server configs
                if item == "TRUE":
                    servers[servername]["plugins"].append(pluginname)
