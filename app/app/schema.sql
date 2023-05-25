DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS donation;

CREATE TABLE book (
    isbn        varchar(20),
    title       varchar(30),
    author      varchar(30),
    local_dir   varchar(50),
    PRIMARY KEY (isbn)
);

CREATE TABLE user (
    user_id     varchar(10),
    username    varchar(30),
    user_type   integer DEFAULT 2,  -- 0: admin, 1: member, 2: admin
    password    varchar(20),
    PRIMARY KEY (user_id)
);

CREATE TABLE donation (
    donation_id varchar(10),
    amount      integer,
    PRIMARY KEY (donation_id)
);