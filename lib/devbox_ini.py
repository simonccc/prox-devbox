#!/usr/bin/env python3

# generate the default devbox.ini
def init_devbox_ini():

  # import config parser
  from configparser import ConfigParser

  # get config
  config = ConfigParser(allow_no_value=True)
  config.read('devbox.ini')

  # proxmox section
  config.add_section('proxmox')

  # proxmox api endpoint
  config.set('proxmox', '; domain or IP to access proxmox')
  config.set('proxmox', 'prox_endpoint', '127.0.0.1')

  # proxmox api port
  config.set('proxmox', '; api port ( usually 8006 ) ')
  config.set('proxmox', 'port', '8006')

  # username
  config.set('proxmox', '; username to connect with / owner of the API token')
  config.set('proxmox', 'user', 'root@pam')

  # api token name
  config.set('proxmox', '; name of api token')
  config.set('proxmox', 'token_name', 'devbox')

  # api key
  config.set('proxmox', '; text of api key')
  config.set('proxmox', 'api_key', 'xxxxxxxxxxxxx')

  # node to operate on
  config.set('proxmox', '; the proxmox node that you will run devbox on - the image and all nodes are created on this host')
  config.set('proxmox', 'node', 'proxmox')

  # storage on node
  config.set('proxmox', '; the proxmox storage to use for devbox - needs to be available on the proxmox node')
  config.set('proxmox', 'storage', 'local-lvm')

  # devbox section
  config.add_section('devbox')
  config.set('devbox', 'dev_id', 'the proxmox id used as the base for devboxes')

  # upstream image
  config.set('devbox', '; the upstream cloud image used to create the devbox image')
  config.set('devbox', 'cloud_image_url', 'https://cloud-images.ubuntu.com/minimal/daily/oracular/current/oracular-minimal-cloudimg-amd64.img')

  # disk size for devbox vms
  config.set('devbox', '; size of vm disk in Gib ')
  config.set('devbox', 'vm_disk', '20')

  # number of cpu cores
  config.set('devbox', '; number of cpu cores ')
  config.set('devbox', 'vm_cpu', '1')

  # ram size
  config.set('devbox', '; amount of ram in Gib ')
  config.set('devbox', 'vm_ram', '2')

  # cloudinit user key and password
  config.set('devbox', '; username for created cloudinit user')
  config.set('devbox', 'cloudinituser', 'user')

  # cloud init user password
  config.set('devbox', '; password for the cloudinit user')
  config.set('devbox', 'cloudinitpass', 'admin')

  # cloud init user ssh key
  config.set('devbox', ';  a ssh public key for the cloudinit user ( required ) ')
  config.set('devbox', 'cloudinitsshkey', 'ssh-rsa cioieocieo')

  # network bridge
  config.set('devbox', '; network bridge to use with devbox')
  config.set('devbox', '; a proxmox sdn can be used by specifying the zone and vnet like this: sdn/zone/vnet')
  config.set('devbox', 'network_bridge', 'vmbr0')

  # devbox network baseip
  config.set('devbox', '; first ip of the ip range used for this devbox cluster')
  config.set('devbox', 'network_ip', '192.168.0.160')

  # netmask / subnet
  config.set('devbox', '; /24 is 255.255.255.0')
  config.set('devbox', 'network_mask', '24')

  # default gateway
  config.set('devbox', '; default gateway for the network ( needs to provide internet access ) ')
  config.set('devbox', 'network_gw', '192.168.0.1')

  # dns server
  config.set('devbox', '; dns server for network')
  config.set('devbox', 'network_dns', '192.168.0.1')

  # network mtu
  config.set('devbox', '; interface mtu set on vms ')
  config.set('devbox', '; set to 1450 if using sdn ')
  config.set('devbox', 'network_mtu', '1500')

  # write config
  # file should not already exist...
  with open('devbox.ini', 'w') as cfile:
    config.write(cfile)
  print('created devbox.ini please edit for your setup')
  return
