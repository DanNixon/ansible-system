# `dannixon.system.arch_mirrorlist`

[![dannixon.system.arch_mirrorlist](https://github.com/DanNixon/ansible-system/actions/workflows/arch_mirrorlist.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-system/actions/workflows/arch_mirrorlist.yml)

Installs an up to date Pacman mirror list from the [mirrorlist generator](https://archlinux.org/mirrorlist/).

## Role Variables

The list of mirrors can be filtered by the following fields:

  - `arch_mirrorlist_countries`
  - `arch_mirrorlist_protocols` (`http`, `https`)
  - `arch_mirrorlist_ip_versions` (`ipv4`, `ipv6`)
  - `arch_mirrorlist_use_status` (`true`, `false`)

Note that for this role to be idempotent `arch_mirrorlist_use_status` should be set to `false`.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    arch_mirrorlist_countries:
      - GB
      - DE

  roles:
    - dannixon.system.arch_mirrorlist
```

## License

MIT
