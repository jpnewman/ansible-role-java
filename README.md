# jpnewman.java

[![Ansible Role](https://img.shields.io/ansible/role/9594.svg?maxAge=2592000)](https://galaxy.ansible.com/jpnewman/java/)
[![Build Status](https://travis-ci.org/jpnewman/ansible-role-java.svg?branch=master)](https://travis-ci.org/jpnewman/ansible-role-java)

This is an Ansible role to install Oracle Java 8 or OpenJDK.

Oracle Java 8 can be installed via apt-get, direct download, or local files.

## Requirements

Ansible 2.x

## Role Variables

|Variable|Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Default|
|---|---|---|
|```apt_cache_valid_time```|Apt Cache Valid Time|600|
|```java_installer_type```|Should be one of the following values: -<br />- ```oracle_ppa```<br />- ```oracle_url```<br />- ```oracle_file```<br />- ```openjdk```|```oracle_ppa```|
|```install_java```|If ```false``` Java is only setup, but not installed|"true"|
|```apt_java_state```|Ansible apt module state|present|
|```codename_apt_codename_map```|Maps actual codename to apt codename to use. Used by mode ```oracle_ppa```|```codename_apt_codename_map_object```|

### ```codename_apt_codename_map_object```

|Variable|Description|Default|
|---|---|---|
|```release_codename```|Actual codename|_e.g._ jessie|
|```use_apt_codename```|Use codename|_e.g._ xenial|

## Oracle Java PPA ```oracle_ppa```

Install Oracle Java JCE from Apt PPA.

|Variable|Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Default|
|---|---|---|
|```apt_java_repo```|Apt Repo|ppa:webupd8team/java|
|```apt_java_package```||oracle-java8-installer|

## Oracle Java URL ```oracle_url```

Install Oracle Java from URL.

|Variable|Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Default|
|---|---|---|
|```oracle_java_url_file```||jdk-8u161-linux-x64.tar.gz|
|```oracle_java_url_path```||http://download.oracle.com/otn-pub/java/jdk/8u161-b12/2f38c3b165be4555a1fa6e98c45e0808/|
|```oracle_java_url_header```||"Cookie:oraclelicense=a"|
|```oracle_java_extract_folder```||```jdk1.8.0_161```|
|```oracle_java_jvm_dir```||/usr/lib/jvm|
|```oracle_java_jvm_folder```||java-8-oracle|
|```oracle_java_install_dir```||```"{{ oracle_java_jvm_dir }}/{{ oracle_java_jvm_folder }}"```|
|```oracle_java_download_folder```||/tmp|
|```oracle_java_usr_bin_dir```||/usr/bin|
|```oracle_java_link_exe```||- java<br />- javac<br />- jar<br />- jrunscript|

## Oracle Java URL, JCE

Install Oracle Java JCE from URL.

|Variable|Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Default|
|---|---|---|
|```oracle_java_jce_install```||true|
|```oracle_java_jce_url_file```||jce_policy-8.zip|
|```oracle_java_jce_url_path```||http://download.oracle.com/otn-pub/java/jce/8/|
|```oracle_java_jce_extract_folder```||UnlimitedJCEPolicyJDK8|

## Oracle Java File

Install Oracle Java from local files.

To use download installers from <http://www.oracle.com/technetwork/java/javase/downloads/index.html> and place in files folder.

|Variable|Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Default|
|---|---|---|
|```oracle_java_file```||jdk-8u161-linux-x64.tar.gz|
|```oracle_java_jce_file```||```jce_policy-8.zip```|

## OpenJDK ```openjdk```

Install OpenJDK.

|Variable|Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Default|
|---|---|---|
|```apt_openjdk_packages```||```codename_ppa_map_object```|

### ```codename_ppa_map_object```

|Variable|Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Default|
|---|---|---|
|```use_apt_codenames```|List of Codenames||
|```apt_repos```|Apt Repo||
|```use_apt_packages```|Packages to install||
|```default_release```|Apt Default Releases||

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
