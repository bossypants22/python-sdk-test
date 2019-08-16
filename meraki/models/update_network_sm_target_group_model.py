# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkSmTargetGroupModel(object):

    """Implementation of the 'updateNetworkSmTargetGroup' model.

    TODO: type model description here.

    Attributes:
        scope (string): The scope and tag options of the target group. Comma
            separated values beginning with one of withAny, withAll,
            withoutAny, withoutAll, all, none, followed by tags. Default to
            none if empty.
        name (string): The name of this target group

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "scope":'scope',
        "name":'name'
    }

    def __init__(self,
                 scope=None,
                 name=None):
        """Constructor for the UpdateNetworkSmTargetGroupModel class"""

        # Initialize members of the class
        self.scope = scope
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
        scope = dictionary.get('scope')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(scope,
                   name)


