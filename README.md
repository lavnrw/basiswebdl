# basiswebdl

BASIS-Web is an administration software for prisons. This tool talks to its
archival export interface.

## Installation

You need Python and the [lxml](https://pypi.org/project/lxml/) and
[requests](https://pypi.org/project/requests/) packages. Use your preferred
installation methods; for development something like
[pipenv](https://pipenv.pypa.io/) with the provided [Pipfile](./Pipfile) is
recommended

## Usage

Adapt the [example config file](./basiswebdl.ini.example) to contain the proper
connection details (host, user name, password) of the BASIS-Web instance you
wish to export data from and, optionally, adjust additional settings. The
configuration can also be specified using command line options; run `basiswebdl
--help` for details.

Now suppose you know that data is available from prisons 512 and 514. The
following command will download the respective XML records to ZIP files
`512.zip` and `514.zip`, warning about obvious errors like missing files,
invalid XML (only if you provide a schema file), and names that look
suspiciously short or contain funny symbols.

~~~
$ basiswebdl export 512 514
INFO: Exported 512.zip
INFO: VALID 2a11987a-abc8-430b-9efd-7ac660032f53
INFO: Exported 514.zip
INFO: VALID 04215618-6907-4db8-9059-62444923a49f
~~~

Make sure the data you downloaded is what you expect, then acknowledge you
received it using the UUIDs from the `basiswebdl export` command output:

~~~
$ basiswebdl commit 2a11987a-abc8-430b-9efd-7ac660032f53 04215618-6907-4db8-9059-62444923a49f
INFO: Commited 2a11987a-abc8-430b-9efd-7ac660032f53
INFO: Commited 04215618-6907-4db8-9059-62444923a49f
~~~

Note that if you specify a log level other than INFO (default) or DEBUG the UUID
won't be printed. It can still be found in the `TransaktionsId` element of the
`rueckgrat.xml` file in the downloaded ZIP though.

You can skip the manual `commit` step altogether by using the `--autocommit`
command line flag (or the respective setting in the config file) to make
`basiswebdl` automatically commit a transaction if it found no errors:

~~~
$ basiswebdl --autocommit export 512 514
INFO: Exported 512.zip
INFO: VALID 2a11987a-abc8-430b-9efd-7ac660032f53
INFO: Commited 2a11987a-abc8-430b-9efd-7ac660032f53
INFO: Exported 514.zip
INFO: VALID 04215618-6907-4db8-9059-62444923a49f
INFO: Commited 04215618-6907-4db8-9059-62444923a49f
~~~

## Development

There is a very simple local mock API server for local tests. Make sure you have
installed [flask](https://pypi.org/project/Flask/), then run and query it like
this:

~~~
$ ./testserver/run
$ basiswebdl --config testserver/basiswebdl.ini export 666
~~~
