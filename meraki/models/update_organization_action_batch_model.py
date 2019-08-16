# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateOrganizationActionBatchModel(object):

    """Implementation of the 'updateOrganizationActionBatch' model.

    TODO: type model description here.

    Attributes:
        synchronous (bool): Set to true to force the batch to run synchronous.
            There can be at most 20 actions in synchronous batch.
        confirmed (bool): A boolean representing whether or not the batch has
            been confirmed. This property cannot be unset once it is true.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "synchronous":'synchronous',
        "confirmed":'confirmed'
    }

    def __init__(self,
                 synchronous=None,
                 confirmed=None):
        """Constructor for the UpdateOrganizationActionBatchModel class"""

        # Initialize members of the class
        self.synchronous = synchronous
        self.confirmed = confirmed


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
        synchronous = dictionary.get('synchronous')
        confirmed = dictionary.get('confirmed')

        # Return an object of this model
        return cls(synchronous,
                   confirmed)


