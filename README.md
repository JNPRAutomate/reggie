# reggie
Lab Student Registration Portal



Setup
-----
The Vagrantfile maps the steps to set up a working environment, but if you already have a python environment


To install Reggie requirements:

```bash
pip install -r /reggie/requirements.txt
```

To setup database the first time

```bash
vagrant@Reggie-testvm:/reggie$ python app.py db migrate
INFO  [alembic.migration] Context impl SQLiteImpl.
INFO  [alembic.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'students'
  Generating /reggie/migrations/versions/20b6609c26e0_.py ... done

vagrant@Reggie-testvm:/reggie$ python app.py db upgrade
INFO  [alembic.migration] Context impl SQLiteImpl.
INFO  [alembic.migration] Will assume non-transactional DDL.
INFO  [alembic.migration] Running upgrade  -> 20b6609c26e0, empty message
```

To run Reggie server:

```bash
vagrant@Reggie-testvm:/reggie$ python app.py runserver --host=0.0.0.0 -dr
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
```

