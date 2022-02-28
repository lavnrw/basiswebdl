# basiswebdl

Downloader for BASIS-Web archiving

## Usage

    $ basiswebdl --help

## Development

Use a very simple local mock API server for tests:

    $ cd testserver
    $ pipenv shell
    $ FLASK_APP=testserver flask run
    $ cd ..
    $ python basiswebdl --config testserver/basiswebdl.ini export 123
