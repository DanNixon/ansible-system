# `dannixon.system.btrfs_scrub`

Enables periodic Btrfs scrub.

## Role Variables

`btrfs_scrub_path` sets the path to the root of the Btrfs volume to scrub.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    btrfs_scrub_path: "/"

  roles:
    - dannixon.system.btrfs_scrub
```

## License

MIT
