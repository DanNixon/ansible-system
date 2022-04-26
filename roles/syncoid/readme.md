# `dannixon.system.syncoid`

Installs and configures [Syncoid](https://github.com/jimsalterjrs/sanoid/#syncoid).
Creates users, configures SSH keys and ZFS permission delegation on both primary and replica sides for a typical primary/(multiple) replica backup strategy, with the replicas having SSH access to the primary.

## Role Variables

`syncoid_role` defined if the host is the primary (`primary`) data store or a replica (`replica`) of the primary.
This variable must be set.

`syncoid_group` and `syncoid_user` set the name of the created group and user respectively.
Both default to `syncoid-backup`.

`syncoid_primary_public_keys` is a list of public key content to be added to the user on the primary side.

`syncoid_ssh_key_name` sets the name of the generated SSH key on the replica side.
Defaults to `syncoid_backup`.

`syncoid_targets` is a list of ZFS datasets that the replication will operate over.
This is used to determine what datasets permission delegation is configured on.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    syncoid_role: primary

    syncoid_primary_public_keys:
      - key1...
      - key2...

    syncoid_targets:
      - rpool

  roles:
    - dannixon.system.syncoid
```

## License

MIT
