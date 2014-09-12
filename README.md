strategypy-bot-example
======================

An example bot for the strategypy game.

Install
-------

```
sudo docker build -t bot-example .
```

Run
---

```
sudo docker run -t -i --rm -p 8000:8000 -v `pwd`:/code/work bot-example
curl localhost:8000
```
