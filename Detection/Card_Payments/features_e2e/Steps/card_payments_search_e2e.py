from behave import *
from behave.formatter import null
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import select





@given ('launch Mozilla browser')
def step_impl1 (context):
    context.myProxy = "10.26.221.13:3128"
    context.desired_capability = webdriver.DesiredCapabilities.FIREFOX
    context.desired_capability['proxy'] = {
        "proxyType": "manual",
        "httpProxy": context.myProxy,
        "ftpProxy": context.myProxy,
        "sslProxy": context.myProxy
    }
    context.profile = webdriver.FirefoxProfile ()
    context.profile.accept_untrusted_certs = True
    context.driver = webdriver.Firefox (firefox_profile=context.profile,
                                        capabilities=context.desired_capability,
                                        executable_path="C:\\drivers\\geckodriver.exe")
    context.driver.get ("https://e2e-fcm-cop-gui.service1.svc.meshcore.net/product-delivery-fcm/en/login/login")
    context.driver.maximize_window ()
    global loginbox
    loginbox = context.driver.find_element_by_id("login")
    global passwordbox
    passwordbox = context.driver.find_element_by_id ("password")
    global loginbutton
    loginbutton = context.driver.find_element_by_id ("bthp")



@when ('open INTFCM Homepage')
def step_impl2 (context):
    title = context.driver.title
    print (title)


@when ('Enter username "{user}" and password "{pwd}"')
def step_impl3 (context, user, pwd):
    loginbox.send_keys (user)
    time.sleep (1)
    passwordbox.send_keys (pwd)
    time.sleep (1)


@when ('Click on login button')
def step_impl4 (context):
    loginbutton.click ()


@when ('User must successfully login to the Dashboard page')
def step_impl5 (context):
    try:
        dash = context.driver.find_element_by_xpath("//h2[contains(text(),'Home')]")
        dashtext = dash.text
    except:
        context.driver.close ()
        assert False, "fail"
    if (dashtext == "HOME"):
        assert True, "login successfully"


@when ('Go to Issuer Fraud Management page')
def step_impl (context):
    ###Press Issuer Fraud Management page
    issrmgt= context.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/ul/li/a")
    issrmgt.click()


@when ('Select Detection Card Payments section')
def step_impl (context):
    ###select Detection
    context.driver.find_element_by_xpath ("//a[contains(text(),'Detection')]").click ()
    ###select Card Payments section
    context.driver.find_element_by_xpath ("//a[contains(text(),'Card Payments')]").click ()

    # context.driver.close()


@when ('search card payment by "{ACC_ID}", "{ACC_Country}", "{MCC}", "{Pan_Reference}", "{Terminal_ID}", "{Clear_Pan}"')
def step_impl (context, ACC_ID, ACC_Country, MCC, Pan_Reference, Terminal_ID, Clear_Pan):
    ###Enter correct ACC_ID 
    context.driver.find_element_by_id ("acceptorId").send_keys (ACC_ID)
    context.driver.find_element_by_id ("acceptorCountryDropDown").send_keys (ACC_Country)
    context.driver.find_element_by_id ("mccIDDropDown").send_keys (MCC)
    context.driver.find_element_by_id ("panReference").send_keys (Pan_Reference)
    context.driver.find_element_by_id ("cardPymtTerminalId").send_keys (Terminal_ID)
    context.driver.find_element_by_id ("clearPan").send_keys (Clear_Pan)


@when ('search card payment by accid&country "{ACC_ID}", "{ACC_Country}"')
def step_impl (context, ACC_ID, ACC_Country):
    ###Enter correct ACC_ID, country
    context.driver.find_element_by_id ("acceptorId").send_keys (ACC_ID)
    context.driver.find_element_by_id ("acceptorCountryDropDown").send_keys (ACC_Country)


@when ('search card payment by accid&mcc "{ACC_ID}", "{MCC}"')
def step_impl (context, ACC_ID, MCC):
    ###Enter correct ACC_ID, mcc
    context.driver.find_element_by_id ("acceptorId").send_keys (ACC_ID)
    context.driver.find_element_by_id ("mccIDDropDown").send_keys (MCC)


@when ('search card payment by accid&panref "{ACC_ID}", "{Pan_Reference}"')
def step_impl (context, ACC_ID, Pan_Reference):
    ###Enter correct ACC_ID, panref
    context.driver.find_element_by_id ("acceptorId").send_keys (ACC_ID)
    context.driver.find_element_by_id ("panReference").send_keys (Pan_Reference)


@when ('search card payment by accid&termid "{ACC_ID}", "{Terminal_ID}"')
def step_impl (context, ACC_ID, Terminal_ID):
    ###Enter correct ACC_ID, termid
    context.driver.find_element_by_id ("acceptorId").send_keys (ACC_ID)
    context.driver.find_element_by_id ("cardPymtTerminalId").send_keys (Terminal_ID)


@when ('search card payment by mcc&acccountry "{MCC}", "{ACC_Country}"')
def step_impl (context, MCC, ACC_Country):
    ###Enter correct ACC_coutry, mcc
    context.driver.find_element_by_id ("mccIDDropDown").send_keys (MCC)
    context.driver.find_element_by_id ("acceptorCountryDropDown").send_keys (ACC_Country)


@when ('search card payment by "{ACC_ID}"')
def step_impl (context, ACC_ID):
    ###Enter correct ACC_ID
    context.driver.find_element_by_id ("acceptorId").send_keys (ACC_ID)


@when ('assert result by accid"{ACC_ID}"')
def step_impl (context, ACC_ID):
    ###Checking
    rpp = context.driver.find_element_by_id ("rppSelect")
    rpp.click ()
    sel500 = context.driver.find_element_by_xpath (
        "/html/body/div[4]/div[2]/div/div[1]/form/div[2]/div[2]/div[1]/p[1]/select/option[6]")
    sel500.click ()
    time.sleep (5)
    count = context.driver.find_element_by_xpath (
        "/html/body/div[4]/div[2]/div/div[1]/form/div[2]/div[2]/div[1]/p[2]/strong").text
    print (count)
    num = int(count) + 1
    print (num)
    accids = []
    x = range (1, num)
    for i in x:
        print ('/html/body/div[4]/div[2]/div/div[1]/form/div[2]/div[2]/div[2]/table/tbody/tr[' + str (
            ++i) + ']/td[5]')
        rowi = context.driver.find_element_by_xpath (
            "/html/body/div[4]/div[2]/div/div[1]/form/div[2]/div[2]/div[2]/table/tbody/tr[" + str (
                ++i) + "]/td[5]")
        cont = rowi.text
        accids.append (cont)
        assert (ACC_ID == cont), "wrong result"
    print (accids)


@when ('search  by "{ACC_Country}"')
def step_impl (context, ACC_Country):
    ###Enter correct ACC_Country
    context.driver.find_element_by_id ("acceptorCountryDropDown").send_keys (ACC_Country)


@when ('assert result by Acc_country"{ACC_Country}"')
def step_impl (context, ACC_Country):
    ###Checking
    rpp = context.driver.find_element_by_id ("rppSelect")
    rpp.click ()
    sel500 = context.driver.find_element_by_xpath (
        "/html/body/div[4]/div[2]/div/div[1]/form/div[2]/div[2]/div[1]/p[1]/select/option[6]")
    sel500.click ()
    time.sleep (2)
    count = context.driver.find_element_by_xpath (
        "/html/body/div[4]/div[2]/div/div[1]/form/div[2]/div[2]/div[1]/p[2]/strong").text
    print (count)
    num = int(count) + 1
    print (num)
    acccountries = []
    x = range (1, num)
    for i in x:
        print ('/html/body/div[4]/div[2]/div/div[1]/form/div[2]/div[2]/div[2]/table/tbody/tr[' + str (
            ++i) + ']/td[30]/label')
        rowi = context.driver.find_element_by_xpath (
            "/html/body/div[4]/div[2]/div/div[1]/form/div[2]/div[2]/div[2]/table/tbody/tr[" + str (
                ++i) + "]/td[30]/label")
        cont = rowi.text
        acccountries.append (cont)
        assert (ACC_Country == cont), "wrong result"
    print (acccountries)


@when ('searching  by "{MCC}"')
def step_impl (context, MCC):
    ###Enter correct MCC
    context.driver.find_element_by_id ("mccIDDropDown").send_keys (MCC)


@when ('assert result by mcc"{MCC}"')
def step_impl (context, MCC):
    ###Checking
    rpp = context.driver.find_element_by_id ("rppSelect")
    rpp.click ()
    sel500 = context.driver.find_element_by_xpath (
        "/html/body/div[4]/div[2]/div/div[1]/form/div[2]/div[2]/div[1]/p[1]/select/option[6]")
    sel500.click ()
    time.sleep (2)
    count = context.driver.find_element_by_xpath (
        "/html/body/div[4]/div[2]/div/div[1]/form/div[2]/div[2]/div[1]/p[2]/strong").text
    print (count)
    num = int(count) + 1
    print (num)
    mccs = []
    x = range (1, num)
    for i in x:
        print ('/html/body/div[4]/div[2]/div/div[1]/form/div[2]/div[2]/div[2]/table/tbody/tr[' + str (
            ++i) + ']/td[12]/label')
        rowi = context.driver.find_element_by_xpath (
            "/html/body/div[4]/div[2]/div/div[1]/form/div[2]/div[2]/div[2]/table/tbody/tr[" + str (
                ++i) + "]/td[12]/label")
        cont = rowi.text
        mccs.append (cont)
        assert (MCC == cont), "wrong result"
    print (mccs)


@when ('search_by "{Pan_Reference}"')
def step_impl (context, Pan_Reference):
    ###Enter correct MPanRef
    context.driver.find_element_by_id ("panReference").send_keys (Pan_Reference)
@when ('assert pan_ref result by "{Masked_Pan}"')
def step_impl (context, Masked_Pan):
    ###Enter correct MPanRef
    #context.driver.find_element_by_id ("panReference").send_keys (Pan_Reference)
    ###Checking
    rpp = context.driver.find_element_by_id("rppSelect")
    rpp.click()
    sel500 = context.driver.find_element_by_xpath(
        "/html/body/div[4]/div[2]/div/div[1]/form/div[2]/div[2]/div[1]/p[1]/select/option[6]")
    sel500.click()
    time.sleep(2)
    count = context.driver.find_element_by_xpath(
        "/html/body/div[4]/div[2]/div/div[1]/form/div[2]/div[2]/div[1]/p[2]/strong").text
    print(count)
    num = int(count) + 1
    print(num)
    masks = []
    x = range(1, num)
    for i in x:
        print('/html/body/div[4]/div[2]/div/div[1]/form/div[2]/div[2]/div[2]/table/tbody/tr[' + str(
            ++i) + ']/td[4]')
        rowi = context.driver.find_element_by_xpath(
            "/html/body/div[4]/div[2]/div/div[1]/form/div[2]/div[2]/div[2]/table/tbody/tr[" + str(
                ++i) + "]/td[4]")
        cont =  rowi.text
        print (cont)
        masks.append(cont)
        assert (Masked_Pan == cont), "wrong pan ref result"
    print(masks)


@when ('searchby  "{Terminal_ID}"')
def step_impl (context, Terminal_ID):
    ###Enter correct TermId
    context.driver.find_element_by_id ("cardPymtTerminalId").send_keys (Terminal_ID)

@when ('search card payment by pan "{Clear_Pan}"')
def step_impl (context, Clear_Pan):
    ###Enter correct PAN
    context.driver.find_element_by_id ("clearPan").send_keys (Clear_Pan)
@when ('search card payment by *pan and dates "{Clear_Pan}"')
def step_impl (context, Clear_Pan):
    ###Enter correct PAN
    #no_res = context.driver.find_element_by_id("empty").text
    #if (no_res=="No Records to Display"):
       #print("Clear pan filter doesn't work properly.")
    #else:
        #count = context.driver.find_element_by_xpath(
           # "//p[@class='total']").text
   # print(count)
    #calendarcpfr=context.driver.find_element_by_id("cardPymtTransactionDateFrom-trigger")
    #context.calendarcpfr.click()
    time.sleep(2)
    datefrom = context.driver.find_element_by_id("cardPymtTransactionDateFrom")
    datefrom.click()
    datefrom.clear()
    datefrom.send_keys("01/07/2020")
    cpbox=context.driver.find_element_by_id("clearPan")
    cpbox.click()
    cpbox.clear()
    cpbox.send_keys("*")



@when('Error message is present or not?')
def step_impl (context):
    error = context.driver.find_element_by_id("ferror")
    errormsg = error.text
    print(errormsg, "so feature *pan is working")
    assert (errormsg== "Please enter valid clear pan") is False
    pass


@when ('click on reset button')
def step_impl (context):
    ###Press reset button
    ###Reset all filled fields
    context.driver.find_element_by_id ("btreset").click ()
    time.sleep(5)


@when ('click on next results')
def step_impl (context):
    context.driver.find_element_by_xpath (
        "//strong[contains(text(),'Click here for the next results')]").click ()


@when ('click on filter button')
def step_impl (context):
    ###click on filter button
    time.sleep (2)
    context.driver.find_element_by_id ("btfilter").click ()
    time.sleep (5)
    #Card_payments_search_result = context.driver.find_element_by_xpath (
        #"//tr[@class='(blank) t-first']//td[@class='acceptorId'][contains(text(),'1095822540')]").text
    #with open (r"C:\Users\geghamy\Desktop\Card_search_results\Card_payments_search_result.txt", "w+") as file:
        #file.write (Card_payments_search_result)


@Then ('close the browser')
def step_impl (context):
    time.sleep (5)
    ###Reset all filled fields
    context.driver.close ()
