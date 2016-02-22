-- Based on: https://wiki.postgresql.org/wiki/First/last_%28aggregate%29

-- Create a function that always returns the last non-NULL item
CREATE OR REPLACE FUNCTION public.last_agg ( anyelement, anyelement )
RETURNS anyelement LANGUAGE sql IMMUTABLE STRICT AS $$
    SELECT $2;
$$;

-- And then wrap an aggregate around it
CREATE AGGREGATE public.last (
    sfunc    = public.last_agg,
    basetype = anyelement,
    stype    = anyelement
);