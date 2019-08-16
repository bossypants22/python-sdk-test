# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.power_exception_model

class UpdateNetworkSwitchSettingsModel(object):

    """Implementation of the 'updateNetworkSwitchSettings' model.

    TODO: type model description here.

    Attributes:
        power_exceptions (list of PowerExceptionModel): Exceptions on a per
            switch basis to "useCombinedPower"
        use_combined_power (bool): The use Combined Power as the default
            behavior of secondary power supplies on supported devices.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "power_exceptions":'powerExceptions',
        "use_combined_power":'useCombinedPower'
    }

    def __init__(self,
                 power_exceptions=None,
                 use_combined_power=None):
        """Constructor for the UpdateNetworkSwitchSettingsModel class"""

        # Initialize members of the class
        self.power_exceptions = power_exceptions
        self.use_combined_power = use_combined_power


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
        power_exceptions = None
        if dictionary.get('powerExceptions') != None:
            power_exceptions = list()
            for structure in dictionary.get('powerExceptions'):
                power_exceptions.append(meraki.models.power_exception_model.PowerExceptionModel.from_dictionary(structure))
        use_combined_power = dictionary.get('useCombinedPower')

        # Return an object of this model
        return cls(power_exceptions,
                   use_combined_power)


