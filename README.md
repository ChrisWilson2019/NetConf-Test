# Netconf Scripts

This repository contains two scripts for testing and troubleshooting NETCONF connectivity on network devices.

---

## 1. Netconf Test Script
### Description
This script tests NETCONF connectivity to a network device.

It performs the following steps:
1. Prompts the user to enter an IP address of the device.
2. Checks if the device is reachable on TCP port 830 (NETCONF port).
3. If the port is open, initiates a NETCONF SSH session to the device.
4. If the port is closed or the device is unreachable, provides an error message.

### Usage
```bash
chmod +x Netconf
./Netconf

When prompted, enter the device IP address.

Requirements

nc (netcat) must be installed for port checking.

SSH access to the target device with NETCONF enabled on port 830.

Default SSH username is prime (modify the script if needed).

###Netconf Fix Script
Installation
sudo python3 -m pip install netmiko
python3 -m pip show netmiko   # verify installation


### Usage

Open terminal and navigate to the directory containing netconf_fix_script.py

Run the script:
python3 netconf_fix_script.py

Enter the requested information when prompted:

Device IP

Username

Password

Enable Password (optional)

The script will execute the commands and print the output for review.

### Creating a Terminal Alias

Creating a Terminal Alias

To run the script from anywhere like a native command:

Make the script executable:
chmod +x ~/.local/bin/Netconf_Fix/netconf_fix_script.py

Edit you shell config file:
nano ~/.bashrc    # bash
nano ~/.zshrc     # zsh

Add:
alias netconf_fix='python3 ~/.local/bin/Netconf_Fix/netconf_fix_script.py'

Apply changes:
source ~/.bashrc # or ~/.zshrc

Now you can run:
netconf_fix

Notes

Tested on Cisco IOS devices (adjust device_type in the script for others).

Ensure SSH is enabled on the target device.

Passwords are not stored for security reasons.

~
