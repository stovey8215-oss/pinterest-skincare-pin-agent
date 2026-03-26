# campaign_analytics.py

def track_campaign_performance(campaign_id, impressions, clicks):
    """
    Track the performance of a campaign.
    
    Parameters:
    campaign_id : str : The ID of the campaign.
    impressions : int : The number of times the campaign was displayed.
    clicks : int : The number of times the campaign was clicked.
    """
    # Calculate performance metrics
    click_through_rate = clicks / impressions if impressions > 0 else 0
    print(f"Campaign ID: {campaign_id}")
    print(f"Impressions: {impressions}")
    print(f"Clicks: {clicks}")
    print(f"Click Through Rate: {click_through_rate:.2%}")


def main():
    # Example usage
    track_campaign_performance("12345", 1000, 150)


if __name__ == "__main__":
    main()