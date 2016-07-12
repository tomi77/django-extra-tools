-- Based on: https://wiki.postgresql.org/wiki/First/last_(aggregate)

-- Create a function that always returns the last non-NULL item
CREATE OR REPLACE FUNCTION public.last_agg(ANYELEMENT, ANYELEMENT)
    RETURNS ANYELEMENT LANGUAGE SQL IMMUTABLE STRICT AS $$
SELECT $2;
$$;

DROP AGGREGATE IF EXISTS public.last( ANYELEMENT );

-- And then wrap an aggregate around it
CREATE AGGREGATE public.last (
SFUNC = PUBLIC.last_agg,
BASETYPE = ANYELEMENT,
STYPE = ANYELEMENT
);