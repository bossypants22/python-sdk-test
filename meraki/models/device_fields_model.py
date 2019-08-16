# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class DeviceFieldsModel(object):

    """Implementation of the 'DeviceFields' model.

    The new fields of the device. Each field of this object is optional.

    Attributes:
        notes (string): New notes for the device
        name (string): New name for the device

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "notes":'notes',
        "name":'name'
    }

    def __init__(self,
                 notes=None,
                 name=None):
        """Constructor for the DeviceFieldsModel class"""

        # Initialize members of the class
        self.notes = notes
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
        notes = dictionary.get('notes')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(notes,
                   name)


