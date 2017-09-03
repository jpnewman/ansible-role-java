"""Jaa Install Specs."""

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_python_package(host):
    """Test Python is installed."""
    python = host.package('python')
    assert python.is_installed


def test_java_common_package(host):
    """Test Java Common is installed."""
    java_common = host.package('java-common')
    assert java_common.is_installed


def test_oracle_java8_installer_package(host):
    """Test Java8 is installed."""
    oracle_java8_installer = host.package('oracle-java8-installer')
    assert oracle_java8_installer.is_installed


def test_oracle_java8_set_default_package(host):
    """Test Java8 Set Default is installed."""
    oracle_java8_set_default = host.package('oracle-java8-set-default')
    assert oracle_java8_set_default.is_installed
