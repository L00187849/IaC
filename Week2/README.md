# IaC


# Title: Week 2 Notes - Desktop Virtualization




### Remote Connections

**RDP** - Remote desktop Protocol pre-installed in Windows
**SSH** - Secure shell for Linux devices 
**Telnet** - Older Version, obsolete due to security concerns



### Virtualization
### Tools mentioned
**VMware Workstation** - more advanced, feature-rich.
**Hyper-V (Windows)** – built-in virtualization tool for windows Education and Pro, simpler but functional.




### Building A virtual machine
Creates a new VM from the Ubuntu 24.04 Server ISO.
Naming scheme is consistent  (e.g., Ubuntu2404-server, Ubuntu2404-web1).
A VM has
- a configuration file that shows the CPU, RAM and network
- a virtual hard disk (VHD) is created and stores the OS and data.
- Dynamic Memory lets VMs share RAM from the host machine.
- Uses the Default Switch to give the VM internet via NAT





# Week 2 Notes - Snapshots and Clones

Explains the different files extensions / file types in the folder that your VM will be installed.

- .vmx file is the virtual machines configuration file where you can manually edit hardware settings for your VM.

- .vmdk file is the actual VM itself as a complete file.

- .vmem file is the Virtual memory of the VM when its running. 


# Snapshot
A (VM) snapshot is a point-in-time copy of a VM's complete state, including its memory, disk, and settings. This allows you to quickly revert the VM to that exact state if a change causes a problem, or to use it as a starting point for a new VM

He explains that the snapshot feature can be used, if something goes wrong i.e. updates caused an issue with your VM you can roll back.


A catch with snapshots - 
The more snapshots you have, the more CBT delta fills up, the slower your storage, the longer (and more painful) it is to remove the snapshots. 


The delta files copy's back over the VM and the delta files gets erased

The snapshot increases in size the more you work on the VM until you either use to go back to the snapshot.

### Full Clone
Shows how to clone a VM, and there is an option to clone from a snapshot
To make a Golden image, build the VM and then clone it, and never use the golden image.

 
Another type of Clone is a linked clone 

- Linked Clone 
- Parent(Full VM)
- Child (Delta File)

Use case for Linked clone if you want to use multiple VM's for short period of time.
