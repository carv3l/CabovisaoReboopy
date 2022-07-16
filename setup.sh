#!/bin/bash


# Text mode commands

# tput bold    # Select bold mode
# tput dim     # Select dim (half-bright) mode
# tput smul    # Enable underline mode
# tput rmul    # Disable underline mode
# tput rev     # Turn on reverse video mode
# tput smso    # Enter standout (bold) mode
# tput rmso    # Exit standout mode



red=`tput setaf 1`
green=`tput setaf 2`
yellow=`tput setaf 3`
blue=`tput setaf 4`
cyan=`tput setaf 6`
reset=`tput sgr0`
#echo "${red}red text ${green}green text${reset}"


# Verify if pip3 is installed 




pip_version_result=$(pip3 --version)


echo "${yellow} PIP3 Version: ${reset}", $pip_version_result


#if [[ $pip_version_result == *"not found"* ]]; then
if [ -z "$pip_version_result" ]; then
        echo "${red}PIP3 IS NOT INSTALLED, INSTALLLING...${reset}"
        apt-get -y install python3-pip
    else
        echo "${green} PIP3 IS INSTALLED, PROCEEDING...${reset}"
        pip3_flag=true
fi


if [$pip3_flag]; then

virtualenv_version_result=$(virtualenv --version)

    echo "${yellow} Virtualenv Version: ${reset}", $virtualenv_version_result

    if [ -z "$virtualenv_version_result"];then
        echo "${red}Virtualenv IS NOT INSTALLED, INSTALLLING...${reset}"
        sudo pip3 install virtualenv
    else
        echo "${green} Virtualenv IS INSTALLED, PROCEEDING...${reset}"

    fi
fi

# Create a geckodriver Folder in the current working directory as follows:
echo "${yellow}Creating directory /drivers ${reset}"
$ mkdir  /drivers


# Create a Python virtual environment in your project directory with the following command:
echo "${yellow}Creating a Python virtual environment ${reset}"
virtualenv .venv


# Activate the Python virtual environment from your project directory with the following command:

echo "${green}Activating the Python virtual environment ${reset}"

source .env/bin/activate


# You can install Selenium Python library using PIP 3 as follows:

echo "${yellow}INSTALLING... Selenium Python library ${reset}"

pip3 install selenium


echo "${green}Cloning latest geckodriver ${reset}"

# You can do this with the --branch flag, which will also accept a tag.

git clone  git@github.com:mozilla/geckodriver.git --branch 0.31.0

# You can extract the geckodriver-v0.26.0-linux64.tar.gz archive from the ~/Downloads directory to the drivers/ directory of your project with the following command:

echo "${Blue} Extracting Geckodriver ${reset}"

tar -xzf /geckodriver-v0.31.0-linux64.tar.gz -C drivers/


## Sourced from https://linuxhint.com/using_selenium_firefox_driver/