CREATE TABLE post (
    id serial PRIMARY KEY,
    author text NOT NULL,
    message text NOT NULL,
    created timestamp NOT NULL DEFAULT now()
);

