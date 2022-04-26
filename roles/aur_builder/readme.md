# `dannixon.system.aur_builder`

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
