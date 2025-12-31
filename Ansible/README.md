# Ansible Automation and Configuration Management

## Description
This folder contains Ansible laboratory exercises completed as part of the *Infrastructure as Code* module. The focus of this work is to develop practical skills in configuration management and automation using Ansible within a virtualised Linux environment. The laboratory demonstrates how Infrastructure as Code (IaC) principles can be applied to manage multiple systems consistently and at scale.

The work covers system preparation, static networking, SSH key-based authentication, inventory management, ad-hoc command execution, and playbook-driven automation. All tasks are documented using industry-standard practices and align with modern DevOps workflows.

---

## Contents

### Ansible Configuration
- **Static Network Configuration** – Configures static IPv4 addressing using Netplan and disables cloud-init network overrides.  
- **Hostname Configuration** – Assigns persistent hostnames to all managed nodes.  
- **Host Resolution** – Implements local name resolution via `/etc/hosts` in the absence of a DNS service.  
- **SSH Key Authentication** – Establishes secure, passwordless access between the control node and managed hosts.  

### Inventory Management
- **YAML Inventory File** – Defines managed hosts using structured groupings.  
- **Group Variables** – Specifies interpreter paths and shared configuration values.  
- **Inventory Validation** – Verifies configuration using `ansible-inventory --list -y`.  

### Ad-Hoc Commands
- **Connectivity Testing** – Uses the Ansible `ping` module to validate SSH and Python availability.  
- **System Auditing** – Executes commands such as `df -h` across all hosts to analyse system state.  

### Playbooks
- **System Updates** – Performs distribution upgrades, detects reboot requirements, and removes unused dependencies.  
- **Web Server Deployment** – Installs and enables Apache on designated web servers.  
- **Database Deployment** – Installs and configures MariaDB on database servers.  

### Supporting Material
- **Screenshots** – Evidence of configuration steps and command execution.  
- **YAML Files** – Inventory files and playbooks used during the laboratory.  
- **Appendices** – Configuration files and scripts referenced in the academic report.

---

## Dependencies
- Ubuntu Server 24.04 (managed nodes)  
- Ubuntu Desktop 24.04 (Ansible control node)  
- Ansible (latest stable release via PPA)  
- OpenSSH  
- Python 3.10+  
- VMware Workstation or equivalent hypervisor  
- Git and GitHub  

---

## Testing Strategy
- Configuration validated through:
  - SSH login verification
  - Ansible `ping` module
  - Inventory listing and group resolution
  - Ad-hoc command execution
- Playbooks tested for idempotence, ensuring systems are modified only when required.
- Full end-to-end execution was limited by Azure Lab infrastructure constraints.

---

## Limitations
Due to restrictions within the Azure Lab environment, it was not possible to deploy and test multiple interconnected virtual machines. As a result, playbook execution across multiple managed nodes could not be fully validated within Azure. This limitation was environmental rather than technical and does not affect the validity of the documented configuration or methodology.

---

## Author
- **LNumber:** L00187849  
- **Name:** Liam Saunders  
- **Course:** PG Dip Cloud Technologies  
- **Module:** Infrastructure as Code (IaC)

---

## License
This repository is submitted as part of academic coursework.  
Reuse or redistribution must comply with ATU academic integrity and assessment regulations.
