@echo off 

:: login to breatheHR
call login_site.exe

:: close browser driver with window
taskkill /im chromedriver.exe /f
