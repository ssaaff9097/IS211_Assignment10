CREATE TABLE Artists(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE Albums(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    artist_id INT,
    FOREIGN KEY (artist_id)
 REFERENCES Artists(id)
 );

 CREATE TABLE Songs(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    album_id INT,
    track_number INT NOT NULL,
    duration INT NOT NULL,
    FOREIGN KEY (album_id) REFERENCES Albums(id)
 );
