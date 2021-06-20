# `dannixon.system.networkd`

Installs, configures and enables systemd-networkd.

## Role Variables

`networkd_config` encodes the configuration for all devices.
The structure is in the format shown below.
`TYPE` is the networkd file "type" (e.g. `netdev`, `network`, etc.).
`SECTION` and `KEY` are as per the options specified for the given file type (see `man 5 systemd.TYPE`).

```yaml
networkd_config:
  NAME:
    TYPE:
      SECTION:
        KEY: VALUE
```

When an array is specified, this is translated into multiple sections or keys.

If `networkd_clean` is set to `true`, files in the destination config directory matching the pattern specified by `networkd_clean_pattern` will be removed.
This provides a means of "resetting" the existing network configuration.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    networkd_config:
      20-wired:
        network:
          Match:
            Type: ether
          Network:
            DHCP: "yes"

    networkd_clean: false
    networkd_clean_pattern: "20-*.*"

  roles:
    - dannixon.system.networkd
```

## License

MIT
