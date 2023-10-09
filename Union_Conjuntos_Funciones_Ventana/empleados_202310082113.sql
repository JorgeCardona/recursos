/*
SELECT NOMBRE,APELLIDO,EDAD,
	   LAG(Edad) OVER(PARTITION BY APELLIDO ORDER BY Edad) AS LAG, -- TRAE EL VALOR DE LA FILA ANTERIOR DE LA AGRUPACION POR PARTICION
	   LEAD(Edad) OVER(PARTITION BY APELLIDO ORDER BY Edad) AS LEAD, -- TRAE EL VALOR DE LA FILA SIGUIENTE DE LA AGRUPACION
	   FIRST_VALUE(NOMBRE) OVER(PARTITION BY APELLIDO) AS FIRST, --  TRAE EL PRIMER VALOR DEL REGISTRO  DE LA AGRUPACION, NO SE DEBE ORDENAR 'ORDER BY' PORQUE GENERA VALORES INCORRECTOS
	   LAST_VALUE (NOMBRE) OVER(PARTITION BY APELLIDO) AS LAST, --  TRAE EL ULTIMO VALOR DEL REGISTRO  DE LA AGRUPACION, NO SE DEBE ORDENAR  'ORDER BY' PORQUE GENERA VALORES INCORRECTOS
	   NTILE(3) OVER(PARTITION BY APELLIDO ORDER BY Edad) AS NTILE, --DIVIDE LA AGRUPACION EN EL NUMERO DE GRUPOS QUE SE DEFINA DENTRO DE NTILE(3)
	   ROW_NUMBER() OVER(PARTITION BY APELLIDO ORDER BY Edad) AS ROW, -- ENUMERA DE 1 EN 1 SIN REPETIR EL NUMERO, PARA CADA UNA DE LAS FILAS DE LA AGRUPACION
	   RANK() OVER(PARTITION BY APELLIDO ORDER BY Edad) AS RANK, -- ENUMERA REPITIENDO EL NUMERO PARA VALORES IDENTICOS Y SALTANDO NO NEESARIAMENTE DE 1 EN 1, PARA LAS FILAS DE LA AGRUPACION
	   DENSE_RANK() OVER(PARTITION BY APELLIDO ORDER BY Edad) AS DENSE, -- ENUMERA DE 1 EN 1 REPITIENDO EL NUMERO PARA VALORES IDENTICOS, PARA LAS FILAS DE LA AGRUPACION
       COUNT (Edad) OVER(PARTITION BY APELLIDO) AS COUNTs, -- CUENTA EL TOTAL DE FILAS PARA EL RESULTADO DE LA AGRUPACION
       MIN(Edad) OVER(PARTITION BY APELLIDO) AS MINs, -- OBTIENE EL VALOR MINIMO PARA LA AGRUPACION
       MAX(Edad) OVER(PARTITION BY APELLIDO) AS MAXs, -- OBTIENE EL VALOR MAXIMO PARA LA AGRUPACION
       ROUND(AVG(Edad) OVER(PARTITION BY APELLIDO), 2) AS AVG, -- OBTIENE EL VALOR PROMEDIO PARA LA AGRUPACION
       SUM(Edad) OVER(PARTITION BY APELLIDO) AS SUM, -- OBTIENE LA SUMA DE LOS VALORES PARA LA AGRUPACION
       SUM(Edad) OVER(PARTITION BY APELLIDO ORDER BY Edad, Edad ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS ACUM, -- OBTIENE LA SUMA DE LOS VALORES ACUMULADOS POR CADA FILA DE LA AGRUPACION. INCLUYE TODAS LAS FILAS
       SUM(Edad) OVER(PARTITION BY APELLIDO ORDER BY Edad ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS SUM1,  -- OBTIENE LA SUMA DE LA FILA ANTERIOR Y DE LA FILA SIGUIENTE
  	   SUM(Edad) OVER(PARTITION BY APELLIDO ORDER BY Edad ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING) AS SUM12  -- OBTIENE LA SUMA DE LAS 2 FILAS ANTERIORES Y DE LAS 2 FILAS SIGUIENTES   
FROM Empleados
ORDER BY APELLIDO;
*/

CREATE TABLE public.empleados (
	id int4 NOT NULL,
	nombre varchar(255) NOT NULL,
	apellido varchar(255) NOT NULL,
	edad int4 NULL,
	id_departamento int4 NULL,
	color_favorito varchar(255) NULL,
	id_region int4 NULL,
	CONSTRAINT empleados_pkey PRIMARY KEY (id)
);

INSERT INTO public.empleados (id,nombre,apellido,edad,id_departamento,color_favorito,id_region) VALUES
	 (12,'Elena','Gómez',35,2,'azul',2),
	 (13,'Fernando','Sánchez',49,3,'rosado',3),
	 (14,'Patricia','Martínez',22,4,'amarillo',4),
	 (15,'Javier','Ramírez',28,5,'rojo',5),
	 (17,'Miguel','García',42,2,'azul',2),
	 (18,'Sofía','Pérez',41,3,'rosado',3),
	 (19,'Diego','Torres',23,4,'amarillo',4),
	 (20,'Andrea','López',44,5,'rojo',5),
	 (21,'Luisa','González',31,1,'verde',1),
	 (22,'Raúl','Hernández',30,2,'azul',2);
INSERT INTO public.empleados (id,nombre,apellido,edad,id_departamento,color_favorito,id_region) VALUES
	 (23,'Cecilia','Martínez',20,3,'rosado',3),
	 (25,'Laura','Sánchez',34,5,'rojo',5),
	 (26,'Pablo','Gómez',23,1,'verde',1),
	 (27,'Valentina','Ramírez',41,2,'azul',2),
	 (28,'Ricardo','Pérez',33,3,'rosado',3),
	 (29,'Marina','García',20,4,'amarillo',4),
	 (30,'Joaquín','Martínez',43,5,'rojo',5),
	 (31,'Natalia','Torres',34,1,'verde',1),
	 (32,'Eduardo','Sánchez',41,2,'azul',2),
	 (33,'Lucía','López',23,3,'rosado',3);
INSERT INTO public.empleados (id,nombre,apellido,edad,id_departamento,color_favorito,id_region) VALUES
	 (35,'Paula','Gómez',27,5,'rojo',5),
	 (36,'Francisco','Hernández',25,1,'verde',1),
	 (37,'Sara','Ramírez',34,2,'azul',2),
	 (38,'Jorge','Pérez',30,3,'rosado',3),
	 (39,'Valentín','García',21,4,'amarillo',4),
	 (40,'Catalina','Martínez',39,5,'rojo',5),
	 (41,'Roberto','Gómez',37,1,'verde',1),
	 (42,'Diana','Ramírez',26,2,'azul',2),
	 (43,'Héctor','Fernández',34,3,'rosado',3),
	 (44,'Lorena','Sánchez',46,4,'amarillo',4);
INSERT INTO public.empleados (id,nombre,apellido,edad,id_departamento,color_favorito,id_region) VALUES
	 (45,'Federico','López',40,5,'rojo',5),
	 (46,'Inés','González',46,1,'verde',1),
	 (47,'Rafael','Martínez',34,2,'azul',2),
	 (48,'Adela','Hernández',24,3,'rosado',3),
	 (49,'Mateo','Fernández',20,4,'amarillo',4),
	 (50,'Cristina','García',48,5,'rojo',5),
	 (51,'Julián','Pérez',37,1,'verde',1),
	 (52,'Beatriz','Ramírez',49,2,'azul',2),
	 (53,'Oscar','Sánchez',27,3,'rosado',3),
	 (54,'Valeria','Martínez',36,4,'amarillo',4);
INSERT INTO public.empleados (id,nombre,apellido,edad,id_departamento,color_favorito,id_region) VALUES
	 (55,'Joaquín','López',42,5,'rojo',5),
	 (56,'Camila','González',49,1,'verde',1),
	 (57,'Lorenzo','Hernández',36,2,'azul',2),
	 (58,'Paulina','Fernández',32,3,'rosado',3),
	 (59,'Manuel','Sánchez',47,4,'amarillo',4),
	 (60,'Isabella','Ramírez',38,5,'rojo',5),
	 (61,'Roberto','Pérez',25,1,'verde',1),
	 (62,'Diana','Gómez',42,2,'azul',2),
	 (63,'Héctor','Martínez',26,3,'rosado',3),
	 (64,'Lorena','Fernández',43,4,'amarillo',4);
INSERT INTO public.empleados (id,nombre,apellido,edad,id_departamento,color_favorito,id_region) VALUES
	 (65,'Federico','García',29,5,'rojo',5),
	 (66,'Inés','López',20,1,'verde',1),
	 (67,'Rafael','Ramírez',42,2,'azul',2),
	 (68,'Adela','Sánchez',23,3,'rosado',3),
	 (69,'Mateo','Martínez',44,4,'amarillo',4),
	 (71,'Julián','González',46,1,'verde',1),
	 (72,'Beatriz','Hernández',30,2,'azul',2),
	 (73,'Oscar','Fernández',41,3,'rosado',3),
	 (74,'Valeria','Sánchez',25,4,'amarillo',4),
	 (75,'Joaquín','García',37,5,'rojo',5);
INSERT INTO public.empleados (id,nombre,apellido,edad,id_departamento,color_favorito,id_region) VALUES
	 (76,'Camila','López',32,1,'verde',1),
	 (77,'Lorenzo','Ramírez',21,2,'azul',2),
	 (78,'Paulina','Sánchez',38,3,'rosado',3),
	 (79,'Manuel','Martínez',43,4,'amarillo',4),
	 (80,'Isabella','Fernández',40,5,'rojo',5),
	 (81,'Roberto','Gómez',45,1,'verde',1),
	 (82,'Diana','Ramírez',28,2,'azul',2),
	 (83,'Héctor','Sánchez',20,3,'rosado',3),
	 (84,'Lorena','García',47,4,'amarillo',4),
	 (85,'Federico','Martínez',29,5,'rojo',5);
INSERT INTO public.empleados (id,nombre,apellido,edad,id_departamento,color_favorito,id_region) VALUES
	 (87,'Rafael','González',23,2,'azul',2),
	 (88,'Adela','Hernández',24,3,'rosado',3),
	 (89,'Mateo','Sánchez',45,4,'amarillo',4),
	 (90,'Cristina','Ramírez',34,5,'rojo',5),
	 (91,'Julián','López',37,1,'verde',1),
	 (92,'Beatriz','Gómez',39,2,'azul',2),
	 (93,'Oscar','Martínez',25,3,'rosado',3),
	 (94,'Valeria','Fernández',38,4,'amarillo',4),
	 (95,'Joaquín','Sánchez',49,5,'rojo',5),
	 (96,'Camila','García',45,1,'verde',1);
INSERT INTO public.empleados (id,nombre,apellido,edad,id_departamento,color_favorito,id_region) VALUES
	 (97,'Lorenzo','Ramírez',47,2,'azul',2),
	 (98,'Paulina','Hernández',25,3,'rosado',3),
	 (99,'Manuel','Gómez',49,4,'amarillo',4),
	 (100,'Isabella','López',24,5,'rojo',5),
	 (101,'Juan','Pérez',45,1,'verde',1),
	 (16,'Isabel','Fernández',22,1,'verde',1),
	 (24,'Antonio','Fernández',22,4,'amarillo',4),
	 (34,'Manuel','Fernández',22,4,'amarillo',4),
	 (70,'Cristina','Fernández',22,5,'rojo',5),
	 (86,'Inés','Díaz',30,1,'verde',1);
INSERT INTO public.empleados (id,nombre,apellido,edad,id_departamento,color_favorito,id_region) VALUES
	 (1,'Juan','Pérez',39,1,'amarillo',1),
	 (2,'María','Rodríguez',45,2,'azul',2),
	 (3,'Carlos','González',49,3,'rojo',3),
	 (4,'Ana','López',39,4,'verde',4),
	 (5,'Luis','Martínez',29,5,'rosado',5),
	 (6,'Laura','García',28,1,'amarillo',1),
	 (8,'Carmen','Díaz',43,3,'rojo',3),
	 (9,'Sergio','Ruiz',26,4,'verde',4),
	 (10,'Ana','Torres',46,5,'rosado',5),
	 (11,'David','López',39,1,'verde',1);
INSERT INTO public.empleados (id,nombre,apellido,edad,id_departamento,color_favorito,id_region) VALUES
	 (7,'Pedro','Díaz',44,2,'azul',2),
	 (102,'María','Rodríguez',46,2,'azul',2),
	 (103,'Carlos','González',48,3,'rosado',3),
	 (104,'Ana','López',40,4,'amarillo',4),
	 (105,'Luis','Martínez',33,5,'rojo',5),
	 (106,'Laura','García',43,1,'verde',1),
	 (107,'Pedro','Fernández',43,2,'azul',2),
	 (109,'Sergio','Ruiz',33,4,'amarillo',4),
	 (110,'Ana','Torres',22,5,'rojo',5),
	 (111,'David','López',45,1,'verde',1);
INSERT INTO public.empleados (id,nombre,apellido,edad,id_departamento,color_favorito,id_region) VALUES
	 (112,'Elena','Gómez',37,2,'azul',2),
	 (113,'Fernando','Sánchez',40,3,'rosado',3),
	 (114,'Patricia','Martínez',47,4,'amarillo',4),
	 (115,'Javier','Ramírez',36,5,'rojo',5),
	 (116,'Isabel','Fernández',38,1,'verde',1),
	 (117,'Miguel','García',26,2,'azul',2),
	 (118,'Sofía','Pérez',42,3,'rosado',3),
	 (119,'Diego','Torres',41,4,'amarillo',4),
	 (120,'Andrea','López',27,5,'rojo',5),
	 (121,'Luisa','González',26,1,'verde',1);
INSERT INTO public.empleados (id,nombre,apellido,edad,id_departamento,color_favorito,id_region) VALUES
	 (122,'Raúl','Hernández',35,2,'azul',2),
	 (123,'Cecilia','Martínez',31,3,'rosado',3),
	 (108,'Gabrilela','Díaz',22,3,'rosado',3);
