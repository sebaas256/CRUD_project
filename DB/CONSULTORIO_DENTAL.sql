create database CONSULTORIO_DENTAL
use CONSULTORIO_DENTAL

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
	Dui_Paciente varchar(10) not null,

)

CREATE TABLE PACIENTES 
(
		Dui_Paciente varchar(10) not null,
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

CREATE TABLE RECETA
(
	Id_Det_Receta int not null,
	deta_receta varchar(200) not null,
	Id_Consulta int not null
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

ALTER TABLE RECETA
ADD CONSTRAINT pk_Det_Receta
PRIMARY KEY (Id_Det_Receta)


-- CREACION DE LLAVES FORANEAS

ALTER TABLE DOCTORES 
ADD CONSTRAINT fk_doc_espc
FOREIGN KEY (Id_Espc)	
REFERENCES DOC_ESPC(Id_Espc)
on update cascade on delete no action

ALTER TABLE CONSULTAS 
ADD CONSTRAINT fk_cons_doc
FOREIGN KEY (Id_Doctor)
REFERENCES DOCTORES(Id_Doctor)
on update cascade on delete no action

ALTER TABLE CONSULTAS 
ADD CONSTRAINT fk_cons_cita
FOREIGN KEY (Id_Cita)
REFERENCES CITAS(Id_Cita)
on update cascade on delete no action

ALTER TABLE CITAS 
ADD CONSTRAINT fk_cita_pac
FOREIGN KEY (Dui_Paciente)
REFERENCES PACIENTES(Dui_Paciente)
on update cascade on delete no action

ALTER TABLE RECETA
ADD CONSTRAINT fk_detatram_consult
FOREIGN KEY (Id_Consulta)
REFERENCES CONSULTAS (Id_Consulta)
on update cascade on delete no action

UPDATE CITAS SET estado_cita = 0 
WHERE estado_cita = 1
 
UPDATE CITAS SET estado_cita = 1
WHERE Id_Cita IN (1,2,3)

select * from CITAS