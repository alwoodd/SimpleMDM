from setuptools import setup, find_packages

setup(
    name="SimpleMDM_device_name_update",
    version="1.0.0",
    description="Uses SimpleMDM API to update all iPad's SimpleMDM name to its device name.",
    author="Dan Alwood",
    author_email="dalwood@yahoo.com",
    packages=["SimpleMDM_device_name_update"],
    install_requires=["my_utilities >= 1.1.0", "requests"],
)
