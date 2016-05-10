# jpnewman.java

This is a Ansible role to installs Java 8

## Requirements

Ansible 2.x

## Role Variables

|Variable|Description|Default|
|---|---|---|
|```apt_cache_valid_time```||600|
|```apt_java_repo```||ppa:webupd8team/java|
|```apt_java_package```||oracle-java8-installer|
|```install_java```||"true"|

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
