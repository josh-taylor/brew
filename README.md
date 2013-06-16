# Brew Manager

Just a "fun" app for managing who's turn it is to make the brew.

### Usage

To use the server run from a terminal:

```shell
python server.py -u user1 -u user2 -u user3
```

Then use the client to add to the users tally or voting that you're ready for a brew by giving a list of arguments.

```shell
python client.py -c add -a Josh

python client.py -c vote -a Josh
```

### Tests

Unit tests can be ran by running the `tests.py` file

```shell
python tests.py
```

### License

See the COPYING file
