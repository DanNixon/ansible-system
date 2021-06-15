# `dannixon.system.package_updates`

[![dannixon.system.package_updates](https://github.com/DanNixon/ansible-system/actions/workflows/package_updates.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-system/actions/workflows/package_updates.yml)

Ensure system packages are up to date.

## Example Playbook

```yaml
- hosts: all
  become: true

  roles:
    - dannixon.system.package_updates
```

## License

MIT
