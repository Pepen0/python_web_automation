from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def googlestart():
    peno = webdriver.Chrome()
    peno.get("https://google.com")
    print(peno.title)  # added this part to troubleshoot the page being oppen
    input_element = peno.find_element(
        By.NAME, "q"
    )  # there is no speciifed iD so we use the name
    print(input_element)
    input_element.send_keys("one piece straming free ")  # type in google Oppenheimer
    input_element.send_keys(Keys.ENTER)  # Press the Enter key
    time.sleep(30)  # to keep the page open for 120 seconds


# googlestart()


def yahooStart():
    peno = webdriver.Chrome()
    peno.get("https://ca.yahoo.com/")
    input_element = peno.find_element(
        By.ID, "ybar-sbq"
    )  # using ID here because it's unique to every element
    input_element.send_keys("Elon Musk")
    input_element.send_keys(Keys.ENTER)
    time.sleep(30)


# yahooStart()


def wayback_Valentine_fill_form():  # this function is used to open waybaack machine and fill up the old valentine page
    peno = webdriver.Chrome()
    peno.get(
        "https://web.archive.org/web/20200810192121/https://www.oxley.com/domain/valentine.com/"
    )
    input_point = peno.find_element(By.NAME, "name")
    input_point.send_keys("Pepeno")

    input_point = peno.find_element(By.NAME, "email")
    input_point.send_keys("Pepeno@gmail.com")

    input_point = peno.find_element(By.NAME, "phone")
    input_point.send_keys("514-frap50")

    input_point = peno.find_element(By.NAME, "offer")
    input_point.send_keys("Code:sinsino")

    input_point = peno.find_element(By.NAME, "message")
    input_point.send_keys(
        "Merci d'avoir utiliser le peno script sponsorisé par la frap "
    )

    time.sleep(30)


# wayback_Valentine_fill_form()


def open_youtuber_video(
    x,
):  # This function should go on a youtubers chanel and start looking for his video list won't work due to youtube anti spam policies
    peno = webdriver.Chrome()
    peno.get("https://www.youtube.com/")

    time.sleep(5)

    search_bar = peno.find_element(By.ID, "search")
    search_bar.click()
    search_bar.send_keys(x)

    click_channel = peno.find_element(By.LINK_TEXT, x)
    click_channel.click

    Click_video = peno.find_element(By.LINK_TEXT, "Vidéos")
    Click_video.click

    time.sleep(15)


# open_youtuber_video("Kai Cenat")


def click_text_on_google(
    x,
):  # this function will open google and press the Gmail button
    peno = webdriver.Chrome()
    peno.get("https://www.google.ca")
    print(peno.title)  # should show google

    time.sleep(3)

    Click_button = peno.find_element(By.LINK_TEXT, x)
    Click_button.click()
    print(peno.title)  # should show gmail
    time.sleep(20)


# click_text_on_google("Gmail")


def click_partial_text_on_google(
    x, y
):  # this function will open google and press the Gmail button and create an account
    peno = webdriver.Chrome()
    peno.get("https://www.google.ca")
    print(peno.title)  # should show "google"

    time.sleep(3)

    Click_button = peno.find_element(By.LINK_TEXT, x)
    Click_button.click()
    print(
        peno.title
    )  # should show "Gmail: Private and secure email at no cost | Google Workspace"

    time.sleep(3)

    Click_button = peno.find_element(By.PARTIAL_LINK_TEXT, y)
    Click_button.click()
    print(peno.title)  # should show "Gmail"

    time.sleep(20)


# click_partial_text_on_google("Gmail", "Create")
