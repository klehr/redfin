import unittest
from redfin_po import Redfin


class TestRedfin(unittest.TestCase):
    def setUp(self):
        self.redfin = Redfin()

    def test_filter(self):
        self.redfin.go_to_page()
        self.redfin.main_search('Sunnyside, NY')
        self.redfin.select_area()

        homecount_in_mainview = self.redfin.get_homecount_mainview()
        # Home count must be > 0.
        if homecount_in_mainview == '0 Homes':
            raise Exception('Site returned {}'.format(homecount_in_mainview))

        self.redfin.show_filters()
        self.redfin.set_property_type_condo()
        self.redfin.set_property_type_other()
        # Turns off for sale toggle
        self.redfin.toggle_for_sale_toggle()
        homecount_in_filterview_filter_applied = self.redfin.get_homecount_filterview()

        # Home count should not be equal to pre-filter value.
        assert homecount_in_mainview != homecount_in_filterview_filter_applied, \
            'Home count did not change after applying 3 filters'
        self.redfin.apply_filters()
        homecount_in_mainview_filter_applied = self.redfin.get_homecount_mainview()

        # Home count in filter view and main view should be the max number of home count in main view.
        assert homecount_in_filterview_filter_applied in homecount_in_mainview_filter_applied, \
            'Prefilter result{prefilter_count} does not match postfilter result{mainview_count}'.format(prefilter_count=homecount_in_filterview_filter_applied, mainview_count=homecount_in_mainview_filter_applied)

        # Check applied specified property filters.
        filter_summary = self.redfin.get_filter_summary()
        assert 'condo' and 'other' in filter_summary

        # Check properties for sale were filtered out as per specified filter.
        for_sale_count = self.redfin.get_for_sale_count()
        assert for_sale_count == 0


if __name__ == '__main__':
    unittest.main()
