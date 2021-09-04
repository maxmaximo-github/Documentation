#!/bin/bash
#: Title                : install.sh
#: Date                 : 2020-04-27
#: Author               : "Max Maximo" <max.maximo.solutions@gmail.com>
#: Version              : 1.0
#: Description          : Automation Install GNS3 on Ubuntu 18.04
#: Options              : None


##### Set Main Path for execution of Script
MAIN_PATH=$( dirname $( realpath "$0" ));


# Get checks functions
source "${MAIN_PATH}/functions/functions.sh";


###### Functions ######

# Create Function install
function gns3_installation() {

    # Function Changes RTC Time
    change_rtc_for_windows;


    # Call function debconf
    install_debconf_utils;

    # Call to function "install_gns3_gns3server"
    install_gns3_gns3server;

    # Call to function "install_python_version"
    install_python_version;

    # Call to function "install_ansible"
    install_ansible;

    # Call to function "install_extra_packages"
    install_extra_packages;

    # Call to function "install_dockers"
    install_dockers;

    # Call to function "install_atom"
    install_atom;

    # Call to function "install_netmiko"
    install_netmiko;

    # Call to function "install_hydrogen"
    install_hydrogen;

    # Call to function "install_zsh"
    install_zsh;

    # Call to function "pimp_my_terminal"
    pimp_my_terminal;

    # Recorder Terminal
    record_terminal;

    # Autoremove command
    autoremove_packages;


    return;
}
