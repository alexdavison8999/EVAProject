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

ALTER TABLE public.confirmations ADD CONSTRAINT confirmations_fk FOREIGN KEY (medicationid,medname) REFERENCES public.medications(id,medname);
