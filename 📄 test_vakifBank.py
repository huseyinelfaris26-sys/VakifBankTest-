from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

class TestVakifBank:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.folderPath = "2023-06-27"
        if not os.path.exists(self.folderPath):
            os.makedirs(self.folderPath)
        self.username = "HUSEIN"
        self.password = "1234567"

    def waitMethod(self, element, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(element)
        )

    def runTests(self):
        try:
            self.driver.get("https://www.vakifbank.com.tr")
            sleep(2)
            self.driver.save_screenshot(f"{self.folderPath}/1.png")
            print("✅ فتح الموقع الرئيسي")

            for j in range(1, 6):
                try:
                    btnCenter = self.driver.find_element(By.XPATH, f"(//nav//li)[{j}]")
                    btnCenter.click()
                    self.driver.execute_script("window.scrollTo(0, 300)")
                    sleep(2)
                    self.driver.save_screenshot(f"{self.folderPath}/{j+5}.png")
                    print(f"✅ زيارة القسم {j}")
                except Exception as e:
                    print(f"⚠️ خطأ في القسم {j}: {e}")

            for k in range(6):
                try:
                    elem_id = f"ctl00_ct116_ct100_ContentPlaceHolder1_link{k}"
                    self.waitMethod((By.ID, elem_id), 3)
                    btnbott = self.driver.find_element(By.ID, elem_id)
                    btnbott.click()
                    self.driver.execute_script("window.scrollTo(0, 500)")
                    self.driver.save_screenshot(f"{self.folderPath}/btn_{k}.png")
                    self.driver.back()
                    sleep(1)
                except:
                    pass

            for l in range(16):
                try:
                    self.waitMethod((By.XPATH, "//*[@id='Form1']//a[contains(@class,'next')]"), 2)
                    btnNext = self.driver.find_element(By.XPATH, "//*[@id='Form1']//a[contains(@class,'next')]")
                    btnNext.click()
                    self.driver.execute_script("window.scrollTo(0, 0)")
                    sleep(1.5)
                    self.driver.save_screenshot(f"{self.folderPath}/page_{l}.png")
                except:
                    break

            print("\n🎉 تم الانتهاء من جميع الاختبارات!")
        except Exception as e:
            print(f"\n❌ خطأ: {e}")
        finally:
            self.driver.quit()
            print("🔒 تم إغلاق المتصفح")

if __name__ == "__main__":
    test = TestVakifBank()
    test.runTests()
