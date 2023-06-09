CREATE DATABASE IF NOT EXISTS school;

USE school;

DROP TABLE IF EXISTS SO, PHONG, LOAI_HINH, LOAI_TRG, GDTX, MN, TiH, THCS, THPT;

CREATE TABLE SO (
	ma INT NOT NULL,
	ten VARCHAR(50) NOT NULL,
	PRIMARY KEY (ma)
);

CREATE TABLE PHONG (
	ma INT NOT NULL,
	ten VARCHAR(50) NOT NULL,
	PRIMARY KEY (ma)
);

CREATE TABLE LOAI_HINH (
	ma INT NOT NULL,
	ten VARCHAR(50) NOT NULL,
	PRIMARY KEY (ma)
);

CREATE TABLE LOAI_TRG (
	ma INT NOT NULL,
	ten VARCHAR(50) NOT NULL,
	PRIMARY KEY (ma)
);

CREATE TABLE GDTX (
	ma VARCHAR(8) NOT NULL,
	ten VARCHAR(255) NOT NULL,
	dc VARCHAR(500),
	so INT NOT NULL,
	phg INT NOT NULL,
	loai_hinh INT NOT NULL,
	loai_trg INT NOT NULL,
	PRIMARY KEY (ma),
	FOREIGN KEY (so) REFERENCES SO(ma),
	FOREIGN KEY (phg) REFERENCES PHONG(ma),
	FOREIGN KEY (loai_hinh) REFERENCES LOAI_HINH(ma),
	FOREIGN KEY (loai_trg) REFERENCES LOAI_TRG(ma)
);

CREATE TABLE MN (
	ma VARCHAR(8) NOT NULL,
	ten VARCHAR(255) NOT NULL,
	dc VARCHAR(500),
	so INT NOT NULL,
	phg INT NOT NULL,
	loai_hinh INT NOT NULL,
	loai_trg INT NOT NULL,
	PRIMARY KEY (ma),
	FOREIGN KEY (so) REFERENCES SO(ma),
	FOREIGN KEY (phg) REFERENCES PHONG(ma),
	FOREIGN KEY (loai_hinh) REFERENCES LOAI_HINH(ma),
	FOREIGN KEY (loai_trg) REFERENCES LOAI_TRG(ma)
);

CREATE TABLE TiH (
	ma VARCHAR(8) NOT NULL,
	ten VARCHAR(255) NOT NULL,
	dc VARCHAR(500),
	so INT NOT NULL,
	phg INT NOT NULL,
	loai_hinh INT NOT NULL,
	loai_trg INT NOT NULL,
	PRIMARY KEY (ma),
	FOREIGN KEY (so) REFERENCES SO(ma),
	FOREIGN KEY (phg) REFERENCES PHONG(ma),
	FOREIGN KEY (loai_hinh) REFERENCES LOAI_HINH(ma),
	FOREIGN KEY (loai_trg) REFERENCES LOAI_TRG(ma)
);

CREATE TABLE THCS (
	ma VARCHAR(8) NOT NULL,
	ten VARCHAR(255) NOT NULL,
	dc VARCHAR(500),
	so INT NOT NULL,
	phg INT NOT NULL,
	loai_hinh INT NOT NULL,
	loai_trg INT NOT NULL,
	PRIMARY KEY (ma),
	FOREIGN KEY (so) REFERENCES SO(ma),
	FOREIGN KEY (phg) REFERENCES PHONG(ma),
	FOREIGN KEY (loai_hinh) REFERENCES LOAI_HINH(ma),
	FOREIGN KEY (loai_trg) REFERENCES LOAI_TRG(ma)
);

CREATE TABLE THPT (
	ma VARCHAR(8) NOT NULL,
	ten VARCHAR(255) NOT NULL,
	dc VARCHAR(500),
	so INT NOT NULL,
	phg INT NOT NULL,
	loai_hinh INT NOT NULL,
	loai_trg INT NOT NULL,
	PRIMARY KEY (ma),
	FOREIGN KEY (so) REFERENCES SO(ma),
	FOREIGN KEY (phg) REFERENCES PHONG(ma),
	FOREIGN KEY (loai_hinh) REFERENCES LOAI_HINH(ma),
	FOREIGN KEY (loai_trg) REFERENCES LOAI_TRG(ma)
);