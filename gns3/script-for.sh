for i in ubridge libvirt kvm wireshark docker; do
  sudo usermod -aG $i $USER
done
