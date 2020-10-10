CREATE TABLE sensors (
 ID int(11) NOT NULL,
 barcode varchar(45),
 name varchar(45),
 type varchar(45),
 number int(11),
 PRIMARY KEY(ID)
);

INSERT INTO (ID, barcode, name, type, number)
(1, "99455941-01-850-00078", "raw water pressure", "RPS", 1),
(2, "98638142-12-020-00038", "raw water mfs", "MFS", 2),
(3, null, "vfs permate", "VFS", 3),
(4, null, "circulation mfs", "MFS", 4),
(5, null, "waterlevel tank", "RPS", 5);
