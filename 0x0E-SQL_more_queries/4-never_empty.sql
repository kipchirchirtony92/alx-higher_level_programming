-- script that create table id_not_null
-- set the DEFAULT value of id to 1
-- set the name constraint to VARCHAR(256)

CREATE TABLE IF NOT EXISTS `id_not_null`(
       `id` INT DEFAULT 1,
       `name` VARCHAR(256)
);
