def open_browser(browser_name):
    print_def_name(open_browser, browser_name)


def go_to_company_name_homepage(page_url):
    print_def_name(go_to_company_name_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):

    print_def_name(find_registration_button_on_login_page, page_url, button_text)


def print_def_name(name, *args):
    name_func = name.__name__.replace("_", " ").capitalize()
    print("{0}".format(name_func), end= ": ")
    print(*args, sep=", ")


open_browser("Chrome Browser")
go_to_company_name_homepage("https://qa.guru/")
find_registration_button_on_login_page("https://qa.guru/", "Личный кабинет")


