# jpnewman.java

[![Ansible Role](https://img.shields.io/ansible/role/9594.svg?maxAge=2592000)](https://galaxy.ansible.com/jpnewman/java/)
[![Build Status](https://travis-ci.org/jpnewman/ansible-role-java.svg?branch=master)](https://travis-ci.org/jpnewman/ansible-role-java)

This is an Ansible role to install Java 8

## Requirements

Ansible 2.x

## Role Variables

|Variable|Description|Default|
|---|---|---|
|```apt_cache_valid_time```|Apt Cache Valid Time|600|
|```apt_java_repo```|Apt-Get Repo|ppa:webupd8team/java|
|```apt_java_package```||oracle-java8-installer|
|```install_java```|If ```false``` Java is only setup, but not installed|"true"|
|```codename_apt_codename_map```|Maps actual codename to apt codename to use|```codename_apt_codename_map_object```|

### ```codename_apt_codename_map_object```

|Variable|Description|Default|
|---|---|---|
|```release_codename```|Actual codename|_e.g._ jessie|
|```use_apt_codename```|Use codename|_e.g._ xenial|

## Dependencies

- none

## Example Playbook

    - hosts: servers
      roles:
         - { role: jpnewman.java, tags: ["init"] }

## License

MIT / BSD

## Author Information

John Paul Newman
