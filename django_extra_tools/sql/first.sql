-- Based on: https://wiki.postgresql.org/wiki/First/last_(aggregate)

-- Create a function that always returns the first non-NULL item
CREATE OR REPLACE FUNCTION public.first_agg(ANYELEMENT, ANYELEMENT)
    RETURNS ANYELEMENT LANGUAGE SQL IMMUTABLE STRICT AS $$
SELECT $1;
$$;

DROP AGGREGATE IF EXISTS public.first( ANYELEMENT );

-- And then wrap an aggregate around it
CREATE AGGREGATE public.first (
SFUNC = PUBLIC.first_agg,
BASETYPE = ANYELEMENT,
STYPE = ANYELEMENT
);