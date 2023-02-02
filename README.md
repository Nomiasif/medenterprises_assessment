# medenterprises_assessment
This repo contains the automation code related to acceptance tests of Medenterprises

I have used python as the scripting language, pyCharm as the IDE and pytest as the automation framework along with selenium to complete assessment.

Moreover, to install all the required plugins, one can simply run the following command in the pyCharm terminal:

pip install -r requirements.txt

To execute the automated cases along with html report, following commmand can be exected in the pyCharm terminal:

pytest .\features\tests\test_acceptance_cases.py --html=reports\tests_execution_report.html
