# jpnewman.java

[![Ansible Role](https://img.shields.io/ansible/role/9594.svg?maxAge=2592000)](https://galaxy.ansible.com/jpnewman/java/)
[![Build Status](https://travis-ci.org/jpnewman/ansible-role-java.svg?branch=master)](https://travis-ci.org/jpnewman/ansible-role-java)

This is an Ansible role to install Java 8

## Requirements

Ansible 2.x

## Role Variables

|Variable|Description|Default|
|---|---|---|
|```apt_cache_valid_time```||600|
|```apt_java_repo```||ppa:webupd8team/java|
|```apt_java_package```||oracle-java8-installer|
|```install_java```||"true"|

Variables specific to Debian:

|Variable|Description|Default|
|---|---|---|
|```apt_java_codename```|Supply series codename for Ubuntu PPA|xenial|

## Dependencies

none

## Example Playbook

    - hosts: servers
      roles:
         - { role: jpnewman.java, tags: ["init"] }

## License

MIT / BSD

## Author Information

John Paul Newman
