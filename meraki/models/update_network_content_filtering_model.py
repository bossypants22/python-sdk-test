# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkContentFilteringModel(object):

    """Implementation of the 'updateNetworkContentFiltering' model.

    TODO: type model description here.

    Attributes:
        blocked_url_patterns (list of string): A blacklist of URL patterns to
            block
        url_category_list_size (string): URL category list size which is
            either 'topSites' or 'fullList'
        allowed_url_patterns (list of string): A whitelist of URL patterns to
            allow
        blocked_url_categories (list of string): A list of URL categories to
            block

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "blocked_url_patterns":'blockedUrlPatterns',
        "url_category_list_size":'urlCategoryListSize',
        "allowed_url_patterns":'allowedUrlPatterns',
        "blocked_url_categories":'blockedUrlCategories'
    }

    def __init__(self,
                 blocked_url_patterns=None,
                 url_category_list_size=None,
                 allowed_url_patterns=None,
                 blocked_url_categories=None):
        """Constructor for the UpdateNetworkContentFilteringModel class"""

        # Initialize members of the class
        self.blocked_url_patterns = blocked_url_patterns
        self.url_category_list_size = url_category_list_size
        self.allowed_url_patterns = allowed_url_patterns
        self.blocked_url_categories = blocked_url_categories


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
        blocked_url_patterns = dictionary.get('blockedUrlPatterns')
        url_category_list_size = dictionary.get('urlCategoryListSize')
        allowed_url_patterns = dictionary.get('allowedUrlPatterns')
        blocked_url_categories = dictionary.get('blockedUrlCategories')

        # Return an object of this model
        return cls(blocked_url_patterns,
                   url_category_list_size,
                   allowed_url_patterns,
                   blocked_url_categories)


