# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.vlan_tagging_model
import meraki.models.content_filtering_model
import meraki.models.bonjour_forwarding_model
import meraki.models.bandwidth_model
import meraki.models.scheduling_model
import meraki.models.firewall_and_traffic_shaping_model

class CreateNetworkGroupPolicyModel(object):

    """Implementation of the 'createNetworkGroupPolicy' model.

    TODO: type model description here.

    Attributes:
        vlan_tagging (VlanTaggingModel): The VLAN tagging settings for your
            group policy. Only available if your network has a wireless
            configuration.
        content_filtering (ContentFilteringModel): The content filtering
            settings for your group policy
        bonjour_forwarding (BonjourForwardingModel): The Bonjour settings for
            your group policy. Only valid if your network has a wireless
            configuration.
        bandwidth (BandwidthModel): The bandwidth settings for clients bound
            to your group policy.
        splash_auth_settings (SplashAuthSettingsEnum): Whether clients bound
            to your policy will bypass splash authorization or behave
            according to the network's rules. Can be one of 'network default'
            or 'bypass'. Only available if your network has a wireless
            configuration.
        name (string): The name for your group policy. Required.
        scheduling (SchedulingModel): The schedule for the group policy.
            Schedules are applied to days of the week.
        firewall_and_traffic_shaping (FirewallAndTrafficShapingModel): The
            firewall and traffic shaping rules and settings for your policy.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "vlan_tagging":'vlanTagging',
        "content_filtering":'contentFiltering',
        "bonjour_forwarding":'bonjourForwarding',
        "bandwidth":'bandwidth',
        "splash_auth_settings":'splashAuthSettings',
        "scheduling":'scheduling',
        "firewall_and_traffic_shaping":'firewallAndTrafficShaping'
    }

    def __init__(self,
                 name=None,
                 vlan_tagging=None,
                 content_filtering=None,
                 bonjour_forwarding=None,
                 bandwidth=None,
                 splash_auth_settings=None,
                 scheduling=None,
                 firewall_and_traffic_shaping=None):
        """Constructor for the CreateNetworkGroupPolicyModel class"""

        # Initialize members of the class
        self.vlan_tagging = vlan_tagging
        self.content_filtering = content_filtering
        self.bonjour_forwarding = bonjour_forwarding
        self.bandwidth = bandwidth
        self.splash_auth_settings = splash_auth_settings
        self.name = name
        self.scheduling = scheduling
        self.firewall_and_traffic_shaping = firewall_and_traffic_shaping


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
        name = dictionary.get('name')
        vlan_tagging = meraki.models.vlan_tagging_model.VlanTaggingModel.from_dictionary(dictionary.get('vlanTagging')) if dictionary.get('vlanTagging') else None
        content_filtering = meraki.models.content_filtering_model.ContentFilteringModel.from_dictionary(dictionary.get('contentFiltering')) if dictionary.get('contentFiltering') else None
        bonjour_forwarding = meraki.models.bonjour_forwarding_model.BonjourForwardingModel.from_dictionary(dictionary.get('bonjourForwarding')) if dictionary.get('bonjourForwarding') else None
        bandwidth = meraki.models.bandwidth_model.BandwidthModel.from_dictionary(dictionary.get('bandwidth')) if dictionary.get('bandwidth') else None
        splash_auth_settings = dictionary.get('splashAuthSettings')
        scheduling = meraki.models.scheduling_model.SchedulingModel.from_dictionary(dictionary.get('scheduling')) if dictionary.get('scheduling') else None
        firewall_and_traffic_shaping = meraki.models.firewall_and_traffic_shaping_model.FirewallAndTrafficShapingModel.from_dictionary(dictionary.get('firewallAndTrafficShaping')) if dictionary.get('firewallAndTrafficShaping') else None

        # Return an object of this model
        return cls(name,
                   vlan_tagging,
                   content_filtering,
                   bonjour_forwarding,
                   bandwidth,
                   splash_auth_settings,
                   scheduling,
                   firewall_and_traffic_shaping)


