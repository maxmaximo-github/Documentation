SSH Configuration
---

1. Configure vty lines 0 to 4
        user-interface vty 0 4
          authentication-mode aaa
          protocol inbound ssh

  ***Note: If you want to permit ssh and telnet on the lines vty, you need to configure with the next command `protocol inbound all`***.

2. You need to verify if the SSH server is enable.

  ![png](./images/serversshstatus.png)


3. If the ssh server is not enable then use the next command `stelnet server enable`

  ![png](./images/sshserverenable.png)


4. Now, create aaa model.
        aaa
          local-user admin_test privilege level 15
          local-user admin_test password cipher test@huawei.com
          local-user admin_test service-type ssh terminal

5. Add user to SSH configuration
        ssh user admin_test
        ssh user admin_test authentication password
        ssh user admin_test service-type stelnet

6. Create RSA PKI.
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
