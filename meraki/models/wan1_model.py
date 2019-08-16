# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Wan1Model(object):

    """Implementation of the 'Wan1' model.

    WAN 1 settings

    Attributes:
        static_gateway_ip (string): The IP of the gateway on the WAN.
        static_dns (list of string): Up to two DNS IPs.
        vlan (int): The VLAN that management traffic should be tagged with.
            Applies whether usingStaticIp is true or false.
        wan_enabled (WanEnabledEnum): Enable or disable the interface (only
            for MX devices). Valid values are 'enabled', 'disabled', and 'not
            configured'.
        static_ip (string): The IP the device should use on the WAN.
        static_subnet_mask (string): The subnet mask for the WAN.
        using_static_ip (bool): Configue the interface to have static IP
            settings or use DHCP.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "static_gateway_ip":'staticGatewayIp',
        "static_dns":'staticDns',
        "vlan":'vlan',
        "wan_enabled":'wanEnabled',
        "static_ip":'staticIp',
        "static_subnet_mask":'staticSubnetMask',
        "using_static_ip":'usingStaticIp'
    }

    def __init__(self,
                 static_gateway_ip=None,
                 static_dns=None,
                 vlan=None,
                 wan_enabled=None,
                 static_ip=None,
                 static_subnet_mask=None,
                 using_static_ip=None):
        """Constructor for the Wan1Model class"""

        # Initialize members of the class
        self.static_gateway_ip = static_gateway_ip
        self.static_dns = static_dns
        self.vlan = vlan
        self.wan_enabled = wan_enabled
        self.static_ip = static_ip
        self.static_subnet_mask = static_subnet_mask
        self.using_static_ip = using_static_ip


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
        static_gateway_ip = dictionary.get('staticGatewayIp')
        static_dns = dictionary.get('staticDns')
        vlan = dictionary.get('vlan')
        wan_enabled = dictionary.get('wanEnabled')
        static_ip = dictionary.get('staticIp')
        static_subnet_mask = dictionary.get('staticSubnetMask')
        using_static_ip = dictionary.get('usingStaticIp')

        # Return an object of this model
        return cls(static_gateway_ip,
                   static_dns,
                   vlan,
                   wan_enabled,
                   static_ip,
                   static_subnet_mask,
                   using_static_ip)


