-- Based on: https://wiki.postgresql.org/wiki/First/last_%28aggregate%29

-- Create a function that always returns the first non-NULL item
CREATE OR REPLACE FUNCTION public.first_agg ( anyelement, anyelement )
RETURNS anyelement LANGUAGE sql IMMUTABLE STRICT AS $$
    SELECT $1;
$$;

-- And then wrap an aggregate around it
CREATE AGGREGATE public.first (
    sfunc    = public.first_agg,
    basetype = anyelement,
    stype    = anyelement
);