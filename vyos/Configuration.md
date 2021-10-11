Change hostname
set system host-name {name}
commit
save

Domains
set system domain-search domain example.com
set system domain-name example.com

Set name-server
set system name-server 2001:db8:cafe:1::500



Interfaces Configuration
set interfaces ethernet eth0 address 2001:db8:cafe:4::2/64
Router Advertisment
***
set service router-advert interface eth0 prefix 2001:db8:cafe:4001::/64

set service router-advert interface eth0 link-mtu 1500


set service router-advert interface eth0 dns


Static Routes
set protocols static route6 ::/0 next-hop 2001:db8:cafe:4::1 200


set protocols ospfv3 parameteres router-id 4.4.4.4

set protocols ospfv3 area 0 interface eth0
set protocols ospfv3 area 0 interface eth1
set protocols ospfv3 area 0 interface eth2


SSH
set service ssh
set service ssh disable-password-authentication


Cisco
interfaces
  ospfv3 1 ipv6 area 0

router ospfv3 1
 address-family ipv6 unicast
 passive-interface default
 default-information originate
 router-id 1.1.1.1
