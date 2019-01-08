from wdclass import Webdriver

webdriver = Webdriver()

search_box              = '.search-input-box'
first_hit               = '.item-title.block'
filters_toggle          = '.wideSidepaneFiltersText'
property_condo          = '.button[data-rf-test-name="uipt2"]'
property_other          = '.button[data-rf-test-name="uipt6"]'
for_sale_toggle         = '#filterContent > div > div:nth-child(1) > div:nth-child(5) > div > label'
prefilter_home_count    = '.homeCount'
postfilter_home_count   = '.homes.summary'
submit_filter           = '.button.Button.primary.applyButton'


class Redfin:
    def go_to_page(self):
        webdriver.visit_page('www.redfin.com')

    def main_search(self, input):
        webdriver.send_input(search_box, input)

    def select_area(self):
        webdriver.clickon(first_hit)

    def show_filters(self):
        webdriver.clickon(filters_toggle)

    def set_property_type_condo(self):
        webdriver.clickon(property_condo)

    def set_property_type_other(self):
        webdriver.clickon(property_other)

    def toggle_for_sale_toggle(self):
        webdriver.clickon(for_sale_toggle)

    def apply_filters(self):
        webdriver.clickon(submit_filter)

    def prefilter_result(self):
        self.prefilter_text = webdriver.get_text(prefilter_home_count)
        return self.prefilter_text

    def postfilter_result(self):
        self.postfilter_result = webdriver.get_text(postfilter_home_count)
        return self.postfilter_result