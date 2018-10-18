# resolve-comments
# Environment

Project uses virtualenv [https://packaging.python.org/guides/installing-using-pip-and-virtualenv/] for
package management. 
To get started run 
        `python3 -m pip install virtualenv

If you encounter any trouble please visit the linked virtualenv installation page. 
To install the packages and replicate the environment, CD into the project root folder and run
        `pipenv install`
In case you install any packages crucial to the development of your user story don't forget to update
your requirements.txt using 
         `pip freeze > requirements.txt`

To make your life easier, consider using Pycharm Pro which can be obtained using your columbia student email. 
It will automatically detect you are using virtual env and handle a lot of things for you. 
## Coding style and code standards

The project will use PEP8 python coding standards. If you guys find any additional linting needed or unnecessary we shall
address it. Pylint will enforce coding style, documentation, error detection and refactoring. A number of precommit hooks have
been installed to ensure that JSON is properly formatted, no trailing white spaces, detect private keys, fix requirents.txt,
enforce pylint's code standards and ensure no one ever commits directly to Master. 

A continuos integration service will be established to ensure Master is always green, builds successfully and that basic code
coverage meets a particular standard. The goal is to ensure at any point, master has something that can be a demo. 

## Code reviews

All pull requests are subject to review by another team member after they have passed the precommit checks and Continuos integration
 checks before getting merged in.