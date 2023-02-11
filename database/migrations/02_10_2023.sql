BEGIN TRAN T1;

CREATE TABLE public.medications (
	id int NOT NULL,
	medname varchar NOT NULL DEFAULT Unknown,
	datefilled date NULL,
	refillsleft int NULL DEFAULT -1,
	refilldate date NULL,
	timesperday int NULL DEFAULT -1,
	timesperweek int NULL DEFAULT -1,
	folderpath varchar NULL,
	CONSTRAINT medications_pk PRIMARY KEY (id,medname);
);

CREATE TABLE public.confirmations (
	id int NOT NULL,
	medname varchar NOT NULL DEFAULT 'unknown',
	taken bool NULL DEFAULT false,
    medicationid int NOT NULL,
	CONSTRAINT confirmations_pk PRIMARY KEY (id)
);

ALTER TABLE public.confirmations ADD created_at date NULL DEFAULT NOW();

COMMIT TRAN T1;

BEGIN TRAN T2;

ALTER TABLE public.confirmations ADD CONSTRAINT confirmations_fk FOREIGN KEY (medicationid,medname) REFERENCES public.medications(id,medname);

ALTER TABLE medications ALTER COLUMN datefilled SET DEFAULT CURRENT_DATE;

ALTER TABLE medications ADD COLUMN created_at DATE DEFAULT CURRENT_DATE;

CREATE SEQUENCE medications_id_seq;

ALTER TABLE medications ALTER COLUMN ID SET DEFAULT nextval('medications_id_seq');

ALTER SEQUENCE medications_id_seq OWNED BY medications.id;

-- Auto-generated SQL script #202302101613
INSERT INTO public.medications (id,medname,refillsleft,timesperday,timesperweek,folderpath)
	VALUES (1,'med',2,2,7,'meds/med/1/');

COMMIT TRAN T2;

BEGIN TRAN T3;

INSERT INTO public.confirmations (id,medname,taken,medicationid,created_at) VALUES
	 (2,'med',true,1,'2023-02-10'),
	 (3,'med',false,1,'2023-02-10'),
	 (4,'med',false,1,'2023-02-10'),
	 (5,'med',true,1,'2023-02-10'),
	 (1,'med',false,1,'2023-02-10'),
	 (6,'med',true,1,'2023-02-10'),
	 (7,'med',true,1,'2023-02-02'),
	 (8,'med',false,1,'2023-02-02'),
	 (9,'med',true,1,'2023-02-02'),
	 (10,'med',false,1,'2023-02-02');

INSERT INTO public.confirmations (id,medname,taken,medicationid,created_at) VALUES
	 (11,'med',false,1,'2023-02-02'),
	 (12,'med',true,1,'2023-02-02'),
	 (13,'med',true,1,'2023-02-02'),
	 (14,'med',true,1,'2023-02-02');

COMMIT TRAN T3;