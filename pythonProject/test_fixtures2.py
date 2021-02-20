import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import os
@pytest.fixture()
def setup():
    print("\n Fixture calling set up")

@pytest.mark.usefixtures("setup")
def test1():
    print("\n Calling test1")

def test2():
    print("\n Calling test2")


