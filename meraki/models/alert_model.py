# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class AlertModel(object):

    """Implementation of the 'Alert' model.

    TODO: type model description here.

    Attributes:
        alert_destinations (object): A hash of destinations for this specific
            alert. Keys include: emails: A list of emails that will recieve
            information about the alert, allAdmins: If true, then all network
            admins will receive emails, and snmp: If true, then an SNMP trap
            will be sent if there is an SNMP trap server configured for this
            network.
        filters (object): A hash of specific configuration data for the alert.
            Only filters specific to the alert will be updated.
        mtype (string): The type of alert
        enabled (bool): A boolean depicting if the alert is turned on or off

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "alert_destinations":'alertDestinations',
        "filters":'filters',
        "mtype":'type',
        "enabled":'enabled'
    }

    def __init__(self,
                 alert_destinations=None,
                 filters=None,
                 mtype=None,
                 enabled=None):
        """Constructor for the AlertModel class"""

        # Initialize members of the class
        self.alert_destinations = alert_destinations
        self.filters = filters
        self.mtype = mtype
        self.enabled = enabled


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
        alert_destinations = dictionary.get('alertDestinations')
        filters = dictionary.get('filters')
        mtype = dictionary.get('type')
        enabled = dictionary.get('enabled')

        # Return an object of this model
        return cls(alert_destinations,
                   filters,
                   mtype,
                   enabled)


