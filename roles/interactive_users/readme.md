# `dannixon.system.interactive_users`

[![dannixon.system.interactive_users](https://github.com/DanNixon/ansible-system/actions/workflows/interactive_users.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-system/actions/workflows/interactive_users.yml)

Creates new users intended to login to a system.

## Role Variables

`interactive_users` is a list of users to add.
Users are defined as a mapping of the follwoing keys:

- `username`: the username of the user to be added
- `password` is the crypted password of the user to be added
- `ssh_pubkey` adds an SSH authorized key entry for the newly created user
- `sudoer` indicates if the new user should be a sudoer

See `man openssl-passwd` for crypted password generation.
Can also be set to `!` to disable password login.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    interactive_users:
      - username: user
        password: ""
        ssh_pubkey: ""
        sudoer: true

  roles:
    - dannixon.system.interactive_users
```

## License

MIT
