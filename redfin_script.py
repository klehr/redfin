import unittest
from redfin_po import Redfin

class RedfinTest(unittest.TestCase):
    def setUp(self):
        self.redfin = Redfin()

    def filter_result(self):
        self.redfin.go_to_page()
        self.redfin.main_search('Sunnyside, NY')
        self.redfin.select_area()
        self.redfin.show_filters()
        self.redfin.set_property_type_condo()
        self.redfin.set_property_type_other()
        self.redfin.toggle_for_sale_toggle()

        prefilter_result = redfin.prefilter_result()
        redfin.apply_filters()
        postfilter_result = redfin.postfilter_result()

        assert prefilter_result in postfilter_result, 'Prefilter result{pre_filter} does not match postfilter result{post_filter}'.format(pre_filter=prefilter_result, post_filter=postfilter_result)

if __name__ == '__main__':
    unittest.main()
