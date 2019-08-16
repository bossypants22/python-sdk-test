# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Rule1Model(object):

    """Implementation of the 'Rule1' model.

    TODO: type model description here.

    Attributes:
        protocol (string): TCP or UDP
        local_port (string): A port or port ranges that will receive the
            forwarded traffic from the WAN
        uplink (string): The physical WAN interface on which the traffic will
            arrive ('internet1' or, if available, 'internet2' or 'both')
        allowed_ips (list of string): An array of ranges of WAN IP addresses
            that are allowed to make inbound connections on the specified
            ports or port ranges (or any)
        name (string): A descriptive name for the rule
        public_port (string): A port or port ranges that will be forwarded to
            the host on the LAN
        lan_ip (string): The IP address of the server or device that hosts the
            internal resource that you wish to make available on the WAN

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "protocol":'protocol',
        "local_port":'localPort',
        "uplink":'uplink',
        "allowed_ips":'allowedIps',
        "name":'name',
        "public_port":'publicPort',
        "lan_ip":'lanIp'
    }

    def __init__(self,
                 protocol=None,
                 local_port=None,
                 uplink=None,
                 allowed_ips=None,
                 name=None,
                 public_port=None,
                 lan_ip=None):
        """Constructor for the Rule1Model class"""

        # Initialize members of the class
        self.protocol = protocol
        self.local_port = local_port
        self.uplink = uplink
        self.allowed_ips = allowed_ips
        self.name = name
        self.public_port = public_port
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
        local_port = dictionary.get('localPort')
        uplink = dictionary.get('uplink')
        allowed_ips = dictionary.get('allowedIps')
        name = dictionary.get('name')
        public_port = dictionary.get('publicPort')
        lan_ip = dictionary.get('lanIp')

        # Return an object of this model
        return cls(protocol,
                   local_port,
                   uplink,
                   allowed_ips,
                   name,
                   public_port,
                   lan_ip)


