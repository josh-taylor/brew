# Brew Manager

Just a sample "fun" app for managing who's turn it is to make the brew.

## Useage

To use server run:

```shell
python server.py
```

Then use the client to add to the users tally or voting that you're ready for a brew by giving a list of arguments.

```shell
python client.py -c add -a Josh

python client.py -c vote -a Josh
```

## License

See the COPYING file
