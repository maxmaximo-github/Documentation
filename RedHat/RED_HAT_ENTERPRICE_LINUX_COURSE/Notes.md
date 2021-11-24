# Red had Entrerprice Linux 8 Cert Guide

Chapter 1
--

* RHEL 8 is a Linux Distribution and you need a subscription.
* RHEL 8 has two free alternatives: CentOS 8, Fedora
* Developer program  https://developers.redhat.com
* CentOS is free and it has the same functionalities as RHEL but without the enterprise support services.
* A repository is the installation source used for installing software.
* If you are using Red Had Enterprise Linux with subscription, you'll need to use the Subscription Manager software to get access to repositories.


***
Setup Requirements
* 1 GiB of RAM
* A 10 GiB hard disk
* A network card

* GiB (Gibibytes) is a standard unit used in the field of data processing and transmission and is defined as base 1024 rather than base 1000. For example, 1 GB is defined as 1000³ bytes, whereas 1 GiB is defined as 1024³ bytes. Unit of measure. Bytes.


***
|Virtual Machine.|
| :---: |

| Virtual Machine 1 | | | |
| :---: | :---: | :---: | ---: |
| Partition1 | /boot  | XFS  | 500 MiB |
| Partition2 | /  | XFS  | 10 GiB |
| Partition3 | swap  | XFS  | 1 GiB |

* RHEL 8 by default uses the XFS file system. This file system cannot be shrunk.

| Credentials |
| :---: |
| Root:`password` |
| student:`password` |



LAB 1.1
***
Repeat the procedure “Performing a Manual Installation” to install one more server. Details about the additional configuration on these servers follow in exercises in later chapters. For now, it is sufficient to ensure that the following conditions are met:

* use the server names server1 and server2.
* Set the network configuration to obtain an Ip address automatically.
* Make sure to keep at least 1 GiB of disk space as unallocated disk space (which is not assignet to any partition) so that you have free space to work on the partitioning exercises in later chapters.
* Install one server using the Minimal Install pattern, and another server using the Server with GUI installation pattern.

Chapter 2
---
Shell
***
* The sheel is the default working environment for a Linux administrator. It is the environment where users and administrators enter commands tahta are executed by the operating system.
* Bash is the mos commond shell.

* The purpose of the Linux shell is to provide an environment in which commands can be executed. The shell makes a distinction between three kinds of commands:
  * Aliases
  * Internal commands
  * External **commands**
* An **alias** is a command that a user can define as needed. Example:
`alias newcommand=oldcommand`
Aliases are executed before anything else.

* An **internal command** is a command that is a part of the shell itsef and, as such, doesn't have to be loaded form disk separately.

* An **external command** is a command that exists as an executable file on the disk of the computer. Because it has to be read rom disk the firs time it is used, it is a bit slower.

Commands
***

* Tipically, command syntax has three basic parts: the command, its options, and its arguments.

  * Command name.
  * Options are a part of program code, and they modify what the command is doing.
  * Argument is the next part of options.


| Command | Action |
| :---: | :--- |
| ls | List current directories and files
| type | To find out whether a command is a Bash internal or an executable file on disk|
| $PATH | This variable defines a list of directories that is searched for matching filename when a user enters a command. |
| which | To find out which exact command the shell will be using|
|type| This command will also work on internal commands and aliases|
|./ | Tell Bash to look for the command in the current directory|
| time |time run the program COMMAND with any given arguments ARG....  Whe COMMAND finishes, time displays information about resources used by COMMAND (on the standard error output, by default). |

The **$PATH** variable can be set for specific users, but in general, most users will be using the same **$PATH** variable.

I/O Redirection
---
By default, when a command is executed, it shows its result on the screen of the computer you are working on. The computer monitor is used as the standar destination for output, whis is also refered to as the **STDOUT**.

Table Standar Input, Output and Error Overview.
---

| Name | Default Destination | Use in redirection | File Descriptor Number |
| :---: | :---: | :---: | :---: |
| STDIN | Computer keyboard | < (same as 0 <) | 0 |
| STDOUT | Computer monitor | > (same as 1) | 1 |
| STDERR | Computer monitor | 2> | 2 |

Redirection is also useful if you want to work whit input from an alternative location, such as a file.

A **Devices files** on Linux is a file taht is used to access specific hardware.
