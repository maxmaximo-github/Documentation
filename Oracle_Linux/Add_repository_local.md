## Add repo local Oracle Linux

Change to root user

``` sh
sudo su
```

Create folter Oracle_Linux

``` sh
mkdir /media/Oracle_Linux
```


Mount cdroom

``` sh
mount /dev/cdrom /media/Oracle_Linux
```



Change to /etc/yum.repos.d/

``` sh
cd /etc/yum.repos.d/
```



Copy oracle-linux-ol8 to oracle-linux-ol8-local

``` sh
copy oracle-linux-ol8 oracle-linux-ol8-local
```


Modified archive oracle-linux-ol8-local
``` sh
[ol8_media_BaseOS]
name=Oracle Linux 8.4 x86_64 BaseOS Local
baseurl=file:///media/Oracle_Linux/BaseOS
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-oracle
gpgcheck=1
enabled=1


[ol8_media_appstream]
name=Oracle Linux 8.4 x86_64 BaseOS Local
baseurl=file:///media/Oracle_Linux/AppStream
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-oracle
gpgcheck=1
enabled=1
```

Show repolist

``` sh
dnf repolist

```


Vamos a instalar el paquete tcpdump para capturar paquetes

```sh
tcpdump -i enp1s0
```


Add telnet cliente y telnet server

```
dnf -y install telnet telnet-server --disablerepo=\* --enablerepo=appstream
```



Enable service
```sh
systemctl start telnet.socket
systemctl enable telnet.socket
systemctl status telnet.socket
```



Enable firewall
```sh
firewall-cmd --permanent --zone=public --add-service=telnet
firewall-cmd --reload
```

Comands

```sh
dnf repolist all
dnf repolist
dnf list
```

Deshabilitar la banderas en los repositorios existentes.
