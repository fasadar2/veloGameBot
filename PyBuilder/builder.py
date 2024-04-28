import subprocess
import sys
import xml.etree.ElementTree as ET
import pkg_resources

__installed_packages = {}
__pre_installed = ["pip", "setuptools", "wheel"]
__xml_package = {}


def install_package(name, version):
    if name == "":
        raise Exception("Empty package_name or package_version")
    if version in ["", "latest"]:
        subprocess.check_call([sys.executable, "-m", "pip", "install", name])
    subprocess.check_call([sys.executable, "-m", "pip", "install", f"{name} == {version}"])


def scan():
    global __xml_package, __installed_packages
    tree = ET.parse('builder.xml')
    root = tree.getroot()
    for package in root.findall('package'):
        name = package.find('name').text.lower()
        version = package.find('version').text
        __xml_package.update({name: version})
    installed_packages = {d.project_name: d.version for d in pkg_resources.working_set}
    for package_name, version in installed_packages.items():
        if package_name not in __pre_installed:
            __installed_packages.update({package_name: version})
    print("Установленные пакетики: ", __installed_packages)
    print("Пакетики в xml: ", __xml_package)


def uninstall_package(package_name):
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", package_name, "-y"])


def uninstall():
    global __installed_packages, __xml_package
    for package_name, version in __installed_packages.items():
        if package_name not in __pre_installed and package_name not in __xml_package.keys():
            uninstall_package(package_name)
        elif package_name in __xml_package and __xml_package[package_name] != version:
            uninstall_package(package_name)


def install_dependencies():
    global __xml_package
    for name, version in __xml_package.items():
        install_package(name, version)


if __name__ == "__main__":
    scan()
    uninstall()
    install_dependencies()
