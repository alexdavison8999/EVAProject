#!/bin/bash


MEDS_DIR="EXPOFILES/database/meds"
DRUG_INFO_IMAGES="EXPOFILES/assets/drugInfoImages"
GENERATED_IMAGES="EXPOFILES/assets/generatedImages"

if [ -d "$MEDS_DIR" ];
	echo "meds dir already exists"
else
	echo "Creating meds dir."
	mkdir "$MEDS_DIR"

if [ -d "$DRUG_INFO_IMAGES" ];
	echo "meds dir already exists"
else
	echo "Creating meds dir."
	mkdir "$DRUG_INFO_IMAGES"

if [ -d "$GENERATED_IMAGES" ];
	echo "meds dir already exists"
else
	echo "Creating meds dir."
	mkdir "$GENERATED_IMAGES"
