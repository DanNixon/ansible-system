from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


def config_list(all_configs):
    items = []
    for name, configs in all_configs.items():
        for t, conf in configs.items():
            items.append({
                "filename": f"{name}.{t}",
                "config": conf,
            })
    return items


class FilterModule(object):
    def filters(self):
        return {
            'networkd_config_list': config_list,
        }
