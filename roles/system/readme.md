# `dannixon.system.system`

[![dannixon.system.system](https://github.com/DanNixon/ansible-system/actions/workflows/system.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-system/actions/workflows/system.yml)

Performs basic system configuration:

  - Sets hostname
  - Populates `/etc/hosts`
  - Generates and sets locale
  - Sets keyboard layout
  - Sets timezone
  - Enables NTP
  - (Archlinux)
    - Configures Pacman

## Role Variables

See example below, variable names should be pretty self explanatory.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    system_hostname: test
    system_locale: en_GB.UTF-8
    system_keymap: uk
    system_timezone: Europe/London

  roles:
    - dannixon.system.system
```

## License

MIT
