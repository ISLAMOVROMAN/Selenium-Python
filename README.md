## 📚 Lessons Overview (Updated)

| **#** | **File**                                                                                                                                         | **Description**                                                                                |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| 1     | [![File](https://img.shields.io/badge/File-1_chromedriver.py-blue)](1_chromedriver.py)                                                             | Demonstrates the basic setup of ChromeDriver using Selenium and `webdriver_manager`. This script includes how to install and initialize the ChromeDriver for test automation. |
| 2     | [![File](https://img.shields.io/badge/File-2_firefoxdriver.py-blue)](2_firefoxdriver.py)                                                           | Covers the setup of FirefoxDriver with Selenium. The script demonstrates downloading, installing, and running GeckoDriver for Firefox automation. |
| 3     | [![File](https://img.shields.io/badge/File-3_navigation.py-blue)](3_navigation.py)                                                                 | Demonstrates how to navigate to web pages, retrieve their URLs and titles, and handle basic browser operations. |
| 4     | [![File](https://img.shields.io/badge/File-4_Verification.py-blue)](4_Verification.py)                                                             | Explains how to verify the presence of web elements on a page using various locators like `ID`, `CLASS_NAME`, `CSS_SELECTOR`, and more. |
| 5     | [![File](https://img.shields.io/badge/File-5_find.py-blue)](5_find.py)                                                                             | Introduces finding elements on a webpage and interacting with them through clicks, inputs, and other actions. Ideal for learning basic Selenium interaction methods. |
| 6     | [![File](https://img.shields.io/badge/File-6_xpath.py-blue)](6_xpath.py)                                                                           | Covers using XPath expressions to locate elements on a webpage. Explains both absolute and relative XPath strategies with examples. |
| 7     | [![File](https://img.shields.io/badge/File-7_clicktutor.py-blue)](7_clicktutor.py)                                                                 | A complete interaction flow script simulating user actions like entering an email, password, and clicking buttons. It also includes error handling for invalid inputs. |
| 8     | [![File](https://img.shields.io/badge/File-8.1_doubleklick.py-blue)](8.1_doubleklick.py)                                                           | Demonstrates double-click actions using Selenium's `ActionChains`. This script includes real-world examples of validating double-click events. |
| 9     | [![File](https://img.shields.io/badge/File-8.2_DEMOQA.py-blue)](8.2_DEMOQA.py)                                                                     | Automates interactions on the DEMOQA website, including handling buttons, forms, alerts, and navigation menus. A practice-oriented example for beginners. |
| 10    | [![File](https://img.shields.io/badge/File-9_BrowserSettings.py-blue)](9_BrowserSettings.py)                                                       | Configures browser settings such as disabling notifications, setting download directories, and optimizing browser performance for testing. |
| 11    | [![File](https://img.shields.io/badge/File-10_Downloading_file.py-blue)](10_Downloading_file.py)                                                   | Automates file download processes, configuring the browser to download files directly without pop-ups or manual intervention. |
| 12    | [![File](https://img.shields.io/badge/File-10.1_Upload_file.py-blue)](10.1_Upload_file.py)                                                         | Automates file upload scenarios, demonstrating how to locate file upload elements and upload files using Selenium. |
| 13    | [![File](https://img.shields.io/badge/File-10.2_Upload_DEMOQA.py-blue)](10.2_Upload_DEMOQA.py)                                                     | Automates file upload testing on the DEMOQA platform, showcasing a real-world example of validating upload functionality. |
| 14    | [![File](https://img.shields.io/badge/File-11.1_Implicitly.py-blue)](11.1_Implicitly.py)                                                           | Demonstrates the use of implicit waits in Selenium, helping manage delays in locating elements on dynamic web pages. |
| 15    | [![File](https://img.shields.io/badge/File-11.2_Explicit.py-blue)](11.2_Explicit.py)                                                               | Explains the use of explicit waits using Selenium's `WebDriverWait` for precise synchronization with dynamically loaded elements. |
# Selenium-Python Project

| 16    | [![File](https://img.shields.io/badge/File-14_1_getCookies.py-blue)](14_1_getCookies.py)                             | Demonstrates retrieving specific cookies and adding new ones. Explains how to manipulate browser cookies using Selenium.                                                                                                                                    |
| 17    | [![File](https://img.shields.io/badge/File-14_2_addCookies.py-blue)](14_2_addCookies.py)                             | Illustrates adding new cookies to the browser session and retrieving specific cookies by name. Designed for learning cookie management.                                                                                                                      |
| 18    | [![File](https://img.shields.io/badge/File-14_3_GetCookiestofile.py-blue)](14_3_GetCookiestofile.py)                 | Explains saving browser cookies to a file and restoring them. Uses pickle for serialization and Selenium for cookie manipulation.                                                                                                                            |
| 19    | [![File](https://img.shields.io/badge/File-14_4_cookies.py-blue)](14_4_cookies.py)                                   | Covers clearing all browser cookies, loading cookies from a file, and refreshing the session. Practical for understanding cookie handling in Selenium.                                                                                                       |
| 20    | [![File](https://img.shields.io/badge/File-14_5_Amazoncart.py-blue)](14_5_Amazoncart.py)                             | Automates adding items to the Amazon cart, saving session cookies, and restoring the cart state. Includes examples of session management and error handling.                                                                                                 |
| 21    | [![File](https://img.shields.io/badge/File-11.3_Explicit.py-blue)](11.3_Explicit.py)                                 | Demonstrates advanced explicit wait strategies in Selenium. Includes waiting for elements to appear, disappear, or change states.                                                                                                                            |
| 22    | [![File](https://img.shields.io/badge/File-12.1_stells_cheking.py-blue)](12.1_stells_cheking.py)                     | Uses undetected_chromedriver to bypass browser automation detection. Includes checks for automation flags and takes screenshots for validation.                                                                                                               |
| 23    | [![File](https://img.shields.io/badge/File-13_Allerts.py-blue)](13_Allerts.py)                                       | Handles various alert types (e.g., basic, confirmation, and prompt) on a test webpage. Demonstrates alert interaction and error handling with examples.                                                                                                       |

---

## ⚙️ Setup and Installation

### 🛠 Prerequisites

- **Python 3.7 or higher**  
- **Selenium** library installed (`pip install selenium`)  
- **Browser-specific drivers** managed by `webdriver_manager`  

---

### 🚀 Installation Steps

1. Clone this repository:  
   ```bash
   git clone https://github.com/ISLAMOVROMAN/Selenium-Python.git
   cd Selenium-Python
---

