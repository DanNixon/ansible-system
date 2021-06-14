# `dannixon.system.networkd`

Installs, configures and enables systemd-networkd.

## Role Variables

`networkd_config`

`networkd_clean`
`networkd_clean_pattern`

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    networkd_config:
      20-wired:
        network:
          Match:
            Name: "en*"
          Network:
            DHCP: "yes"

    networkd_clean: false
    networkd_clean_pattern: "20-*.*"

  roles:
    - dannixon.system.networkd
```

## License

MIT
