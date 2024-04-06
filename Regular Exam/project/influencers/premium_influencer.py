from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    PAYMENT_PERCENTAGE = 0.85
    CAMPAIGN_TYPE = {
        "HighBudgetCampaign": 1.5,
        "LowBudgetCampaign": 0.8,
    }

    def calculate_payment(self, campaign: BaseCampaign):
        return campaign.budget * self.PAYMENT_PERCENTAGE

    def reached_followers(self, campaign_type: str):
        return int(self.CAMPAIGN_TYPE[campaign_type] * self.followers * self.engagement_rate)
