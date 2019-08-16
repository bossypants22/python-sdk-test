# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Rule3Model(object):

    """Implementation of the 'Rule3' model.

    TODO: type model description here.

    Attributes:
        protocol (string): Either of the following: 'tcp', 'udp', 'icmp-ping'
            or 'any'
        uplink (string): The physical WAN interface on which the traffic will
            arrive ('internet1' or, if available, 'internet2')
        destination_ports (string): An array of ports or port ranges that will
            be forwarded to the host on the LAN
        allowed_ips (string): An array of ranges of WAN IP addresses that are
            allowed to make inbound connections on the specified ports or port
            ranges, or 'any'
        name (string): A descriptive name for the rule
        allowed_inbound (list of object): The ports this mapping will provide
            access on, and the remote IPs that will be allowed access to the
            resource
        public_ip (string): The IP address that will be used to access the
            internal resource from the WAN
        lan_ip (string): The IP address of the server or device that hosts the
            internal resource that you wish to make available on the WAN

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "protocol":'protocol',
        "uplink":'uplink',
        "destination_ports":'destinationPorts',
        "allowed_ips":'allowedIps',
        "name":'name',
        "allowed_inbound":'allowedInbound',
        "public_ip":'publicIp',
        "lan_ip":'lanIp'
    }

    def __init__(self,
                 protocol=None,
                 uplink=None,
                 destination_ports=None,
                 allowed_ips=None,
                 name=None,
                 allowed_inbound=None,
                 public_ip=None,
                 lan_ip=None):
        """Constructor for the Rule3Model class"""

        # Initialize members of the class
        self.protocol = protocol
        self.uplink = uplink
        self.destination_ports = destination_ports
        self.allowed_ips = allowed_ips
        self.name = name
        self.allowed_inbound = allowed_inbound
        self.public_ip = public_ip
        self.lan_ip = lan_ip


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
        protocol = dictionary.get('protocol')
        uplink = dictionary.get('uplink')
        destination_ports = dictionary.get('destinationPorts')
        allowed_ips = dictionary.get('allowedIps')
        name = dictionary.get('name')
        allowed_inbound = dictionary.get('allowedInbound')
        public_ip = dictionary.get('publicIp')
        lan_ip = dictionary.get('lanIp')

        # Return an object of this model
        return cls(protocol,
                   uplink,
                   destination_ports,
                   allowed_ips,
                   name,
                   allowed_inbound,
                   public_ip,
                   lan_ip)


