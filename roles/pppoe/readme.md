# `dannixon.system.pppoe`

[![dannixon.system.pppoe](https://github.com/DanNixon/ansible-system/actions/workflows/pppoe.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-system/actions/workflows/pppoe.yml)

Installs and configures a PPPoE client.

## Role Variables

`pppoe_peer_config` provides configuration for a peer named `pppoe_peer_name`.
Note that the plugin is fixed to `rp-pppoe.so`, so this can (and should) be omitted from `pppoe_peer_config`.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    pppoe_peer_name: bt
    pppoe_peer_config:
      - noauth
      - nodetach
      - noipdefault
      - noproxyarp
      - noremoteip
      - defaultroute
      - maxfail 100
      - persist
      - nic-eth0
      - ifname wan0
      - user bthomehub@btbroadband.com
      - password x

  roles:
    - dannixon.system.pppoe
```

## License

MIT
