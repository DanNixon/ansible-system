import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_file(host):
    f = host.file("/etc/sanoid/sanoid.conf")
    assert f.is_file
    assert f.md5sum == "b76d45d8129b732e16eef49217d75a14"
