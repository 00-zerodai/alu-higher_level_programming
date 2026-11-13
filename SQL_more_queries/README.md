# SQL - More Queries

This project contains MySQL scripts for user privileges, table constraints,
foreign keys, subqueries, and joins.

The scripts are intended for MySQL 8.0. Scripts that operate on an existing
database can be run by passing its name to the MySQL client, for example:

```sh
mysql -uroot -p hbtn_0d_usa < 8-cities_of_california_subquery.sql
```

Scripts `0-privileges.sql` and `1-create_user.sql` and `2-create_read_user.sql`
run without selecting a database. The `6-states.sql` and `7-cities.sql` scripts
create the `hbtn_0d_usa` database and their respective tables.
