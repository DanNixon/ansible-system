import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package_is_installed(host):
    assert host.package("sanoid").is_installed


def test_group_is_created(host):
    assert host.group("syncoid-backup").exists


def test_user_is_created(host):
    assert host.user("syncoid-backup").exists
