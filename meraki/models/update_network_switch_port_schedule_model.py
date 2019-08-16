# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.port_schedule_model

class UpdateNetworkSwitchPortScheduleModel(object):

    """Implementation of the 'updateNetworkSwitchPortSchedule' model.

    TODO: type model description here.

    Attributes:
        port_schedule (PortScheduleModel): The schedule for switch port
            scheduling. Schedules are applied to days of the week.     When
            it's empty, default schedule with all days of a week are
            configured.     Any unspecified day in the schedule is added as a
            default schedule configuration of the day.
        name (string): The name for your port schedule.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "port_schedule":'portSchedule',
        "name":'name'
    }

    def __init__(self,
                 port_schedule=None,
                 name=None):
        """Constructor for the UpdateNetworkSwitchPortScheduleModel class"""

        # Initialize members of the class
        self.port_schedule = port_schedule
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
        port_schedule = meraki.models.port_schedule_model.PortScheduleModel.from_dictionary(dictionary.get('portSchedule')) if dictionary.get('portSchedule') else None
        name = dictionary.get('name')

        # Return an object of this model
        return cls(port_schedule,
                   name)


