# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.dhcp_option_model
import meraki.models.reserved_ip_range_model

class UpdateNetworkVlanModel(object):

    """Implementation of the 'updateNetworkVlan' model.

    TODO: type model description here.

    Attributes:
        dns_nameservers (string): The DNS nameservers used for DHCP responses,
            either "upstream_dns", "google_dns", "opendns", or a newline
            seperated string of IP addresses or domain names
        subnet (string): The subnet of the VLAN
        dhcp_handling (string): The appliance's handling of DHCP requests on
            this VLAN. One of: "Run a DHCP server", "Relay DHCP to another
            server", or "Do not respond to DHCP requests"
        dhcp_options (list of DhcpOptionModel): The list of DHCP options that
            will be included in DHCP responses. Each object in the list should
            have "code", "type", and "value" properties.
        dhcp_boot_options_enabled (bool): Use DHCP boot options specified in
            other properties
        dhcp_boot_next_server (string): DHCP boot option to direct boot
            clients to the server to load the boot file from
        fixed_ip_assignments (object): The DHCP fixed IP assignments on the
            VLAN. This should be an object that contains mappings from MAC
            addresses to objects that themselves each contain "ip" and "name"
            string fields. See the sample request/response for more details.
        dhcp_lease_time (string): The term of DHCP leases if the appliance is
            running a DHCP server on this VLAN. One of: "30 minutes", "1
            hour", "4 hours", "12 hours", "1 day", "1 week".
        vpn_nat_subnet (string): The translated VPN subnet if VPN and VPN
            subnet translation are enabled on the VLAN
        dhcp_relay_server_ips (list of string): The IPs of the DHCP servers
            that DHCP requests should be relayed to
        name (string): The name of the VLAN
        appliance_ip (string): The local IP of the appliance on the VLAN
        dhcp_boot_filename (string): DHCP boot option for boot filename
        reserved_ip_ranges (list of ReservedIpRangeModel): The DHCP reserved
            IP ranges on the VLAN

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dns_nameservers":'dnsNameservers',
        "subnet":'subnet',
        "dhcp_handling":'dhcpHandling',
        "dhcp_options":'dhcpOptions',
        "dhcp_boot_options_enabled":'dhcpBootOptionsEnabled',
        "dhcp_boot_next_server":'dhcpBootNextServer',
        "fixed_ip_assignments":'fixedIpAssignments',
        "dhcp_lease_time":'dhcpLeaseTime',
        "vpn_nat_subnet":'vpnNatSubnet',
        "dhcp_relay_server_ips":'dhcpRelayServerIps',
        "name":'name',
        "appliance_ip":'applianceIp',
        "dhcp_boot_filename":'dhcpBootFilename',
        "reserved_ip_ranges":'reservedIpRanges'
    }

    def __init__(self,
                 dns_nameservers=None,
                 subnet=None,
                 dhcp_handling=None,
                 dhcp_options=None,
                 dhcp_boot_options_enabled=None,
                 dhcp_boot_next_server=None,
                 fixed_ip_assignments=None,
                 dhcp_lease_time=None,
                 vpn_nat_subnet=None,
                 dhcp_relay_server_ips=None,
                 name=None,
                 appliance_ip=None,
                 dhcp_boot_filename=None,
                 reserved_ip_ranges=None):
        """Constructor for the UpdateNetworkVlanModel class"""

        # Initialize members of the class
        self.dns_nameservers = dns_nameservers
        self.subnet = subnet
        self.dhcp_handling = dhcp_handling
        self.dhcp_options = dhcp_options
        self.dhcp_boot_options_enabled = dhcp_boot_options_enabled
        self.dhcp_boot_next_server = dhcp_boot_next_server
        self.fixed_ip_assignments = fixed_ip_assignments
        self.dhcp_lease_time = dhcp_lease_time
        self.vpn_nat_subnet = vpn_nat_subnet
        self.dhcp_relay_server_ips = dhcp_relay_server_ips
        self.name = name
        self.appliance_ip = appliance_ip
        self.dhcp_boot_filename = dhcp_boot_filename
        self.reserved_ip_ranges = reserved_ip_ranges


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        dns_nameservers = dictionary.get('dnsNameservers')
        subnet = dictionary.get('subnet')
        dhcp_handling = dictionary.get('dhcpHandling')
        dhcp_options = None
        if dictionary.get('dhcpOptions') != None:
            dhcp_options = list()
            for structure in dictionary.get('dhcpOptions'):
                dhcp_options.append(meraki.models.dhcp_option_model.DhcpOptionModel.from_dictionary(structure))
        dhcp_boot_options_enabled = dictionary.get('dhcpBootOptionsEnabled')
        dhcp_boot_next_server = dictionary.get('dhcpBootNextServer')
        fixed_ip_assignments = dictionary.get('fixedIpAssignments')
        dhcp_lease_time = dictionary.get('dhcpLeaseTime')
        vpn_nat_subnet = dictionary.get('vpnNatSubnet')
        dhcp_relay_server_ips = dictionary.get('dhcpRelayServerIps')
        name = dictionary.get('name')
        appliance_ip = dictionary.get('applianceIp')
        dhcp_boot_filename = dictionary.get('dhcpBootFilename')
        reserved_ip_ranges = None
        if dictionary.get('reservedIpRanges') != None:
            reserved_ip_ranges = list()
            for structure in dictionary.get('reservedIpRanges'):
                reserved_ip_ranges.append(meraki.models.reserved_ip_range_model.ReservedIpRangeModel.from_dictionary(structure))

        # Return an object of this model
        return cls(dns_nameservers,
                   subnet,
                   dhcp_handling,
                   dhcp_options,
                   dhcp_boot_options_enabled,
                   dhcp_boot_next_server,
                   fixed_ip_assignments,
                   dhcp_lease_time,
                   vpn_nat_subnet,
                   dhcp_relay_server_ips,
                   name,
                   appliance_ip,
                   dhcp_boot_filename,
                   reserved_ip_ranges)


