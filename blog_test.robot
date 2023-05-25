*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Keywords ***
Login
    [Arguments]    ${username}    ${password}
    Open Browser    http://127.0.0.1:8000/account/login/    chrome  options=add_argument("--headless")
    Set Window Size    982    823
    Input Text    id=login-username    ${username}
    Input Text    id=login-pwd    ${password}
    Click Element    css=.login
    Click Element    css=.btn-primary

*** Test Cases ***
Test Successful Registration
    Open Browser    http://127.0.0.1:8000/account/register/    chrome   options=add_argument("--headless")
    Set Window Size    982    823
    Input Text    id=id_user_name    new_user_for_testing3
    Input Text    id=id_email    new_user_for_testing3@gmail.com
    Input Text    id=id_password    asdf@1234
    Input Text    id=id_password2    asdf@1234
    Click Element    css=.btn-primary
    Page Should Contain    Реєстрація успішна!
    Page Should Contain Element    css=.btn:nth-child(3)
    Page Should Contain Element    css=.btn:nth-child(4)
    Close Browser

Test Successful Login
    Open Browser    http://127.0.0.1:8000/account/login/    chrome  options=add_argument("--headless")
    Click Element    css=.account-form
    Input Text    id=login-username    new_user_for_testing3@gmail.com
    Input Text    id=login-pwd    asdf@1234
    Click Element    css=.login
    Click Element    css=.btn-primary
    Page Should Contain Element    css=.btn:nth-child(3)
    Page Should Contain Element    css=.btn:nth-child(4)
    Close Browser

Test View Profile
    Login   new_user_for_testing3@gmail.com     asdf@1234
    Click Element    css=.btn:nth-child(4)
    Title Should Be    My Profile
    Page Should Contain Element    css=.btn:nth-child(4)
    Close Browser

Test Successful Land On Add Blog Post
    Login    new_user_for_testing3@gmail.com    asdf@1234
    Set Window Size    982    823
    Click Element    xpath=//*[@id="add-post"]
    Title Should Be    Add New Post
    Close Browser

Test Successful Add Blog Post
    Login    new_user_for_testing3@gmail.com    asdf@1234
    Click Element    id=add-post
    Input Text    xpath=//*[@id="title"]    Some title
    Input Text    xpath=/html/body/div/div/div/form/div[2]/textarea   Some body
    Click Element    xpath=//*[@id="add-post"]
    Page Should Contain Element    css=.message
    Close Browser

Test Successful Add Comment
    Login    new_user_for_testing3@gmail.com    asdf@1234
    Set Window Size    982    823
    Click Element    link=Some title
    Title Should Be    Post Detail Page
    Input Text    id=id_content    asdf
    Click Element    css=.btn-primary:nth-child(3)
    Page Should Contain Element    css=.message
    Page Should Contain    asdf
    Close Browser


Test Edit Profile
    Login    new_user_for_testing3@gmail.com    asdf@1234
    Set Window Size    982    823
    Click Element    css=.bi-person
    Click Element    css=.col-12
    Clear Element Text    id=firstname
    Input Text    id=firstname    ashis
    Click Element    css=.login
    Clear Element Text    id=lastname
    Input Text    id=lastname    raj
    Clear Element Text    id=age
    Input Text    id=age    25
    Clear Element Text    id=website
    Input Text    id=website    https://example.com
    Select From List By Label    id=gender    Чоловік
    Capture Page Screenshot    screenshot.png
    Click Element    css=.btn-primary
    Page Should Contain Element    css=.message
    Close Browser
