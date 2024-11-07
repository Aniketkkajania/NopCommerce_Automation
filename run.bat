pytest -v -s -p no:warnings -m "sanity" --html=./Reports/report.html testCases/ --browser chrome
::python -v -s -p no:warnings -m "regression" --html=./Reports/report.html --browser chrome
::python -v -s -p no:warnings -m "sanity or regression" --html=./Reports/report.html --browser chrome
::python -v -s -p no:warnings -m "sanity and regression" --html=./Reports/report.html --browser chrome

::C:\QA SDET\Hybrid Framework\
