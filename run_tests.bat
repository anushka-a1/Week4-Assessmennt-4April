@echo off

call .venv\Scripts\activate.bat

if not exist reports mkdir reports

pytest tests ^
 --html=reports\test_report.html ^
 --self-contained-html ^
 --junitxml=reports\junit_report.xml ^
 -v ^
 --tb=short
