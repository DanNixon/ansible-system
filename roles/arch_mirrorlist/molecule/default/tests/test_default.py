import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

mirrotlist_filename = "/etc/pacman.d/mirrorlist"


def test_file_exists(host):
    assert host.file(mirrotlist_filename).is_file


def test_countries(host):
    f = host.file(mirrotlist_filename)
    assert f.contains("## United Kingdom")
    assert f.contains("## Germany")


def test_protocols(host):
    f = host.file(mirrotlist_filename)
    assert f.contains("https://")
    assert not f.contains("http://")
