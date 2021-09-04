#!/bin/bash
#: Title                : gns3.sh
#: Date                 : 2020-04-27
#: Author               : "Max Maximo" <max.maximo.solutions@gmail.com>
#: Version              : 1.0
#: Description          : Automation Install GNS3 on Ubuntu 18.04
#: Options              : None 


##### Set Main Path for execution of Script
MAIN_PATH=$( dirname $( realpath "$0" ));


# Get checks functions
source "${MAIN_PATH}/functions/functions.sh";


# Get Install Function
source "${MAIN_PATH}/install/install.sh";


# Main function
function main() {
    # Define Local Variables
    local SCRIPT_VERSION="1.0";



    ### Print Installation Screen. ###
    echo $'\n'\
        "###############################################################"$'\n'\
        "##############   GNS3 Installation Script    ##############"$'\n'\
        "###############################################################"$'\n'$'\n'\
        "##############     VERSION. ${SCRIPT_VERSION}  ####################"$'\n'$'\n'\
        "##############     List of available options    ##############"$'\n'\

    PS3=$'\n'"Please enter your choice (2 quit): "


    # Create array of options
    options=(
        "Install GNS3"
        "Quit"
    );


    select option in "${options[@]}"
    do
        case $option in
            "Install GNS3")
                echo;
                echo "### $option ###";

                # Call function "install_function"
                gns3_installation;

                ;;

            "Quit")
                exit 0;

                ;;

            *)
                echo "Invalid Option $REPLY";
                ;;
        esac
    done


    return;
}


main "$@";