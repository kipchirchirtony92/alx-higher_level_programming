-- create the user_0d_1 having all the privileges
CREATE USER
       IF NOT EXISTS 'user_0d_1'@'localhost'
       IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
      ON *.*
      TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
