CREATE TABLE outputs (
 ID int(11) NOT NULL,
 type varchar(45),
 Name varchar(45),
 FK_values int(11),
 ready bit(1),
 feedback_in int(32),
 ready_pin int(11),
 run_pin int(11),
 feedback_pin int(11),
 active bit(1) DEFAULT b'1',
 FK_values_disorder int(11),
 PRIMARY KEY(ID)
 );

INSERT INTO (ID, type, Name, FK_values, ready, feedback_in, ready_pin, run_pin, feedback_pin, active, FK_values_disorder)
(1, "pump", "Antiskalantpumpe", 34, 0, 0, 19, 26, 13, 1, 4),
(2, "pump", "Feedpumpe", 35, 0, 0, 16, 20, 21, 0, 4),
(3, "ventil", "Rohwasserventil", 32, null, null, null, 22, null, 1, 4),
(4, "ventil", "Konzentratventil", 33, null, null, null, 23, null, 1, 4) ;
