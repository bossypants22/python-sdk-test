# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CreateOrganizationNetworkModel(object):

    """Implementation of the 'createOrganizationNetwork' model.

    TODO: type model description here.

    Attributes:
        name (string): The name of the new network
        time_zone (string): The timezone of the network. For a list of allowed
            timezones, please see the 'TZ' column in the table in <a
            target='_blank'
            href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'
            >this article.</a>
        disable_remote_status_page (bool): Disables access to the device
            status page (<a target='_blank'>http://[device's LAN IP])</a>.
            Optional. Can only be set if disableMyMerakiCom is set to false
        disable_my_meraki_com (bool): Disables the local device status pages
            (<a target='_blank' href='http://my.meraki.com/'>my.meraki.com,
            </a><a target='_blank' href='http://ap.meraki.com/'>ap.meraki.com,
            </a><a target='_blank'
            href='http://switch.meraki.com/'>switch.meraki.com, </a><a
            target='_blank'
            href='http://wired.meraki.com/'>wired.meraki.com</a>). Optional
            (defaults to false)
        mtype (string): The type of the new network. Valid types are wireless,
            appliance, switch, systemsManager, camera, or a space-separated
            list of those for a combined network.
        copy_from_network_id (string): The ID of the network to copy
            configuration from. Other provided parameters will override the
            copied configuration, except type which must match this network's
            type exactly.
        tags (string): A space-separated list of tags to be applied to the
            network

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "mtype":'type',
        "time_zone":'timeZone',
        "disable_remote_status_page":'disableRemoteStatusPage',
        "disable_my_meraki_com":'disableMyMerakiCom',
        "copy_from_network_id":'copyFromNetworkId',
        "tags":'tags'
    }

    def __init__(self,
                 name=None,
                 mtype=None,
                 time_zone=None,
                 disable_remote_status_page=None,
                 disable_my_meraki_com=None,
                 copy_from_network_id=None,
                 tags=None):
        """Constructor for the CreateOrganizationNetworkModel class"""

        # Initialize members of the class
        self.name = name
        self.time_zone = time_zone
        self.disable_remote_status_page = disable_remote_status_page
        self.disable_my_meraki_com = disable_my_meraki_com
        self.mtype = mtype
        self.copy_from_network_id = copy_from_network_id
        self.tags = tags


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
        name = dictionary.get('name')
        mtype = dictionary.get('type')
        time_zone = dictionary.get('timeZone')
        disable_remote_status_page = dictionary.get('disableRemoteStatusPage')
        disable_my_meraki_com = dictionary.get('disableMyMerakiCom')
        copy_from_network_id = dictionary.get('copyFromNetworkId')
        tags = dictionary.get('tags')

        # Return an object of this model
        return cls(name,
                   mtype,
                   time_zone,
                   disable_remote_status_page,
                   disable_my_meraki_com,
                   copy_from_network_id,
                   tags)


