# `dannixon.system.package_updates`

Ensure system packages are up to date.

## Role Variables

Setting `package_updates_reboot` to `true` will reboot the system and wait for it to become available again.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    package_updates_reboot: true

  roles:
    - dannixon.system.package_updates
```

## License

MIT
