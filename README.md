# Netconf Fix Script

## Description
This Python script logs into a network device via SSH, toggles the `netconf-yang` feature off and then back on, and saves the configuration.

Specifically, it performs the following actions:

1. Enter configuration mode.
2. Disable `netconf-yang`.
3. Save the configuration.
4. Re-enable `netconf-yang`.
5. Save the configuration again.

The script is fully interactive and prompts the user for:

- Device IP address
- Username
- Password
- Enable (secret) password (if applicable)

---

# Netconf Fix Script

This script logs into a network device, disables and re-enables **NETCONF-YANG**, and saves the configuration.  
It is useful for resetting NETCONF functionality on Cisco devices.

---

## Installation & Setup

You can install this tool in two ways:

### Option 1: Clone from GitHub (recommended)
```bash
# Clone the repository
git clone https://github.com/ChrisWilson2019/NetConf-Fix-Script.git
cd NetConf-Fix-Script

# (Optional) Create a Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt


## Prerequisites

The script requires **Python 3** and the **Netmiko** library to interact with network devices.

### Installing Netmiko

If you don’t have Netmiko installed, use `pip`:

```bash
# Install for current user
python3 -m pip install --user netmiko

# Or system-wide (requires sudo)
sudo python3 -m pip install netmiko# Netconf Fix Script

## Description
This Python script logs into a network device via SSH, toggles the `netconf-yang` feature off and then back on, and saves the configuration.

Specifically, it performs the following actions:

1. Enter configuration mode.
2. Disable `netconf-yang`.
3. Save the configuration.
4. Re-enable `netconf-yang`.
5. Save the configuration again.

The script is fully interactive and prompts the user for:

- Device IP address
- Username
- Password
- Enable (secret) password (if applicable)

---

## Prerequisites

The script requires **Python 3** and the **Netmiko** library to interact with network devices.

### Installing Netmiko

If you don’t have Netmiko installed, use `pip`:

```bash
# Install for current user
python3 -m pip install --user netmiko

# Or system-wide (requires sudo)
sudo python3 -m pip install netmiko

#Verify installation
python3 -m pip show netmiko

#Usage
1. Open terminal and navigate to the directory containing netconf_fix_script.py
2. Run the script
3. Enter the requested information when prompted
	- Device IP
	- Username
	- Password
	- Enabel Password(optional)
4. The scrip will execute the commands and print the output for the review

#Creating a Terminal Alias

You can create an alias to run the script from anywhere, like a native command:

1. Make the script executable:
chmod +x ~/.local/bin/Netconf_Fix/netconf_fix_script.py

2. Opn your shell configuration file
# For bash
nano ~/.bashrc

# For zsh
nano ~/.zshrc

3. Add this line at the end of the file 
alias netconf_fix='python3 ~/.local/bin/Netconf_Fix/netconf_fix_script.py'

4. Apply the changes
source ~/.bashrc
or
source ~/.zshrc

5. Now you can run the script from anywhere with
netconf_fix


#Notes
- Tested on Cisco IOS devices; adjust the device_type in the script for other platforms.
- Ensure SSH is enabled on the target device.
- Passwords are not stored by the script for security reasons.
