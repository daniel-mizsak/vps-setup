## <div align="center"> ☁️ vps-setup</div>

<div align="center">
<a href="https://github.com/daniel-mizsak/vps-setup/actions/workflows/ci.yml" target="_blank"><img src="https://github.com/daniel-mizsak/vps-setup/actions/workflows/ci.yml/badge.svg" alt="build status"></a>
<a href="https://results.pre-commit.ci/latest/github/daniel-mizsak/vps-setup/main" target="_blank"><img src="https://results.pre-commit.ci/badge/github/daniel-mizsak/vps-setup/main.svg" alt="pre-commit.ci status"></a>
<a href="https://img.shields.io/github/license/daniel-mizsak/vps-setup" target="_blank"><img src="https://img.shields.io/github/license/daniel-mizsak/vps-setup" alt="license"></a>
</div>

## Overview
This repository was heavily inspired by [Dreams of Codes](https://www.youtube.com/@dreamsofcode)'s [Setting up a production ready VPS](https://youtu.be/F-9KWQByeU0?si=v7OE4IBhpqrzaD1R) video.

The idea was to automate the whole process using `ansible`, while making some minor improvements to the original setup.\
I also created a solution where the deployment is done using a `k3s` kubernetes cluster. Both methods should implement roughly the same features.

## VPS Setup
After cloning the repository create a python virtual environment and install the requirements:
```bash
python -m venv --upgrade-deps .venv
source .venv/bin/activate
```
```bash
cd ansible
pip install --requirement requirements.txt
```

Rename the inventory file and add your VPS's IP address to it:
```bash
mv example.inventory.ini inventory.ini
```

The `vps-setup` playbook assumes that your public SSH key is already added to the root user's `authorized_keys`. Make sure that this is the case.\
Next, set the hashed password in the `vps-setup.yml` file. [Ansible's guide on generating hashed password](https://docs.ansible.com/ansible/latest/reference_appendices/faq.html#how-do-i-generate-encrypted-passwords-for-the-user-module).

The `vps-setup` playbook can be run with the following command:
```bash
ansible-playbook vps-setup.yml --inventory inventory.ini
```

It is recommended to reboot the machine after the playbook has finished running.

## Docker setup

## K3S setup
