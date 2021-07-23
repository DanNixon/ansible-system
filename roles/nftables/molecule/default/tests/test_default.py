import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_file(host):
    f = host.file("/etc/nftables.conf")
    assert f.is_file
    assert f.md5sum == "d097edb5f414dc8c07c9c02fc6b4c97e"
