# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Rule7Model(object):

    """Implementation of the 'Rule7' model.

    TODO: type model description here.

    Attributes:
        src_cidr (string): Comma-separated list of source IP address(es) (in
            IP or CIDR notation), or 'any' (note: FQDN not supported for
            source addresses)
        protocol (string): The type of protocol (must be 'tcp', 'udp', 'icmp'
            or 'any')
        syslog_enabled (bool): Log this rule to syslog (true or false, boolean
            value) - only applicable if a syslog has been configured
            (optional)
        dest_port (string): Comma-separated list of destination port(s)
            (integer in the range 1-65535), or 'any'
        comment (string): Description of the rule (optional)
        src_port (string): Comma-separated list of source port(s) (integer in
            the range 1-65535), or 'any'
        dest_cidr (string): Comma-separated list of destination IP address(es)
            (in IP or CIDR notation), fully-qualified domain names (FQDN) or
            'any'
        policy (string): 'allow' or 'deny' traffic specified by this rule

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "src_cidr":'srcCidr',
        "protocol":'protocol',
        "dest_cidr":'destCidr',
        "policy":'policy',
        "syslog_enabled":'syslogEnabled',
        "dest_port":'destPort',
        "comment":'comment',
        "src_port":'srcPort'
    }

    def __init__(self,
                 src_cidr=None,
                 protocol=None,
                 dest_cidr=None,
                 policy=None,
                 syslog_enabled=None,
                 dest_port=None,
                 comment=None,
                 src_port=None):
        """Constructor for the Rule7Model class"""

        # Initialize members of the class
        self.src_cidr = src_cidr
        self.protocol = protocol
        self.syslog_enabled = syslog_enabled
        self.dest_port = dest_port
        self.comment = comment
        self.src_port = src_port
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
        src_cidr = dictionary.get('srcCidr')
        protocol = dictionary.get('protocol')
        dest_cidr = dictionary.get('destCidr')
        policy = dictionary.get('policy')
        syslog_enabled = dictionary.get('syslogEnabled')
        dest_port = dictionary.get('destPort')
        comment = dictionary.get('comment')
        src_port = dictionary.get('srcPort')

        # Return an object of this model
        return cls(src_cidr,
                   protocol,
                   dest_cidr,
                   policy,
                   syslog_enabled,
                   dest_port,
                   comment,
                   src_port)


