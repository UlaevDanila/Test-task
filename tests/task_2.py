from pages.SbisPage.SbisPage import SbisPage


def test_region_changes(browser):
    sbis_page = SbisPage(browser)
    sbis_page.open_sbis_page()
    sbis_page.sbis_page()
    sbis_page.sbis_contacts_page()
    cities = sbis_page.cities_locator()
    partners_names = sbis_page.names_locator()
    partners_address = sbis_page.address_locator()
    partners_phones = sbis_page.phones_locator()
    element = sbis_page.region_locator()
    sbis_page.change_region()
    new_cities = sbis_page.cities_locator()
    new_partners_names = sbis_page.names_locator()
    new_partners_address = sbis_page.address_locator()
    new_partners_phones = sbis_page.phones_locator()
    is_passed = True
    if cities == new_cities:
        is_passed = False
    elif partners_names == new_partners_names:
        is_passed = False
    elif partners_address == new_partners_address:
        is_passed = False
    elif partners_phones == new_partners_phones:
        is_passed = False
    else:
        assert is_passed == True
