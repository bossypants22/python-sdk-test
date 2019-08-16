# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.sunday_model
import meraki.models.saturday_model
import meraki.models.tuesday_model
import meraki.models.wednesday_model
import meraki.models.thursday_model
import meraki.models.friday_model
import meraki.models.monday_model

class SchedulingModel(object):

    """Implementation of the 'Scheduling' model.

    The schedule for the group policy. Schedules are applied to days of the
    week.

    Attributes:
        sunday (SundayModel): The schedule object for Sunday.
        saturday (SaturdayModel): The schedule object for Saturday.
        tuesday (TuesdayModel): The schedule object for Tuesday.
        wednesday (WednesdayModel): The schedule object for Wednesday.
        thursday (ThursdayModel): The schedule object for Thursday.
        friday (FridayModel): The schedule object for Friday.
        enabled (bool): Whether scheduling is enabled (true) or disabled
            (false). Defaults to false. If true, the schedule objects for each
            day of the week (monday - sunday) are parsed.
        monday (MondayModel): The schedule object for Monday.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "sunday":'sunday',
        "saturday":'saturday',
        "tuesday":'tuesday',
        "wednesday":'wednesday',
        "thursday":'thursday',
        "friday":'friday',
        "enabled":'enabled',
        "monday":'monday'
    }

    def __init__(self,
                 sunday=None,
                 saturday=None,
                 tuesday=None,
                 wednesday=None,
                 thursday=None,
                 friday=None,
                 enabled=None,
                 monday=None):
        """Constructor for the SchedulingModel class"""

        # Initialize members of the class
        self.sunday = sunday
        self.saturday = saturday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.enabled = enabled
        self.monday = monday


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
        sunday = meraki.models.sunday_model.SundayModel.from_dictionary(dictionary.get('sunday')) if dictionary.get('sunday') else None
        saturday = meraki.models.saturday_model.SaturdayModel.from_dictionary(dictionary.get('saturday')) if dictionary.get('saturday') else None
        tuesday = meraki.models.tuesday_model.TuesdayModel.from_dictionary(dictionary.get('tuesday')) if dictionary.get('tuesday') else None
        wednesday = meraki.models.wednesday_model.WednesdayModel.from_dictionary(dictionary.get('wednesday')) if dictionary.get('wednesday') else None
        thursday = meraki.models.thursday_model.ThursdayModel.from_dictionary(dictionary.get('thursday')) if dictionary.get('thursday') else None
        friday = meraki.models.friday_model.FridayModel.from_dictionary(dictionary.get('friday')) if dictionary.get('friday') else None
        enabled = dictionary.get('enabled')
        monday = meraki.models.monday_model.MondayModel.from_dictionary(dictionary.get('monday')) if dictionary.get('monday') else None

        # Return an object of this model
        return cls(sunday,
                   saturday,
                   tuesday,
                   wednesday,
                   thursday,
                   friday,
                   enabled,
                   monday)


