# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateDeviceSwitchPortModel(object):

    """Implementation of the 'updateDeviceSwitchPort' model.

    TODO: type model description here.

    Attributes:
        stp_guard (string): The state of the STP guard ("disabled", "Root
            guard", "BPDU guard", "Loop guard")
        port_schedule_id (string): The ID of the port schedule. A value of
            null will clear the port schedule.
        rstp_enabled (bool): The rapid spanning tree protocol status
        isolation_enabled (bool): The isolation status of the switch port
        mtype (string): The type of the switch port ("access" or "trunk")
        enabled (bool): The status of the switch port
        tags (string): The tags of the switch port
        allowed_vlans (string): The VLANs allowed on the switch port. Only
            applicable to trunk ports.
        access_policy_number (int): The number of the access policy of the
            switch port. Only applicable to access ports.
        link_negotiation (string): The link speed for the switch port
        vlan (int): The VLAN of the switch port
        voice_vlan (int): The voice VLAN of the switch port. Only applicable
            to access ports.
        poe_enabled (bool): The PoE status of the switch port
        name (string): The name of the switch port

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "stp_guard":'stpGuard',
        "port_schedule_id":'portScheduleId',
        "rstp_enabled":'rstpEnabled',
        "isolation_enabled":'isolationEnabled',
        "mtype":'type',
        "enabled":'enabled',
        "tags":'tags',
        "allowed_vlans":'allowedVlans',
        "access_policy_number":'accessPolicyNumber',
        "link_negotiation":'linkNegotiation',
        "vlan":'vlan',
        "voice_vlan":'voiceVlan',
        "poe_enabled":'poeEnabled',
        "name":'name'
    }

    def __init__(self,
                 stp_guard=None,
                 port_schedule_id=None,
                 rstp_enabled=None,
                 isolation_enabled=None,
                 mtype=None,
                 enabled=None,
                 tags=None,
                 allowed_vlans=None,
                 access_policy_number=None,
                 link_negotiation=None,
                 vlan=None,
                 voice_vlan=None,
                 poe_enabled=None,
                 name=None):
        """Constructor for the UpdateDeviceSwitchPortModel class"""

        # Initialize members of the class
        self.stp_guard = stp_guard
        self.port_schedule_id = port_schedule_id
        self.rstp_enabled = rstp_enabled
        self.isolation_enabled = isolation_enabled
        self.mtype = mtype
        self.enabled = enabled
        self.tags = tags
        self.allowed_vlans = allowed_vlans
        self.access_policy_number = access_policy_number
        self.link_negotiation = link_negotiation
        self.vlan = vlan
        self.voice_vlan = voice_vlan
        self.poe_enabled = poe_enabled
        self.name = name


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
        stp_guard = dictionary.get('stpGuard')
        port_schedule_id = dictionary.get('portScheduleId')
        rstp_enabled = dictionary.get('rstpEnabled')
        isolation_enabled = dictionary.get('isolationEnabled')
        mtype = dictionary.get('type')
        enabled = dictionary.get('enabled')
        tags = dictionary.get('tags')
        allowed_vlans = dictionary.get('allowedVlans')
        access_policy_number = dictionary.get('accessPolicyNumber')
        link_negotiation = dictionary.get('linkNegotiation')
        vlan = dictionary.get('vlan')
        voice_vlan = dictionary.get('voiceVlan')
        poe_enabled = dictionary.get('poeEnabled')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(stp_guard,
                   port_schedule_id,
                   rstp_enabled,
                   isolation_enabled,
                   mtype,
                   enabled,
                   tags,
                   allowed_vlans,
                   access_policy_number,
                   link_negotiation,
                   vlan,
                   voice_vlan,
                   poe_enabled,
                   name)


