-- CREAR Y USAR BASE DE DATOS
CREATE DATABASE CONSULTORIO_DENTAL
USE CONSULTORIO_DENTAL

-- CREACION DE TABLAS 
CREATE TABLE DOCTORES 
(
	Id_Doctor int not null,
	Nombres varchar(50) not null,
	Apellidos varchar(50) not null,
	telefono int not null,
	correo varchar(60) not null,
	Id_Espc int not null,


)

CREATE TABLE CONSULTAS
(
	Id_Consulta int not null,
	diagnostico varchar(500) not null,
	observaciones varchar(500) not null,
	fecha_consulta date not null,
	Id_Doctor int not null,
	Id_Cita int not null
)

CREATE TABLE CITAS
(
	Id_Cita int not null,
	fecha_cita datetime not null,
	consultorio varchar(5) not null,
	descripcion varchar(50) not null,
	estado_cita bit not null,
	Dui_Paciente int not null,

)

CREATE TABLE PACIENTES 
(
		Dui_Paciente int not null,
		Nombres varchar(50) not null,
		Apellidos varchar (50) not null,
		fecha_nacimiento date not null,
		telefono int not null,
		direccion varchar(200) null,
		correo varchar(100) null
)

CREATE TABLE DOC_ESPC
(
	Id_Espc int not null,
	Nombre_esp varchar(40) not null,
)

CREATE TABLE CONSULT_TRATAM
(
	Id_Cnslt_Trat int not null,
	Id_Consulta int not null,
	Id_Det_Trat int not null,
)

CREATE TABLE DETA_TRATAM
(
	Id_Det_Trat int not null,
	deta_trat varchar(200) not null,
	Id_Pago int not null,
)

CREATE TABLE DETALLE_PAGO
(
	Id_Pago int not null,
	pago_consulta money not null,
	pago_tratamiento money not null,
	pago_total money not null
)

-- CREACION DE LAS LLAVES PRIMARIAS
ALTER TABLE DOCTORES 
ADD CONSTRAINT pk_doctor
PRIMARY KEY (Id_Doctor) 

ALTER TABLE CONSULTAS
ADD CONSTRAINT pk_consulta
PRIMARY KEY (Id_Consulta)

ALTER TABLE CITAS
ADD CONSTRAINT pk_cita
PRIMARY KEY (Id_Cita)

ALTER TABLE PACIENTES
ADD CONSTRAINT pk_paciente
PRIMARY KEY (Dui_Paciente)

ALTER TABLE DOC_ESPC
ADD CONSTRAINT pk_doc_espc
PRIMARY KEY (Id_Espc)

ALTER TABLE DETALLE_PAGO
ADD CONSTRAINT pk_Det_Pago
PRIMARY KEY (Id_Pago)

ALTER TABLE DETA_TRATAM
ADD CONSTRAINT pk_Det_Trat
PRIMARY KEY (Id_Det_Trat)

ALTER TABLE CONSULT_TRATAM
ADD CONSTRAINT pk_Cnslt_Trat
PRIMARY KEY (Id_Cnslt_Trat)

-- CREACION DE LLAVES FORANEAS

ALTER TABLE DOCTORES 
ADD CONSTRAINT fk_doc_espc
FOREIGN KEY (Id_Espc)	
REFERENCES DOC_ESPC(Id_Espc)

ALTER TABLE CONSULTAS 
ADD CONSTRAINT fk_cons_doc
FOREIGN KEY (Id_Doctor)
REFERENCES DOCTORES(Id_Doctor)

ALTER TABLE CONSULTAS 
ADD CONSTRAINT fk_cons_cita
FOREIGN KEY (Id_Cita)
REFERENCES CITAS(Id_Cita)

ALTER TABLE CITAS 
ADD CONSTRAINT fk_cita_pac
FOREIGN KEY (Dui_Paciente)
REFERENCES PACIENTES(Dui_Paciente)

ALTER TABLE CONSULT_TRATAM
ADD CONSTRAINT fk_constram_consulta
FOREIGN KEY (Id_Consulta)
REFERENCES CONSULTAS(Id_Consulta)

ALTER TABLE CONSULT_TRATAM
ADD CONSTRAINT fk_cosntram_detatram
FOREIGN KEY (Id_Det_Trat)
REFERENCES DETA_TRATAM (Id_Det_Trat)

ALTER TABLE DETA_TRATAM
ADD CONSTRAINT fk_detatram_detpago
FOREIGN KEY (Id_Pago)
REFERENCES DETALLE_PAGO (Id_Pago)

