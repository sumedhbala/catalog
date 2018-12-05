# Project Title

Application to maintain a catalog of Items.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Python 2.7.X https://www.python.org/downloads/
Virtualenv https://virtualenv.pypa.io/en/latest/
Docker (for development) https://www.docker.com/get-started
```

### Installing

Download the project from github

```
git clone https://github.com/sumedhbala/catalog.git
```

start the virtualenv inside the project 
https://virtualenv.pypa.io/en/latest/userguide/#usage

```
cd /path/to/project && virtualenv $ENV && source /path/to/$ENV/bin/activate
```

Install the python requirements

```
pip install -r requirements.txt
```


## Running the tests

NA


### coding style.

The project uses black for enforcing coding style in the python files. Since black requires python3 it is
implemented inside a docker container.
To run the coding checks

```
cd /path/to/project/ && docker build  ./ -t $tag_name && docker run -v path/to/project:/tmp $tag_name
```

## Deployment

Enter the type of environment being run using the variable FLASK_ENV in .flaskenv in the project directory.
The different types of environments are defined in path/to/project/app/config.py

From the virtual environment

```
cd /path/to/project && python run.py
```

OR

```
cd /path/to/project && flask run
```

The website should be accessible via http://127.0.0.1:5000/ on the machine that is running the application.


## Built With

* Language: Python 2.7.X
* Framework: Flask + SQLAlchemy + Flask-Login + Flask-WTF
* UI: Bootstrap4 + Jinja + DataTables

## Contributing

NA

## Versioning

NA

## Authors

* Sumedh Bala

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

