# `dannixon.system.nftables`

Installs, configures and enables a firewall using [nftables](https://www.nftables.org/).

## Role Variables

See example.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    nftables_tables:
      - name: filter
        family: inet

        sets:
          - name: s1
            type: ipv4_addr
            counter: true
            elements:
              - 10.0.0.1
              - 10.0.0.2

          - name: s2
            typeof: udp dport
            elements:
              - domain

        chains:
          - "{{ nftables_application_chains.ssh }}"

          - name: input
            config:
              type: filter
              hook: input
              priority: filter
              policy: drop
            rules:
              - iif lo counter accept
              - ct state invalid counter drop
              - 'ct state { established, related } counter accept'
              - 'ip6 nexthdr icmpv6 icmpv6 type { nd-neighbor-solicit, echo-request, nd-router-advert, nd-neighbor-advert } counter accept'
              - jump input_ssh
              - 'log prefix "firewall: dropped " counter drop'

          - name: forward
            config:
              type: filter
              hook: forward
              priority: filter
              policy: drop

          - name: output
            config:
              type: filter
              hook: output
              priority: filter
              policy: accept

  roles:
    - dannixon.system.nftables
```

## License

MIT
