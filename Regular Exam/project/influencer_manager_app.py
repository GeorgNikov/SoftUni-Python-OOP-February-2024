from typing import List

from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCER = {
        "PremiumInfluencer": PremiumInfluencer,
        "StandardInfluencer": StandardInfluencer,
    }

    VALID_CAMPAIGNS = {
        "HighBudgetCampaign": HighBudgetCampaign,
        "LowBudgetCampaign": LowBudgetCampaign,
    }

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_INFLUENCER:
            return f"{influencer_type} is not an allowed influencer type."

        if self.__find_influencer_by_username(username):
            return f"{username} is already registered."

        influencer = self.VALID_INFLUENCER[influencer_type](username, followers, engagement_rate)
        self.influencers.append(influencer)

        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGNS:
            return f"{campaign_type} is not a valid campaign type."

        if self.__find_campaign_by_id(campaign_id):
            return f"Campaign ID {campaign_id} has already been created."

        campaign = self.VALID_CAMPAIGNS[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(campaign)

        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = self.__find_influencer_by_username(influencer_username)
        if not influencer:
            return f"Influencer '{influencer_username}' not found."

        campaign = self.__find_campaign_by_id(campaign_id)
        if not campaign:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return (f"Influencer '{influencer_username}' does not meet the eligibility "
                    f"criteria for the campaign with ID {campaign_id}.")

        payment = influencer.calculate_payment(campaign)

        if payment > 0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment
            influencer.campaigns_participated.append(campaign)

            return (f"Influencer '{influencer_username}' has successfully "
                    f"participated in the campaign with ID {campaign_id}.")

    def calculate_total_reached_followers(self):
        result = {}
        for campaign in self.campaigns:
            for influencer in [i for i in campaign.approved_influencers if campaign.approved_influencers]:
                result[campaign] = influencer.reached_followers(campaign.__class__.__name__)

        return result

    def influencer_campaign_report(self, username: str):
        influencer = self.__find_influencer_by_username(username)

        if not influencer.campaigns_participated:
            return f"{username} has not participated in any campaigns."

        return str(influencer.display_campaigns_participated())

    def campaign_statistics(self):
        sorted_campaigns = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))

        result = f"$$ Campaign Statistics $$"
        for camp in sorted_campaigns:
            result += (f"\n  * Brand: {camp.brand}, "
                       f"Total influencers: {len(camp.approved_influencers)}, "
                       f"Total budget: ${camp.budget:.2f}, "
                       f"Total reached followers: {sum(i.reached_followers(camp.__class__.__name__) for i in camp.approved_influencers)}")

        return result

    def __find_campaign_by_id(self, campaign_id):
        campaign = [c for c in self.campaigns if c.campaign_id == campaign_id]
        return campaign[0] if campaign else None

    def __find_influencer_by_username(self, username):
        influencer = [i for i in self.influencers if i.username == username]
        return influencer[0] if influencer else None
