Descargar el archivo de la maquina virtual GNS3 VM
https://github.com/GNS3/gns3-gui/releases


Descomprimir el archivo en la ruta donde se encuentran los disco duros de Hyper-V.

Editar el archivo create-vm.ps1

 Aumentar la cantidad de memoria a la deseada.


Opcional
Aumentar la cantidad de CPU a 2 o más.


Maquina GNS3

1. Asignar una dirección IP fija a la maquina virtual del rango establecido.



2. Cambiar el teclado

  Reiniciar el servidor.






3. Crear llaves publicas dentro de la carpeta .ssh del usuario local
ssh-keygen -t rsa -b 4096 -f gns3vm_id_rsa -C "gns3@172.27.96.25"


3.1 Start ssh-agent with PowerShell
get-service -name ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent


3.2 Agregar las la frase secreta  al agente ssh
ssh-add gns3vm_id_rsa


3.2 Crear la carpeta .ssh en el servidor.

3.3 Copiar la llave publica del cliente al servidor.
type $env:USERPROFILE\.ssh\gns3vm_id_rsa.pub | ssh gns3@172.27.96.25 "cat >> .ssh/authorized_keys"

3.4 Visualizar en el servidor la llave publica copiada


Modificar bridges en el servidor.

4. Ingresar al servidor

4.1 Visualizar los bridges virtuales


4.4 Crear el archivo de nombre virbr1.xml
<network>
    <name>virbr1</name>
    <bridge name="virbr1" />
</network>

4.5 Iniciar el bridge
sudo virsh net-define virbr1.xml
sudo virsh net-start virbr1
sudo virsh net-autostart virbr1

4.6 Asignar IP al bridge
sudo virsh net-edit virbr1

4.7 Reiniciar el servidor.

5. Agregar VS Code


5.1 Instalar el complemento Remote SSH

5.2 Editar el archivo .ssh/config

5.3 Conectarse al servidor.

5.4 Crear el directorio




Notas:

Primero actualizar,
Despues instalar bridge y vim
Despues eliminar bridge virtual
Despues crear el bridged




References
https://www.chrisjhart.com/Windows-10-ssh-copy-id/
https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement
https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement
https://linuxconfig.org/how-to-use-bridged-networking-with-libvirt-and-kvm
https://www.tecmint.com/create-ssh-tunneling-port-forwarding-in-linux/
https://stackoverflow.com/questions/18683092/how-to-run-ssh-add-on-windows
https://bbs.archlinux.org/viewtopic.php?id=203279



Agregar VS Code

Creacion de las llaves ssh

En el servidor gns3 crear la carpeta .ssh
mkdir .ssh

En el cliente windows utilizar el siguiente comando
type $env:USERPROFILE\.ssh\gns3vm_id_rsa.pub | ssh 172.23.80.30 "cat >> .ssh/authorized_keys"

Instalar python3-venv

Crear el ambiente virtual

Instalar netmiko


VirtualBridge directory
/etc/libvirt/qemu/networks/autostart/


Cambiado del teclado
localectl set-keymap la-latin1


Editar el archivo de configuration de la maquina virtual y reiniciar
