# Minecraft-Network
Setup your own copy of the ORE Minecraft Network. This is currently a labor intensive procedure that is completely manual. Any points in the todo-list that isn't done, will be assumed done manually by the finished products. This is why the priority is ordered seemingly backwards. I am automating the last step of the setup first and building my way up.

## TODO List
Points will be in the order of priority. The things that are not done will be assumed done by the implemented systems.
+ Setup plugins from a config.
+ Setup each Minecraft server.
+ Setup the proxy to make a network from the minecraft servers.
+ Make installation personally configurable
+ Create an upgrade tool
+ Setup an instance on a persistence system (systemd)


## Installation
You can install the package from pip:
```
python3 pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple ore-network
```

or you can build from source by running setup.py:
```
python3 -m pip install --user --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
```
In both cases, you should have the cli installed in PATH.

## Usage

First step is to install an ORE-network somewhere.

1. Navigate to where you want to install the minecraft network
1. run the command `orenetwork-setup` which should create a folder for each minecraft server.
1. WIP: This will create a configuration file which you can edit to customize the installation and potentially change something in the future.
1. WIP: When you have finished configuring and are ready to install, you can run `orenetwork-install` which will create the servers.
1. WIP: You can now use the command `orenetwork` to control the installed instance.