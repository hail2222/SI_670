#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time
import re
import pandas as pd
from tqdm import tqdm

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



def convert_unit(s):

    if not isinstance(s, str):
        return None

    raw = s.replace(",", "").strip()

    try:
        if "만" in raw: #unit for korean
            return int(float(raw.replace("만", "")) * 10000)

        if raw.endswith(("k", "K")):
            return int(float(raw[:-1]) * 1000)

        if raw.endswith(("m", "M")):
            return int(float(raw[:-1]) * 1_000_000)

        return int(float(raw))

    except:
        return None



def extract_followers_text(driver):


    spans = [s.text.strip() for s in driver.find_elements(By.TAG_NAME, "span") if s.text.strip()]
    anchors = [a.text.strip() for a in driver.find_elements(By.TAG_NAME, "a") if a.text.strip()]

    all_texts = spans + anchors

    kor = [t for t in all_texts if t.startswith("팔로워 ")]
    if kor:
        return kor[0].replace("팔로워", "").strip()

    eng = [t for t in all_texts if t.lower().endswith(" followers")]
    if eng:
        return eng[0].lower().replace("followers", "").strip()

    eng2 = [t for t in all_texts if t.lower().startswith("followers ")]
    if eng2:
        return eng2[0].lower().replace("followers", "").strip()

    return None


def get_followers(driver, username):
    url = f"https://www.instagram.com/{username}/"

    try:
        driver.get(url)
    except:
        return None

    time.sleep(2.3)

    raw = extract_followers_text(driver)
    if raw is None:
        return None

    return convert_unit(raw)



def connect_chrome(port=9222):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.debugger_address = f"127.0.0.1:{port}"

    print("Connecting to Chrome...")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    print("✔ Connected!\n")
    return driver



if __name__ == "__main__":
    print("Loading usernames from dataset...")

    df = pd.read_csv("clean_posts_featured_with_engagement.csv")

    usernames = sorted(df["owner_username"].dropna().unique())
    print(f"Total usernames: {len(usernames)}")

    driver = connect_chrome(port=9222)

    results = {}

    print("Starting scraping...\n")

    for u in tqdm(usernames, desc="Scraping users"):
        try:
            results[u] = get_followers(driver, u)
        except:
            results[u] = None

    print("\nScraping finished!")
    print("Saving followers_output.csv...\n")

    out_df = pd.DataFrame({
        "owner_username": list(results.keys()),
        "followers": list(results.values())
    })

    out_df.to_csv("followers_output.csv", index=False)

    print("Done → followers_output.csv")
