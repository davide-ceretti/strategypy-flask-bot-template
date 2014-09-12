strategypy-bot-example
======================

An example bot for the strategypy game, running on a flask web service docker container.
The web service listen to strategypy json contexts and send back the action to execute.

It is currently running at
strategypy-bot-example-davide-ceretti.delta.tutum.io:49158

System dependencies
-------------------

Docker


Quickstart
----------

```
./install.sh
./run.sh

```

Test
----

```
# (in your virtualenv)
# (with your application running)
pip install -r test-requirements.txt
python test.py
```
