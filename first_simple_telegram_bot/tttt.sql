BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "music" (
	"Id"	INTEGER,
	"file_id"	TEXT,
	"right_asnwer"	TEXT,
	"wrong_answer"	TEXT,
	PRIMARY KEY("Id" AUTOINCREMENT)
);
COMMIT;
