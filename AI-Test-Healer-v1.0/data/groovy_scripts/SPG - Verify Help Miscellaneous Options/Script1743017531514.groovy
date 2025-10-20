import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testng.keyword.TestNGBuiltinKeywords as TestNGKW
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

WebUI.openBrowser('')

WebUI.navigateToUrl(GlobalVariable.TFBaseURL)

WebUI.click(findTestObject('Object Repository/TripFocus/Page_TripFocus/button_Sign in'))

WebUI.setText(findTestObject('Object Repository/TripFocus/Page_TripFocus/input_Username (e.g. email address)_Username'), 
    GlobalVariable.TripFocusBleachTechSPGUsername)

WebUI.setText(findTestObject('Object Repository/TripFocus/Page_TripFocus/input_Password_Password'), GlobalVariable.TripFocusFDGSPGPassword)

WebUI.click(findTestObject('Object Repository/TripFocus/Page_TripFocus/button_Login'))

WebUI.maximizeWindow()

WebUI.waitForElementVisible(findTestObject('TripFocus/Testing_Notification_btn'), 15, FailureHandling.OPTIONAL)

//WebUI.delay(30)
if (WebUI.verifyElementVisible(findTestObject('TripFocus/Testing_Notification_btn'), FailureHandling.OPTIONAL) == true) {
	WebUI.click(findTestObject('TripFocus/Testing_Notification_btn'))

	WebUI.delay(1)
}

//WebUI.delay(3)

WebUI.click(findTestObject('TripFocus/Help/Help_Tab'))

WebUI.delay(3)

WebUI.verifyTextPresent('Recommended browsers', false)

WebUI.verifyTextPresent('Latest changes/general errors', false)

WebUI.verifyTextPresent('Clearing browser cache', false)

