# `dannixon.system.sanoid`

[![dannixon.system.sanoid](https://github.com/DanNixon/ansible-system/actions/workflows/sanoid.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-system/actions/workflows/sanoid.yml)

Installs, configures and enables [Sanoid](https://github.com/jimsalterjrs/sanoid).

## Role Variables

`sanoid_datasets` and `sanoid_templates` encode the content of the Sanoid configuration file.

## Example Playbook

This example encodes the example configuration shown [here](https://github.com/jimsalterjrs/sanoid/blob/master/README.md).

```yaml
- hosts: all
  become: true

  vars:
    sanoid_datasets:
      - path: data/home
        config:
          use_template: production
      - path: data/images
        config:
          use_template: production
          recursive: "yes"
          process_children_only: "yes"
      - path: data/images/win7
        config:
          hourly: 4

    sanoid_templates:
      - name: production
        config:
          autosnap: "yes"
          autoprune: "yes"
          frequently: 0
          hourly: 36
          daily: 30
          monthly: 3
          yearly: 0

  roles:
    - dannixon.system.sanoid
```

## License

MIT
