import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ore_network",
    version="0.0.1",
    author="Omar Saad",
    author_email="omar.saad0705@gmail.com",
    description="Set up your own ORE Minecraft network",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OpenRedstoneEngineers/Minecraft-Network",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    python_requires='>=3.8',
    entry_points = {
        'console_scripts': ['orenetwork-setup=ore_network.command_line:main'],
    },
    include_package_data=True,
)
