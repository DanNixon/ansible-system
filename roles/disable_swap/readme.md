# `dannixon.system.disable_swap`

Disables swap for subsequent boots.
Does not disable swap if it is currently active, but does provide the option to reboot a machine if any changes to `fstab` have been made.

## Role Variables

`disable_swap_reboot` defines if the host should be rebooted after changes have been made (defaults to `false`).

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    disable_swap_reboot: true

  roles:
    - dannixon.system.disable_swap
```

## License

MIT
