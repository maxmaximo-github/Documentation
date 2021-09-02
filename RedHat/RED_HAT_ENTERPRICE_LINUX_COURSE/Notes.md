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
Virtual Machine.

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
