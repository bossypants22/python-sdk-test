# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Rule10Model(object):

    """Implementation of the 'Rule10' model.

    TODO: type model description here.

    Attributes:
        protocol (string): 'tcp' or 'udp'
        port_rules (list of object): An array of associated forwarding rules
        local_port (string): Destination port of the forwarded traffic that
            will be sent from the MX to the specified host on the LAN. If you
            simply wish to forward the traffic without translating the port,
            this should be the same as the Public port
        uplink (string): The physical WAN interface on which the traffic will
            arrive ('internet1' or, if available, 'internet2')
        allowed_ips (string): Remote IP addresses or ranges that are permitted
            to access the internal resource via this port forwarding rule, or
            'any'
        name (string): A description of the rule
        public_port (string): Destination port of the traffic that is arriving
            on the WAN
        local_ip (string): Local IP address to which traffic will be
            forwarded
        public_ip (string): The IP address that will be used to access the
            internal resource from the WAN

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "protocol":'protocol',
        "port_rules":'portRules',
        "local_port":'localPort',
        "uplink":'uplink',
        "allowed_ips":'allowedIps',
        "name":'name',
        "public_port":'publicPort',
        "local_ip":'localIp',
        "public_ip":'publicIp'
    }

    def __init__(self,
                 protocol=None,
                 port_rules=None,
                 local_port=None,
                 uplink=None,
                 allowed_ips=None,
                 name=None,
                 public_port=None,
                 local_ip=None,
                 public_ip=None):
        """Constructor for the Rule10Model class"""

        # Initialize members of the class
        self.protocol = protocol
        self.port_rules = port_rules
        self.local_port = local_port
        self.uplink = uplink
        self.allowed_ips = allowed_ips
        self.name = name
        self.public_port = public_port
        self.local_ip = local_ip
        self.public_ip = public_ip


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
        port_rules = dictionary.get('portRules')
        local_port = dictionary.get('localPort')
        uplink = dictionary.get('uplink')
        allowed_ips = dictionary.get('allowedIps')
        name = dictionary.get('name')
        public_port = dictionary.get('publicPort')
        local_ip = dictionary.get('localIp')
        public_ip = dictionary.get('publicIp')

        # Return an object of this model
        return cls(protocol,
                   port_rules,
                   local_port,
                   uplink,
                   allowed_ips,
                   name,
                   public_port,
                   local_ip,
                   public_ip)


