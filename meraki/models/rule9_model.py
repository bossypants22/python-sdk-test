# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Rule9Model(object):

    """Implementation of the 'Rule9' model.

    TODO: type model description here.

    Attributes:
        protocol (string): The type of protocol (must be 'tcp', 'udp', 'icmp'
            or 'any')
        dest_port (string): Comma-separated list of destination port(s)
            (integer in the range 1-65535), or 'any'
        comment (string): Description of the rule (optional)
        dest_cidr (string): Comma-separated list of destination IP address(es)
            (in IP or CIDR notation), fully-qualified domain names (FQDN) or
            'any'
        policy (string): 'allow' or 'deny' traffic specified by this rule

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "protocol":'protocol',
        "dest_cidr":'destCidr',
        "policy":'policy',
        "dest_port":'destPort',
        "comment":'comment'
    }

    def __init__(self,
                 protocol=None,
                 dest_cidr=None,
                 policy=None,
                 dest_port=None,
                 comment=None):
        """Constructor for the Rule9Model class"""

        # Initialize members of the class
        self.protocol = protocol
        self.dest_port = dest_port
        self.comment = comment
        self.dest_cidr = dest_cidr
        self.policy = policy


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
        dest_cidr = dictionary.get('destCidr')
        policy = dictionary.get('policy')
        dest_port = dictionary.get('destPort')
        comment = dictionary.get('comment')

        # Return an object of this model
        return cls(protocol,
                   dest_cidr,
                   policy,
                   dest_port,
                   comment)


