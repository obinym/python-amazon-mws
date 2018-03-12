"""
Tests for the Recommendations API class.
"""
import unittest
import mws
from .utils import CommonRequestTestTools


class RecommendationsTestCase(unittest.TestCase, CommonRequestTestTools):
    """
    Test cases for Recommendations.
    """
    # TODO: Add remaining methods for Recommendations
    def setUp(self):
        self.api = mws.Recommendations(
            self.CREDENTIAL_ACCESS,
            self.CREDENTIAL_SECRET,
            self.CREDENTIAL_ACCOUNT,
            auth_token=self.CREDENTIAL_TOKEN
        )
        self.api._test_request_params = True

    def test_get_last_updated_time_for_recommendations(self):
        """
        GetLastUpdatedTimeForRecommendations operation
        """
        marketplace_id = "marketplace_foobar"
        params = self.api.get_last_updated_time_for_recommendations(marketplace_id)
        self.assert_common_params(params)
        assert params['Action'] == 'ListRecommendations'
        assert params['MarketplaceId'] == marketplace_id

    def test_list_recommendations(self):
        """
        ListRecommendations operation
        """
        marketplace_id = "marketplace_bazbar"
        recommendationcategory = "muffin balls"
        params = self.api.list_recommendations(
            marketplace_id=marketplace_id,
            recommendationcategory=recommendationcategory,
        )
        self.assert_common_params(params)
        assert params['Action'] == 'ListRecommendations'
        assert params['MarketplaceId'] == marketplace_id
        assert params['RecommendationCategory'] == recommendationcategory

    def test_list_recommendations_by_next_token(self):
        """
        ListRecommendationsByNextToken operation, by way of method decorator.
        """
        next_token = "foobar123"
        params = self.api.list_recommendations(next_token=next_token)
        self.assert_common_params(params)
        assert params['Action'] == 'ListRecommendationsByNextToken'
        assert params['NextToken'] == next_token

    def test_list_recommendations_by_next_token_alias(self):
        """
        ListRecommendationsByNextToken operation, by way of alias method.
        """
        next_token = "barbaz456"
        params = self.api.list_recommendations_by_next_token(next_token)
        self.assert_common_params(params)
        assert params['Action'] == 'ListRecommendationsByNextToken'
        assert params['NextToken'] == next_token
