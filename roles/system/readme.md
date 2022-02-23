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

- `system_hostname`: sets system hostname.
- `system_locale`: sets system locale.
- `system_timezone`: sets system timezone.
- `system_console_keymap`: set the keyboard layout used on the console.
- `system_console_font` (optional): set the font used on the console.
- `system_reboot` (optional): if true, unconditionally reboots the system after configuration.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    system_hostname: test
    system_locale: en_GB.UTF-8
    system_timezone: Europe/London
    system_console_keymap: uk
    system_console_font: ter-v24b
    system_reboot: true

  roles:
    - dannixon.system.system
```

## License

MIT
