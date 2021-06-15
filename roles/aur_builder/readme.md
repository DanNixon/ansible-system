# `dannixon.system.aur_builder`

[![dannixon.system.aur_builder](https://github.com/DanNixon/ansible-system/actions/workflows/aur_builder.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-system/actions/workflows/aur_builder.yml)

Satisfies dependencies for building AUR packages (for example, using [`kewlfft.aur`](https://github.com/kewlfft/ansible-aur)).

Once this role is executed, the `aur_builder` user may be used for building and installing packages from the AUR.

## Example Playbook

```yaml
- hosts: all
  become: true

  roles:
    - dannixon.system.aur_builder
```

## License

MIT
