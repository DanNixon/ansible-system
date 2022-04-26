# `dannixon.system.healthcheck_heartbeat`

Configures periodic pinging of a [Healthchecks](https://healthchecks.io) check, providing a basic system heartbeat.

## Role Variables

`healthcheck_heartbeat_url` sets the URL of the Healthchecks service to notify.
It defaults to the healthchecks.io instance.

`healthcheck_heartbeat_uuid` is the UUID of the check to ping.

`healthcheck_heartbeat_time_period` is the frequency at which to ping.
Accepts any valid option that can be given to `OnCalendar` (see `man 5 systemd.timer`).
Defaults to every 5 minutes.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    healthcheck_heartbeat_uuid: "abc123"

  roles:
    - dannixon.system.healthcheck_heartbeat
```

## License

MIT
