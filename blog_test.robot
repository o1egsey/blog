*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Keywords ***
Login
    [Arguments]    ${username}    ${password}
    Open Browser    http://127.0.0.1:8000/account/login/    chrome  options=add_argument("--headless")
    Set Window Size    982    823
    Click Element    css=.account-form
    Input Text    id=login-username    ${username}
    Input Text    id=login-pwd    ${password}
    Click Element    css=.login
    Click Element    css=.btn-primary

*** Test Cases ***
Test Successful Registration
    Open Browser    http://127.0.0.1:8000/account/register/    chrome   options=add_argument("--headless")
    Click Element    id=id_user_name
    Input Text    id=id_user_name    123asddff.asassedff334aaa1a
    Click Element    id=id_email
    Input Text    id=id_email    123a1aasdvffff.asdd12faa34sa3sd@eexample.com
    Click Element    id=id_password
    Input Text    id=id_password    asdf@1234
    Click Element    id=id_password2
    Input Text    id=id_password2    asdf@1234
    Click Element    css=.btn-primary
    Page Should Contain    Реєстрація успішна!
    Page Should Contain Element    css=.btn:nth-child(3)
    Page Should Contain Element    css=.btn:nth-child(4)
    Close Browser

Test Successful Login
    Open Browser    http://127.0.0.1:8000/account/login/    chrome  options=add_argument("--headless")
    Click Element    css=.account-form
    Input Text    id=login-username    123a1aasdvffff.asdd12faa34sa3sd@eexample.com
    Input Text    id=login-pwd    asdf@1234
    Click Element    css=.login
    Click Element    css=.btn-primary
    Page Should Contain Element    css=.btn:nth-child(3)
    Page Should Contain Element    css=.btn:nth-child(4)
    Close Browser

Test View Profile
#    Login   1aaasdvfff.asdd12faa34sa3sd@example.com     asdf@1234
    Open Browser    http://127.0.0.1:8000/account/login/    chrome  options=add_argument("--headless")
    Click Element    css=.account-form
    Input Text    id=login-username    123a1aasdvffff.asdd12faa34sa3sd@eexample.com
    Input Text    id=login-pwd    asdf@1234
    Click Element    css=.login
    Click Element    css=.btn-primary
    ${title}    Get Title
    Log To Console    Page title: ${title}
    Click Element    css=.btn:nth-child(3)
    Title Should Be    My Profile
    Page Should Contain Element    css=.btn:nth-child(4)
    Close Browser

Test Successful Land On Add Blog Post
    Login    1aaasdvfff.asdd12faa34sa3sd@example.com    asdf@1234
    ${title}    Get Title
    Log To Console    Page title: ${title}
    Set Window Size    982    823
    Click Element    xpath=//*[@id="add-post"]
    Title Should Be    Add New Post
    Close Browser

Test Successful Add Blog Post
    Login    1aaasdvfff.asdd12faa34sa3sd@example.com    asdf@1234
    ${title}    Get Title
    Log To Console    Page title: ${title}
    Click Element    xpath=//*[@id="add-post"]
    Input Text    xpath=//*[@id="title"]    Some title
    Input Text    xpath=//*[@id="content"]    Some body
    Click Element    xpath=//*[@id="add-post"]
    Page Should Contain Element    css=.message
    Close Browser

#Test Successful Add Comment
#    Login    1aaasdvfff.asdd12faa34sa3sd@example.com    asdf@1234
#    Set Window Size    982    823
#    Click Element    link=Some title
#    Title Should Be    Post Detail Page
#    Input Text    id=id_content    asdf
#    Click Element    css=.btn-primary:nth-child(3)
#    Page Should Contain Element    css=.message
#    Page Should Contain    asdf
#    Close Browser
#
#
#Test Edit Profile
#    Login    1aaasdvfff.asdd12faa34sa3sd@example.com    asdf@1234
#    Set Window Size    982    823
#    Click Element    css=.bi-person
#    Click Element    css=.col-12
#    Clear Element Text    id=firstname
#    Input Text    id=firstname    ashis
#    Click Element    css=.login
#    Clear Element Text    id=lastname
#    Input Text    id=lastname    raj
#    Clear Element Text    id=age
#    Input Text    id=age    25
#    Clear Element Text    id=website
#    Input Text    id=website    https://example.com
#    Select From List By Label    id=gender    Чоловік
#    Capture Page Screenshot    screenshot.png
#    Click Element    css=.btn-primary
#    Page Should Contain Element    css=.message
#    Close Browser
