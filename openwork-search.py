# coding:utf-8
from selenium import webdriver
from time import sleep

if __name__ == "__main__":
    driver = webdriver.Chrome()

    driver.get('https://www.vorkers.com/')
    
    #searchElement = driver.find_element_by_name("q")
    #https://qiita.com/Taro56/items/7cb048f5e8e8bae192e0
    #https://www.seleniumqref.com/api/python/element_set/Python_special_send_keys.html
    #http://chyka.hatenablog.jp/entry/2018/02/01/%E3%83%A1%E3%83%AB%E3%82%AB%E3%83%AA%E5%87%BA%E5%93%81%E3%81%AE%E3%83%96%E3%83%A9%E3%82%A6%E3%82%B6%E4%B8%8A%E6%93%8D%E4%BD%9C%E3%82%92%E8%87%AA%E5%8B%95%E5%8C%96%E3%81%99%E3%82%8B_%E3%81%9D%E3%81%AE#%E8%87%AA%E5%8B%95%E5%8C%96%E3%81%97%E3%81%9F%E5%8B%95%E4%BD%9C%E3%81%AF%E3%81%93%E3%82%93%E3%81%AA%E6%84%9F%E3%81%98
    #https://kurozumi.github.io/selenium-python/locating-elements.html
    #https://tanuhack.com/selenium-change-window/
    searchElement = driver.find_element_by_name("src_str")
    searchElement.send_keys('google')

    searchElement.submit()

    # 読み込み遅いかもしれないから3秒待つ。
    sleep(3)

    print(driver.current_url)
    print(driver.current_url)
    print(driver.current_url)
    print(driver.current_url)

    #driver.get('driver.current_url')
    #driver.get('https://www.vorkers.com/company_list?field=&pref=&src_str=google&sort=1')

    #リンクテキスト名が"グーグル合同会社"の要素を取得
    clickElement = driver.find_element_by_link_text('グーグル合同会社')
    #リンクをクリック
    clickElement.click()



    #driver.quit()