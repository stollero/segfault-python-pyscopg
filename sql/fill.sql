DO $$
BEGIN
    FOR i IN 1..1000000 LOOP
        INSERT INTO current_object (zoid, tid) VALUES (i, 100 + i);
        INSERT INTO object_state (zoid, tid, state) VALUES (i, 100 + i, CASE WHEN i % 2 = 0 THEN 'E' ELSE 'O' END);
    END LOOP;
END$$;