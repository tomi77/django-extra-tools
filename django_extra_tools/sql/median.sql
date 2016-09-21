-- Based on: https://wiki.postgresql.org/wiki/Aggregate_Median

CREATE OR REPLACE FUNCTION _final_median(NUMERIC [])
    RETURNS NUMERIC AS
$$
SELECT AVG(val)
FROM (
         SELECT val
         FROM unnest($1) val
         ORDER BY 1
         LIMIT 2 - MOD(array_upper($1, 1), 2)
         OFFSET CEIL(array_upper($1, 1) / 2.0) - 1
     ) sub;
$$
LANGUAGE 'sql' IMMUTABLE;

DROP AGGREGATE IF EXISTS median( NUMERIC );

CREATE AGGREGATE median( NUMERIC ) (
SFUNC = array_append,
STYPE = NUMERIC [],
FINALFUNC = _final_median,
INITCOND = '{}'
);

CREATE OR REPLACE FUNCTION _final_median(double precision [])
    RETURNS DOUBLE PRECISION AS
$$
SELECT AVG(val)
FROM (
         SELECT val
         FROM unnest($1) val
         ORDER BY 1
         LIMIT 2 - MOD(array_upper($1, 1), 2)
         OFFSET CEIL(array_upper($1, 1) / 2.0) - 1
     ) sub;
$$
LANGUAGE 'sql' IMMUTABLE;

DROP AGGREGATE IF EXISTS median( DOUBLE PRECISION );

CREATE AGGREGATE median( DOUBLE precision ) (
SFUNC = array_append,
STYPE = DOUBLE PRECISION [],
FINALFUNC = _final_median,
INITCOND = '{}'
);

CREATE OR REPLACE FUNCTION _final_median(INTERVAL [])
    RETURNS INTERVAL AS
$$
SELECT AVG(val)
FROM (
         SELECT val
         FROM unnest($1) val
         ORDER BY 1
         LIMIT 2 - MOD(array_upper($1, 1), 2)
         OFFSET CEIL(array_upper($1, 1) / 2.0) - 1
     ) sub;
$$
LANGUAGE 'sql' IMMUTABLE;

DROP AGGREGATE IF EXISTS median( INTERVAL );

CREATE AGGREGATE median( INTERVAL ) (
SFUNC = array_append,
STYPE = INTERVAL [],
FINALFUNC = _final_median,
INITCOND = '{}'
);