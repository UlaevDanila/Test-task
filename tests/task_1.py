from pages.SbisPage.SbisPage import SbisPage

def test_block_presence(browser):
    sbis_page = SbisPage(browser)
    sbis_page.open_sbis_page()
    sbis_page.sbis_page()
    sbis_page.sbis_contacts_page()
    tensor_page = sbis_page.tensor_page()
    tensor_page.tensor_page_peoples()
    images = tensor_page.get_images()
    previous_value = images[0].size
    for i in range(1, len(images)):
        assert previous_value == images[i].size

