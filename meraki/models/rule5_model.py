# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Rule5Model(object):

    """Implementation of the 'Rule5' model.

    TODO: type model description here.

    Attributes:
        mtype (Type4Enum): Type of the L7 rule. One of: 'application',
            'applicationCategory', 'host', 'port', 'ipRange'
        value (string): The 'value' of what you want to block. Format of
            'value' varies depending on type of the rule. See sample request.
            The application categories and application ids can be retrieved
            from the the 'MX L7 application categories' endpoint. The
            countries follow the two-letter ISO 3166-1 alpha-2 format.
        policy (Policy1Enum): 'Deny' traffic specified by this rule

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype":'type',
        "value":'value',
        "policy":'policy'
    }

    def __init__(self,
                 mtype=None,
                 value=None,
                 policy=None):
        """Constructor for the Rule5Model class"""

        # Initialize members of the class
        self.mtype = mtype
        self.value = value
        self.policy = policy


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
        mtype = dictionary.get('type')
        value = dictionary.get('value')
        policy = dictionary.get('policy')

        # Return an object of this model
        return cls(mtype,
                   value,
                   policy)


