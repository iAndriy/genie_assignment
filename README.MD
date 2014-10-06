Genie Code Assignment
===

About
-----

### Intro ###
The goal of this assignment is to build a set of Selenium-based unit tests which run against a Tornado Web server running a static version of Semantic UI documentation pages.

### Goals ###
The project repository should include all resources including a setup.py to run the included tests. Selenium should use either Chrome or Firefox to run the tests and should include tests which follow pages through link clicking.

### Hints ###
Tornado can be run in a background process instantiated within the setup of a unit test (see tornado asynctestcase).
The website documentation branch of Semantic UI exists in the gh_pages branch of their github repository.
Use pytest or nosetest for simpler and more full featured testing in python.

### Extra Credit ###
Use selenium to manipulate a page to cause a normally unintended consequence such as removing an element or manipulating a link href attribute.
Inject JavaScript into the page in one step, and call one of the injected variables later on in the test.


Setup
-----
### System Requirements ###
    * Python 2
    * Xvfb

### Semantic-UI ###
Semantic-UI repo is added as submodule of genie_assignment.git. To pull changes from Semantic-UI repo please run:

        $ git submodule update --init
        $ git submodule update --remote

### Install ###
To install package please run:

        $ python setup.py install

### Tests ###
To run tests please run:

        $ python setup.py nosetests