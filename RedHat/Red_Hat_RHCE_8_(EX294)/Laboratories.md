
## Lab 2-1

Set up an Ansible environment according to the directins in this chapter. Make sure this environment meets the following requirements.

* Three hosts are used: control.example.com, ansible1.example.com, and ansible2.example.com.
* A user named ansible is created on all hosts.
* On ansible1 as well as ansbile2, the ansible user is allowed to run root commands using sudo, without being required to enter a password.
* User ansible can log in to ansible1 and ansible2 using ssh. based on passphrase-less private keys.

* The ansible software is installed on control.

### Solution

Add repo epel
***
1. Install epel-repo over `dnf install`
```sh
dnf install -y epel-release
```

2. Install Ansible
```sh
dnf -y install ansible
```

3. Check Ansible version
```
ansible --versionq
```



Create username
***
1. Create user with name "ansible."
```sh
adduser ansible
```
2. Add password to user.
```sh
passwd ansible
```

3. Add user to wheel group
```sh
usermod -aG wheel ansible
```

Setting Up Privilege Escalation
***

1. As root, you need to add next line to `/etc/sudoers.d/ansible`

```sh
echo "ansible ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/ansible
```

Create public and privite keys.
***

1. We need to run next command.
```sh
ssh-keygen -f name_id_rsa -b 4096 -C username@hostname
```

2. Start the ssh-agent in the background.
```sh
eval "$(ssh-agent -s)"
```

3. Add passphare to `ssh-add`.
```sh
ssh-add -i name_id_rsa
```

4. Copy pub key to server.
```sh
ssh-copy-id -i name_id_rsa.pub username@hostname
```
