# umuc-cs-slack

A Django web app for automating the invite process for the UMUC-CS Slack team that is currently deployed on Heroku:

[UMUC-CS Slack Invite Page](https://umuc-cs-slack.herokuapp.com)

This project is powered by the [Django Slack Invite Tool](https://github.com/sanchagrins/SlackInvite).

## Development
Interested in helping contribute to the community? Please see [CONTRIBUTING.md](https://github.com/umuc-cs/umuc-cs-slack/CONTRIBUTING.md) for more details on how to properly configure the web application for local development and other guidelines.

## Setup

### Requirements
Make sure you have the following installed:

* Python 3.6
* pip3
* [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)/[Vivrtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/install.html)
* [Heroku Toolbelt](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

### Setting up the Development Environment

Create your virtual environments, specifying the path to python3:

    $ mkvirtualenv --python=/usr/bin/python3 dev

    $ mkvirtualenv --pytohn=/usr/bin/python3 prod

    $ mkvirtualenv --python=/usr/bin/python3 test

Set the local environment variables in the [postactivate](#) and [predactive](#) scripts.

Switch to the dev environment and install the required packages:

    $ workon dev
    (dev)$ pip install -r requirements.txt

### Test the local Development Environment

Verify the local Django web server:

    (dev)$ python slack_invite/manage.py runserver

Open your web browser and navigate to `http://localhost:8000`

Terminate the local Django server from the command line with `Ctrl+c`

Switch to the production environment and verify the local Heroku Server:

    (dev)$ deactivate
    $ workon prod
    (prod)$ heroku local

Open your web browser and navigate to `http://localhost:5000`

### Functional Testing

Switch to the test environment and verify that the functional tests pass:

    (prod)$ deactivate
    $ workon test
    (test)$ python slack_invite/manage.py test