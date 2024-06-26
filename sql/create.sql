CREATE TABLE current_object (
    zoid INTEGER PRIMARY KEY,
    tid INTEGER
);

CREATE TABLE object_state (
    zoid INTEGER,
    tid INTEGER,
    state CHAR,
    PRIMARY KEY (zoid, tid),
    FOREIGN KEY (zoid) REFERENCES current_object(zoid)
);