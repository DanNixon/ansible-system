# `dannixon.system.tailscale`

Installs the [Tailscale](https://tailscale.com/) client.

## Role Variables

- `tailscale_restart`: restarts the Tailscale service if set to `true`.

## Example Playbook

```yaml
- hosts: all
  become: true

  roles:
    - dannixon.system.tailscale
```

## License

MIT
