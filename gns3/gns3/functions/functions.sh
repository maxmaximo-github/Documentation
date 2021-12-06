
#!/bin/bash


# Function for change rtc for windows clock correctily
function change_rtc_for_windows() {
    echo "Change Time Zone RTC in Local TZ to yes.";
    sudo timedatectl set-local-rtc 1;

    return;
}


# Function to install Ansible
function install_ansible() {

    # Update Systemdocdd
    update_and_upgrade_system;

    # Add repository especially
    sudo apt -y install software-properties-common > /dev/null 2>&1;
    sudo apt-add-repository --yes --update ppa:ansible/ansible > /dev/null 2>&1;
    sudo apt -y install sshpass

    # Install Ansible
    echo "Install Ansible";
    sudo apt -y install ansible > /dev/null 2>&1;

    # Add support to Windows Remote Management.
    pip3 install pywinrm==0.4.1 > /dev/null 2>&1;
    pip3 install pywinrm[basic] > /dev/null 2>&1;

    return;
}


# Funtion to install Atom
function install_atom() {

    # Install atom
    echo "Install Atom.";

    # Change directory to /tmp
    cd /tmp

    # Get Atom Package oficcial repository
    wget -qO - https://packagecloud.io/AtomEditor/atom/gpgkey | sudo apt-key add - > /dev/null 2>&1;
    sudo sh -c 'echo "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main" > /etc/apt/sources.list.d/atom.list' > /dev/null 2>&1;

    # Update System
    update_and_upgrade_system > /dev/null 2>&1;

    # Install Atom form repository
    sudo apt -y install atom > /dev/null 2>&1;

    # Add Atom packages
    # Atom Packets
    apm install linter > /dev/null 2>&1;
    apm install linter-ui-default > /dev/null 2>&1;
    apm install --production file-icons > /dev/null 2>&1;
    apm install linter-flake8 > /dev/null 2>&1;
    sudo snap install termshark > /dev/null 2>&1;
    apm install autocomplete-python > /dev/null 2>&1;
    pip3 install autopep8 > /dev/null 2>&1;
    apm install python-autopep8 > /dev/null 2>&1;
    apm install script > /dev/null 2>&1;
    apm install atom-file-icons > /dev/null 2>&1;
    apm install atom-material-syntax > /dev/null 2>&1;
    apm install minimap > /dev/null 2>&1;
    apm install minimap-git-diff > /dev/null 2>&1;
    apm install minimap-highlight-selected > /dev/null 2>&1;
    apm install terminal-plus > /dev/null 2>&1;

    return;
}


# Function to install extra packages
function install_extra_packages() {

    # Create array extra packages
    local packages_list=(
        "tigervnc-viewer" "python3-tk" "graphviz" \
        "nmap" "qemu" "qemu-kvm" "qemu-efi" \
        "ovmf" "libvirt-clients" \
        "libvirt-daemon-system" "bridge-utils" \
        "virt-manager" "virt-viewer" "uml-utilities" \
        "dmg2img" "git" "wget" "libguestfs-tools" \
        "curl" "vim" "unrar" "libvirt-bin"
        );

    # Install extra packages APT
    echo "Install Extra Packages.";
    sudo apt install -y "${packages_list[@]}" > /dev/null 2>&1;

    # Add Users to groups
    sudo adduser ${USER} libvirt > /dev/null 2>&1;
    sudo adduser ${USER} libvirt-qemu  > /dev/null 2>&1;
    sudo adduser ${USER} kvm > /dev/null 2>&1;
    sudo usermod -a -G kvm ${USER} > /dev/null 2>&1;

    # Pip install Extra Packages.
    # Instal python-nmap
    pip3 install python-nmap > /dev/null 2>&1;
    # Install pyshark
    pip3 install pyshark > /dev/null 2>&1;

    sudo snap install gh > /dev/null 2>&1;

    return;
}


# Function to install debconf-utils
function install_debconf_utils() {

    # Update System
    update_and_upgrade_system;

    echo "Install debconf-utils";
    sudo apt -y install debconf-utils > /dev/null 2>&1;

    local UBRIDE_CONF="ubridge ubridge/install-setuid boolean true"
    local WIRESHARK_CONF="wireshark-common wireshark-common/install-setuid boolean true"
    sudo debconf-set-selections <<< $UBRIDE_CONF
    sudo debconf-set-selections <<< $WIRESHARK_CONF

    return;
}


# Function to install Dockers
function install_dockers() {

    echo "Install Dockers.";
    # Add Repositories
    sudo apt install -y apt-transport-https ca-certificates curl software-properties-common  > /dev/null 2>&1;
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -  > /dev/null 2>&1;
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"  > /dev/null 2>&1;


    # Update System
    update_and_upgrade_system;

    # Install Dockers
    apt-cache policy docker-ce  > /dev/null 2>&1;
    sudo apt install -y docker-ce  > /dev/null 2>&1;

    # Add user to Docker group
    sudo usermod -aG docker ${USER}  > /dev/null 2>&1;


    return;
}

# Function tu install GNS3
function install_gns3_gns3server() {

    # Add repository
    sudo add-apt-repository --yes --update ppa:gns3/ppa > /dev/null 2>&1;

    # Update System
    update_and_upgrade_system;

    # Install GNS3 Server and Client
    echo "Install GNS3 Server and Client.";
    sudo apt -y install gns3-gui gns3-server > /dev/null 2>&1;

    # Add support to architecture i386
    sudo dpkg --add-architecture i386 > /dev/null 2>&1;
    update_and_upgrade_system;
    sudo apt -y install lib32stdc++6 gns3-iou > /dev/null 2>&1;

    # Change GNS3 Permisos
    sudo chmod 755 /usr/bin/ubridge > /dev/null 2>&1;
    sudo gpasswd -a ${USER} wireshark > /dev/null 2>&1;
    sudo chgrp ${USER} /usr/bin/dumpcap > /dev/null 2>&1;
    sudo chmod 750 /usr/bin/dumpcap > /dev/null 2>&1;
    sudo setcap cap_net_raw,cap_net_admin+eip /usr/bin/dumpcap > /dev/null 2>&1;


    return;
}


# Function to install Hydrogen
function install_hydrogen() {

    # Install Hydrogen for Atom
    sudo apt -y install jupyter > /dev/null 2>&1;
    sudo -H pip3 install jupyter > /dev/null 2>&1;
    sudo apt -y install python3-venv > /dev/null 2>&1;
    apm install hydrogen > /dev/null 2>&1;
    python3 -m pip install ipykernel > /dev/null 2>&1;
    sudo python3 -m ipykernel install > /dev/null 2>&1;
    python3 -m ipykernel install --user > /dev/null 2>&1;

    return;
}


# Function to install Netmiko
function install_netmiko() {


    echo "Install Netmiko.";
    # Netmiko Install
    pip3 install netmiko > /dev/null 2>&1;
    pip3 install paramiko > /dev/null 2>&1;
    pip3 install textfsm > /dev/null 2>&1;
    pip3 install dnspython > /dev/null 2>&1;
    cd ~
    git clone https://github.com/networktocode/ntc-templates.git > /dev/null 2>&1;
    cd ~
    ls ~/ntc-templates/templates/index > /dev/null 2>&1;
    export NET_TEXTFSM=/home/${USER}/ntc-templates/templates/
    pip3 install pyshark > /dev/null 2>&1;
    pip3 install flake8 > /dev/null 2>&1;
    pip3 install autopep8 > /dev/null 2>&1;
    pip3 install pycodestyle > /dev/null 2>&1;
    pip3 install pylint > /dev/null 2>&1;
    pip3 install flake8-docstrings > /dev/null 2>&1;
    pip3 install graphviz --user > /dev/null 2>&1;
    pip3 install matplotlib > /dev/null 2>&1;
    pip3 install networkx > /dev/null 2>&1;
    pip3 install napalm > /dev/null 2>&1;
    pip3 install simplejson > /dev/null 2>&1;
    pip3 install jupyterlab > /dev/null 2>&1;


    return;
}

# Function tu install GNS3
function install_python_version() {

    # Install Python 3.8
    sudo apt -y install python3 > /dev/null 2>&1;

    # Install Python3-pip
    sudo apt -y install python3-pip > /dev/null 2>&1;

    # Upgrade Pip
    python3 -m pip install --upgrade pip > /dev/null 2>&1;


    return;
}


# Function to remove packages
function autoremove_packages() {

    echo "Finish Configuration.";
    sudo apt -y autoremove > /dev/null 2>&1;

    return;
}

# Function to update and upgrade system
function update_and_upgrade_system() {

    sudo apt -y update > /dev/null 2>&1;
    sudo apt -y upgrade > /dev/null 2>&1;

    return;
}



# Function to install ZSH
function install_zsh() {
    echo "install ZSH"
    sudo apt -y install fonts-powerline zsh tmux
    sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
    echo "exec zsh" >> ~/.bashrc

    return;
}


function pimp_my_terminal() {
    echo "install Pimp my Terminal";

    git clone https://github.com/daniruiz/dotfiles.git
    sh ./dotfiles/install.sh


    git clone https://github.com/romkatv/powerlevel10k.git

    fc-cache -f


    # bash -c "$(curl -sLo- https://git.io/vQgMr)"

    sudo add-apt-repository --yes --update ppa:daniruiz/flat-remix > /dev/null 2>&1;
    sudo apt update > /dev/null 2>&1;
    sudo apt install -y flat-remix-gnome > /dev/null 2>&1;


    alias ls='ls --color=auto'
    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
    alias diff='diff --color=auto'

    export LESS_TERMCAP_mb=$'\e[1;32m'
    export LESS_TERMCAP_md=$'\e[1;32m'
    export LESS_TERMCAP_me=$'\e[0m'
    export LESS_TERMCAP_se=$'\e[0m'
    export LESS_TERMCAP_so=$'\e[01;33m'
    export LESS_TERMCAP_ue=$'\e[0m'
    export LESS_TERMCAP_us=$'\e[1;4;31m'

    sudo snap install lsd > /dev/null 2>&1;
    sudo snap install htop > /dev/null 2>&1;
    sudo snap install bashtop > /dev/null 2>&1;
    sudo snap install lolcat > /dev/null 2>&1;

    command -v bashtop > /dev/null && alias top='bashtop'
    command -v lsd > /dev/null && alias ls='lsd --group-dirs first'
    command -v lsd > /dev/null && alias ls='lsd --tree'
    command -v htop > /dev/null && alias top='htop'
    command -v ytop > /dev/null && alias top='ytop --per-cpu'
    command -v ytop > /dev/null && alias top='ytop --per-cpu -c default-dark'
    alias bat='bat --theme=ansi-dark'
    alias bat='bat --theme=ansi-light'
    command -v bat > /dev/null && alias cat='bat --pager=never'
    command -v bat > /dev/null && alias cat='bat'

    return;
}

function record_terminal() {
  echo "Install my stupid and sesual terminal";

  local packages_list=(
    "imagemagick" "ttyrec" "ttygif" \
    "gcc" "x11-apps" "make" \
    "git" "xdotool" "asciinema"
  );

  # Install array packages
  sudo apt install -y "${packages_list[@]}" > /dev/null 2>&1;

  return;
}
