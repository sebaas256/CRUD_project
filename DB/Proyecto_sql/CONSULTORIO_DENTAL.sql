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
Go

--PROCESOS ALMACENADOS
CREATE PROCEDURE AgregarCita 
@IdCita int, @Fecha datetime, @consultorio varchar(5), @desc varchar(50),
@estado bit, @Dui_paciente varchar(10)
	AS
		INSERT INTO CITAS VALUES (@IdCita, @Fecha, @consultorio, @desc, @estado, @Dui_paciente)
GO

CREATE PROCEDURE AgregarPaciente
@Dui_paciente varchar(10), @Nombres varchar(50), @Apellidos varchar (50), @fecha_nac date, @telefono int,
@direccion varchar(200), @correo varchar(100)
	AS
		INSERT INTO PACIENTES VALUES (@Dui_paciente , @Nombres, @Apellidos, @fecha_nac, @telefono, @direccion, @correo)
GO

CREATE PROCEDURE AgregarConsultas
@Id_Consulta int, @diag varchar(500), @obser varchar(500), @fecha_consulta date, @Id_Doctor int,
@Id_Cita int
	AS
		INSERT INTO CONSULTAS VALUES (@Id_Consulta, @diag, @obser, @fecha_consulta, @Id_Doctor, @Id_Cita)
GO

CREATE PROCEDURE AgregarEspecialidades
@Id_Espc int, @Nombre_Esp varchar(40)
	AS
		INSERT INTO DOC_ESPC VALUES (@Id_Espc, @Nombre_Esp)
GO	

CREATE PROCEDURE AgregarDoctores
@Id_Doctor int, @Nombres varchar(50), @Apellidos varchar(50), @telefono int,
@correo varchar(60), @Id_Espc int
	AS
		INSERT INTO DOCTORES VALUES (@Id_Doctor, @Nombres, @Apellidos, @telefono, @correo, @Id_Espc)
GO	

CREATE PROCEDURE AgregarReceta
@Id_Det_Receta int, @deta_receta varchar(200), @Id_Consulta int
	AS
		INSERT INTO RECETA VALUES (@Id_Det_Receta, @deta_receta, @Id_Consulta)
GO	

--INSERTANDO DATOS
EXEC AgregarEspecialidades 1, 'Dentista general'
EXEC AgregarEspecialidades 2, 'Odontopediatra'
EXEC AgregarEspecialidades 3, 'Ortodoncista'
EXEC AgregarEspecialidades 4, 'Periodoncista'
EXEC AgregarEspecialidades 5, 'Endodoncista'

EXEC AgregarDoctores 1, 'Freddie', 'Mercury', 22709090, 'freddie@clinic.com', 3;
EXEC AgregarDoctores 2, 'Lady', 'Gaga', 22709081, 'gaga@clinic.com', 2;
EXEC AgregarDoctores 3, 'Kurt', 'Cobain', 22709072, 'kurt@clinic.com', 1;
EXEC AgregarDoctores 4, 'Beyonce', 'Knowles', 22709063, 'bey@clinic.com', 4;
EXEC AgregarDoctores 5, 'Elvis', 'Presley', 22709054, 'elvis@clinic.com', 1;
EXEC AgregarDoctores 6, 'Adele', 'Adkins', 22709045, 'adele@clinic.com', 5;
EXEC AgregarDoctores 7, 'David', 'Bowie', 22709036, 'bowie@clinic.com', 3;
EXEC AgregarDoctores 8, 'Miley', 'Cyrus', 22709027, 'miley@clinic.com', 2;
EXEC AgregarDoctores 9, 'Bruno', 'Mars', 22709018, 'bruno@clinic.com', 4;
EXEC AgregarDoctores 10, 'Shakira', 'Ripoll', 22709009, 'shakira@clinic.com', 5;

EXEC AgregarPaciente '481027391', 'Calvin', 'Harris', '1984-01-17', 700100101, 'Col. Escalon, San Salvador', 'calvin@edmpatient.com';
EXEC AgregarPaciente '729103846', 'Sophie', 'Xeon', '1985-09-17', 700200202, 'Barrio El Centro, Santa Tecla', 'sophie@edmpatient.com';
EXEC AgregarPaciente '605982713', 'David', 'Guetta', '1967-11-07', 700300303, 'Av. Morazan, San Miguel', 'guetta@edmpatient.com';
EXEC AgregarPaciente '317948205', 'Alison', 'Wonderland', '1986-09-27', 700400404, 'Col. Altamira, Sonsonate', 'alison@edmpatient.com';
EXEC AgregarPaciente '894210376', 'Zedd', 'Anton', '1989-09-02', 700500505, 'Res. San Andres, Ahuachapan', 'zedd@edmpatient.com';
EXEC AgregarPaciente '236790584', 'Charlotte', 'de Witte', '1992-07-21', 700600606, 'Barrio El Calvario, San Vicente', 'charlotte@edmpatient.com';
EXEC AgregarPaciente '510328947', 'Marshmello', 'Mello', '1992-05-19', 700700707, 'Col. Los Angeles, Zacatecoluca', 'marsh@edmpatient.com';
EXEC AgregarPaciente '682410359', 'Deadmau', 'Zimmerman', '1981-01-05', 700800808, 'Canton El Carmen, Chalatenango', 'mau5@edmpatient.com';
EXEC AgregarPaciente '793120684', 'Peggy', 'Gou', '1991-07-03', 700900909, 'Col. La Paz, Sensuntepeque', 'peggy@edmpatient.com';
EXEC AgregarPaciente '109283745', 'Kygo', 'Kyrre', '1991-09-11', 701000101, 'Barrio El Angel, Usulutan', 'kygo@edmpatient.com';
EXEC AgregarPaciente '324681907', 'Steve', 'Aoki', '1977-11-30', 701100202, 'Res. El Trebol, La Union', 'aoki@edmpatient.com';
EXEC AgregarPaciente '580213964', 'Nina', 'Kraviz', '1982-10-02', 701200303, 'Col. San Antonio, Cojutepeque', 'nina@edmpatient.com';
EXEC AgregarPaciente '867390251', 'Madeon', 'Leclercq', '1994-05-30', 701300404, 'Res. Santa Rosa, Apopa', 'madeon@edmpatient.com';
EXEC AgregarPaciente '412395780', 'Porter', 'Robinson', '1992-07-15', 701400505, 'Canton El Guayabo, Metapan', 'porter@edmpatient.com';
EXEC AgregarPaciente '643219875', 'REZZ', 'Spencer', '1995-03-28', 701500606, 'Barrio Concepcion, La Libertad', 'rezz@edmpatient.com';

EXEC AgregarCita 1, '2025-06-01 08:00:00', 'A101', 'Limpieza dental', 0, '481027391';
EXEC AgregarCita 2, '2025-06-01 09:00:00', 'A102', 'Revision general', 0, '729103846';
EXEC AgregarCita 3, '2025-06-01 10:00:00', 'A103', 'Consulta ortodoncia', 0, '605982713';
EXEC AgregarCita 4, '2025-06-02 08:00:00', 'B201', 'Chequeo anual', 1, '317948205';
EXEC AgregarCita 5, '2025-06-02 09:00:00', 'B202', 'Dolor dental', 1, '894210376';
EXEC AgregarCita 6, '2025-06-02 10:00:00', 'B203', 'Evaluacion encias', 1, '236790584';
EXEC AgregarCita 7, '2025-06-03 08:00:00', 'C301', 'Carillas esteticas', 1, '510328947';
EXEC AgregarCita 8, '2025-06-03 09:00:00', 'C302', 'Tratamiento caries', 1, '682410359';
EXEC AgregarCita 9, '2025-06-03 10:00:00', 'C303', 'Brackets revision', 1, '793120684';
EXEC AgregarCita 10, '2025-06-04 08:00:00', 'D401', 'Evaluacion general', 1, '109283745';
EXEC AgregarCita 11, '2025-06-04 09:00:00', 'D402', 'Diagnostico encias', 1, '324681907';
EXEC AgregarCita 12, '2025-06-04 10:00:00', 'D403', 'Extraccion molar', 1, '580213964';
EXEC AgregarCita 13, '2025-06-05 08:00:00', 'E501', 'Consulta revision', 1, '867390251';
EXEC AgregarCita 14, '2025-06-05 09:00:00', 'E502', 'Limpieza encias', 1, '412395780';
EXEC AgregarCita 15, '2025-06-05 10:00:00', 'E503', 'Dolor persistente', 1, '643219875';
EXEC AgregarCita 16, '2025-06-06 08:00:00', 'F601', 'Chequeo anual', 1, '481027391';
EXEC AgregarCita 17, '2025-06-06 09:00:00', 'F602', 'Consulta dolor', 1, '729103846';
EXEC AgregarCita 18, '2025-06-06 10:00:00', 'F603', 'Caries profunda', 1, '605982713';
EXEC AgregarCita 19, '2025-06-07 08:00:00', 'G701', 'Evaluacion estetica', 1, '317948205';
EXEC AgregarCita 20, '2025-06-07 09:00:00', 'G702', 'Bruxismo diagnostico', 1, '894210376';

EXEC AgregarConsultas 1, 'Sin problemas visibles', 'Paciente en buen estado.', '2025-06-01', 1, 1;
EXEC AgregarConsultas 2, 'Placa moderada', 'Recomendada limpieza profunda.', '2025-06-01', 2, 2;
EXEC AgregarConsultas 3, 'Maloclusion leve', 'Se recomienda ortodoncia.', '2025-06-01', 3, 3;
EXEC AgregarConsultas 4, 'Revision sin anomalias', 'Control en 6 meses.', '2025-06-02', 4, 4;
EXEC AgregarConsultas 5, 'Dolor en muela inferior', 'Recetado analgesico.', '2025-06-02', 5, 5;
EXEC AgregarConsultas 6, 'Encias inflamadas', 'Se sugiere periodoncista.', '2025-06-02', 6, 6;
EXEC AgregarConsultas 7, 'Carillas recomendadas', 'Paciente desea procedimiento.', '2025-06-03', 7, 7;
EXEC AgregarConsultas 8, 'Caries en molar', 'Preparar para empaste.', '2025-06-03', 8, 8;
EXEC AgregarConsultas 9, 'Brackets en buen estado', 'Revision en 1 mes.', '2025-06-03', 9, 9;
EXEC AgregarConsultas 10, 'Revision general', 'Sin hallazgos.', '2025-06-04', 10, 10;
EXEC AgregarConsultas 11, 'Inflamacion leve', 'Se recomienda tratamiento.', '2025-06-04', 1, 11;
EXEC AgregarConsultas 12, 'Extraccion sin complicaciones', 'Reposo por 3 dias.', '2025-06-04', 2, 12;
EXEC AgregarConsultas 13, 'Dolor intermitente', 'Posible infeccion.', '2025-06-05', 3, 13;
EXEC AgregarConsultas 14, 'Encias con sangrado leve', 'Usar enjuague especializado.', '2025-06-05', 4, 14;
EXEC AgregarConsultas 15, 'Dolor cronico', 'Derivar a especialista.', '2025-06-05', 5, 15;
EXEC AgregarConsultas 16, 'Chequeo sin anomalias', 'Control en 1 año.', '2025-06-06', 6, 16;
EXEC AgregarConsultas 17, 'Dolor por caries', 'Se prepara endodoncia.', '2025-06-06', 7, 17;
EXEC AgregarConsultas 18, 'Caries muy avanzada', 'Urgente tratamiento.', '2025-06-06', 8, 18;
EXEC AgregarConsultas 19, 'Estetica dental', 'Plan de blanqueamiento.', '2025-06-07', 9, 19;
EXEC AgregarConsultas 20, 'Bruxismo diagnosticado', 'Uso de guarda nocturna.', '2025-06-07', 10, 20;

EXEC AgregarReceta 1, 'Usar enjuague bucal con fluor cada noche.', 1;
EXEC AgregarReceta 2, 'Agendar limpieza profunda en 3 meses.', 2;
EXEC AgregarReceta 3, 'Colocacion de ligas correctoras en la siguiente cita.', 3;




--Vistas--
--1 Mostrar los detalles de la cita de un paciente con su doctor--
create view detalle_cita as 
select 
pac.Dui_Paciente, 
concat(pac.Nombres, ' ',pac.Apellidos) as paciente, 
cit.fecha_cita, cit.consultorio, cit.estado_cita,
concat(docs.Nombres, ' ',docs.Apellidos) as doctor
from PACIENTES pac
join CITAS cit on (pac.Dui_Paciente = cit.Dui_Paciente)
join CONSULTAS consu on (cit.Id_Cita = consu.Id_Cita)
join DOCTORES docs on (consu.Id_Doctor = docs.Id_Doctor)


--2 Mostrar el total de consultas hechas o por hacer de un doctor--
create view promedio_consultas_doctor as 
select
doc.Id_Doctor, 
concat(doc.Nombres, ' ',doc.Apellidos) as doctor,
count(consu.Id_Consulta) as total_consultas
from DOCTORES doc
left join CONSULTAS consu on (consu.Id_Doctor = doc.Id_Doctor)
group by doc.Id_Doctor, doc.Nombres, doc.Apellidos


--3 Mostrar el total de doctores de cada especialidad--
create view doctores_por_especialidad as 
select 
esp.Nombre_esp as especialidad,
count(d.Id_Doctor) as cantidad_doctores
from DOC_ESPC esp
join DOCTORES d on (d.Id_Espc = esp.Id_Espc)
group by esp.Nombre_esp


--4 Mostrar la informacion de las citas que estan pendientes por realizarse--
create view citas_pendientes as 
select 
c.fecha_cita, 
concat(p.Nombres, ' ',p.Apellidos) as paciente, 
concat(d.Nombres, ' ',d.Apellidos) as doctor, 
c.estado_cita
from CITAS c
join PACIENTES p on (p.Dui_Paciente = c.Dui_Paciente)
join CONSULTAS cons on (c.Id_Cita = cons.Id_Cita)
join DOCTORES d on (cons.Id_Doctor = d.Id_Doctor)
where c.estado_cita = 0


--5 Mostrar pacientes que tengan dos o mas consultas--
create view pacientes_varias_consultas as
select 
p.Dui_Paciente, 
concat(p.Nombres, ' ',p.Apellidos )as paciente
from PACIENTES p 
where (
select count(*)
from CITAS c 
join CONSULTAS cons on (c.Id_Cita = cons.Id_Cita)
where c.Dui_Paciente = p.Dui_Paciente 
) >= 2


--6 Mostrar todos los doctores que no tengan ninguna consulta registrada--
create view doctores_sin_consultas as
select 
d.Id_Doctor,
CONCAT(d.Nombres, ' ',d.Apellidos) as doctor
from DOCTORES d
left join CONSULTAS cons on (cons.Id_Doctor = d.Id_Doctor)
where cons.Id_Consulta = null


--7 Mostra el historial completo de consultas con detalles del paciente doctor y receta--
create view consultas_completas as 
select 
cons.Id_Consulta,
p.Dui_Paciente,
concat(p.Nombres, ' ',p.Apellidos) AS paciente,
concat(d.Nombres, ' ', d.Apellidos) AS doctor,
esp.Nombre_esp AS especialidad,
cons.fecha_consulta,
cons.diagnostico,
cons.observaciones,
r.deta_receta AS receta
from CONSULTAS cons
join CITAS c on (cons.Id_Cita = c.Id_Cita)
join PACIENTES p on (c.Dui_Paciente = p.Dui_Paciente)
join DOCTORES d on (cons.Id_Doctor = d.Id_Doctor)
join DOC_ESPC esp on (esp.Id_Espc = d.Id_Espc)
left join RECETA r on (cons.Id_Consulta = r.Id_Consulta)


--8 mostrar los pacientes que tuvieron una consulta el primer dia de cualquier mes--
create view consultas_primer_dia_mes as
select 
p.Dui_Paciente, 
CONCAT(p.Nombres, ' ',p.Apellidos) as paciente,
cons.fecha_consulta,
cons.diagnostico,
CONCAT(d.Nombres, ' ',d.Apellidos) as doctor
from PACIENTES p 
inner join CITAS c on (c.Dui_Paciente = p.Dui_Paciente)
inner join CONSULTAS cons on (c.Id_Cita = cons.Id_Cita)
inner join DOCTORES d on (d.Id_Doctor = cons.Id_Doctor)
where DAY(cons.fecha_consulta) = 1

