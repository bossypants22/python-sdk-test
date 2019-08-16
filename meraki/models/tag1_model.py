# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Tag1Model(object):

    """Implementation of the 'Tag1' model.

    TODO: type model description here.

    Attributes:
        access (string): The privilege of the dashboard administrator on the
            tag
        tag (string): The name of the tag

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access":'access',
        "tag":'tag'
    }

    def __init__(self,
                 access=None,
                 tag=None):
        """Constructor for the Tag1Model class"""

        # Initialize members of the class
        self.access = access
        self.tag = tag


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
        access = dictionary.get('access')
        tag = dictionary.get('tag')

        # Return an object of this model
        return cls(access,
                   tag)


