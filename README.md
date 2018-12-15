# resolve-comments

Resolve-Comments is a Sublime text 3 plugin that allows users to view their Github issues and pull requests within their terminal, eliminating the need to switch between browser tabs and your editing environnment.

# Setup

To initialize this Sublime Text 3 Plugin on Linux  machines simply clone the repository in the following directory:

        ~/.config/sublime-text-3/Packages/

For Mac machines:
        `/Users/{user}/Library/Application Support/Sublime Text 2/Packages`
Mac Machines might also require an install of some xcode tools with the terminal line below:
        ```xcode-select --install```

The plugin must be run in the Sublime Text 3 interface within a folder that has an initialized git repository. To run the plugin simply click the view tab in the Sublime text interface and click the Show Console option. If done correctly there should be a console on the bottom of the screen. Starting the plugin requires running the following command in the console:

        view.run_command("insert_panel")
        
On running this command you will be promped with a username and password on the bottom of the screen. Type your Github username and password to run the plugin. Given that the authentication is correct the user should be presented with a panel of issues and pull requests that are searchable and selectable. 
 
`
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

To ensure all pre-commit hooks are enforced run this from the project root directory.
        `precommit install`

## Coding style and code standards

The project will use PEP8 python coding standards. If you guys find any additional linting needed or unnecessary we shall
address it. Pylint will enforce coding style, documentation, error detection and refactoring. A number of precommit hooks have
been installed to ensure that JSON is properly formatted, no trailing white spaces, detect private keys, fix requirents.txt,
enforce pylint's code standards and ensure no one ever commits directly to Master. To have an easy time, set your editor or IDE
to PEP8 coding style and install the linting file. 

A continuos integration service will be established to ensure Master is always green, builds successfully and that basic code
coverage meets a particular standard. The goal is to ensure at any point, master has something that can be a demo. 

## Code reviews

All pull requests are subject to review by another team member after they have passed the precommit checks and Continuos integration
 checks before getting merging in
 https://travis-ci.com/Raphaeljunior/resolve-comments/builds
 
