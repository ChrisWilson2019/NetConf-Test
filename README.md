# Netconf Test Script

This repository contains a Python script to test NETCONF connectivity on network devices.

---

## Description

`netconf_test_script.py` performs the following:

1. Prompts the user to enter the IP address of a network device.
2. Checks if the device is reachable on TCP port 830 (the default NETCONF port).
3. If the port is open, initiates a NETCONF SSH session.
4. If the device is unreachable or the port is closed, it provides an error message.

---

## Description

`netconf_test_script.py` performs the following:

1. Prompts the user to enter the IP address of a network device.
2. Checks if the device is reachable on TCP port 830 (the default NETCONF port).3. If the port is open, initiates a NETCONF SSH session.
4. If the device is unreachable or the port is closed, it provides an error message.

---

## Usage

1. Make sure the script is executable:
./netconf_test_script.py

2. Run the script:
./netconf_test_script.py

## Create Terminal Alias(Optional but recommended)

1. Move or copy the script to a folder in your PATH (e.g., ~/.local/bin):
cp netconf_test_script.py ~/.local/bin/

2. Edit your local shell configuration file:
nano ~/.bashrc   # for bash
nano ~/.zshrc    # for zsh
or
nvim ~/.bashrc   # for bash
nvim ~/.zshrc    # for zsh

3. Add this line at the end:
alias Netconf='python3 ~/.local/bin/netconf_test_script.py'

4. Apply the changes:
source ~/.bashrc   # or source ~/.zshrc

5. Now you can run the script from anywhere:
Netconf

## Requirements

1. nc(netcat) must be installed for the port checking
2. SSH access to the target device with NETCONF enabled on port 830
3. The script uses specified user as the SSH username(replace <username> with your username)

## Notes

1. Ensure you have the correct credentials for the device
2. Passwords are not stored by the script for security reasons


