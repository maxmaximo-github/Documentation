SSH Configuration
---

1. Configure vty lines
        user-interface vty 0 4
          authentication-mode aaa
          protocol inbound ssh


2. Enable ssh service (ssh server)
        stelnet server enable


3. Create aaa model
        aaa
          local-user admin_test privilege level 15 password irreversible-cipher test@huawei.com
          local-user admin_test service-type ssh terminal

4. Add user to SSH configuration
        ssh user admin_test
        ssh user admin_test authentication password
        ssh user admin_test service-type stelnet

5. Create RSA PKI.
        rsa local-key-pair create




Troubleshooting
---

1. If Wireshark shows the next packages:
![png](./images/1.ssh.not_service_enable.png)
then check if the ssh server status.

  ![png](./images/1.ssh.display_ssh_server_status.png)

2. If Wireshark shows the next packages:
![png](./images/2.ssh.wireshark.png)
then configure SSH with this guide.

3. If appears in terminal the next text
![png](./images/6.error_password_ssh.png)
You need type the next command:
        ssh user admin_test authentication-type password
