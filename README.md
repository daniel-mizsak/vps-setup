## <div align="center"> ☁️ vps-setup</div>

<div align="center">
<a href="https://github.com/daniel-mizsak/vps-setup/actions/workflows/ci.yml" target="_blank"><img src="https://github.com/daniel-mizsak/vps-setup/actions/workflows/ci.yml/badge.svg" alt="build status"></a>
<a href="https://results.pre-commit.ci/latest/github/daniel-mizsak/vps-setup/main" target="_blank"><img src="https://results.pre-commit.ci/badge/github/daniel-mizsak/vps-setup/main.svg" alt="pre-commit.ci status"></a>
<a href="https://img.shields.io/github/license/daniel-mizsak/vps-setup" target="_blank"><img src="https://img.shields.io/github/license/daniel-mizsak/vps-setup" alt="license"></a>
</div>

## Overview
The deployed web application **should** be available at [mlops.top](https://mlops.top).

This repository was heavily inspired by [Dreams of Codes](https://www.youtube.com/@dreamsofcode)'s [Setting up a production ready VPS](https://youtu.be/F-9KWQByeU0?si=v7OE4IBhpqrzaD1R) video.\
The idea was to automate the whole dockerized deployment process using `ansible`, while making minor improvements to the original setup.

Additional solutions where the deployment is done using `k3s` and `podman` were also created. All methods implement the same features.

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

Rename the example inventory file and replace the placeholder with your VPS's IP address.
```bash
mv example.inventory.ini inventory.ini
```

The `vps-setup` playbook assumes that your public SSH key is already added to the root user's `~/.ssh/authorized_keys` file. Make sure that this is the case.\
Next, set the hashed password under `vars` in the `vps-setup.yml` file. [Ansible's guide on generating hashed password](https://docs.ansible.com/ansible/latest/reference_appendices/faq.html#how-do-i-generate-encrypted-passwords-for-the-user-module).

The `vps-setup` playbook can be run with the following command:
```bash
ansible-playbook vps-setup.yml
```

It is recommended to reboot the machine after the playbook has finished running.\
(Since I often do slight modifications/experiments on the VPS, I usually also [setup my terminal](https://github.com/daniel-mizsak/macos-setup/blob/main/docs/ubuntu-terminal-setup.md) for a more comfortable experience. This is completely optional.)

List of changes made to the original vps setup:
- Did not disable `UsePAM` in `/etc/ssh/sshd_config` as I am not exactly sure when it is needed
- Did not modify the `/etc/ssh/sshd_config.d/50-cloud-init.conf` file as it should be overwritten by the other file in the directory
- Added some additional apt packages, most importantly `fail2ban` with the default configuration

## Docker setup
Since the requirements are identical to `vps-setup`, the application setup using `docker` can be run by:
```bash
ansible-playbook fastapi-app-setup-docker.yml
```

List of my changes:
- Use `python` webapp instead of `go`. This can easily be modified in the `compose.yml` file under `files/docker` in the repository. The database was also dropped.
- Moved the general `traefik` configurations into a separate file resulting in a cleaner `compose.yml` file

## K3S setup
Run the `k3s-setup` playbook with the following command:
```bash
ansible-playbook fastapi-app-setup-k3s.yml
```

Unfortunately, I found no trivial solution on making the cluster automatically pull down the latest image from the registry, like how `watchtower` does.

Also, pay attention to the default `ufw` settings applied during the `vps-setup`, as it might block so features of `k3s`.


## Podman setup
The main advantage of using `podman` instead of `docker`, is that by default it is considered more secure.\
Run the `podman-setup` playbook with the following command:
```bash
ansible-playbook fastapi-app-setup-podman.yml
```

Unfortunately, similarly to `k3s`, the automated deployment process is not working.\
It is a limitation of `podman`, but [should be fixed](https://github.com/containrrr/watchtower/issues/1060) in the future.
