CREATE DATABASE remotejob;

CREATE USER ubuntu WITH PASSWORD 'password@123';
ALTER ROLE ubuntu SET client_encoding TO 'utf8';
ALTER ROLE ubuntu SET default_transaction_isolation TO 'read committed';
ALTER ROLE ubuntu SET timezone TO 'UTC';