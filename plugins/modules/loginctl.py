#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
import subprocess
from ansible.module_utils.basic import AnsibleModule

__metaclass__ = type

DOCUMENTATION = r'''
---
module: loginctl

short_description: Perform operations using loginctl

version_added: "0.0.63"

description: Perform operations using loginctl

options:
    user:
        description: User to apply changes to, can be username or UID.
        required: true
        type: str
    linger:
        description: Enable/disable user session lingering.
        required: false
        type: bool

author:
    - Dan Nixon (@DanNixon)
'''

EXAMPLES = r'''
# Enable session linger for user foo
- name: Test with a message
  dannixon.system.loginctl:
    user: foo
    linger: true
'''


def run_module():
    module_args = dict(
        user=dict(type='str', required=True),
        linger=dict(type='bool', required=False),
    )
    result = dict(changed=False)
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if module.params['linger'] is not None:
        current_linger_state = b'yes' in subprocess.check_output([
            'loginctl',
            'show-user',
            '--property',
            'Linger',
            module.params['user'],
        ])

        if current_linger_state is not module.params['linger']:
            if not module.check_mode:
                subprocess.check_output([
                    'loginctl',
                    'enable-linger'
                    if module.params['linger'] else 'disable-linger',
                    module.params['user'],
                ])
            result['changed'] = True

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
