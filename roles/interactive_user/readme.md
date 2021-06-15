# `dannixon.system.interactive_user`

[![dannixon.system.interactive_user](https://github.com/DanNixon/ansible-system/actions/workflows/interactive_user.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-system/actions/workflows/interactive_user.yml)

Creates a new user intended to login to a system.

## Role Variables

`interactive_user_username` is the username of the user to be added.

`interactive_user_password` is the crypted password of the user to be added.
See `man openssl-passwd` for crypted password generation.
Can also be set to `!` to disable password login.

`interactive_user_ssh_key` adds an SSH authorized key entry for the newly created user.

`interactive_user_sudoer` indicates if the new user should be a sudoer.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    interactive_user_username: user
    interactive_user_password: ""
    interactive_user_ssh_key: ""
    interactive_user_sudoer: true

  roles:
    - dannixon.system.interactive_user
```

## License

MIT
