Netconf Test Script
==================

Description:
------------
This script is designedto test NETCONF connectivity to a network device.

It performs the following steps:
1. Prompts the user to enter an IP address of the device.
2. Checks if the device is reachable on TCP port 830 (NETCONF port).
3. If the port is open, initiates a NETCONF SSH session to the device.
4. If the port is closed or the device is unreachable, provides an error message.

Usage:
------
1. Make sure the script is executable:
   chmod +x Netconf

2. Run the script:
   ./Netconf

3. Enter the IP address of the device when prompted.

Requirements:
-------------
- `nc` (netcat) must be installed for port checking.
- SSH access to the target device with NETCONF enabled on port 830.

Notes:
------
- Ensure you have the correct credentials for the device.
- The script currently uses 'prime' as the SSH username. Modify if necessary.
