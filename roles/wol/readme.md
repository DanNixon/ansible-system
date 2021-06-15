# `dannixon.system.wol`

[![dannixon.system.wol](https://github.com/DanNixon/ansible-system/actions/workflows/wol.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-system/actions/workflows/wol.yml)

Enables waking on WoL magic packets on a given interface.

This role should only be used when systemd-networkd is not used, otherwise setting `WakeOnLan` is likely the simpler option (see `man 5 systemd.netdev`).

## Role Variables

`wol_interface` defines the interface to enable WoL on.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    wol_interface: eth0

  roles:
    - dannixon.system.wol
```

## License

MIT
