"""Java Install Specs."""

import yaml
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def GetJavaInstallerType():
    """Get Java Installer Type."""
    with open("defaults/main.yml") as default_vars:
        yaml_data = yaml.load(default_vars)
        return yaml_data["java_installer_type"]


def test_python_package(host):
    """Test Python is installed."""
    python = host.package('python')
    assert python.is_installed


@pytest.mark.skipif(GetJavaInstallerType() != "oracle_ppa",
                    reason="oracle_ppa method only.")
def test_java_common_package(host):
    """Test Java Common is installed."""
    java_common = host.package('java-common')
    assert java_common.is_installed


@pytest.mark.skipif(GetJavaInstallerType() != "oracle_ppa",
                    reason="oracle_ppa method only.")
def test_oracle_java8_installer_package(host):
    """Test Java8 is installed."""
    oracle_java8_installer = host.package('oracle-java8-installer')
    assert oracle_java8_installer.is_installed


@pytest.mark.skipif(GetJavaInstallerType() != "oracle_ppa",
                    reason="oracle_ppa method only.")
def test_oracle_java8_set_default_package(host):
    """Test Java8 Set Default is installed."""
    oracle_java8_set_default = host.package('oracle-java8-set-default')
    assert oracle_java8_set_default.is_installed


def test_java_version(host):
    """Test Java JCE."""
    command = host.run("java -version")
    assert "version" in command.stderr.strip()


@pytest.mark.skipif(GetJavaInstallerType() == "openjdk",
                    reason="Not for openjdk method.")
def test_java_jce(host):
    """Test Java JCE."""
    command = host.run("jrunscript -e \"print (javax.crypto.Cipher.getMaxAllowedKeyLength('AES') >= 256)\"")
    assert command.stdout.strip() == 'true'
