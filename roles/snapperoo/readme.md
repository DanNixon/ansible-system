# `dannixon.system.snapperoo`

Installs, configures and enables [Snapperoo](https://github.com/DanNixon/snapperoo).

## Role Variables

`snapperoo_config` encodes the YAML representation of the JSON config expected by Snapperoo.
See `man 5 snapperoo`.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    snapperoo_config:
      - source: "/"
        target: "/.snapshots/root"
        schedules:
          daily:
            retention_count: 7
          weekly:
            retention_count: 4
          monthly:
            retention_count: 12

  roles:
    - dannixon.system.snapperoo
```

## License

MIT
