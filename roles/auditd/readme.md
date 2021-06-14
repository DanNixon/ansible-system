# `dannixon.system.auditd`

[![dannixon.system.auditd](https://github.com/DanNixon/ansible-system/actions/workflows/auditd.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-system/actions/workflows/auditd.yml)

Installs and configures auditd.

## Role Variables

Rules are provided via the `auditd_rules` variable.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    auditd_rules: |
      -a always,exit -F arch=b32 -S init_module,finit_module -F key=module-load
      -a always,exit -F arch=b64 -S init_module,finit_module -F key=module-load
      -a always,exit -F arch=b32 -S delete_module -F key=module-unload
      -a always,exit -F arch=b64 -S delete_module -F key=module-unload

  roles:
    - dannixon.system.auditd
```

## License

MIT
