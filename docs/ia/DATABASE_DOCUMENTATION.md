# Documentacion Tecnica de Base de Datos

## Tabla: `A_ACTO_REGI_SID`

### Descripcion funcional
Tabla usada en Legasys para registrar actos registrales SID vinculados a servicios SID. Permite identificar el acto, su registro relacionado y los importes o parametros economicos asociados que el sistema puede necesitar para procesos registrales.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `ID_ACTO_REGI_SID` | `int` | Identificador interno del registro. |
| `CO_ACTO_REGI_SID` | `varchar(10)` | Codigo del acto registral SID. |
| `CO_SERV_SID` | `int` | Codigo del servicio SID asociado al acto. |
| `CO_REGI_SID` | `varchar(5)` | Codigo del registro SID relacionado. |
| `NO_ACTO_REGI_SID` | `varchar(190)` | Nombre o descripcion visible del acto registral SID. |
| `CO_ACTO_URI` | `varchar(5)` | Codigo complementario o referencia corta del acto. |
| `MO_CALI` | `decimal(11,2)` | Monto asociado a la calificacion del acto. |
| `MO_INSC` | `decimal(11,2)` | Monto asociado a la inscripcion del acto. |
| `NU_PORC_UIT` | `decimal(11,2)` | Porcentaje de UIT relacionado al acto o servicio. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `ID_ACTO_REGI_SID` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Los campos `MO_CALI`, `MO_INSC` y `NU_PORC_UIT` indican que la tabla no solo identifica actos SID, sino que tambien conserva datos economicos que pueden influir en la operacion registral. |

---

## Tabla: `A_ALIA_PLAN`

### Descripcion funcional
Tabla usada en Legasys para registrar alias reutilizables asociados a configuraciones internas o planes del sistema. Permite identificar un alias unico, su descripcion y la ruta o referencia que utiliza el software.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ALIA_PLAN` | `bigint unsigned` | Identificador interno del alias. |
| `NO_ALIA` | `varchar(60)` | Nombre unico del alias usado por el sistema. |
| `DE_ALIA` | `varchar(300)` | Descripcion breve del alias. |
| `TX_RUTA` | `varchar(500)` | Ruta, referencia o valor asociado al alias dentro del sistema. |
| `IN_ESTA` | `tinyint` | Estado del alias en Legasys. |
| `TS_USUA_MODI` | `timestamp` | Fecha y hora de la ultima modificacion. |
| `CO_USUA_MODI` | `varchar(20)` | Usuario que realizo la ultima modificacion. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ALIA_PLAN` | Clave principal de la tabla. |
| Unique | `uq_no_alia` | `NO_ALIA` | Evita alias duplicados dentro del sistema. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | `NO_ALIA` debe mantenerse unico porque identifica alias reutilizables consumidos por Legasys. |
| Funcional | Los campos `TS_USUA_MODI` y `CO_USUA_MODI` permiten trazabilidad basica de cambios. |

---

## Tabla: `A_ARAN_NOTA`

### Descripcion funcional
Tabla usada en Legasys para registrar rangos o valores arancelarios asociados a una notaria. Permite definir importes iniciales, finales y valores operativos que el sistema puede usar en configuraciones economicas por `CO_COMP`.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ARAN_NOTA` | `int` | Identificador interno del registro arancelario. |
| `CO_COMP` | `int` | Codigo de la notaria o compania a la que pertenece el registro. |
| `NU_INIC` | `decimal(11,2)` | Valor inicial del rango o tramo. |
| `NU_FINA` | `decimal(11,2)` | Valor final del rango o tramo. |
| `MO_VALO` | `decimal(11,2)` | Monto o valor aplicado al rango definido. |
| `IN_ESTA` | `int` | Estado del registro en el sistema. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ARAN_NOTA` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | La presencia de `CO_COMP` indica que la configuracion arancelaria se maneja por notaria, por lo que debe respetar el contexto multinotaria de Legasys. |
| Funcional | Los campos `NU_INIC`, `NU_FINA` y `MO_VALO` sugieren una parametrizacion por tramos o rangos economicos. |

---

## Tabla: `A_BANC`

### Descripcion funcional
Tabla usada en Legasys para registrar bancos disponibles en el sistema. Permite almacenar su identificador, nombre, descripcion corta, estado y datos de trazabilidad basica para procesos administrativos o financieros.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_BANC` | `int unsigned` | Identificador interno del banco. |
| `CO_PDT` | `int unsigned` | Codigo relacionado a una parametrizacion o catalogo externo del sistema. |
| `CO_CNL` | `varchar(5)` | Codigo corto o abreviado del banco. |
| `DE_BANC` | `varchar(100)` | Nombre o descripcion principal del banco. |
| `DC_BANC` | `varchar(100)` | Descripcion complementaria o nombre corto del banco. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del banco dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_BANC` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla funciona como catalogo maestro de bancos consumido por modulos administrativos o financieros de Legasys. |
| Funcional | `IN_ESTA` permite habilitar o deshabilitar bancos sin eliminarlos del catalogo. |

---

## Tabla: `A_BANC_CAJA`

### Descripcion funcional
Tabla usada en Legasys para registrar bancos o entidades financieras disponibles especificamente en el contexto de Caja. Permite mantener un catalogo ordenado para operaciones de cobro, pago o configuraciones relacionadas.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_BANC_CAJA` | `int unsigned` | Identificador interno del banco en Caja. |
| `DE_BANC_CAJA` | `varchar(100)` | Nombre principal del banco o entidad financiera. |
| `DC_BANC_CAJA` | `varchar(100)` | Descripcion complementaria o nombre corto del banco en Caja. |
| `NU_ORDE` | `smallint` | Orden de visualizacion o prioridad dentro del catalogo. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del modulo de Caja. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_BANC_CAJA` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | `NU_ORDE` sugiere que este catalogo puede mostrarse ordenado en interfaces o listas del modulo Caja. |
| Funcional | Aunque existe `A_BANC`, esta tabla parece responder a una necesidad especifica del modulo Caja. |

---

## Tabla: `A_BIEN_MUEB`

### Descripcion funcional
Tabla usada en Legasys para registrar tipos o categorias de bienes muebles. Sirve como catalogo base para procesos donde el sistema necesita clasificar bienes muebles dentro de tramites o mantenimientos.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_BIEN_MUEB` | `int` | Identificador interno del bien mueble. |
| `DE_BIEN_MUEB` | `varchar(100)` | Nombre o descripcion principal del bien mueble. |
| `DC_BIEN_MUEB` | `varchar(50)` | Descripcion corta o complementaria del bien mueble. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_BIEN_MUEB` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Funciona como catalogo maestro para clasificar bienes muebles dentro de Legasys. |

---

## Tabla: `A_CAJA`

### Descripcion funcional
Tabla usada en Legasys para registrar cajas disponibles en el sistema. Permite identificar cada caja por nombre y serie, lo que resulta util para configuraciones operativas o administrativas del modulo Caja.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CAJA` | `int` | Identificador interno de la caja. |
| `DE_CAJA` | `varchar(50)` | Nombre o descripcion de la caja. |
| `DE_SERI_CAJA` | `varchar(20)` | Serie asociada a la caja. |
| `IN_ESTA` | `int` | Estado de la caja dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CAJA` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | La presencia de `DE_SERI_CAJA` sugiere una relacion con configuraciones operativas o de identificacion propias del modulo Caja. |

---

## Tabla: `A_CAUS_PROT`

### Descripcion funcional
Tabla usada en Legasys para registrar causas o motivos de protesto. Sirve como catalogo para seleccionar o clasificar este tipo de informacion en los flujos donde el sistema gestione protestos.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CAUS_PROT` | `int` | Identificador interno de la causa de protesto. |
| `DE_CAUS_PROT` | `varchar(100)` | Descripcion principal de la causa de protesto. |
| `DC_CAUS_PROT` | `varchar(50)` | Descripcion corta o complementaria. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CAUS_PROT` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Opera como catalogo de apoyo para procesos notariales o registrales relacionados con protestos. |

---

## Tabla: `A_CLAS_BIEN_type`

### Descripcion funcional
Tabla usada en Legasys para registrar clasificaciones de bienes. Permite mantener un catalogo estructurado con nombre unico y codigos auxiliares que el sistema puede usar para clasificar bienes en distintos procesos.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CLAS_BIEN` | `int unsigned` | Identificador interno de la clasificacion del bien. |
| `DE_CLAS_BIEN` | `varchar(60)` | Nombre unico de la clasificacion. |
| `CO_PDT` | `varchar(2)` | Codigo auxiliar asociado a la clasificacion. |
| `CO_BIEN` | `varchar(2)` | Codigo de bien relacionado a la clasificacion. |
| `CO_TIPO` | `varchar(2)` | Codigo de tipo asociado a la clasificacion. |
| `CO_CNL` | `varchar(10)` | Codigo complementario o de integracion usado por el sistema. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del catalogo. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CLAS_BIEN` | Clave principal de la tabla. |
| Unique | `A_CLAS_BIEN_type_unique` | `DE_CLAS_BIEN` | Evita clasificaciones duplicadas por nombre. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | `DE_CLAS_BIEN` debe mantenerse unico para evitar duplicidad de clasificaciones en Legasys. |
| Tecnica relevante | El nombre de la tabla termina en `_type`, por lo que debe respetarse exactamente en minuscula al referenciarla. |

---

## Tabla: `A_CLAS_PIC`

### Descripcion funcional
Tabla usada en Legasys como catalogo de clasificaciones relacionadas con `P_PIC`. Permite registrar clases activas con codigo, descripcion y trazabilidad basica para procesos donde el sistema necesite categorizar estos registros.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CLAS_PIC` | `int unsigned` | Identificador interno de la clasificacion. |
| `DE_CLAS_PIC` | `varchar(100)` | Nombre o descripcion principal de la clasificacion. |
| `DC_CLAS_PIC` | `varchar(10)` | Codigo corto o descripcion abreviada. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del catalogo. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CLAS_PIC` | Clave principal de la tabla. |
| Referenciada por | `P_PIC_ibfk_4` | `CO_CLAS_PIC` | La tabla `P_PIC` referencia esta clasificacion con restriccion `RESTRICT` en delete y update. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla actua como catalogo maestro para clasificar registros consumidos por `P_PIC`. |

---

## Tabla: `A_COBR`

### Descripcion funcional
Tabla usada en Legasys para registrar cobradores o responsables de cobranza asociados a una notaria. Permite identificar el nombre del cobrador y su indicador corto dentro del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_COBR` | `int` | Identificador interno del cobrador. |
| `CO_COMP` | `int` | Codigo de la notaria o compania a la que pertenece el cobrador. |
| `NO_COBR` | `varchar(100)` | Nombre del cobrador o responsable de cobranza. |
| `IN_INIC_COBR` | `varchar(5)` | Iniciales o identificador corto del cobrador. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_COBR` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | La presencia de `CO_COMP` indica que el catalogo de cobradores se maneja por notaria. |

---

## Tabla: `A_COMP`

### Descripcion funcional
Tabla central de Legasys para registrar la configuracion de cada notaria o compania. Define datos de identificacion, informacion institucional, parametros operativos, opciones de caja, integraciones, QR, facturacion electronica, pago web y otras banderas que condicionan el comportamiento del sistema por `CO_COMP`.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_COMP` | `int unsigned` | Identificador interno de la notaria o compania. |
| `DE_COMP` | `varchar(80)` | Nombre principal de la notaria o compania. |
| `DC_COMP` | `varchar(50)` | Descripcion corta o nombre alterno. |
| `NU_RUC` | `varchar(20)` | Numero de RUC de la notaria o compania. |
| `NO_NOTA` | `varchar(180)` | Nombre del notario o nombre institucional visible. |
| `AP_PATE` | `varchar(50)` | Apellido paterno del notario. |
| `AP_MATE` | `varchar(50)` | Apellido materno del notario. |
| `NO_PRES` | `varchar(50)` | Nombre de presentacion o representacion institucional. |
| `NU_DOCU` | `varchar(8)` | Numero de documento asociado al notario o representante. |
| `NU_REGI_NOTA` | `varchar(10)` | Numero de registro notarial. |
| `CO_SISE` | `char(6)` | Codigo unico configurado para la notaria en el sistema. |
| `CO_SUNA_SISE` | `varchar(20)` | Codigo relacionado a integracion o referencia SUNARP/SISE. |
| `CO_EMPR_UIF` | `varchar(10)` | Codigo de empresa para flujos UIF. |
| `CO_OFIC_UIF` | `varchar(10)` | Codigo de oficina para flujos UIF. |
| `DE_DIRE` | `varchar(200)` | Direccion principal de la notaria. |
| `IM_LOGO` | `varchar(20)` | Nombre o referencia historica del logo. |
| `CO_UBIG` | `varchar(6)` | Codigo de ubigeo de la notaria. |
| `DE_HORA_NOTA` | `varchar(100)` | Horario de atencion de la notaria. |
| `NU_TELE_NOTA` | `varchar(50)` | Telefono de la notaria. |
| `NU_TEFA_NOTA` | `varchar(50)` | Telefono adicional o fax de la notaria. |
| `NU_FAX_NOTA` | `varchar(50)` | Fax de la notaria. |
| `DE_URL_NOTA` | `varchar(100)` | URL principal de la notaria. |
| `DE_MAIL_NOTA` | `varchar(100)` | Correo electronico institucional. |
| `CO_OFIC_REGI` | `int unsigned` | Codigo de oficina registral asociada. |
| `IN_GENE_INST` | `char(1)` | Indicador de generacion de instrumento. |
| `IN_GENE_MINU` | `char(1)` | Indicador de generacion de minutas. |
| `IN_VALDAR_UIF` | `int unsigned` | Indicador o configuracion de validacion UIF. |
| `IN_SEGU_CAJA` | `char(1)` | Configuracion relacionada al seguimiento de Caja. |
| `IN_CALC_LIQU` | `char(1)` | Configuracion de calculo de liquidacion. |
| `IN_TICK_INIC` | `char(1)` | Indicador relacionado a la inicializacion de tickets. |
| `IN_SALT_PART` | `char(1)` | Configuracion relacionada a salto o flujo de participantes. |
| `IN_AUTO_CAJA` | `char(1)` | Indicador de automatizacion en Caja. |
| `IN_ANUL_CAJA` | `int` | Configuracion relacionada a anulacion en Caja. |
| `IN_GENE_WORD` | `char(1)` | Indicador de generacion de documentos Word. |
| `IN_AUTO_CART` | `int` | Configuracion de automatizacion de caratula o cartas. |
| `IN_PAGA_IMPU` | `int` | Configuracion relacionada a pago de impuestos. |
| `NU_TOKEN_FE` | `varchar(100)` | Token usado para facturacion electronica. |
| `DE_URL_FE` | `varchar(100)` | URL de integracion de facturacion electronica. |
| `DE_URL_DESC_FE` | `varchar(150)` | URL complementaria para descarga o consulta de facturacion electronica. |
| `CO_BANC_DETR` | `int` | Banco configurado para detracciones. |
| `NU_CUEN_DETR` | `varchar(200)` | Numero de cuenta para detracciones. |
| `IN_ACTI_FE` | `int` | Indicador de activacion de facturacion electronica. |
| `CO_CODNOTARIA` | `varchar(13)` | Codigo interno o externo de la notaria. |
| `CO_CODNOTARIO` | `varchar(8)` | Codigo interno o externo del notario. |
| `ACTI_NOTA` | `int` | Indicador de activacion operativa de la notaria. |
| `IN_JAVA` | `int` | Configuracion historica o tecnica asociada a Java. |
| `IN_QR` | `int` | Indicador de funcionalidad QR. |
| `IN_RRPP` | `int` | Indicador de funcionalidades de Registros Publicos. |
| `IN_CART_NUEV` | `char(1)` | Configuracion relacionada a una nueva version de caratula o cartas. |
| `IN_RENI_SUNA` | `int` | Indicador de integracion con RENIEC o SUNARP. |
| `IN_TIPO_ADVE_COMP` | `int` | Tipo de advertencia o comportamiento configurado por compania. |
| `IN_ENVI_FACT_CRED` | `smallint` | Configuracion de envio de facturas de credito. |
| `IN_ENVI_DOMI` | `int` | Indicador de envio o gestion de domicilios. |
| `IN_NUEV_CONS_LEGA` | `int` | Habilita o identifica nueva consulta legal. |
| `IN_GUAR_CARP` | `int` | Configuracion de guardado de carpeta o expedientes. |
| `IN_COLA_TICK` | `int` | Configuracion de cola de tickets. |
| `IN_ROBO_PART` | `int` | Indicador relacionado a robo o bloqueo de partidas. |
| `NU_DIAS_PART` | `int` | Numero de dias asociado a una regla sobre partidas. |
| `IN_ROBO_VEHI` | `int` | Indicador relacionado a robo o bloqueo vehicular. |
| `IN_REPO_VEHI` | `int` | Indicador de reporte vehicular. |
| `NO_TOKE_TIU` | `varchar(200)` | Token o nombre de token de integracion TIU. |
| `DE_URL_TICK` | `varchar(200)` | URL relacionada a tickets. |
| `DE_URL_PERU_NOTA` | `varchar(200)` | URL de integracion con Peru Notarios u otro servicio notarial. |
| `DE_TOKE_PERU_NOTA` | `text` | Token de integracion por notaria usado por servicios externos. |
| `DE_URL_QR` | `varchar(200)` | URL base o publica para funcionalidades QR. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `date` | Fecha de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado general de la notaria en el sistema. |
| `IN_URL_QR` | `int` | Indicador asociado al uso de URL para QR. |
| `IN_CONS_WEB` | `int` | Configuracion de consulta web publica. |
| `IN_PAGO_WEB` | `int` | Configuracion de pago web. |
| `IN_MINU_IA` | `int` | Configuracion relacionada a Minuta IA. |
| `IN_GRUP_ECON` | `int` | Indicador de uso de grupos economicos. |
| `IN_CORR` | `int` | Configuracion relacionada a correlativos o comportamiento interno. |
| `IN_NUME_TELF` | `int` | Configuracion sobre uso de numero telefonico. |
| `IN_TIPO_SERV` | `int` | Configuracion de tipos de servicio habilitados para la notaria. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_COMP` | Clave principal de la tabla. |
| Unique | `A_COMP_UNIQUE` | `NU_RUC` | Evita repetir RUC entre notarías o companias. |
| Unique | `CO_SISE` | `CO_SISE` | Evita duplicar el codigo `CO_SISE`. |
| Referenciada por | `A_SEMI_KARD_ibfk_1` | `CO_COMP` | La tabla `A_SEMI_KARD` referencia esta tabla con restriccion `RESTRICT`. |
| Referenciada por | `H_REQU_SERV_ibfk_2` | `CO_COMP` | La tabla `H_REQU_SERV` referencia esta tabla con restriccion `RESTRICT`. |
| Referenciada por | `P_PIC_ibfk_3` | `CO_COMP` | La tabla `P_PIC` referencia esta tabla con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | `A_COMP` es una de las tablas mas sensibles de Legasys porque condiciona el comportamiento del sistema por notaria. |
| Funcional | El uso de `CO_COMP` es clave en el contexto multinotaria y debe respetarse en consultas, configuraciones y catalogos asociados. |
| Funcional | Contiene parametros directamente relacionados con Caja, QR, facturacion electronica, Registros Publicos, pago web y Minuta IA. |

---

## Tabla: `A_COMP_SEGU`

### Descripcion funcional
Tabla usada en Legasys como catalogo de companias de seguros o entidades equivalentes. Permite mantener una lista activa con trazabilidad basica para procesos donde el sistema deba asociar seguros a tramites o registros.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_COMP_SEGU` | `int unsigned` | Identificador interno de la compania de seguros. |
| `DE_COMP_SEGU` | `varchar(100)` | Nombre o descripcion principal de la compania de seguros. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del catalogo. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_COMP_SEGU` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Funciona como catalogo maestro para procesos que requieran asociar una compania de seguros en Legasys. |

---

## Tabla: `A_CPTO_EGRE`

### Descripcion funcional
Tabla usada en Legasys para registrar conceptos de egreso e ingreso usados por el modulo Caja. Permite clasificar movimientos externos y distinguir su tipo funcional dentro del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CPTO_EGRE` | `int unsigned` | Identificador interno del concepto. |
| `IN_TIPO_EGRE` | `char(1)` | Tipo funcional del concepto. |
| `DE_CPTO_EGRE` | `varchar(100)` | Descripcion principal del concepto de egreso o ingreso. |
| `DC_CPTO_EGRE` | `varchar(50)` | Descripcion corta o complementaria del concepto. |
| `IN_ESTA` | `int unsigned` | Estado del concepto dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CPTO_EGRE` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Segun la captura, `IN_TIPO_EGRE` distingue categorias como personal, proveedor, depositos, otros egresos, ingresos, nota de credito y devolucion RRPP. |
| Funcional | Esta tabla es relevante para el comportamiento del modulo de movimientos externos de Caja. |

---

## Tabla: `A_DATO_CORR`

### Descripcion funcional
Tabla usada en Legasys para almacenar configuraciones de correo por notaria o compania. Define host, puerto, usuario y clave para los envios salientes que el sistema realiza desde sus flujos operativos.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DATO_CORR` | `int` | Identificador interno de la configuracion de correo. |
| `CO_COMP` | `int` | Codigo de la notaria o compania a la que pertenece la configuracion. |
| `NO_HOST` | `varchar(50)` | Servidor o host de correo saliente. |
| `NO_SMTP` | `varchar(10)` | Puerto o identificador SMTP configurado. |
| `NU_PUER` | `varchar(5)` | Numero de puerto usado por el servicio de correo. |
| `NO_USUA` | `varchar(100)` | Usuario o cuenta de autenticacion del correo. |
| `DE_PASS` | `varchar(100)` | Clave asociada a la cuenta de correo configurada. |
| `IN_ESTA` | `char(1)` | Estado de la configuracion en el sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DATO_CORR` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | La presencia de `CO_COMP` indica que la configuracion de correo puede variar por notaria. |
| Tecnica relevante | Contiene credenciales operativas del sistema, por lo que su tratamiento debe considerarse sensible. |

---

## Tabla: `A_DEPA`

### Descripcion funcional
Tabla usada en Legasys como catalogo geografico de departamentos. Permite organizar informacion territorial y sirve de base para provincias, distritos y otros registros que dependen de la ubicacion.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DEPA` | `int unsigned` | Identificador interno del departamento. |
| `CO_PAIS` | `int unsigned` | Codigo del pais al que pertenece el departamento. |
| `CO_INEI_DEPA` | `varchar(2)` | Codigo INEI del departamento. |
| `DE_DEPA` | `varchar(50)` | Nombre del departamento. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del catalogo. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DEPA` | Clave principal de la tabla. |
| Unique | `A_DEPA_UNIQUE` | `CO_PAIS, CO_INEI_DEPA` | Evita duplicar el codigo INEI por pais. |
| Index | `A_DEPA_FKIndex1` | `CO_PAIS` | Indice de apoyo para relaciones por pais. |
| Index | `A_DEPA_INEI_INDEX` | `CO_INEI_DEPA` | Indice de apoyo para busquedas por codigo INEI. |
| Referenciada por | `A_PROV_ibfk_1` | `CO_DEPA` | La tabla `A_PROV` referencia esta tabla con restriccion `RESTRICT`. |
| Referenciada por | `P_PIC_ibfk_1` | `CO_DEPA` | La tabla `P_PIC` referencia esta tabla con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Es parte del catalogo geografico base de Legasys y soporta dependencias territoriales del sistema. |

---

## Tabla: `A_DIST`

### Descripcion funcional
Tabla usada en Legasys como catalogo geografico de distritos. Permite ubicar registros dentro de una provincia y soporta procesos que dependen de la estructura territorial del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DIST` | `int unsigned` | Identificador interno del distrito. |
| `CO_PROV` | `int unsigned` | Codigo de la provincia a la que pertenece el distrito. |
| `CO_INEI_DIST` | `varchar(2)` | Codigo INEI del distrito. |
| `DE_DIST` | `varchar(50)` | Nombre del distrito. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del catalogo. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DIST` | Clave principal de la tabla. |
| Unique | `A_DIST_UNIQUE` | `CO_PROV, CO_INEI_DIST` | Evita duplicar el codigo INEI por provincia. |
| Index | `A_DIST_FKIndex1` | `CO_PROV` | Indice de apoyo para relaciones por provincia. |
| Index | `A_DIST_INEI_INDEX` | `CO_INEI_DIST` | Indice de apoyo para busquedas por codigo INEI. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Forma parte del catalogo geografico usado por Legasys para direcciones, ubigeos y registros dependientes del distrito. |

---

## Tabla: `A_DIAS_FERI`

### Descripcion funcional
Tabla usada en Legasys para registrar dias feriados. Permite al sistema identificar fechas no laborables y ajustar comportamientos operativos o validaciones basadas en calendario.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DIAS_FERI` | `int` | Identificador interno del feriado. |
| `FE_DIAS_FERI` | `date` | Fecha marcada como dia feriado. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DIAS_FERI` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo puede influir en agendas, vencimientos o validaciones de fechas dentro de Legasys. |

---

## Tabla: `A_DOCU_FIRM`

### Descripcion funcional
Tabla usada en Legasys para registrar tipos o configuraciones de documentos vinculados al flujo de firma. Permite asociar documentos a un registro notarial y mantener su estado dentro del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DOCU_FIRM` | `int unsigned` | Identificador interno del documento de firma. |
| `CO_REGI_NOTA` | `int` | Codigo de registro notarial asociado. |
| `DE_DOCU_FIRM` | `varchar(100)` | Nombre o descripcion principal del documento. |
| `DC_DOCU_FIRM` | `varchar(50)` | Descripcion corta o abreviada del documento. |
| `CO_USUA_MOD` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `date` | Fecha de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del catalogo. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DOCU_FIRM` | Clave principal de la tabla. |
| Referenciada por | `H_CODO_ibfk_1` | `CO_DOCU_FIRM` | La tabla `H_CODO` referencia esta tabla con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla participa en el ecosistema documental y de firma del sistema. |

---

## Tabla: `A_EFEC_MONE`

### Descripcion funcional
Tabla usada en Legasys para registrar denominaciones monetarias de billetes y monedas. Sirve de apoyo para procesos de Caja donde el sistema requiere contar o detallar efectivo por tipo de moneda y valor.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_EFEC_MONE` | `int` | Identificador interno del registro de efectivo. |
| `CO_TIPO_MONE` | `int` | Tipo de moneda asociado. Segun la captura: `1 = soles`, `2 = dolares`. |
| `DE_EFEC_MONE` | `varchar(100)` | Descripcion de la denominacion monetaria. |
| `NU_EFEC_MONE` | `decimal(18,2)` | Valor monetario de la denominacion. |
| `IN_EFEC_MONE` | `smallint` | Tipo de efectivo. Segun la captura: `1 = billetes`, `2 = monedas`. |
| `IN_ESTA` | `smallint` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_EFEC_MONE` | Clave principal de la tabla. |
| Referenciada por | `fk_H_DETA_CIER_CAJA_A_EFEC_MONE_1` | `CO_EFEC_MONE` | La tabla `R_DETA_CIER_CAJA` referencia esta tabla con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Es un catalogo operativo del modulo Caja para el control de billetes y monedas en cierres o arqueos. |

---

## Tabla: `A_ENTI_PIC`

### Descripcion funcional
Tabla usada en Legasys como catalogo de entidades relacionadas con `P_PIC`. Permite clasificar o asociar registros de ese modulo a una entidad determinada.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ENTI` | `int unsigned` | Identificador interno de la entidad. |
| `DE_ENTI` | `varchar(100)` | Nombre o descripcion principal de la entidad. |
| `DC_ENTI` | `varchar(10)` | Codigo corto o descripcion abreviada. |
| `CO_USUA_MOD` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `date` | Fecha de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del catalogo. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ENTI` | Clave principal de la tabla. |
| Referenciada por | `P_PIC_ibfk_2` | `CO_ENTI` | La tabla `P_PIC` referencia esta tabla con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Funciona como catalogo maestro consumido por `P_PIC`. |

---

## Tabla: `A_ESTA_CAJA`

### Descripcion funcional
Tabla usada en Legasys para registrar los estados posibles del modulo Caja. Permite controlar el ciclo de vida operativo de registros o comprobantes vinculados a Caja.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ESTA_CAJA` | `int` | Identificador del estado de Caja. |
| `DE_ESTA_CAJA` | `varchar(100)` | Nombre del estado de Caja. |
| `DC_ESTA_CAJA` | `varchar(50)` | Nombre corto del estado de Caja. |
| `IN_ESTA` | `smallint` | Estado del registro en el catalogo. Segun la captura: `1 = activo`, `0 = inactivo`. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ESTA_CAJA` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Es un catalogo base del modulo Caja y define estados consumidos por sus flujos operativos. |

---

## Tabla: `A_ESTA_CIVI`

### Descripcion funcional
Tabla usada en Legasys como catalogo de estados civiles. Permite clasificar participantes o personas naturales segun su condicion civil dentro del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ESTA_CIVI` | `int unsigned` | Identificador interno del estado civil. |
| `CO_UIF` | `varchar(3)` | Codigo asociado a flujos o clasificaciones UIF. |
| `CO_SID` | `varchar(2)` | Codigo asociado a integraciones o clasificaciones SID. |
| `DE_ESTA_CIVI` | `varchar(50)` | Nombre del estado civil. |
| `DC_GENE_MASC` | `varchar(50)` | Descripcion generica o forma asociada al genero masculino. |
| `DC_GENE_FEME` | `varchar(50)` | Descripcion generica o forma asociada al genero femenino. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ESTA_CIVI` | Clave principal de la tabla. |
| Referenciada por | `H_PRTC_NATU_ibfk_5` | `CO_ESTA_CIVI` | La tabla `H_PRTC_NATU` referencia esta tabla con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo impacta directamente en participantes y personas naturales dentro de Legasys. |

---

## Tabla: `A_ESTA_PAGO_LINE`

### Descripcion funcional
Tabla usada en Legasys para registrar los estados del flujo de pago en linea. Permite controlar la evolucion de operaciones de pago web y sirve como catalogo base para cabeceras e historiales del modulo.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ESTA_PAGO_LINE` | `int` | Identificador interno del estado de pago en linea. |
| `DE_ESTA_PAGO_LINE` | `varchar(100)` | Nombre principal del estado. |
| `DC_ESTA_PAGO_LINE` | `varchar(20)` | Codigo corto o descripcion breve del estado. |
| `NU_ORDE` | `int` | Orden del estado dentro del flujo. |
| `IN_ESTA` | `int` | Estado del registro dentro del catalogo. |
| `CO_USUA_MOD` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ESTA_PAGO_LINE` | Clave principal de la tabla. |
| Unique | `UK_A_ESTA_PAGO_LINE_01` | `DC_ESTA_PAGO_LINE` | Evita codigos cortos duplicados para estados del flujo. |
| Index | `IDX_A_ESTA_PAGO_LINE_01` | `IN_ESTA` | Indice de apoyo para filtrar estados activos/inactivos. |
| Referenciada por | `FK_H_ESTA_PAGO_LINE_02` | `CO_ESTA_PAGO_LINE` | La tabla `H_ESTA_PAGO_LINE` referencia esta tabla con restriccion `RESTRICT`. |
| Referenciada por | `FK_P_CABE_PAGO_LINE_01` | `CO_ESTA_PAGO_LINE` | La tabla `P_CABE_PAGO_LINE` referencia esta tabla con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es clave para el modulo de pago en linea porque normaliza los estados consumidos por la cabecera del pago y su historial. |

---

## Tabla: `A_ESTA_PROT`

### Descripcion funcional
Tabla usada en Legasys para registrar los estados aplicables a protestos. Funciona como catalogo de apoyo para identificar en que situacion se encuentra un protesto dentro del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ESTA_PROT` | `int` | Identificador interno del estado de protesto. |
| `DE_ESTA_PROT` | `varchar(100)` | Nombre del estado de protesto. |
| `DC_ESTA_PROT` | `varchar(50)` | Descripcion corta o abreviada del estado. |
| `IN_ESTA` | `int` | Estado del registro dentro del catalogo. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ESTA_PROT` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Sirve como catalogo base para procesos notariales vinculados a protestos. |

---

## Tabla: `A_ETAP_TRAM_type`

### Descripcion funcional
Tabla usada en Legasys para definir las etapas del tramite. Es un catalogo central para el avance operativo y documental de los kardex o tramites dentro del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ETAP_TRAM` | `int unsigned` | Identificador interno de la etapa del tramite. |
| `CO_MODU` | `int` | Modulo o ambito del sistema al que pertenece la etapa. |
| `DE_ETAP_TRAM` | `varchar(50)` | Nombre unico de la etapa. |
| `DC_ETAP_TRAM` | `varchar(50)` | Descripcion corta o abreviada de la etapa. |
| `DE_ETAP_TRAM_` | `varchar(50)` | Texto complementario o variante descriptiva de la etapa. |
| `DE_WEB_ETAP_T` | `varchar(100)` | Descripcion visible o adaptada para uso web. |
| `IN_ORDE` | `int` | Orden en el que avanzan los estados o etapas. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ETAP_TRAM` | Clave principal de la tabla. |
| Unique | `A_ETAP_TRAM_type_UNIQUE` | `DE_ETAP_TRAM` | Evita etapas duplicadas por nombre. |
| Referenciada por | `H_SGMT_TRAM_ibfk_2` | `CO_ETAP_TRAM` | La tabla `H_SGMT_TRAM` referencia esta tabla con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | `IN_ORDE` es especialmente relevante porque, segun la captura, define el orden en el que van avanzando los estados. |
| Tecnica relevante | El nombre de la tabla termina en `_type`, por lo que debe respetarse exactamente en minuscula al referenciarla. |

---

## Tabla: `A_FORM_PAGO`

### Descripcion funcional
Tabla usada en Legasys como catalogo general de formas de pago. Permite definir medios de pago reutilizables en distintos procesos del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_FORM_PAGO` | `int unsigned` | Identificador interno de la forma de pago. |
| `CO_UIF` | `varchar(1)` | Codigo auxiliar asociado a flujos UIF u otras clasificaciones. |
| `DE_FORM_PAGO` | `varchar(100)` | Nombre de la forma de pago. |
| `DC_FORM_PAGO` | `varchar(50)` | Descripcion corta o abreviada. |
| `CO_USUA_MOD` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del catalogo. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_FORM_PAGO` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Opera como catalogo general de medios de pago dentro de Legasys. |

---

## Tabla: `A_FORM_PAGO_CAJA`

### Descripcion funcional
Tabla usada en Legasys como catalogo de formas de pago especificas del modulo Caja. Permite mantener una lista operativa separada para los flujos de cobro y pago en Caja.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_FORM_PAGO_CAJA` | `int unsigned` | Identificador interno de la forma de pago en Caja. |
| `DE_FORM_PAGO_CAJA` | `varchar(100)` | Nombre de la forma de pago en Caja. |
| `DC_FORM_PAGO_CAJA` | `varchar(50)` | Descripcion corta o abreviada. |
| `CO_USUA_MOD` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `date` | Fecha de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del catalogo. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_FORM_PAGO_CAJA` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Aunque existe `A_FORM_PAGO`, esta tabla parece especializar el catalogo para el modulo Caja. |

---

## Tabla: `A_FUNC_PLAN`

### Descripcion funcional
Tabla usada en Legasys para registrar funciones o piezas reutilizables asociadas a planes, alias o configuraciones internas. Permite guardar nombre, tipo de recurso, definicion funcional y codigo fuente consumido por el sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_FUNC_PLAN` | `bigint unsigned` | Identificador interno de la funcion o recurso. |
| `NO_FUNC` | `varchar(100)` | Nombre de la funcion o configuracion. |
| `TI_RESO` | `varchar(20)` | Tipo de recurso. Segun la captura, el valor por defecto es `FUNCION`. |
| `DE_FUNC` | `varchar(300)` | Descripcion funcional del recurso. |
| `TX_CODI` | `text` | Codigo o contenido fuente asociado a la funcion. |
| `IN_ESTA` | `tinyint` | Estado del registro dentro del sistema. |
| `TS_USUA_MODI` | `timestamp` | Fecha y hora de la ultima modificacion. |
| `CO_USUA_MODI` | `varchar(20)` | Usuario que realizo la ultima modificacion. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_FUNC_PLAN` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | `TX_CODI` sugiere que esta tabla almacena logica configurable o codigo reutilizable consumido por Legasys. |
| Funcional | Esta tabla es especialmente relevante para funcionalidades configurables, alias o comportamientos dinamicos del sistema. |

---

## Tabla: `A_IGV`

### Descripcion funcional
Tabla usada en Legasys para registrar configuraciones del IGV. Permite almacenar valores o parametros vigentes del impuesto que pueden ser consumidos por procesos de liquidacion, Caja o calculos tributarios.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_IGV` | `int unsigned` | Identificador interno de la configuracion de IGV. |
| `NU_IGV` | `int` | Valor entero o referencia principal del IGV. |
| `FE_CAMB` | `date` | Fecha de cambio o vigencia de la configuracion. |
| `NU_IGV_1` | `decimal(12,2)` | Valor decimal complementario del IGV. |
| `NU_IGV_2` | `decimal(12,2)` | Segundo valor decimal complementario del IGV. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_IGV` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla puede influir en calculos tributarios del sistema, especialmente en modulos economicos como Caja o liquidacion. |

---

## Tabla: `A_INDI_GENE_type`

### Descripcion funcional
Tabla usada en Legasys como catalogo de indicadores de genero. Permite clasificar personas o participantes usando un valor estandarizado dentro del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_INDI_GENE` | `int unsigned` | Identificador interno del indicador de genero. |
| `DE_INDI_GENE` | `varchar(20)` | Descripcion unica del indicador de genero. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_INDI_GENE` | Clave principal de la tabla. |
| Unique | `DE_INDI_GENE` | `DE_INDI_GENE` | Evita indicadores de genero duplicados por descripcion. |
| Referenciada por | `H_PRTC_NATU_ibfk_3` | `CO_INDI_GENE` | La tabla `H_PRTC_NATU` referencia esta tabla con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo impacta directamente en participantes y personas naturales dentro de Legasys. |
| Tecnica relevante | El nombre de la tabla termina en `_type`, por lo que debe respetarse exactamente en minuscula al referenciarla. |

---

## Tabla: `A_INDI_OCUP_type`

### Descripcion funcional
Tabla usada en Legasys como catalogo de indicadores u ocupaciones. Permite clasificar a personas naturales segun una ocupacion o condicion ocupacional dentro del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_INDI_OCUP` | `int unsigned` | Identificador interno del indicador u ocupacion. |
| `DE_INDI_OCUP` | `varchar(50)` | Descripcion unica de la ocupacion o indicador ocupacional. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_INDI_OCUP` | Clave principal de la tabla. |
| Unique | `DE_INDI_OCUP` | `DE_INDI_OCUP` | Evita ocupaciones duplicadas por descripcion. |
| Referenciada por | `H_PRTC_NATU_ibfk_4` | `CO_INDI_OCUP` | La tabla `H_PRTC_NATU` referencia esta tabla con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo impacta directamente en participantes y personas naturales dentro de Legasys. |
| Tecnica relevante | El nombre de la tabla termina en `_type`, por lo que debe respetarse exactamente en minuscula al referenciarla. |

---

## Tabla: `A_INDI_PEP`

### Descripcion funcional
Tabla usada en Legasys para registrar indicadores o clasificaciones PEP. Permite identificar condiciones relacionadas con cumplimiento o validaciones de personas expuestas politicamente.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_INDI_PEP` | `int` | Identificador interno del indicador PEP. |
| `DE_INDI_PEP` | `varchar(200)` | Descripcion principal del indicador PEP. |
| `CO_UIF` | `varchar(10)` | Codigo auxiliar asociado a flujos UIF. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_INDI_PEP` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo es relevante para reglas de cumplimiento, UIF y validaciones asociadas a personas. |

---

## Tabla: `A_LIBR_REGI`

### Descripcion funcional
Tabla usada en Legasys para registrar libros registrales vinculados a un codigo SUNARP o registral. Sirve como catalogo de apoyo para procesos que requieren identificar el libro registral correspondiente.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_LIBR_REGI` | `int unsigned` | Identificador interno del libro registral. |
| `CO_REGI_SUNA` | `int unsigned` | Codigo registral o SUNARP asociado al libro. |
| `DE_LIBR_REGI` | `varchar(100)` | Nombre o descripcion principal del libro registral. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_LIBR_REGI` | Clave principal de la tabla. |
| Index | `A_LIBR_REGI_FKIndex1` | `CO_REGI_SUNA` | Indice de apoyo para consultas por codigo registral. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla soporta flujos donde el sistema necesita mapear libros registrales con clasificaciones registrales o SUNARP. |

---

## Tabla: `A_MEDI_PAGO`

### Descripcion funcional
Tabla usada en Legasys como catalogo de medios de pago. Permite registrar medios reutilizables con codigos auxiliares y trazabilidad basica para procesos administrativos, de Caja o integraciones.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_MEDI_PAGO` | `int` | Identificador interno del medio de pago. |
| `DE_MEDI_PAGO` | `varchar(100)` | Nombre del medio de pago. |
| `DC_MEDI_PAGO` | `varchar(50)` | Descripcion corta o abreviada. |
| `CO_UIF` | `varchar(3)` | Codigo auxiliar asociado a flujos UIF. |
| `MEDI_PAGO_PDT` | `varchar(3)` | Codigo del medio de pago para PDT u otra integracion externa. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_MEDI_PAGO` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo puede alimentar procesos de Caja, cobros y validaciones de medios de pago en Legasys. |

---

## Tabla: `A_MENS`

### Descripcion funcional
Tabla usada en Legasys para registrar mensajeros o responsables de mensajeria asociados a una notaria. Permite identificar al usuario relacionado y su abreviatura operativa dentro del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_MENS` | `int unsigned` | Identificador interno del mensajero. |
| `CO_COMP` | `int unsigned` | Codigo de la notaria o compania a la que pertenece el mensajero. |
| `CO_USUA` | `int` | Usuario del sistema asociado al mensajero. |
| `NO_MENS` | `varchar(100)` | Nombre del mensajero. |
| `IN_INIC_MENS` | `varchar(5)` | Iniciales o identificador corto del mensajero. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_MENS` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | La presencia de `CO_COMP` indica que este catalogo se maneja por notaria. |

---

## Tabla: `A_MES`

### Descripcion funcional
Tabla usada en Legasys como catalogo de meses. Permite representar el numero, nombre y abreviatura del mes para reportes, formatos o procesos dependientes del calendario.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_MES` | `int` | Identificador interno del mes. |
| `NU_MES` | `varchar(2)` | Numero o codigo del mes. |
| `NO_MES` | `varchar(50)` | Nombre del mes. |
| `DC_MES` | `varchar(10)` | Abreviatura o descripcion corta del mes. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_MES` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Es un catalogo base de calendario reutilizable por distintos modulos del sistema. |

---

## Tabla: `A_MODU_type`

### Descripcion funcional
Tabla usada en Legasys como catalogo de modulos del sistema. Permite clasificar servicios y otros elementos segun el modulo funcional al que pertenecen.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_MODU` | `int unsigned` | Identificador interno del modulo. |
| `DE_MODU` | `varchar(50)` | Nombre unico del modulo. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_MODU` | Clave principal de la tabla. |
| Unique | `DE_MODU` | `DE_MODU` | Evita modulos duplicados por nombre. |
| Referenciada por | `P_SERV_ibfk_3` | `CO_MODU` | La tabla `P_SERV` referencia esta tabla con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo impacta directamente en la organizacion funcional de servicios dentro de Legasys. |
| Tecnica relevante | El nombre de la tabla termina en `_type`, por lo que debe respetarse exactamente en minuscula al referenciarla. |

---

## Tabla: `A_MOTI_FALLO_CAJA`

### Descripcion funcional
Tabla usada en Legasys para registrar motivos de fallo o error en el modulo Caja. Sirve como catalogo de apoyo para clasificar incidencias operativas dentro de ese flujo.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_MOTI_FALLO_CAJA` | `int` | Identificador interno del motivo de fallo. |
| `DE_MOTI_FALLO_CAJA` | `varchar(100)` | Descripcion principal del motivo. |
| `DC_MOTI_FALLO_CAJA` | `varchar(50)` | Descripcion corta o abreviada. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_MOTI_FALLO_CAJA` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Es un catalogo de soporte para incidencias o errores del modulo Caja. |

---

## Tabla: `A_MOTI_NOTA`

### Descripcion funcional
Tabla usada en Legasys para registrar motivos de nota de credito o nota de debito. Permite clasificar el motivo aplicado en comprobantes o ajustes dentro de procesos de Caja y facturacion.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_MOTI_NOTA` | `int` | Identificador interno del motivo de nota. |
| `IN_CLAS_NOTA` | `int` | Clase de nota. Segun la captura: `1 = nota credito`, `2 = nota debito`. |
| `IN_TIPO_NOTA` | `int` | Tipo especifico del motivo aplicado a la nota. |
| `DE_MOTI_NOTA` | `varchar(100)` | Descripcion principal del motivo. |
| `DC_MOTI_NOTA` | `varchar(50)` | Descripcion corta o abreviada. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_MOTI_NOTA` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Segun la regla compartida, `IN_TIPO_NOTA` puede representar: `1 = Anulacion de la operacion`, `2 = Anulacion por error en el RUC`, `3 = Correccion por error en la descripcion`, `4 = Descuento global`, `5 = Descuento por item`, `6 = Devolucion total`, `7 = Devolucion por item`, `8 = Bonificacion`, `9 = Disminucion en el valor`. |
| Funcional | Esta tabla es relevante para notas de credito y debito dentro de los flujos de Caja y facturacion. |

---

## Tabla: `A_NACI_type`

### Descripcion funcional
Tabla usada en Legasys como catalogo de nacionalidades. Permite clasificar personas juridicas u otros registros segun su nacionalidad dentro del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_NACI` | `int unsigned` | Identificador interno de la nacionalidad. |
| `DE_NACI` | `varchar(30)` | Descripcion unica de la nacionalidad. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_NACI` | Clave principal de la tabla. |
| Unique | `DE_NACI` | `DE_NACI` | Evita nacionalidades duplicadas por descripcion. |
| Referenciada por | `H_PRTC_JURI_ibfk_2` | `CO_NACI` | La tabla `H_PRTC_JURI` referencia esta tabla con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo influye en participantes juridicos y datos de clasificacion de personas en Legasys. |
| Tecnica relevante | El nombre de la tabla termina en `_type`, por lo que debe respetarse exactamente en minuscula al referenciarla. |

---

## Tabla: `A_NATU_DOCU_type`

### Descripcion funcional
Tabla usada en Legasys como catalogo de naturaleza documental. Permite clasificar documentos segun un tipo o naturaleza estandarizada dentro del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_NATU_DOCU` | `int unsigned` | Identificador interno de la naturaleza documental. |
| `DE_NATU_DOCU` | `varchar(50)` | Descripcion unica de la naturaleza documental. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_NATU_DOCU` | Clave principal de la tabla. |
| Unique | `DE_NATU_DOCU` | `DE_NATU_DOCU` | Evita naturalezas documentales duplicadas por descripcion. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Tecnica relevante | El nombre de la tabla termina en `_type`, por lo que debe respetarse exactamente en minuscula al referenciarla. |

---

## Tabla: `A_OFIC_REGI`

### Descripcion funcional
Tabla usada en Legasys para registrar oficinas registrales. Permite asociar una oficina a una zona registral y manejar codigos auxiliares utilizados por procesos registrales o integraciones.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_OFIC_REGI` | `int unsigned` | Identificador interno de la oficina registral. |
| `CO_ZONA_REGI` | `int unsigned` | Codigo de la zona registral a la que pertenece la oficina. |
| `CO_API_TIU` | `int` | Codigo auxiliar asociado a integraciones o APIs. |
| `DE_OFIC_REGI` | `varchar(100)` | Nombre o descripcion principal de la oficina registral. |
| `CO_ZONA_OFIC_SUNA` | `varchar(4)` | Codigo unico de zona u oficina SUNARP. |
| `IN_INIC_PLAC` | `varchar(100)` | Configuracion o dato auxiliar relacionado con placa o iniciales. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_OFIC_REGI` | Clave principal de la tabla. |
| Unique | `A_OFIC_REGI_UNIQUE` | `CO_ZONA_OFIC_SUNA` | Evita duplicar el codigo SUNARP de zona u oficina. |
| Index | `A_OFIC_REGI_ZONA_REGI` | `CO_ZONA_REGI` | Indice de apoyo para consultas por zona registral. |
| Foreign Key | `A_OFIC_REGI_ibfk_1` | `CO_ZONA_REGI` | Referencia a `A_ZONA_REGI` con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es parte del catalogo registral consumido por flujos vinculados a SUNARP o configuraciones notariales. |

---

## Tabla: `A_OFIC_REGI_SID`

### Descripcion funcional
Tabla usada en Legasys para registrar oficinas registrales SID. Permite mantener un catalogo de oficinas con nombre, descripcion y datos auxiliares consumidos por procesos registrales o integraciones SID.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_OFIC_REGI_SID` | `int` | Identificador interno de la oficina registral SID. |
| `VA_OFIC_REGI_SID` | `varchar(100)` | Valor o nombre corto de la oficina registral SID. |
| `DE_OFIC_REGI_SID` | `varchar(200)` | Descripcion principal de la oficina registral SID. |
| `IN_INIC_PLAC` | `varchar(100)` | Dato auxiliar o configuracion operativa asociada. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_OFIC_REGI_SID` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo parece complementar la configuracion registral usada por integraciones o flujos SID. |

---

## Tabla: `A_OFIC_REGI_SUNA`

### Descripcion funcional
Tabla usada en Legasys para registrar oficinas registrales SUNARP. Sirve como catalogo base para identificar oficinas consumidas por procesos registrales.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_OFIC_REGI_SUNA` | `int` | Identificador interno de la oficina registral SUNARP. |
| `VA_OFIC_REGI_SUNA` | `varchar(50)` | Valor o codigo corto de la oficina registral SUNARP. |
| `DE_OFIC_REGI_SUNA` | `varchar(100)` | Nombre o descripcion principal de la oficina registral SUNARP. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_OFIC_REGI_SUNA` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Forma parte de los catalogos registrales usados por Legasys. |

---

## Tabla: `A_OPOR_PAGO`

### Descripcion funcional
Tabla usada en Legasys como catalogo de oportunidades o condiciones de pago. Permite clasificar reglas o escenarios operativos asociados al proceso de pago.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_OPOR_PAGO` | `int` | Identificador interno de la oportunidad de pago. |
| `CO_UIF` | `varchar(2)` | Codigo auxiliar asociado a clasificaciones UIF. |
| `DE_OPOR_PAGO` | `varchar(100)` | Descripcion principal de la oportunidad o condicion de pago. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `date` | Fecha de la ultima modificacion. |
| `IN_ESTA` | `varchar(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_OPOR_PAGO` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo puede apoyar validaciones o clasificaciones relacionadas con pagos. |

---

## Tabla: `A_ORIG_PIC`

### Descripcion funcional
Tabla usada en Legasys como catalogo de origenes relacionados con `P_PIC`. Permite clasificar el origen de registros consumidos por ese modulo.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ORIG_PIC` | `int unsigned` | Identificador interno del origen. |
| `DE_ORIG_PIC` | `varchar(100)` | Descripcion principal del origen. |
| `DC_ORIG_PIC` | `varchar(10)` | Codigo corto o abreviatura del origen. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del catalogo. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ORIG_PIC` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Funciona como catalogo maestro consumido por `P_PIC` o procesos relacionados. |

---

## Tabla: `A_ORIG_UIF`

### Descripcion funcional
Tabla usada en Legasys como catalogo de origenes para flujos UIF. Permite clasificar el origen de registros o datos dentro de procesos de cumplimiento.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ORIG_UIF` | `int` | Identificador interno del origen UIF. |
| `CO_UIF` | `varchar(10)` | Codigo auxiliar asociado al origen. |
| `DE_ORIG_UIF` | `varchar(150)` | Descripcion principal del origen UIF. |
| `DC_ORIG_UIF` | `varchar(150)` | Descripcion corta o complementaria del origen UIF. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ORIG_UIF` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Es relevante para clasificaciones y validaciones asociadas a UIF dentro de Legasys. |

---

## Tabla: `A_PAGO_CAPI_type`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de pago de capital. Permite clasificar este tipo de operaciones mediante un valor estandarizado.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PAGO_CAPI` | `int unsigned` | Identificador interno del tipo de pago de capital. |
| `DE_PAGO_CAPI` | `varchar(30)` | Descripcion unica del tipo de pago de capital. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PAGO_CAPI` | Clave principal de la tabla. |
| Unique | `DE_PAGO_CAPI` | `DE_PAGO_CAPI` | Evita tipos duplicados por descripcion. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Tecnica relevante | El nombre de la tabla termina en `_type`, por lo que debe respetarse exactamente en minuscula al referenciarla. |

---

## Tabla: `A_PAGO_ONP`

### Descripcion funcional
Tabla usada en Legasys como catalogo de pagos ONP. Permite definir tipos o clasificaciones basicas relacionadas con este concepto previsional.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PAGO_ONP` | `int` | Identificador interno del tipo de pago ONP. |
| `DE_PAGO_ONP` | `varchar(50)` | Descripcion principal del pago ONP. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PAGO_ONP` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Es un catalogo especializado para clasificaciones de pagos ONP dentro de Legasys. |

---

## Tabla: `A_PAGO_UIF`

### Descripcion funcional
Tabla usada en Legasys como catalogo de pagos asociados a flujos UIF. Permite clasificar pagos con codigos auxiliares y mantener trazabilidad basica.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PAGO_UIF` | `varchar(3)` | Identificador o codigo principal del pago UIF. |
| `DE_PAGO_UIF` | `varchar(100)` | Descripcion principal del pago UIF. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `date` | Fecha de la ultima modificacion. |
| `IN_ESTA` | `varchar(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PAGO_UIF` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo es relevante para clasificaciones o validaciones de pagos en flujos UIF. |

---

## Tabla: `A_PAIS`

### Descripcion funcional
Tabla usada en Legasys como catalogo de paises. Permite identificar paises con distintos codigos auxiliares usados por el sistema, UIF u otras integraciones.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PAIS` | `int unsigned` | Identificador interno del pais. |
| `CO_INEI_PAIS` | `varchar(2)` | Codigo INEI del pais. |
| `CO_UIF` | `varchar(2)` | Codigo auxiliar asociado a flujos UIF. |
| `NO_PAIS` | `varchar(50)` | Nombre del pais. |
| `NC_PAIS` | `varchar(20)` | Nombre corto o codigo complementario del pais. |
| `DC_PAIS_GERU` | `varchar(60)` | Descripcion complementaria del pais. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PAIS` | Clave principal de la tabla. |
| Index | `A_PAIS_UNIQUE` | `CO_INEI_PAIS` | Indice de apoyo para consultas por codigo INEI del pais. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Es parte del catalogo geografico base consumido por Legasys. |

---

## Tabla: `A_PLAN`

### Descripcion funcional
Tabla usada en Legasys para registrar plantillas. Permite almacenar nombre, descripcion corta y ubicaciones asociadas tanto para uso interno como web.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PLAN` | `int unsigned` | Identificador interno del plan. |
| `DE_PLAN` | `varchar(100)` | Nombre o descripcion principal del plan. |
| `DC_PLAN` | `varchar(50)` | Descripcion corta o abreviada de la plantilla. |
| `DE_UBIC_PLAN` | `varchar(100)` | Ubicacion o ruta interna asociada a la plantilla. |
| `DE_UBIC_PLAN_WEB` | `varchar(100)` | Ubicacion o ruta web asociada a la plantilla. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `date` | Fecha de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PLAN` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla guarda el registro de nombre para generar plantilla por servicio |

| `IN_REIN_INST` | `char(1)` | Define si reinicia instrumento. Segun la captura: `1 = reinicia`, `2 = no reinicia`. |
| `IN_CALI_NOTA` | `char(1)` | Define si califica. Segun la captura: `1 = califica`, `2 = no califica`. |
| `IN_GENE_INST` | `char(1)` | Define si genera instrumento automaticamente. Segun la captura: `1 = genera automaticamente instrumento`, `2 = no genera automaticamente instrumento`. |
| `IN_GENE_OPEN` | `char(1)` | Define modo de generacion documental. Segun la captura: `1 = genera Open`, `2 = genera Office`. |
| `NU_CUEN_INGR` | `varchar(200)` | Cuenta o referencia de ingreso asociada al registro. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_REGI_NOTA` | Clave principal de la tabla. |
| Referenciada por | `P_SERV_ibfk_1` | `CO_REGI_NOTA` | La tabla `P_SERV` referencia esta tabla con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Es una tabla muy relevante para Legasys porque condiciona comportamiento notarial, documental y operativo de los servicios. |
| Funcional | Los indicadores `IN_REIN_INST`, `IN_CALI_NOTA`, `IN_GENE_INST` e `IN_GENE_OPEN` afectan reglas concretas del flujo del sistema. |

---

## Tabla: `A_REGI_ONP`

### Descripcion funcional
Tabla usada en Legasys para registrar configuraciones o codigos registrales relacionados con ONP. Sirve como catalogo de apoyo para clasificaciones previsionales o tributarias.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_REGI_ONP` | `int` | Identificador interno del registro ONP. |
| `DE_REGI_NOTA` | `varchar(20)` | Descripcion o codigo principal del registro ONP. |
| `NU_REGI_NOTA` | `varchar(10)` | Numero o codigo adicional del registro ONP. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_REGI_ONP` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Parece ser un catalogo especializado de apoyo para flujos ONP dentro de Legasys. |

---

## Tabla: `A_REGI_SID`

### Descripcion funcional
Tabla usada en Legasys para registrar tipos de registro SID vinculados a servicios SID. Permite identificar codigos y nombres consumidos por integraciones o flujos registrales SID.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `ID_REGI_SID` | `int` | Identificador interno del registro SID. |
| `CO_REGI_SID` | `varchar(5)` | Codigo del registro SID. |
| `CO_SERV_SID` | `int` | Codigo del servicio SID asociado. |
| `NO_REGI_SID` | `varchar(190)` | Nombre o descripcion principal del registro SID. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `ID_REGI_SID` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Forma parte de la estructura de catalogos consumidos por integraciones o flujos SID. |

---

## Tabla: `A_REGI_SUNA`

### Descripcion funcional
Tabla usada en Legasys para registrar tipos de registro SUNARP o registrales. Permite mantener un catalogo con nombre, area y trazabilidad basica para procesos registrales.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_REGI_SUNA` | `int unsigned` | Identificador interno del registro SUNARP. |
| `DE_REGI_SUNA` | `varchar(100)` | Nombre o descripcion principal del registro SUNARP. |
| `CO_AREA_REGI` | `varchar(5)` | Codigo de area registral asociada. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_REGI_SUNA` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Es parte del catalogo registral consumido por Legasys para procesos vinculados a SUNARP. |

---

## Tabla: `A_RELA_PRTC`

### Descripcion funcional
Tabla usada en Legasys para registrar relaciones de participacion entre personas o participantes. Permite estandarizar tipos de relacion reutilizados por flujos de firmas y participantes.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_RELA_PRTC` | `int unsigned` | Identificador interno de la relacion de participante. |
| `DE_RELA_PRTC` | `varchar(50)` | Descripcion unica de la relacion. |
| `RELA_PRTC_UIF` | `varchar(3)` | Codigo auxiliar asociado a flujos UIF. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_RELA_PRTC` | Clave principal de la tabla. |
| Unique | `A_RELA_PRTC_type_UNIQUE` | `DE_RELA_PRTC` | Evita relaciones duplicadas por descripcion. |
| Referenciada por | `H_TRAM_FIRM_ibfk_1` | `CO_RELA_PRTC` | La tabla `H_TRAM_FIRM` referencia esta tabla con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo impacta directamente en participantes y firmas dentro de Legasys. |

---

## Tabla: `A_REQU`

### Descripcion funcional
Tabla usada en Legasys como catalogo de requisitos. Permite definir requisitos reutilizables que luego pueden asociarse a servicios u otros flujos del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_REQU` | `int` | Identificador interno del requisito. |
| `DE_REQU` | `varchar(100)` | Descripcion principal del requisito. |
| `DC_REQU` | `varchar(50)` | Descripcion corta o abreviada del requisito. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_REQU` | Clave principal de la tabla. |
| Referenciada por | `H_REQU_SERV_ibfk_3` | `CO_REQU` | La tabla `H_REQU_SERV` referencia esta tabla con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Es un catalogo base para la gestion de requisitos asociados a servicios en Legasys. |

---

## Tabla: `A_SEMI_INST`

### Descripcion funcional
Tabla usada en Legasys para administrar secuenciales de instrumentos por notaria y anio. Permite controlar numeracion operativa en flujos notariales.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_SEMI_INST` | `int unsigned` | Identificador interno del secuencial de instrumento. |
| `CO_COMP` | `int` | Codigo de la notaria o compania a la que pertenece el secuencial. |
| `IN_KARD` | `char(1)` | Indicador asociado al flujo de kardex. |
| `NU_INST` | `int unsigned` | Numero secuencial actual del instrumento. |
| `NU_ANIO` | `year` | Anio al que corresponde el secuencial. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_SEMI_INST` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla participa en el control de numeracion de instrumentos notariales. |

---

## Tabla: `A_SEMI_KARD`

### Descripcion funcional
Tabla usada en Legasys para administrar secuenciales de kardex por notaria. Permite controlar el correlativo operativo del kardex dentro del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_SEMI_KARD` | `int unsigned` | Identificador interno del secuencial de kardex. |
| `CO_COMP` | `int unsigned` | Codigo de la notaria o compania a la que pertenece el secuencial. |
| `IN_KARD` | `char(20)` | Indicador o tipo de kardex asociado al secuencial. |
| `NU_KARD` | `int` | Numero secuencial actual del kardex. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `date` | Fecha de la ultima modificacion. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_SEMI_KARD` | Clave principal de la tabla. |
| Index | `A_SEMI_KARD_FKIndex1` | `CO_COMP` | Indice de apoyo para consultas por notaria. |
| Index | `H_A_SEMI_KARD_INDEX` | `CO_COMP, IN_KARD` | Indice de apoyo para busquedas por notaria y tipo de kardex. |
| Foreign Key | `A_SEMI_KARD_ibfk_1` | `CO_COMP` | Referencia a `A_COMP` con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | `CO_COMP` confirma que el secuencial de kardex se maneja por notaria. |
| Funcional | Es una tabla operativa clave para la numeracion del kardex en Legasys. |

---

## Tabla: `A_SEMI_MINU`

### Descripcion funcional
Tabla usada en Legasys para administrar secuenciales de minutas por notaria, registro notarial y anio. Permite controlar la numeracion operativa del minutario.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_SEMI_MINU` | `int unsigned` | Identificador interno del secuencial de minuta. |
| `CO_COMP` | `int` | Codigo de la notaria o compania a la que pertenece el secuencial. |
| `IN_KARD` | `char(1)` | Indicador asociado al flujo de kardex. |
| `CO_REGI_NOTA` | `int` | Registro notarial asociado al secuencial. |
| `NU_MINU` | `int unsigned` | Numero secuencial actual de la minuta. |
| `NU_ANIO` | `year` | Anio al que corresponde el secuencial. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_SEMI_MINU` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla interviene en la numeracion operativa del minutario en Legasys. |

---

## Tabla: `A_SEMI_MINU_INTE`

### Descripcion funcional
Tabla usada en Legasys para administrar secuenciales de minuta interna, vinculados a notaria y ticket de servicio. Permite manejar numeracion operativa interna con trazabilidad de modificacion y eliminacion.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_SEMI_MINU_INTE` | `int` | Identificador interno del secuencial de minuta interna. |
| `CO_COMP` | `int` | Codigo de la notaria o compania. |
| `CO_TICK_SERV` | `int` | Ticket o servicio asociado al secuencial. |
| `NU_MINU_INTE` | `int` | Numero secuencial de minuta interna. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_ELIM` | `datetime` | Fecha y hora de eliminacion logica o desactivacion. |
| `CO_USUA_ELIM` | `int` | Usuario que realizo la eliminacion logica o desactivacion. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_SEMI_MINU_INTE` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Parece usarse para numeracion interna de minutas con trazabilidad operativa mas detallada. |

---

## Tabla: `A_SEMI_TDOC`

### Descripcion funcional
Tabla usada en Legasys para administrar secuenciales de tipos de documento por notaria, caja y anio. Permite controlar serie, numero y datos asociados a la emision documental.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_SEMI_TDOC` | `int unsigned` | Identificador interno del secuencial de tipo documental. |
| `CO_COMP` | `int` | Codigo de la notaria o compania. |
| `CO_TDOC` | `int unsigned` | Tipo de documento asociado. |
| `CO_CAJA` | `int` | Caja asociada al secuencial. |
| `NU_ANIO` | `year` | Anio al que corresponde el secuencial. |
| `NU_SERI` | `varchar(4)` | Serie documental configurada. |
| `NU_DOCU` | `int` | Numero correlativo actual del documento. |
| `NU_ADIC_TDOC` | `varchar(5)` | Dato adicional del tipo de documento. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_SEMI_TDOC` | Clave principal de la tabla. |
| Index | `CO_TDOC` | `CO_TDOC` | Indice de apoyo para consultas por tipo de documento. |
| Foreign Key | `A_SEMI_TDOC_ibfk_1` | `CO_TDOC` | Referencia a `A_TDOC` con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es clave para el control de serie y numeracion documental en Legasys. |
| Funcional | Combina contexto de notaria, caja, tipo documental y anio para manejar correlativos operativos. |

---

## Tabla: `A_SERV_CALC`

### Descripcion funcional
Tabla usada en Legasys para configurar servicios con calculo por cantidad. Permite definir rangos, montos base y montos adicionales que el sistema puede usar en liquidaciones o calculos operativos.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_SERV_CALC` | `int` | Identificador interno de la configuracion del servicio. |
| `CO_COMP` | `int` | Codigo de la notaria o compania a la que pertenece la configuracion. |
| `DE_SERV` | `varchar(190)` | Nombre o descripcion del servicio. |
| `IN_CANT` | `int` | Cantidad o tramo principal asociado al calculo. |
| `NU_CANT_INIC` | `int` | Cantidad inicial usada como referencia del calculo. |
| `NU_MONT_CANT` | `decimal(11,2)` | Monto aplicado por cantidad agregada. |
| `NU_MONT` | `decimal(11,2)` | Monto base del servicio. |
| `NU_REGI` | `decimal(11,2)` | Valor adicional relacionado al registro o calculo complementario. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `FE_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_SERV_CALC` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Segun la captura, `NU_MONT_CANT` representa el monto por cantidad agregada. |
| Funcional | La presencia de `CO_COMP` indica que esta configuracion se maneja por notaria. |

---

## Tabla: `A_SERV_SID`

### Descripcion funcional
Tabla usada en Legasys para registrar servicios SID. Permite mantener un catalogo de servicios consumidos por integraciones o flujos registrales SID.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `ID` | `int` | Identificador interno del registro. |
| `CO_SERV_SID` | `int` | Codigo del servicio SID. |
| `CO_REGI_SUNA` | `int` | Codigo registral SUNARP asociado al servicio SID. |
| `NO_SERV_SID` | `varchar(190)` | Nombre o descripcion principal del servicio SID. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `ID` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Forma parte del conjunto de catalogos usados por integraciones o flujos SID en Legasys. |

---

## Tabla: `A_SITU_TRAM_type`

### Descripcion funcional
Tabla usada en Legasys para registrar situaciones del tramite. Permite definir estados o situaciones operativas con informacion de texto, envio y plazos que impactan flujos de seguimiento y registros publicos.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_SITU_TRAM` | `int unsigned` | Identificador interno de la situacion del tramite. |
| `DE_SITU_TRAM` | `varchar(50)` | Descripcion unica de la situacion. |
| `DE_TEXT_MAIL` | `text` | Texto de correo asociado a la situacion. |
| `IN_ENVI` | `char(1)` | Indicador de envio asociado a la situacion. |
| `NU_DIAS` | `int` | Numero de dias asociado a la situacion. |
| `DIAS_HABI` | `varchar(10)` | Indicador o valor relacionado a dias habiles. |
| `DIAS_ACCI` | `varchar(10)` | Indicador o valor relacionado a dias de accion. |
| `DIAS_VENC` | `varchar(10)` | Indicador o valor relacionado a dias de vencimiento. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_SITU_TRAM` | Clave principal de la tabla. |
| Unique | `DE_SITU_TRAM` | `DE_SITU_TRAM` | Evita situaciones duplicadas por descripcion. |
| Referenciada por | `H_SGMT_CALI_ibfk_1` | `CO_SITU_TRAM` | La tabla `H_SGMT_CALI` referencia esta tabla con restriccion `RESTRICT`. |
| Referenciada por | `H_SGMT_ORLC_ibfk_2` | `CO_SITU_TRAM` | La tabla `H_SGMT_ORLC` referencia esta tabla con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es importante para seguimiento de tramites y especialmente para flujos de Registros Publicos. |
| Tecnica relevante | El nombre de la tabla termina en `_type`, por lo que debe respetarse exactamente en minuscula al referenciarla. |

---

## Tabla: `A_TABS`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tabs o pestanas del sistema. Permite definir elementos de navegacion o agrupacion visual reutilizables.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TABS` | `int` | Identificador interno del tab o pestana. |
| `DE_TABS` | `varchar(50)` | Nombre o descripcion principal del tab. |
| `DC_TABS` | `varchar(20)` | Descripcion corta o abreviada. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TABS` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Parece funcionar como catalogo de apoyo para agrupaciones o navegacion en la interfaz. |

---

## Tabla: `A_TDOC`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de documento. Permite definir tipos documentales, sus codigos y referencias para procesos de emision, Caja y numeracion documental.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TDOC` | `int unsigned` | Identificador interno del tipo documental. |
| `DE_TDOC` | `varchar(60)` | Nombre o descripcion principal del tipo de documento. |
| `DC_TDOC` | `varchar(10)` | Codigo corto o abreviatura del tipo documental. |
| `NU_ORDE` | `int unsigned` | Orden de visualizacion o prioridad del tipo documental. |
| `CO_SUNA` | `varchar(5)` | Codigo auxiliar asociado a SUNARP o integraciones. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TDOC` | Clave principal de la tabla. |
| Referenciada por | `A_SEMI_TDOC_ibfk_1` | `CO_TDOC` | La tabla `A_SEMI_TDOC` referencia esta tabla con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo es base para numeracion y manejo de tipos documentales en Legasys. |

---

## Tabla: `A_TDOC_IDEN`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de documento de identidad. Permite clasificar documentos usados por participantes y relacionarlos con codigos auxiliares para UIF, SID, ONP o facturacion electronica.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TDOC_IDEN` | `int unsigned` | Identificador interno del tipo de documento de identidad. |
| `DE_TDOC_IDEN` | `varchar(60)` | Nombre o descripcion principal del documento de identidad. |
| `DC_TDOC_IDEN` | `varchar(5)` | Codigo corto del documento de identidad. |
| `CO_DOCU_SUNAT` | `char(2)` | Codigo del documento usado en SUNAT. |
| `CO_DOCU_SID` | `varchar(2)` | Codigo del documento usado en flujos SID. |
| `ID_ONP` | `varchar(2)` | Codigo del documento usado en ONP. |
| `CO_UIF` | `varchar(3)` | Codigo del documento usado en UIF. |
| `CO_FACT_ELEC` | `int` | Codigo asociado a facturacion electronica. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TDOC_IDEN` | Clave principal de la tabla. |
| Referenciada por | `H_PRTC_NATU_ibfk_1` | `CO_TDOC_IDEN` | La tabla `H_PRTC_NATU` referencia esta tabla con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla impacta directamente en participantes y validaciones documentarias del sistema. |
| Funcional | Reune codigos auxiliares usados por varias integraciones o dominios regulatorios. |

---

## Tabla: `A_TIEM_PAGO`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tiempos o plazos de pago. Permite definir periodos y dias asociados para clasificar condiciones de pago.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIEM_PAGO` | `int` | Identificador interno del tiempo de pago. |
| `DE_TIEM_PAGO` | `varchar(50)` | Descripcion principal del tiempo o plazo de pago. |
| `NU_DIAS` | `int` | Numero de dias asociados al plazo. |
| `NU_DIAS_ALER` | `int` | Numero de dias de alerta asociados al plazo. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIEM_PAGO` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo puede influir en creditos, vencimientos o alertas de pago en Legasys. |

---

## Tabla: `A_TIPO_ACTO_JURI`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de acto juridico. Permite clasificar actos juridicos mediante nombre, descripcion corta y estado.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_ACTO_JURI` | `int` | Identificador interno del tipo de acto juridico. |
| `DE_TIPO_ACTO_JURI` | `varchar(100)` | Descripcion principal del tipo de acto juridico. |
| `IPO_ACTO_JURI` | `varchar(50)` | Descripcion corta, abreviatura o codigo complementario del acto juridico. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_ACTO_JURI` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Es un catalogo juridico de apoyo para clasificaciones dentro de Legasys. |

---

## Tabla: `A_TIPO_ADVE`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de advertencia. Permite clasificar advertencias o mensajes operativos que el sistema puede mostrar o asociar a distintos flujos.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_ADVE` | `int` | Identificador interno del tipo de advertencia. |
| `DE_TIPO_ADVE` | `varchar(100)` | Descripcion principal del tipo de advertencia. |
| `DC_TIPO_ADVE` | `varchar(50)` | Descripcion corta o abreviada. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_ADVE` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Puede servir como catalogo base para reglas o mensajes de advertencia dentro de Legasys. |

---

## Tabla: `A_TIPO_APOD`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de apoderado o apoderamiento. Permite clasificar esta condicion dentro de procesos notariales o de participantes.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_APOD` | `int unsigned` | Identificador interno del tipo de apoderado. |
| `DE_TIPO_APOD` | `varchar(20)` | Descripcion principal del tipo de apoderado. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `date` | Fecha de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_APOD` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo puede impactar directamente en participantes o representaciones dentro de Legasys. |

---

## Tabla: `A_TIPO_APOR_type`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de aporte. Permite clasificar aportes con una descripcion unica para procesos donde el sistema requiera esta distincion.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_APOR` | `int unsigned` | Identificador interno del tipo de aporte. |
| `DE_TIPO_APOR` | `varchar(100)` | Descripcion unica del tipo de aporte. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_APOR` | Clave principal de la tabla. |
| Unique | `DE_TIPO_APOR` | `DE_TIPO_APOR` | Evita tipos de aporte duplicados por descripcion. |
| Referenciada por | `H_TRAM_CAPI_ibfk_1` | `CO_TIPO_APOR` | La tabla `H_TRAM_CAPI` referencia esta tabla con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo es relevante para flujos donde se registren aportes o capitales. |
| Tecnica relevante | El nombre de la tabla termina en `_type`, por lo que debe respetarse exactamente en minuscula al referenciarla. |

---

## Tabla: `A_TIPO_AREA`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de area. Permite clasificar areas o ambitos asociados a un registro notarial o configuracion del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_AREA` | `int` | Identificador interno del tipo de area. |
| `DE_TIPO_AREA` | `varchar(100)` | Descripcion principal del tipo de area. |
| `DC_TIPO_AREA` | `varchar(50)` | Descripcion corta o abreviada. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |
| `CO_REGI_NOTA` | `int` | Registro notarial asociado al tipo de area. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_AREA` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | La presencia de `CO_REGI_NOTA` sugiere que este catalogo puede depender del contexto registral notarial. |

---

## Tabla: `A_TIPO_ASEV`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de acto o servicio especial identificado por codigos auxiliares. Permite clasificar registros usando codigos SUNA, UIF y trazabilidad basica.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ASEV` | `varchar(1)` | Identificador o codigo principal del tipo. |
| `DE_ASEV` | `varchar(20)` | Descripcion principal del tipo. |
| `CO_SUNA` | `varchar(2)` | Codigo auxiliar asociado a SUNARP u otra integracion. |
| `CO_UIF` | `varchar(2)` | Codigo auxiliar asociado a UIF. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `date` | Fecha de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ASEV` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo parece servir como clasificacion auxiliar para integraciones o reglas regulatorias. |

---

## Tabla: `A_TIPO_BENE_JURI`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de beneficiario juridico. Permite clasificar beneficiarios dentro de procesos de personas juridicas o cumplimiento.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_BENE_JURI` | `int` | Identificador interno del tipo de beneficiario juridico. |
| `DE_TIPO_BENE_JURI` | `varchar(100)` | Descripcion principal del tipo de beneficiario juridico. |
| `IN_ESTA` | `smallint` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_BENE_JURI` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo puede ser relevante para beneficiarios finales, personas juridicas o cumplimiento. |

---

## Tabla: `A_TIPO_BIEN`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de bien. Permite clasificar bienes mediante una descripcion y un codigo auxiliar.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_BIEN` | `int unsigned` | Identificador interno del tipo de bien. |
| `DE_TIPO_BIEN` | `varchar(50)` | Descripcion principal del tipo de bien. |
| `CO_PDT` | `varchar(2)` | Codigo auxiliar asociado al tipo de bien. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_BIEN` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Sirve como catalogo base para clasificaciones de bienes dentro de Legasys. |

---

## Tabla: `A_TIPO_CAMB`

### Descripcion funcional
Tabla usada en Legasys para registrar tipos de cambio por moneda y fecha. Permite almacenar valores de compra y venta que pueden influir en calculos economicos o procesos financieros del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_CAMB` | `int` | Identificador interno del tipo de cambio. |
| `CO_TIPO_MONE` | `int` | Tipo de moneda asociado al registro. |
| `FE_TIPO_CAMB` | `date` | Fecha de vigencia del tipo de cambio. |
| `NU_CAMB_VENT` | `decimal(11,3)` | Valor de cambio para venta. |
| `NU_CAMB_COMP` | `decimal(11,3)` | Valor de cambio para compra. |
| `NU_CAMB_VENT_LIBR` | `decimal(11,2)` | Valor de venta usado para libros o registros auxiliares. |
| `NU_CAMB_COMP_LIBR` | `decimal(11,2)` | Valor de compra usado para libros o registros auxiliares. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_CAMB` | Clave principal de la tabla. |
| Unique | `UNIQUE_TIPO_CAMB` | `CO_TIPO_MONE, FE_TIPO_CAMB` | Evita duplicar un tipo de cambio para la misma moneda y fecha. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla puede impactar calculos economicos, conversiones monetarias y reportes financieros de Legasys. |

---

## Tabla: `A_TIPO_CAMP_type`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de campo. Permite clasificar campos dinamicos o configurables usados por el sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_CAMP` | `int unsigned` | Identificador interno del tipo de campo. |
| `DE_TIPO_CAMP` | `varchar(50)` | Descripcion unica del tipo de campo. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_CAMP` | Clave principal de la tabla. |
| Unique | `DE_TIPO_CAMP` | `DE_TIPO_CAMP` | Evita tipos de campo duplicados por descripcion. |
| Referenciada por | `H_CODO_ibfk_2` | `CO_TIPO_CAMP` | La tabla `H_CODO` referencia esta tabla con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo es relevante para la estructura de campos dinamicos de Legasys. |
| Tecnica relevante | El nombre de la tabla termina en `_type`, por lo que debe respetarse exactamente en minuscula al referenciarla. |

---

## Tabla: `A_TIPO_CARG`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de cargo. Permite clasificar cargos o funciones asociadas a personas, usuarios o flujos regulatorios.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_CARG` | `int unsigned` | Identificador interno del tipo de cargo. |
| `DE_TIPO_CARG` | `varchar(200)` | Descripcion principal del tipo de cargo. |
| `CO_CARG_UIF` | `varchar(3)` | Codigo auxiliar asociado a UIF. |
| `CO_USUA_MODI` | `varchar(5)` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `date` | Fecha de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_CARG` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Puede influir en clasificaciones de personas, representantes o flujos UIF dentro de Legasys. |

---

## Tabla: `A_TIPO_CIIU`

### Descripcion funcional
Tabla usada en Legasys como catalogo de codigos CIIU. Permite clasificar actividades economicas mediante un codigo y su descripcion.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_CIIU` | `int` | Identificador interno del registro CIIU. |
| `CO_CIIU` | `varchar(11)` | Codigo CIIU asociado a la actividad economica. |
| `DE_TIPO_CIIU` | `varchar(120)` | Descripcion principal de la actividad economica. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_CIIU` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo es util para clasificaciones economicas y puede impactar datos de clientes o personas juridicas. |

---

## Tabla: `A_TIPO_CLIE`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de cliente. Permite clasificar clientes mediante una descripcion principal y una abreviatura.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_CLIE` | `int` | Identificador interno del tipo de cliente. |
| `DE_TIPO_CLIE` | `varchar(100)` | Descripcion principal del tipo de cliente. |
| `DC_TIPO_CLIE` | `varchar(50)` | Descripcion corta o abreviada. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_CLIE` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo puede usarse para segmentar clientes dentro de Legasys. |

---

## Tabla: `A_TIPO_CONS_NOTA`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de constancia notarial. Permite clasificar constancias mediante descripcion y estado.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_CONS_NOTA` | `int` | Identificador interno del tipo de constancia notarial. |
| `DE_TIPO_CONS_NOTA` | `varchar(200)` | Descripcion principal del tipo de constancia. |
| `DC_TIPO_CONS_NOTA` | `varchar(150)` | Descripcion corta o abreviada. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_CONS_NOTA` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo es de apoyo para documentos o constancias dentro del dominio notarial de Legasys. |

---

## Tabla: `A_TIPO_CPTO`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de concepto. Permite clasificar conceptos economicos u operativos con orden de visualizacion y trazabilidad basica.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_CPTO` | `int unsigned` | Identificador interno del tipo de concepto. |
| `DE_TIPO_CPTO` | `varchar(100)` | Descripcion principal del tipo de concepto. |
| `DC_TIPO_CPTO` | `varchar(50)` | Descripcion corta o abreviada. |
| `NU_ORDE` | `int` | Orden de visualizacion o prioridad. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `int unsigned` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_CPTO` | Clave principal de la tabla. |
| Referenciada por | `P_CPTO_ibfk_1` | `CO_TIPO_CPTO` | La tabla `P_CPTO` referencia esta tabla con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo es relevante para conceptos economicos y puede impactar Caja, liquidaciones o configuraciones operativas. |

---

## Tabla: `A_TIPO_CUEN_BANC`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de cuenta bancaria. Permite clasificar cuentas mediante una descripcion principal y una abreviatura.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_CUEN_BANC` | `int` | Identificador interno del tipo de cuenta bancaria. |
| `DE_TIPO_CUEN_BANC` | `varchar(100)` | Descripcion principal del tipo de cuenta bancaria. |
| `DC_TIPO_CUEN_BANC` | `varchar(50)` | Descripcion corta o abreviada. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_CUEN_BANC` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo sirve como apoyo para mantenimientos y operaciones vinculadas a cuentas bancarias. |

---

## Tabla: `A_TIPO_DIGI`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos digitales o documentales digitales. Permite clasificar tipos usados en flujos web, firma, documentos digitales o integraciones.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_DIGI` | `int` | Identificador interno del tipo digital. |
| `DE_TIPO_DIGI` | `varchar(100)` | Descripcion principal del tipo digital. |
| `DE_URL_API` | `varchar(200)` | URL o endpoint API asociado al tipo digital. |
| `TI_TIPO_DIGI` | `varchar(50)` | Tipo o clasificacion adicional del registro digital. |
| `IN_WEB` | `int` | Indicador de uso o publicacion web. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |
| `IN_SID_SUNA` | `int` | Indicador relacionado con SID o SUNARP. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_DIGI` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es relevante para flujos documentales digitales e integraciones. |
| Funcional | `DE_URL_API` puede condicionar integraciones externas asociadas al tipo digital. |

---

## Tabla: `A_TIPO_DIRE_type`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de direccion. Permite clasificar direcciones usando una descripcion estandarizada.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_DIRE` | `int unsigned` | Identificador interno del tipo de direccion. |
| `DE_TIPO_DIRE` | `varchar(50)` | Descripcion unica del tipo de direccion. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_DIRE` | Clave principal de la tabla. |
| Unique | `DE_TIPO_DIRE` | `DE_TIPO_DIRE` | Evita tipos de direccion duplicados por descripcion. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo puede impactar direcciones de participantes, clientes o registros operativos. |
| Tecnica relevante | El nombre de la tabla termina en `_type`, por lo que debe respetarse exactamente en minuscula al referenciarla. |

---

## Tabla: `A_TIPO_DOCU_REMI`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de documento de remision. Permite clasificar documentos externos o remitidos dentro de flujos documentales.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_DOCU_REMI` | `int unsigned` | Identificador interno del tipo de documento de remision. |
| `DE_TIPO_DOCU_REMI` | `varchar(60)` | Descripcion unica del tipo de documento remitido. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_DOCU_REMI` | Clave principal de la tabla. |
| Unique | `DE_TIPO_DOCU_REMI` | `DE_TIPO_DOCU_REMI` | Evita tipos duplicados por descripcion. |
| Referenciada por | `H_DOCU_EXTE_ibfk_2` | `CO_TIPO_DOCU_REMI` | La tabla `H_DOCU_EXTE` referencia esta tabla con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo es relevante para documentos externos o remitidos dentro de Legasys. |

---

## Tabla: `A_TIPO_EMPR_type`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de empresa. Permite clasificar personas juridicas mediante una descripcion estandarizada.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_EMPR` | `int unsigned` | Identificador interno del tipo de empresa. |
| `DE_TIPO_EMPR` | `varchar(10)` | Descripcion unica o abreviada del tipo de empresa. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_EMPR` | Clave principal de la tabla. |
| Unique | `DE_TIPO_EMPR` | `DE_TIPO_EMPR` | Evita tipos de empresa duplicados por descripcion. |
| Referenciada por | `H_PRTC_JURI_ibfk_3` | `CO_TIPO_EMPR` | La tabla `H_PRTC_JURI` referencia esta tabla con restriccion `RESTRICT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo impacta directamente en participantes juridicos dentro de Legasys. |
| Tecnica relevante | El nombre de la tabla termina en `_type`, por lo que debe respetarse exactamente en minuscula al referenciarla. |

---

## Tabla: `A_TIPO_FOLI_type`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de folio. Permite clasificar folios mediante una descripcion estandarizada.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_FOLI` | `int unsigned` | Identificador interno del tipo de folio. |
| `DE_TIPO_FOLI` | `varchar(50)` | Descripcion unica del tipo de folio. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_FOLI` | Clave principal de la tabla. |
| Unique | `DE_TIPO_FOLI` | `DE_TIPO_FOLI` | Evita tipos de folio duplicados por descripcion. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo puede ser relevante para flujos documentales o registrales que distingan tipos de folio. |
| Tecnica relevante | El nombre de la tabla termina en `_type`, por lo que debe respetarse exactamente en minuscula al referenciarla. |

---

## Tabla: `A_TIPO_FORM`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de formulario. Permite clasificar formularios mediante una descripcion principal y su estado.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_FORM` | `int` | Identificador interno del tipo de formulario. |
| `DE_TIPO_FORM` | `varchar(500)` | Descripcion principal del tipo de formulario. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_FORM` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo puede servir de apoyo para formularios o configuraciones documentales dentro de Legasys. |

---

## Tabla: `A_TIPO_INIC`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de inicio o inicializacion. Permite clasificar este concepto con trazabilidad basica de modificacion.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_INIC` | `int unsigned` | Identificador interno del tipo de inicio. |
| `DE_TIPO_INIC` | `varchar(100)` | Descripcion principal del tipo de inicio. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `date` | Fecha de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_INIC` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Puede utilizarse como catalogo de apoyo para distintos flujos de configuracion o inicio dentro de Legasys. |

---

## Tabla: `A_TIPO_INSC`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de inscripcion. Permite clasificar inscripciones mediante descripcion y codigo auxiliar UIF.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_INSC` | `int` | Identificador interno del tipo de inscripcion. |
| `CO_UIF` | `varchar(3)` | Codigo auxiliar asociado a UIF. |
| `DE_TIPO_INS` | `varchar(100)` | Descripcion principal del tipo de inscripcion. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_INSC` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo puede influir en clasificaciones notariales o regulatorias dentro de Legasys. |

---

## Tabla: `A_TIPO_LIBR`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de libro. Permite clasificar libros y relacionarlos con un codigo registral SUNARP.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_LIBR` | `int unsigned` | Identificador interno del tipo de libro. |
| `DE_TIPO_LIBR` | `varchar(100)` | Descripcion principal del tipo de libro. |
| `CO_LIBR_SUNA` | `int unsigned` | Codigo de libro SUNARP asociado. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_LIBR` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo puede ser relevante para libros notariales o registrales dentro de Legasys. |

---

## Tabla: `A_TIPO_MONE`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de moneda. Permite clasificar monedas con codigos auxiliares para SUNA, UIF, CNL y SID, ademas de trazabilidad basica.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_MONE` | `int unsigned` | Identificador interno del tipo de moneda. |
| `CO_SUNA` | `varchar(1)` | Codigo auxiliar asociado a SUNARP u otra integracion. |
| `CO_UIF` | `varchar(3)` | Codigo auxiliar asociado a UIF. |
| `CO_CNL` | `varchar(2)` | Codigo auxiliar asociado a CNL u otro dominio. |
| `CO_SID_SUNA` | `varchar(10)` | Codigo auxiliar asociado a SID o SUNARP. |
| `DE_TIPO_MONE` | `varchar(20)` | Descripcion principal del tipo de moneda. |
| `SI_MONE` | `varchar(4)` | Simbolo o abreviatura de la moneda. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `date` | Fecha de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_MONE` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo es relevante para Caja, tipos de cambio, pagos e integraciones regulatorias. |

---

## Tabla: `A_TIPO_MOVI_NOTA`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de movimiento de nota. Permite clasificar movimientos vinculados a notas con orden de visualizacion y estado.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_MOVI_NOTA` | `int` | Identificador interno del tipo de movimiento de nota. |
| `NO_TIPO_MOVI_NOTA` | `varchar(50)` | Nombre o descripcion principal del tipo de movimiento. |
| `IN_TIPO_MOVI_NOTA` | `int` | Indicador o clasificacion interna del movimiento. |
| `NU_ORDE` | `int` | Orden de visualizacion o prioridad. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_MOVI_NOTA` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo puede apoyar la logica de notas de credito o debito dentro de Legasys. |

---

## Tabla: `A_TIPO_MUEB`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de bien mueble. Permite clasificar bienes muebles con trazabilidad basica de modificacion.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_MUEB` | `int unsigned` | Identificador interno del tipo de bien mueble. |
| `DE_TIPO_MUEB` | `varchar(250)` | Descripcion principal del tipo de bien mueble. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `date` | Fecha de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_MUEB` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo complementa la clasificacion de bienes dentro de Legasys. |

---

## Tabla: `A_TIPO_OCUP`

### Descripcion funcional
Tabla usada en Legasys como catalogo de ocupaciones. Permite clasificar ocupaciones usando un indicador ocupacional, descripcion y codigos auxiliares.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_OCUP` | `int` | Identificador interno de la ocupacion. |
| `CO_INDI_OCUP` | `int` | Indicador ocupacional asociado. |
| `DE_OCUP` | `varchar(180)` | Descripcion principal de la ocupacion. |
| `CO_UIF` | `varchar(3)` | Codigo auxiliar asociado a UIF. |
| `CO_USUA_MODI` | `varchar(5)` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `date` | Fecha de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_OCUP` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo es relevante para participantes, personas naturales y flujos UIF dentro de Legasys. |

---

## Tabla: `A_TIPO_OCUR`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de ocurrencia. Permite clasificar ocurrencias asociadas a servicios y almacenar textos operativos usados en certificados, notas o pies de documento.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_OCUR` | `int unsigned` | Identificador interno del tipo de ocurrencia. |
| `NO_INDI_OCUR` | `varchar(5)` | Indicador corto o abreviatura de la ocurrencia. |
| `CO_SERV` | `int unsigned` | Servicio asociado a la ocurrencia. |
| `DE_TIPO_OCUR` | `varchar(60)` | Descripcion principal de la ocurrencia. |
| `DE_CERT` | `varchar(4000)` | Texto asociado a certificado. |
| `DE_PIE` | `varchar(600)` | Texto asociado al pie de documento. |
| `DE_NOTA` | `varchar(400)` | Texto asociado a nota. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `date` | Fecha de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_OCUR` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla parece relevante para textos operativos o plantillas asociadas a servicios dentro de Legasys. |

---

## Tabla: `A_TIPO_PERS_UIF`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de persona para flujos UIF. Permite clasificar personas con una descripcion principal y codigo auxiliar UIF.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_PERS_UIF` | `int` | Identificador interno del tipo de persona UIF. |
| `CO_UIF` | `varchar(3)` | Codigo auxiliar asociado a UIF. |
| `DE_TIPO_PERS` | `varchar(100)` | Descripcion principal del tipo de persona. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_PERS_UIF` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo es relevante para clasificaciones regulatorias o de cumplimiento dentro de Legasys. |

---

## Tabla: `A_TIPO_PERS_type`

### Descripcion funcional
Tabla usada en Legasys como catalogo general de tipos de persona. Permite clasificar personas mediante una descripcion unica.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_PERS` | `int unsigned` | Identificador interno del tipo de persona. |
| `DE_TIPO_PERS` | `varchar(100)` | Descripcion unica del tipo de persona. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_PERS` | Clave principal de la tabla. |
| Unique | `DE_TIPO_PERS` | `DE_TIPO_PERS` | Evita tipos de persona duplicados por descripcion. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo puede impactar multiples flujos donde Legasys diferencie tipos de persona. |
| Tecnica relevante | El nombre de la tabla termina en `_type`, por lo que debe respetarse exactamente en minuscula al referenciarla. |

---

## Tabla: `A_TIPO_PRED`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de predio. Permite clasificar predios con descripcion principal, codigo auxiliar UIF y trazabilidad basica.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_PRED` | `int` | Identificador interno del tipo de predio. |
| `CO_UIF` | `varchar(10)` | Codigo auxiliar asociado a UIF. |
| `DE_TIPO_PRED` | `varchar(200)` | Descripcion principal del tipo de predio. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_PRED` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo es util para clasificaciones de predios o bienes inmuebles dentro de Legasys. |

---

## Tabla: `A_TIPO_PROT_DIGI`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de protocolo digital. Permite clasificar protocolos digitales mediante una descripcion principal y una abreviatura.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_PROT_DIGI` | `int` | Identificador interno del tipo de protocolo digital. |
| `DE_TIPO_PROT_DIGI` | `varchar(100)` | Descripcion principal del tipo de protocolo digital. |
| `DC_TIPO_PROT_DIGI` | `varchar(100)` | Descripcion corta o abreviada. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_PROT_DIGI` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo puede ser relevante para documentos o protocolos digitales dentro de Legasys. |

---

## Tabla: `A_TIPO_RETE`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de retencion. Permite definir porcentajes o valores de retencion usados por procesos economicos del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_RETE` | `int` | Identificador interno del tipo de retencion. |
| `NO_TIPO_RETE` | `varchar(100)` | Nombre o descripcion principal del tipo de retencion. |
| `NU_RETE` | `decimal(11,2)` | Valor principal de retencion. |
| `NU_RETE_2` | `decimal(11,2)` | Valor complementario de retencion. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_RETE` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo puede impactar calculos tributarios o financieros dentro de Legasys. |

---

## Tabla: `A_TIPO_SOSP`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de sospecha o clasificaciones de operacion sospechosa. Permite categorizar registros vinculados a cumplimiento o UIF.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_SOSP` | `int` | Identificador interno del tipo de sospecha. |
| `DE_TIPO_SOSP` | `varchar(100)` | Descripcion principal del tipo de sospecha. |
| `DC_TIPO_SOSP` | `varchar(50)` | Descripcion corta o abreviada. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_SOSP` | Clave principal de la tabla. |
| Referenciada por | `T_PERS_SOSP_UIF` | `CO_TIPO_SOSP` | La tabla `T_PERS_SOSP_UIF` referencia esta tabla mediante la columna `CO_TIPO_SOSP`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo es relevante para flujos de cumplimiento, UIF u operaciones sospechosas dentro de Legasys. |

---

## Tabla: `A_TIPO_SUCU_type`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de sucursal. Permite clasificar sucursales mediante una descripcion unica.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_SUCU` | `int unsigned` | Identificador interno del tipo de sucursal. |
| `NO_TIPO_SUCU` | `varchar(100)` | Descripcion unica del tipo de sucursal. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_SUCU` | Clave principal de la tabla. |
| Unique | `NO_TIPO_SUCU` | `NO_TIPO_SUCU` | Evita tipos de sucursal duplicados por descripcion. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Puede servir como catalogo base para clasificaciones de estructura organizacional dentro de Legasys. |
| Tecnica relevante | El nombre de la tabla termina en `_type`, por lo que debe respetarse exactamente en minuscula al referenciarla. |

---

## Tabla: `A_TIPO_TARI`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de tarifa. Permite clasificar tarifas mediante una descripcion principal y estado.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_TARI` | `int unsigned` | Identificador interno del tipo de tarifa. |
| `DE_TIPO_TARI` | `varchar(100)` | Descripcion principal del tipo de tarifa. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_TARI` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo puede usarse en parametrizaciones economicas de Legasys. |

---

## Tabla: `A_TIPO_TARJ`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de tarjeta. Permite clasificar tarjetas y asociarles una cuenta bancaria vinculada.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_TARJ` | `int` | Identificador interno del tipo de tarjeta. |
| `DE_TIPO_TARJ` | `varchar(100)` | Descripcion principal del tipo de tarjeta. |
| `DC_TIPO_TARJ` | `varchar(50)` | Descripcion corta o abreviada. |
| `NU_CUEN_BANC_TARJ` | `varchar(100)` | Cuenta bancaria asociada al tipo de tarjeta. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_TARJ` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo puede impactar pagos, cobros o configuraciones bancarias dentro de Legasys. |

---

## Tabla: `A_TIPO_TERC`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de tercero. Permite clasificar terceros mediante descripcion y un monto asociado.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_TERC` | `int` | Identificador interno del tipo de tercero. |
| `DE_TIPO_TERC` | `varchar(200)` | Descripcion principal del tipo de tercero. |
| `DC_TIPO_TERC` | `varchar(200)` | Descripcion corta o complementaria. |
| `NU_MONT` | `decimal(11,2)` | Monto asociado al tipo de tercero. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_TERC` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo puede servir para clasificaciones de terceros o terceros vinculados a montos en Legasys. |

---

## Tabla: `A_TIPO_USUA_type`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de usuario. Permite clasificar usuarios mediante una descripcion unica y soporta la asignacion de perfiles funcionales dentro del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_USUA` | `int unsigned` | Identificador interno del tipo de usuario. |
| `DE_TIPO_USUA` | `varchar(50)` | Descripcion unica del tipo de usuario. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_USUA` | Clave principal de la tabla. |
| Unique | `DE_TIPO_USUA` | `DE_TIPO_USUA` | Evita tipos de usuario duplicados por descripcion. |
| Referenciada por | `P_USUA` | `CO_TIPO_USUA` | La tabla `P_USUA` referencia esta tabla mediante la columna `CO_TIPO_USUA`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es clave para la segmentacion funcional de usuarios dentro de Legasys. |
| Tecnica relevante | El nombre de la tabla termina en `_type`, por lo que debe respetarse exactamente en minuscula al referenciarla. |

---

## Tabla: `A_TIPO_VALO`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de valor. Permite clasificar valores mediante descripcion principal y abreviatura.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_VALO` | `int` | Identificador interno del tipo de valor. |
| `DE_TIPO_VALO` | `varchar(100)` | Descripcion principal del tipo de valor. |
| `DC_TIPO_VALO` | `varchar(50)` | Descripcion corta o abreviada. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_VALO` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo puede servir de apoyo a configuraciones o clasificaciones economicas dentro de Legasys. |

---

## Tabla: `A_TIPO_VIAJ_PODE`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de viaje o poder relacionados con autorizaciones de viaje. Permite clasificar estos casos con trazabilidad basica.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_VIAJ_PODE` | `int unsigned` | Identificador interno del tipo de viaje o poder. |
| `DE_TIPO_VIAJ_PODE` | `varchar(100)` | Descripcion principal del tipo. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_VIAJ_PODE` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo puede influir en flujos de autorizacion de viaje o poderes dentro de Legasys. |

---

## Tabla: `A_UIT`

### Descripcion funcional
Tabla usada en Legasys para registrar el valor de la UIT por anio. Permite almacenar este parametro economico para calculos y validaciones financieras o notariales.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_UIT` | `int` | Identificador interno del registro UIT. |
| `NU_UIT` | `decimal(11,2)` | Valor monetario de la UIT. |
| `NU_ANIO` | `varchar(6)` | Anio al que corresponde el valor UIT. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_UIT` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es importante para calculos economicos, tarifas y validaciones dentro de Legasys. |

---

## Tabla: `A_VENT_RRPP`

### Descripcion funcional
Tabla usada en Legasys como catalogo de ventanillas o ventanas de Registros Publicos. Permite clasificar puntos de atencion o instancias relacionadas con RR.PP.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_VENT_RRPP` | `int unsigned` | Identificador interno de la ventanilla RR.PP. |
| `DE_VENT_RRPP` | `varchar(150)` | Descripcion principal de la ventanilla. |
| `DC_VENT_RRPP` | `varchar(50)` | Descripcion corta o abreviada. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_VENT_RRPP` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo puede ser relevante para procesos de Registros Publicos dentro de Legasys. |

---

## Tabla: `A_ZONA_REGI`

### Descripcion funcional
Tabla usada en Legasys como catalogo de zonas registrales. Permite clasificar zonas consumidas por oficinas registrales y otros procesos vinculados a SUNARP o RR.PP.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ZONA_REGI` | `int unsigned` | Identificador interno de la zona registral. |
| `CO_UIF` | `varchar(2)` | Codigo auxiliar asociado a UIF. |
| `DE_ZONA_REGI` | `varchar(50)` | Descripcion principal de la zona registral. |
| `DC_ZONA_REGI` | `varchar(40)` | Descripcion corta o abreviada. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ZONA_REGI` | Clave principal de la tabla. |
| Referenciada por | `A_OFIC_REGI` | `CO_ZONA_REGI` | La tabla `A_OFIC_REGI` referencia esta tabla mediante la columna `CO_ZONA_REGI`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo es parte del dominio registral usado por Legasys. |

---

## Tabla: `A_TIPO_PROY`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de proyecto. Permite clasificar proyectos mediante una descripcion principal y trazabilidad basica de modificacion.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_PROY` | `int` | Identificador interno del tipo de proyecto. |
| `DE_TIPO_PROY` | `varchar(200)` | Descripcion principal del tipo de proyecto. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_PROY` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este catalogo puede servir como apoyo para clasificaciones internas o configuraciones relacionadas con proyectos en Legasys. |

---

## Tabla: `A_TIPO_PRTC`

### Descripcion funcional
Tabla usada en Legasys como catalogo de tipos de participante. Permite clasificar participantes con codigos auxiliares para distintos dominios regulatorios o integraciones del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_PRTC` | `int unsigned` | Identificador interno del tipo de participante. |
| `DE_TIPO_PRTC` | `varchar(50)` | Descripcion principal del tipo de participante. |
| `CO_TIPO_UIF` | `char(1)` | Codigo auxiliar asociado a UIF. |
| `CO_TIPO_PDT` | `int` | Codigo auxiliar asociado a PDT. |
| `CO_INTE_CNL` | `varchar(3)` | Codigo auxiliar asociado a CNL. |
| `CO_TIPO_CNL_ULTI` | `varchar(5)` | Codigo auxiliar adicional asociado a CNL u otra integracion. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_PRTC` | Clave principal de la tabla. |
| Referenciada por | `R_PRTC_SERV` | `CO_TIPO_PRTC` | La tabla `R_PRTC_SERV` referencia esta tabla mediante la columna `CO_TIPO_PRTC`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es relevante para la configuracion de participantes por servicio dentro de Legasys. |
| Funcional | Los campos auxiliares `CO_TIPO_UIF`, `CO_TIPO_PDT`, `CO_INTE_CNL` y `CO_TIPO_CNL_ULTI` sugieren integraciones o mapeos hacia otros dominios funcionales. |

---

## Tabla: `H_ABOG_EXTE`

### Descripcion funcional
Tabla usada en Legasys para registrar abogados externos asociados a una notaria o a un departamento. Permite almacenar sus datos principales y relacionarlos con tickets.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ABOG_EXTE` | `int unsigned` | Identificador interno del abogado externo. |
| `CO_DEPA` | `int unsigned` | Departamento asociado al abogado externo. |
| `CO_COMP` | `int` | Codigo de la notaria o compania asociada. |
| `AP_ABOG_EXTE` | `varchar(50)` | Apellido del abogado externo. |
| `NO_ABOG_EXTE` | `varchar(50)` | Nombre del abogado externo. |
| `NU_COLE` | `varchar(10)` | Numero de colegiatura. |
| `SI_COLE` | `varchar(10)` | Sigla o referencia del colegio profesional. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `date` | Fecha de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ABOG_EXTE` | Clave principal de la tabla. |
| Referenciada por | `P_TICK` | `CO_ABOG_EXTE` | La tabla `P_TICK` referencia esta tabla mediante la columna `CO_ABOG_EXTE`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es relevante para tickets y asignaciones de abogados externos dentro de Legasys. |

---

## Tabla: `H_AGEN_FIRM`

### Descripcion funcional
Tabla usada en Legasys para registrar citas de agenda de firmas. Centraliza fecha, horario, responsables, ubicacion, estado de la cita y observaciones del flujo de firmas.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_AGEN_FIRM` | `int unsigned` | Identificador interno de la cita de agenda de firmas. |
| `CO_COMP` | `int` | Codigo de la notaria o compania. |
| `CO_TICK_CONT` | `int` | Ticket contenedor asociado a la cita. |
| `CO_TICK_SERV` | `int` | Ticket de servicio asociado. |
| `CO_SERV_ALTE` | `int` | Servicio alterno asociado, si aplica. |
| `FE_AGEN` | `date` | Fecha programada de la cita. |
| `HO_INI` | `time` | Hora de inicio de la cita. |
| `HO_FIN` | `time` | Hora de fin de la cita. |
| `CO_USUA_RESP` | `int` | Usuario responsable de la cita. |
| `CO_USUA_ABOG` | `int` | Usuario abogado asociado a la cita. |
| `IN_TIPO_LUGA` | `tinyint` | Tipo de lugar de la cita. |
| `DE_DIRE_CITA` | `varchar(255)` | Direccion donde se realizara la cita. |
| `DE_URL_MAPS` | `varchar(500)` | URL de mapa o ubicacion. |
| `NU_LATI` | `decimal(10,7)` | Latitud de la ubicacion. |
| `NU_LONG` | `decimal(10,7)` | Longitud de la ubicacion. |
| `DE_OBSE` | `varchar(500)` | Observaciones de la cita. |
| `IN_ESTA_CITA` | `tinyint` | Estado especifico de la cita. |
| `TS_USUA_MODI` | `timestamp` | Fecha y hora de la ultima modificacion. |
| `CO_USUA_MODI` | `varchar(20)` | Usuario que realizo la ultima modificacion. |
| `IN_ESTA` | `tinyint` | Estado general del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_AGEN_FIRM` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Es una tabla operativa clave del modulo de Agenda de Firmas en Legasys. |
| Funcional | Reune informacion de agenda, responsables, geolocalizacion y estado de la cita. |

---

## Tabla: `H_AGEN_FIRM_DETA`

### Descripcion funcional
Tabla usada en Legasys para registrar el detalle de participantes o firmas vinculadas a una cita de agenda de firmas. Permite relacionar una cita con tramites y participantes especificos.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_AGEN_FIRM_DETA` | `int unsigned` | Identificador interno del detalle de agenda. |
| `CO_AGEN_FIRM` | `int unsigned` | Cita principal de agenda de firmas asociada. |
| `CO_TRAM_FIRM` | `int` | Tramite de firma asociado. |
| `CO_PRTC_TRAM` | `int` | Participante del tramite asociado. |
| `TS_USUA_MODI` | `timestamp` | Fecha y hora de la ultima modificacion. |
| `CO_USUA_MODI` | `varchar(20)` | Usuario que realizo la ultima modificacion. |
| `IN_ESTA` | `tinyint` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_AGEN_FIRM_DETA` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Complementa a `H_AGEN_FIRM` detallando quienes participan o firman en cada cita. |

---

## Tabla: `H_ALER_RENI`

### Descripcion funcional
Tabla usada en Legasys para registrar alertas relacionadas con RENIEC. Permite almacenar mensajes o alertas vinculadas a un DNI o a un detalle RENIEC.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ALER_RENI` | `int` | Identificador interno de la alerta RENIEC. |
| `CO_DETA_RENI` | `int` | Detalle RENIEC asociado a la alerta. |
| `NU_DNI` | `varchar(8)` | DNI asociado a la alerta. |
| `NO_ALER` | `varchar(200)` | Descripcion o mensaje de alerta. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ALER_RENI` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla puede apoyar validaciones documentarias o alertas operativas ligadas a RENIEC. |

---

## Tabla: `H_ALIA_COLM`

### Descripcion funcional
Tabla usada en Legasys para registrar alias de columnas dentro de estructuras dinamicas o configurables. Permite definir metadatos de columnas, listas, formatos de salida y valores por defecto consumidos por configuraciones del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ALIA_COLM` | `int unsigned` | Identificador interno del alias de columna. |
| `NO_TABL` | `varchar(50)` | Nombre de la tabla asociada al alias. |
| `NO_COLM` | `varchar(50)` | Nombre real de la columna. |
| `DE_COLM` | `varchar(50)` | Descripcion visible de la columna. |
| `TI_DATA` | `varchar(50)` | Tipo de dato asociado a la columna. |
| `NU_DATA_LONG` | `int unsigned` | Longitud del dato. |
| `NU_DATA_SCAL` | `int unsigned` | Escala del dato. |
| `IN_LSTA` | `int unsigned` | Indicador asociado al uso en listas. |
| `NU_ORDE` | `int unsigned` | Orden de visualizacion. |
| `NO_CAMP` | `varchar(50)` | Nombre de campo asociado. |
| `NO_TABL_LIST` | `varchar(50)` | Tabla asociada para listas. |
| `NO_CAMP_LIST` | `varchar(50)` | Campo asociado para listas. |
| `CO_CAMP_LIST` | `varchar(50)` | Codigo de campo asociado a listas. |
| `TI_FORM_SALI` | `varchar(50)` | Tipo de formato de salida. |
| `VA_DEFE` | `varchar(50)` | Valor por defecto. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ALIA_COLM` | Clave principal de la tabla. |
| Foreign Key | `NO_TABL` | `NO_TABL` | Referencia a `P_ALIA_TABL.NO_TABL`. |
| Referenciada por | `R_SERV_COLM` | `CO_ALIA_COLM` | La tabla `R_SERV_COLM` referencia esta tabla mediante la columna `CO_ALIA_COLM`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es muy relevante para estructuras dinamicas, alias y configuraciones internas de Legasys. |
| Funcional | Permite mapear metadata tecnica y visual de columnas usadas por el sistema. |

---

## Tabla: `H_APER_CIER_CAJA`

### Descripcion funcional
Tabla usada en Legasys para registrar aperturas y cierres de caja. Guarda datos de fecha, hora, usuarios responsables, totales por medio de pago, diferencias y observaciones del cierre.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_APER_CIER_CAJA` | `int` | Identificador interno de la apertura/cierre de caja. |
| `CO_CAJA` | `int` | Caja asociada al registro. |
| `CO_TIPO_CAMB` | `int` | Tipo de cambio usado en el cierre o apertura. |
| `CO_COMP` | `int` | Codigo de la notaria o compania. |
| `FE_APER_CIER_CAJA` | `date` | Fecha de apertura o cierre. |
| `HO_APER_CAJA` | `time` | Hora de apertura de caja. |
| `CO_USUA_APER_CAJA` | `int` | Usuario que abrio la caja. |
| `HO_CIER_CAJA` | `time` | Hora de cierre de caja. |
| `CO_USUA_CIER_CAJA` | `int` | Usuario que cerro la caja. |
| `NU_TOTA_BILLE` | `decimal(18,2)` | Total de billetes. |
| `NU_TOTA_MONE` | `decimal(18,2)` | Total de monedas. |
| `NU_TOTA_DOLA` | `decimal(18,2)` | Total en dolares. |
| `NU_TOTA_TARJ` | `decimal(18,2)` | Total en tarjetas. |
| `NU_TOTA_DEPO` | `decimal(18,2)` | Total en depositos. |
| `NU_TOTA_CHEQ` | `decimal(18,2)` | Total en cheques. |
| `NU_TOTA_CAJA` | `decimal(18,2)` | Total fisico o total de caja. |
| `NU_TOTA_SIST` | `decimal(18,2)` | Total segun sistema. |
| `NU_TOTA_DIFE` | `decimal(18,2)` | Diferencia entre total de caja y total del sistema. |
| `DE_OBSE` | `text` | Observaciones del cierre o apertura. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_APER_CIER_CAJA` | Clave principal de la tabla. |
| Referenciada por | `R_DETA_CIER_CAJA` | `CO_APER_CIER_CAJA` | La tabla `R_DETA_CIER_CAJA` referencia esta tabla mediante la columna `CO_APER_CIER_CAJA`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Es una tabla operativa clave del modulo Caja para apertura, cierre y cuadre. |
| Funcional | Consolida totales por medio de pago y diferencia entre caja fisica y sistema. |

---

## Tabla: `H_ARCH_MINU`

### Descripcion funcional
Tabla usada en Legasys para registrar archivos o categorias de archivo del minutario. Permite mantener un catalogo con trazabilidad basica.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ARCH_MINU` | `int` | Identificador interno del archivo de minuta. |
| `DE_ARCH_MINU` | `varchar(100)` | Descripcion principal del archivo o categoria. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ARCH_MINU` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Puede servir como catalogo auxiliar para clasificaciones del minutario. |

---

## Tabla: `H_AUTO_HIJO`

### Descripcion funcional
Tabla usada en Legasys para registrar hijos dentro de flujos de autorizacion o viaje asociados a un ticket de servicio. Permite guardar identidad, edad y fechas relacionadas.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_AUTO_HIJO` | `bigint` | Identificador interno del registro del hijo. |
| `CO_TICK_SERV` | `bigint` | Ticket de servicio asociado. |
| `CO_TICK_SERV_SUB` | `int` | Subservicio asociado, si aplica. |
| `NU_CORR` | `int unsigned` | Correlativo interno del registro. |
| `CO_TDOC_IDEN` | `int unsigned` | Tipo de documento de identidad asociado. |
| `NU_DOCU_IDEN` | `varchar(20)` | Numero de documento de identidad. |
| `NO_HIJO` | `varchar(80)` | Nombre del hijo. |
| `NU_EDAD_ANIO` | `int unsigned` | Edad en anios. |
| `NU_EDAD_MES` | `varchar(20)` | Edad en meses o detalle complementario. |
| `FE_NACI_HIJO` | `date` | Fecha de nacimiento del hijo. |
| `FE_INSC_HIJO` | `date` | Fecha de inscripcion del hijo. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `date` | Fecha de la ultima modificacion. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_AUTO_HIJO` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla parece formar parte de autorizaciones de viaje o flujos relacionados con menores. |

---

## Tabla: `H_AUTO_VJE`

### Descripcion funcional
Tabla usada en Legasys para registrar autorizaciones de viaje asociadas a un ticket de servicio. Permite guardar tipo, destino, medio, observaciones, fechas de viaje y ubicacion.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_AUTO_VJE` | `bigint` | Identificador interno de la autorizacion de viaje. |
| `CO_TICK_SERV` | `bigint` | Ticket de servicio asociado. |
| `CO_TICK_SERV_SUB` | `int` | Subservicio asociado, si aplica. |
| `CO_TIPO_VIAJ_PODE` | `int unsigned` | Tipo de viaje o poder asociado. |
| `NO_DEST_VIAJ` | `varchar(200)` | Destino del viaje. |
| `DE_MEDI_TRAM` | `varchar(100)` | Medio de tramite o transporte asociado. |
| `NO_OBSE` | `text` | Observacion o nota complementaria. |
| `TS_EMIS` | `date` | Fecha de emision. |
| `FE_VIAJ_INI` | `date` | Fecha de inicio del viaje. |
| `FE_VIAJ_FIN` | `date` | Fecha de fin del viaje. |
| `DE_OBSE` | `text` | Observaciones generales. |
| `CO_UBIG` | `varchar(6)` | Ubigeo asociado al viaje. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_AUTO_VJE` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es relevante para el flujo de autorizaciones de viaje dentro de Legasys. |

---

## Tabla: `H_CAJA_PAGO_LINE`

### Descripcion funcional
Tabla usada en Legasys para relacionar pagos en linea con comprobantes o documentos de Caja. Permite almacenar el documento asociado, monto, estado y trazabilidad de creacion.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CAJA_PAGO_LINE` | `int` | Identificador interno del registro de caja para pago en linea. |
| `CO_CABE_PAGO_LINE` | `int` | Cabecera del pago en linea asociada. |
| `CO_CABE_CAJA` | `int` | Cabecera de Caja asociada. |
| `CO_TDOC` | `int` | Tipo de documento asociado. |
| `NU_CABE_CAJA` | `varchar(30)` | Numero o identificador del documento de caja. |
| `MO_DOCU` | `decimal(11,2)` | Monto del documento asociado. |
| `IN_PRIN` | `int` | Indicador de principalidad del documento. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |
| `CO_USUA_CREA` | `int` | Usuario que creo el registro. |
| `TS_USUA_CREA` | `datetime` | Fecha y hora de creacion del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CAJA_PAGO_LINE` | Clave principal de la tabla. |
| Foreign Key | `CO_CABE_PAGO_LINE` | `CO_CABE_PAGO_LINE` | Referencia a `P_CABE_PAGO_LINE.CO_CABE_PAGO_LINE`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es relevante para la integracion entre pagos en linea y Caja dentro de Legasys. |
| Funcional | Permite vincular comprobantes de Caja a una cabecera de pago web. |

---

## Tabla: `H_DETA_CORR_UIF`

### Descripcion funcional
Tabla usada en Legasys para registrar detalles o parametros de correlacion UIF. Permite almacenar umbrales, tipo de cambio, vigencia y archivo asociado a controles regulatorios.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DETA_CORR_UIF` | `int` | Identificador interno del detalle UIF. |
| `NU_UMBR` | `decimal(11,2)` | Umbral economico asociado al control. |
| `NU_TIPO_CAMB` | `decimal(11,2)` | Tipo de cambio usado para el control. |
| `FE_INIC` | `date` | Fecha de inicio de vigencia. |
| `FE_FINA` | `date` | Fecha de fin de vigencia. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `NO_ARCH` | `varchar(150)` | Nombre del archivo asociado al registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DETA_CORR_UIF` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla parece ligada a controles regulatorios o reportes UIF basados en umbrales y vigencias. |

---

## Tabla: `H_DETA_DOCU`

### Descripcion funcional
Tabla usada en Legasys para registrar el detalle de entrega o gestion documental asociado a un ticket de servicio. Permite controlar fechas, receptor, mensajeria, montos, ocurrencias y evidencias del flujo documental.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DETA_DOCU` | `bigint` | Identificador interno del detalle documental. |
| `CO_TICK_SERV` | `bigint` | Ticket de servicio asociado. |
| `CO_TICK_SERV_SUB` | `int` | Subservicio asociado, si aplica. |
| `CO_MENS` | `char(2)` | Mensajero asociado. |
| `CO_TIPO_OCUR` | `int unsigned` | Tipo de ocurrencia asociado. |
| `CO_COUR` | `int` | Courier asociado. |
| `FE_DOCU` | `date` | Fecha del documento o gestion. |
| `NU_CART_REFE` | `varchar(10)` | Numero de carta o referencia. |
| `NO_RECE` | `varchar(120)` | Nombre de quien recibe. |
| `FE_RECO` | `date` | Fecha de recojo o recepcion. |
| `NO_RECO` | `varchar(120)` | Nombre de quien recoge. |
| `NU_DOCU` | `int unsigned` | Numero documental asociado. |
| `FE_ENTR` | `date` | Fecha de entrega. |
| `DE_DESC` | `text` | Descripcion u observacion del detalle. |
| `HO_ENTR` | `varchar(10)` | Hora de entrega. |
| `FE_DEVO` | `date` | Fecha de devolucion. |
| `HO_DEVO` | `time` | Hora de devolucion. |
| `FE_CERT` | `date` | Fecha de certificacion. |
| `HO_CERT` | `time` | Hora de certificacion. |
| `NU_MONT` | `decimal(15,2)` | Monto asociado al tramite o entrega. |
| `IM_FOTO_DIRE` | `longblob` | Evidencia fotografica o imagen relacionada. |
| `IN_TIPO_CART` | `int` | Tipo de carta asociado. |
| `IN_RECE_MENS` | `int` | Indicador de recepcion por mensajero. |
| `FE_RECE_MENS` | `datetime` | Fecha de recepcion por mensajero. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DETA_DOCU` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es importante para entrega documental, mensajeria, recojo y certificacion dentro de Legasys. |
| Funcional | Maneja fechas, receptor, courier, evidencias y montos del flujo documental. |

---

## Tabla: `H_DETA_FIRM`

### Descripcion funcional
Tabla usada en Legasys para registrar el detalle de firmas realizadas dentro de un tramite. Permite vincular tramite, participante, usuario firmante y momento exacto de la firma.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DETA_FIRM` | `int` | Identificador interno del detalle de firma. |
| `CO_TRAM_FIRM` | `int` | Tramite de firma asociado. |
| `CO_TICK_SERV` | `int` | Ticket de servicio asociado. |
| `CO_PRTC_TRAM` | `int` | Participante del tramite asociado. |
| `CO_USUA_FIRM` | `int` | Usuario que realizo la firma. |
| `FE_FIRM` | `date` | Fecha de la firma. |
| `HO_FIRM` | `time` | Hora de la firma. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DETA_FIRM` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla complementa el flujo de firmas registrando quien firmo y cuando lo hizo. |

---

## Tabla: `H_DETA_GRAV`

### Descripcion funcional
Tabla usada en Legasys para registrar detalle de gravamenes, consultas vehiculares o verificaciones relacionadas con un ticket de servicio. Almacena datos del propietario, placa, consulta, oficina registral, resultados y banderas de validacion.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DETA_GRAV` | `int` | Identificador interno del detalle. |
| `CO_DETA_SUB_GRAV` | `int` | Subdetalle o referencia interna del gravamen. |
| `CO_TICK_SERV` | `int` | Ticket de servicio asociado. |
| `CO_TRAM_VEHI` | `int` | Tramite vehicular asociado. |
| `CO_CONS` | `int` | Consulta asociada. |
| `CO_NOTI` | `int` | Notificacion asociada. |
| `CO_REPR_VEHI` | `text` | Representacion o codigo del vehiculo. |
| `CO_OFIC_REGI` | `int` | Oficina registral asociada. |
| `NO_API_REPR_VEHI` | `text` | Respuesta API de representacion vehicular. |
| `NO_API_REPR_VEHI_ANTE` | `text` | Respuesta API anterior de representacion vehicular. |
| `NO_API_GRAV` | `text` | Respuesta API de gravamen. |
| `NO_API_REPO` | `text` | Respuesta API de reporte. |
| `NO_API_PAPE` | `text` | Respuesta API de papeletas. |
| `NO_API_SUTR` | `text` | Respuesta API de SUTRAN. |
| `NO_PROP` | `varchar(250)` | Nombre del propietario. |
| `NO_DOCU_IDEN` | `varchar(15)` | Tipo o descripcion del documento de identidad. |
| `NU_DOCU` | `varchar(20)` | Numero de documento. |
| `NO_DIRE` | `varchar(250)` | Direccion asociada. |
| `NU_PLAC` | `varchar(10)` | Numero de placa. |
| `CO_CARP_TICK` | `int` | Carpeta o relacion interna del ticket. |
| `FE_CONS` | `datetime` | Fecha de la consulta. |
| `IN_GRAV` | `int` | Indicador de gravamen. |
| `IN_PAPE_LIMA` | `int` | Indicador de papeletas en Lima. |
| `IN_PAPE_CALL` | `int` | Indicador de papeletas en Callao. |
| `IN_SOAT` | `int` | Indicador de SOAT. |
| `IN_IMPU` | `int` | Indicador de impuestos. |
| `IN_REVI_TECN` | `int` | Indicador de revision tecnica. |
| `IN_ASIE` | `int` | Indicador de asiento. |
| `IN_MULT_ELEC` | `int` | Indicador de multas electronicas. |
| `IN_CAPT_SAT` | `int` | Indicador de captura SAT. |
| `IN_TITU_SUNA` | `int` | Indicador de titularidad SUNARP. |
| `IN_SUTR` | `int` | Indicador de SUTRAN. |
| `IN_ATU` | `int` | Indicador de ATU. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_APRO_CONS` | `int` | Indicador de aprobacion de consulta. |
| `NU_MONT` | `decimal(11,2)` | Monto asociado a la consulta o tramite. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |
| `IN_TIPO` | `int` | Tipo interno del registro. |
| `IN_DOBL_PLAC` | `int` | Indicador de doble placa. |
| `IN_AUTO_PAGO` | `int` | Indicador de autopago. |
| `CO_USUA_FINA` | `int` | Usuario que finalizo el proceso. |
| `FE_USUA_FINA` | `datetime` | Fecha y hora de finalizacion. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DETA_GRAV` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es muy relevante para consultas vehiculares, gravamenes y validaciones operativas dentro de Legasys. |
| Funcional | Consolida respuestas de APIs, resultados de validacion y datos del propietario o vehiculo. |

---

## Tabla: `H_DETA_INFO`

### Descripcion funcional
Tabla usada en Legasys para registrar detalle de informacion consultada o revisada sobre personas o registros asociados a un ticket de servicio. Permite almacenar datos de identidad, revisiones y tiempos de consulta.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DETA_INFO` | `int` | Identificador interno del detalle de informacion. |
| `CO_TICK_SERV` | `int` | Ticket de servicio asociado. |
| `CO_PIC` | `int` | PIC asociado. |
| `IN_TIPO_PERS` | `int` | Tipo de persona asociado. |
| `CO_TDOC_IDEN` | `int` | Tipo de documento de identidad. |
| `NU_DOCU_IDEN` | `varchar(20)` | Numero de documento de identidad. |
| `AP_PATE` | `varchar(100)` | Apellido paterno. |
| `AP_MATE` | `varchar(100)` | Apellido materno. |
| `NO_PERS` | `varchar(300)` | Nombre de la persona. |
| `NO_PERS_TOTA` | `varchar(300)` | Nombre completo totalizado. |
| `NO_BUSQ` | `varchar(300)` | Nombre o termino usado en la busqueda. |
| `NU_CANT` | `int` | Cantidad asociada al resultado. |
| `CO_USUA` | `int` | Usuario asociado a la consulta. |
| `FE_USUA_REVI` | `datetime` | Fecha de revision por usuario. |
| `FE_INIC_CONS` | `datetime` | Fecha de inicio de consulta. |
| `FE_FIN_CONS` | `datetime` | Fecha de fin de consulta. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `CO_UIF_REVI` | `int` | Usuario o referencia de revision UIF. |
| `FE_UIF_REVI` | `datetime` | Fecha de revision UIF. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |
| `IN_TIPO` | `int` | Tipo interno del registro. |
| `IN_REVI` | `int` | Indicador de revision. |
| `IN_REVI_UIF` | `int` | Indicador de revision UIF. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DETA_INFO` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla parece ligada a consultas de informacion, revisiones y validaciones sobre personas dentro de Legasys. |

---

## Tabla: `H_DETA_NOTA`

### Descripcion funcional
Tabla usada en Legasys para registrar el detalle de conceptos incluidos en una nota de credito o debito. Permite vincular el detalle original de caja con cantidades, tarifa y monto total de la nota.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DETA_NOTA` | `int` | Identificador interno del detalle de nota. |
| `CO_CABE_NOTA` | `int` | Cabecera de la nota asociada. |
| `CO_DETA_CAJA` | `int` | Detalle de Caja asociado. |
| `NU_CANT` | `int` | Cantidad asociada al detalle de nota. |
| `MO_TARI` | `decimal(12,2)` | Tarifa o monto unitario. |
| `MO_TOTA` | `decimal(12,2)` | Monto total del detalle de nota. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DETA_NOTA` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es relevante para notas de credito y debito al detallar el impacto sobre conceptos cobrados. |

---

## Tabla: `H_DETA_PAGO_LINE`

### Descripcion funcional
Tabla usada en Legasys para registrar el detalle de conceptos incluidos en un pago en linea. Permite vincular presupuesto, ticket, concepto, cantidad, monto pendiente y monto cobrado.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DETA_PAGO_LINE` | `int` | Identificador interno del detalle del pago en linea. |
| `CO_CABE_PAGO_LINE` | `int` | Cabecera de pago en linea asociada. |
| `CO_PRES_TICK` | `int` | Presupuesto del ticket asociado. |
| `CO_TICK_CONT` | `int` | Ticket contenedor asociado. |
| `CO_TICK_SERV` | `int` | Ticket de servicio asociado. |
| `CO_CPTO` | `int` | Concepto asociado. |
| `CO_TIPO_CPTO` | `int` | Tipo de concepto asociado. |
| `DE_CPTO` | `varchar(250)` | Nombre principal del concepto. |
| `DE_DETA_CPTO` | `varchar(500)` | Detalle o descripcion ampliada del concepto. |
| `NU_CANT` | `decimal(11,2)` | Cantidad asociada al concepto. |
| `MO_PEND_PAGO_LINE` | `decimal(11,2)` | Monto pendiente de pago en linea. |
| `MO_COBR_PAGO_LINE` | `decimal(11,2)` | Monto cobrado en linea. |
| `PO_IGV` | `decimal(5,2)` | Porcentaje de IGV asociado. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DETA_PAGO_LINE` | Clave principal de la tabla. |
| Foreign Key | `FK_H_DETA_PAGO_LINE_01` | `CO_CABE_PAGO_LINE` | Referencia a `P_CABE_PAGO_LINE.CO_CABE_PAGO_LINE`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es clave para el detalle economico de pagos en linea dentro de Legasys. |
| Funcional | Relaciona conceptos, cantidades, montos pendientes y montos cobrados por ticket o presupuesto. |

---

## Tabla: `H_DETA_PAPE`

### Descripcion funcional
Tabla usada en Legasys para registrar detalle de papeletas o consultas asociadas a un ticket de servicio. Permite almacenar tipo de papeleta, placa, fecha de consulta y trazabilidad.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DETA_PAPE` | `int` | Identificador interno del detalle de papeleta. |
| `CO_TICK_SERV` | `int` | Ticket de servicio asociado. |
| `CO_TIPO_PAPE` | `int` | Tipo de papeleta asociado. |
| `NU_PLAC` | `varchar(20)` | Numero de placa asociado. |
| `FE_CONS` | `datetime` | Fecha de la consulta. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DETA_PAPE` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla parece asociada a consultas o control de papeletas en flujos vehiculares. |

---

## Tabla: `H_DETA_PRES_TICK`

### Descripcion funcional
Tabla usada en Legasys para registrar el detalle de conceptos dentro de un presupuesto de ticket. Permite almacenar concepto, tipo de concepto, montos y texto visible del detalle presupuestal.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DETA_PRES_TICK` | `int` | Identificador interno del detalle presupuestal. |
| `CO_PRES_TICK` | `int` | Presupuesto del ticket asociado. |
| `CO_TICK_SERV` | `int` | Ticket de servicio asociado. |
| `CO_TICK_CONT` | `int` | Ticket contenedor asociado. |
| `CO_TIPO_CPTO` | `int` | Tipo de concepto asociado. |
| `CO_CPTO` | `int` | Concepto asociado. |
| `MO_TRAN_TICK` | `decimal(14,2)` | Monto trasladado o calculado inicialmente. |
| `MO_TRAN_TICK_NUEV` | `decimal(14,2)` | Monto trasladado o actualizado. |
| `CO_SERV_CPTO_TARI` | `int` | Relacion de servicio, concepto o tarifa asociada. |
| `DE_DETA_CPTO` | `varchar(250)` | Descripcion visible del concepto. |
| `CO_USUA_CREA` | `int` | Usuario que creo el registro. |
| `TS_USUA_CREA` | `datetime` | Fecha y hora de creacion. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DETA_PRES_TICK` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es muy relevante para presupuestos y detalle economico de tickets en Legasys. |
| Funcional | Almacena el detalle visible de conceptos presupuestados por ticket o servicio. |

---

## Tabla: `H_DETA_RENI`

### Descripcion funcional
Tabla usada en Legasys para registrar el detalle de consultas RENIEC. Permite almacenar datos personales, estado civil, direccion, montos, fechas de consulta y otros resultados de validacion documental.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DETA_RENI` | `int` | Identificador interno del detalle RENIEC. |
| `CO_TICK_SERV` | `int` | Ticket de servicio asociado. |
| `CO_CONS` | `int` | Consulta asociada. |
| `CO_CARP_TICK` | `int` | Carpeta o relacion interna del ticket. |
| `NU_DNI` | `varchar(10)` | Numero de DNI consultado. |
| `NO_PATE` | `varchar(100)` | Apellido paterno. |
| `NO_MATE` | `varchar(100)` | Apellido materno. |
| `NO_NOMB` | `varchar(100)` | Nombres. |
| `NO_SEXO` | `varchar(100)` | Sexo o genero reportado. |
| `NO_GRAD_INST` | `varchar(200)` | Grado de instruccion reportado. |
| `NO_REST` | `varchar(250)` | Restricciones reportadas. |
| `NO_OBSE` | `varchar(250)` | Observaciones reportadas. |
| `FE_NACI` | `date` | Fecha de nacimiento. |
| `CO_ESTA_CIVI` | `int` | Estado civil asociado. |
| `NO_ESTA_CIVI` | `varchar(50)` | Descripcion del estado civil. |
| `NO_DEPA` | `varchar(100)` | Departamento reportado. |
| `NO_PROV` | `varchar(100)` | Provincia reportada. |
| `NO_DIST` | `varchar(100)` | Distrito reportado. |
| `NO_DIRE` | `varchar(100)` | Direccion reportada. |
| `CUP` | `int` | Campo auxiliar de la respuesta. |
| `NS_PRTC` | `int` | Campo auxiliar de participante. |
| `NS_DIRE` | `int` | Campo auxiliar de direccion. |
| `CO_UBIG` | `int` | Ubigeo reportado. |
| `NU_MONT` | `decimal(11,2)` | Monto asociado a la consulta. |
| `FE_CONS` | `datetime` | Fecha y hora de la consulta. |
| `CO_USUA_CREA` | `int` | Usuario que creo el registro. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |
| `IN_ERRO` | `int` | Indicador de error. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DETA_RENI` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es relevante para consultas RENIEC y validaciones documentarias dentro de Legasys. |
| Funcional | Almacena informacion personal consultada, direccion, estado civil y trazabilidad del proceso. |

---

## Tabla: `H_DETA_SOLI`

### Descripcion funcional
Tabla usada en Legasys para registrar detalle de solicitudes asociadas a un ticket de servicio. Permite almacenar numeros de solicitud, titulo y trazabilidad basica.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DETA_SOLI` | `int` | Identificador interno del detalle de solicitud. |
| `CO_TICK_SERV` | `int` | Ticket de servicio asociado. |
| `NU_SOLI` | `varchar(40)` | Numero de solicitud. |
| `NU_TITU` | `varchar(40)` | Numero de titulo asociado. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DETA_SOLI` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla puede servir como soporte para solicitudes y titulos vinculados a tickets. |

---

## Tabla: `H_DETA_TITU`

### Descripcion funcional
Tabla usada en Legasys para registrar el detalle de titulos consultados o seguidos dentro de procesos registrales. Permite almacenar estado, etapa, representante, monto, fecha registral e imagen.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DETA_TITU` | `int` | Identificador interno del detalle de titulo. |
| `CO_SGMT_ORLC` | `int` | Seguimiento ORLC asociado. |
| `CO_DETA_SGMT` | `int` | Detalle de seguimiento asociado. |
| `NU_KARD` | `varchar(50)` | Numero de kardex asociado. |
| `NU_TITU` | `varchar(50)` | Numero de titulo. |
| `NO_ESTA` | `varchar(100)` | Estado reportado del titulo. |
| `NO_ESTA_LEGA` | `varchar(100)` | Estado legal reportado. |
| `NO_ETAP` | `varchar(100)` | Etapa reportada. |
| `NO_REPR` | `varchar(200)` | Nombre del representante. |
| `NU_MONT` | `varchar(20)` | Monto asociado. |
| `FE_REGI` | `varchar(30)` | Fecha registral reportada. |
| `DE_IMAG` | `varchar(100)` | Imagen o referencia grafica asociada. |
| `FE_CONS` | `timestamp` | Fecha y hora de la consulta. |
| `IN_TERM` | `int` | Indicador complementario del termino o resultado. |
| `IN_MODU` | `int` | Modulo asociado. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DETA_TITU` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es relevante para seguimiento registral, consulta de titulos y trazabilidad de estados en Legasys. |

---

## Tabla: `H_DETA_UIF`

### Descripcion funcional
Tabla usada en Legasys para registrar el detalle operativo y regulatorio de operaciones UIF. Permite almacenar datos de la operacion, intervinientes, documentos, montos, origen, forma de pago y clasificaciones requeridas para cumplimiento.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DETA_UIF` | `int` | Identificador interno del detalle UIF. |
| `NU_REGI` | `int` | Numero de registro asociado. |
| `TI_TRAN` | `char(1)` | Tipo de transaccion. |
| `TI_ENVI` | `char(1)` | Tipo de envio o modalidad asociada. |
| `TI_INST` | `char(1)` | Tipo de instrumento asociado. |
| `NU_INST` | `int` | Numero de instrumento. |
| `FE_INST` | `date` | Fecha del instrumento. |
| `IN_CONC` | `char(1)` | Indicador de conclusion o concepto asociado. |
| `DE_CONC` | `char(1)` | Dato complementario del concepto. |
| `FE_FIRM` | `date` | Fecha de firma. |
| `CO_MODE_OPER` | `char(1)` | Modo de operacion. |
| `IN_MODA` | `char(1)` | Indicador de modalidad. |
| `CA_OPER` | `varchar(10)` | Categoria o codigo de operacion. |
| `IN_GARA` | `char(1)` | Indicador relacionado a garantia. |
| `IN_REPR` | `char(1)` | Indicador de representante. |
| `IN_PROP` | `char(1)` | Indicador de propietario. |
| `IN_BENE` | `char(1)` | Indicador de beneficiario. |
| `IN_PART` | `char(1)` | Indicador de participante. |
| `IN_PERS` | `char(1)` | Indicador de persona. |
| `TI_REPR` | `varchar(1)` | Tipo de representante. |
| `IN_RESI` | `char(1)` | Indicador de residencia. |
| `TI_PERS` | `char(1)` | Tipo de persona. |
| `TI_DOCU` | `char(1)` | Tipo de documento. |
| `NU_DOCU` | `varchar(20)` | Numero de documento. |
| `NU_RUC` | `varchar(11)` | Numero de RUC. |
| `AP_PATE` | `varchar(120)` | Apellido paterno. |
| `AP_MATE` | `varchar(40)` | Apellido materno. |
| `NO_PERS` | `varchar(40)` | Nombre de la persona. |
| `CO_PAIS_NACI` | `varchar(2)` | Pais de nacimiento. |
| `FE_NACI` | `date` | Fecha de nacimiento. |
| `ES_CIVL` | `char(1)` | Estado civil. |
| `CO_CARG` | `varchar(3)` | Codigo de cargo. |
| `CO_OCUP` | `varchar(3)` | Codigo de ocupacion. |
| `CO_CIIU` | `varchar(6)` | Codigo CIIU. |
| `DE_SOCI` | `varchar(40)` | Denominacion social o razon social. |
| `CO_ZONA` | `varchar(2)` | Zona asociada. |
| `NU_PART` | `varchar(50)` | Numero de partida. |
| `DE_DIRE` | `varchar(150)` | Direccion. |
| `CO_UBIG_DEPA` | `varchar(2)` | Ubigeo de departamento. |
| `CO_UBIG_PROV` | `varchar(2)` | Ubigeo de provincia. |
| `CO_UBIG_DIST` | `varchar(2)` | Ubigeo de distrito. |
| `NU_TELE` | `varchar(40)` | Numero telefonico. |
| `IN_PART_CONY` | `char(1)` | Indicador de participacion del conyuge. |
| `DE_CONY` | `varchar(1)` | Dato complementario del conyuge. |
| `AP_PATE_CONY` | `varchar(40)` | Apellido paterno del conyuge. |
| `AP_MATE_CONY` | `varchar(40)` | Apellido materno del conyuge. |
| `NO_CONY` | `varchar(40)` | Nombre del conyuge. |
| `TI_FOND` | `varchar(3)` | Tipo de fondo. |
| `TI_OPER` | `varchar(3)` | Tipo de operacion. |
| `FO_PAGO` | `char(1)` | Forma de pago. |
| `CO_OPOR` | `varchar(2)` | Codigo de oportunidad. |
| `DE_OPOR` | `varchar(40)` | Descripcion de la oportunidad. |
| `DE_ORIG` | `varchar(40)` | Descripcion del origen. |
| `CO_FORM_PAGO` | `varchar(10)` | Codigo de forma de pago. |
| `CO_MONE` | `varchar(3)` | Codigo de moneda. |
| `MO_OPER` | `decimal(18,2)` | Monto de la operacion. |
| `MO_PRTC_OPER` | `decimal(15,2)` | Monto parcial de la operacion. |
| `MO_TOTA_OPER` | `decimal(18,2)` | Monto total de la operacion. |
| `IN_INSC_BIEN` | `char(1)` | Indicador de inscripcion de bien. |
| `TI_CAMB` | `decimal(6,3)` | Tipo de cambio aplicado. |
| `CO_ZONA_BIEN` | `varchar(2)` | Zona del bien. |
| `NU_PART_BIEN` | `varchar(20)` | Numero de partida del bien. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DETA_UIF` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Es una tabla de alto valor para cumplimiento, UIF y trazabilidad regulatoria en Legasys. |
| Funcional | Consolida datos de operacion, participantes, documentos, montos, origen y forma de pago en una sola estructura. |

---

## Tabla: `H_DL939_PAGO`

### Descripcion funcional
Tabla usada en Legasys para registrar pagos asociados al flujo `DL939`, incluyendo medio de pago, moneda, bancos, documento, imagen y relacion con adjuntos digitales o participantes.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DL939_PAGO` | `bigint` | Identificador interno del pago. |
| `CO_TICK_SERV` | `bigint` | Ticket de servicio asociado. |
| `CO_TICK_SERV_SUB` | `int` | Subservicio asociado, si aplica. |
| `CO_UPDA_DIGI` | `int` | Relacion con actualizacion o adjunto digital. |
| `CO_PRTC_TRAM` | `int` | Participante del tramite asociado. |
| `MO_PAGA_FECH` | `decimal(14,2)` | Monto pagado. |
| `CO_MEDI_PAGO` | `int` | Medio de pago asociado. |
| `CO_TIPO_MONE` | `int unsigned` | Tipo de moneda asociado. |
| `NU_DOCU_PAGO` | `varchar(50)` | Numero de documento del pago. |
| `CO_BANC` | `int unsigned` | Banco origen asociado. |
| `NU_CUEN` | `varchar(50)` | Numero de cuenta origen. |
| `CO_BANC_DEST` | `int` | Banco destino asociado. |
| `NU_CUEN_DEST` | `varchar(100)` | Numero de cuenta destino. |
| `FE_DOCU_PAGO` | `date` | Fecha del documento de pago. |
| `CO_ASEV` | `varchar(1)` | Codigo auxiliar asociado. |
| `FE_INIC` | `date` | Fecha de inicio del periodo o vigencia. |
| `FE_TERM` | `date` | Fecha de termino del periodo o vigencia. |
| `IN_IMAG` | `int` | Indicador de imagen adjunta. |
| `IN_EXHI` | `int` | Indicador de exhibicion o visibilidad. |
| `DE_URL_IMAG` | `varchar(300)` | URL o ruta de la imagen adjunta. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DL939_PAGO` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es muy relevante para el flujo de medios de pago y minutario digital en Legasys. |
| Funcional | `CO_UPDA_DIGI` conecta el pago con adjuntos o registros digitales asociados al proceso. |
| Funcional | `CO_TICK_SERV_SUB` es clave cuando el pago pertenece a un subservicio especifico. |

---

## Tabla: `H_DOCU_DIGI_QR_ESTA`

### Descripcion funcional
Tabla usada en Legasys para registrar el historial de estados de un documento digital QR. Permite almacenar eventos, payloads JSON, observaciones y trazabilidad del flujo documental digital.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DOCU_DIGI_QR_ESTA` | `int` | Identificador interno del historial de estado. |
| `CO_DOCU_DIGI_QR` | `int` | Documento digital QR asociado. |
| `IN_ESTA_DOCU_DIGI` | `tinyint` | Estado del documento digital. |
| `DE_EVEN` | `varchar(255)` | Nombre o descripcion del evento. |
| `TX_JSON_EVEN` | `json` | Payload JSON del evento. |
| `TX_OBSE` | `text` | Observaciones del evento o cambio de estado. |
| `CO_USUA_MODI` | `int` | Usuario que registro el cambio. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora del cambio. |
| `IN_ESTA` | `tinyint(1)` | Estado general del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DOCU_DIGI_QR_ESTA` | Clave principal de la tabla. |
| Foreign Key | `FK_DOCU_DIGI_QR_ESTA` | `CO_DOCU_DIGI_QR` | Referencia a `P_DOCU_DIGI_QR.CO_DOCU_DIGI_QR`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es clave para la trazabilidad de estados del documento digital LEGASYS/QR. |
| Funcional | Permite registrar no solo el estado, sino tambien el evento y su contexto JSON. |

---

## Tabla: `H_DOCU_DIGI_QR_PRTC`

### Descripcion funcional
Tabla usada en Legasys para registrar los participantes de un documento digital QR. Permite almacenar rol, calidad, identidad y observaciones de cada participante involucrado en el documento.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DOCU_DIGI_QR_PRTC` | `int` | Identificador interno del participante del documento digital. |
| `CO_DOCU_DIGI_QR` | `int` | Documento digital QR asociado. |
| `NU_ORDE` | `int` | Orden del participante dentro del documento. |
| `DE_ROL_PRTC` | `varchar(100)` | Rol del participante. |
| `DE_CALI_PRTC` | `varchar(100)` | Calidad o condicion del participante. |
| `DE_NOMB_COMP` | `varchar(255)` | Nombre completo del participante. |
| `DE_TDOC_IDEN` | `varchar(50)` | Tipo de documento de identidad. |
| `NU_DOCU_IDEN` | `varchar(30)` | Numero de documento de identidad. |
| `DE_TIPO_PERS` | `varchar(50)` | Tipo de persona. |
| `DE_REPR_DE` | `varchar(255)` | Representa a quien o descripcion de representacion. |
| `TX_OBSE` | `text` | Observaciones del participante. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `tinyint(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DOCU_DIGI_QR_PRTC` | Clave principal de la tabla. |
| Foreign Key | `FK_DOCU_DIGI_QR_PRTC` | `CO_DOCU_DIGI_QR` | Referencia a `P_DOCU_DIGI_QR.CO_DOCU_DIGI_QR`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es clave para la composicion de participantes del documento digital QR. |

---

## Tabla: `H_DOCU_TEMP`

### Descripcion funcional
Tabla usada en Legasys para registrar documentos temporales asociados a un ticket de servicio. Permite relacionar un documento de identidad temporal con un usuario y un estado.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DOCU_TEMP` | `int` | Identificador interno del documento temporal. |
| `CO_TICK_SERV` | `int` | Ticket de servicio asociado. |
| `NU_DOCU_IDEN` | `varchar(12)` | Numero de documento de identidad temporal. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DOCU_TEMP` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla parece servir como apoyo temporal para documentos asociados a tickets. |

---

## Tabla: `H_ENVI_CNL`

### Descripcion funcional
Tabla usada en Legasys para registrar envios hacia CNL asociados a tickets. Permite almacenar fecha de envio, respuesta, ruta XML, observaciones de error y estado del proceso.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ENVI_CNL` | `int` | Identificador interno del envio CNL. |
| `CO_TICK_CONT` | `int` | Ticket contenedor asociado. |
| `CO_TICK_SERV` | `int` | Ticket de servicio asociado. |
| `CO_USUA` | `int` | Usuario asociado al envio. |
| `FE_ENVI` | `datetime` | Fecha y hora del envio. |
| `DE_OBSE_ERRO` | `text` | Observaciones o mensaje de error. |
| `DE_RESP_CNL` | `varchar(190)` | Respuesta recibida desde CNL. |
| `DE_RUTA_XML` | `varchar(190)` | Ruta del XML generado o enviado. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ENVI_CNL` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es relevante para integraciones de envio CNL dentro de Legasys. |
| Funcional | Permite trazar fecha, respuesta, errores y ruta del XML del envio. |

---

## Tabla: `H_ENVI_DESP`

### Descripcion funcional
Tabla usada en Legasys para registrar envios de despacho. Permite almacenar usuario, notaria, cantidad, fecha, hora y estado del despacho realizado.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ENVI_DESP` | `int` | Identificador interno del envio de despacho. |
| `CO_USUA` | `int` | Usuario asociado al envio. |
| `CO_COMP` | `int` | Codigo de la notaria o compania. |
| `NU_CANT` | `int` | Cantidad asociada al envio. |
| `FE_ENVI_DESP` | `date` | Fecha del despacho. |
| `HO_ENVI_DESP` | `time` | Hora del despacho. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ENVI_DESP` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla parece servir para trazabilidad de despachos o remisiones operativas. |

---

## Tabla: `H_ENVI_WHAT`

### Descripcion funcional
Tabla usada en Legasys para registrar envios de WhatsApp asociados a tickets. Permite almacenar telefono, texto, URL, codigo de WhatsApp y trazabilidad de modificacion.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ENVI_WHAT` | `int` | Identificador interno del envio WhatsApp. |
| `CO_WHAT_TICK` | `int` | Relacion o cabecera del envio WhatsApp. |
| `CO_TICK_CONT` | `int` | Ticket contenedor asociado. |
| `CO_TICK_SERV` | `int` | Ticket de servicio asociado. |
| `NU_TELF` | `varchar(20)` | Numero telefonico de destino. |
| `CO_WHAT` | `varchar(50)` | Codigo o referencia interna del envio. |
| `NO_TEXTO` | `varchar(240)` | Texto del mensaje enviado. |
| `DE_URL` | `text` | URL asociada al envio. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ENVI_WHAT` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es relevante para trazabilidad de envios WhatsApp vinculados a tickets dentro de Legasys. |

---

## Tabla: `H_CAJA_TICK`

### Descripcion funcional
Tabla usada en Legasys para relacionar tickets con registros de Caja. Permite vincular un ticket contenedor con una cabecera de caja y su estado dentro del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CAJA_TICK` | `int` | Identificador interno de la relacion ticket-caja. |
| `CO_TICK_CONT` | `int` | Ticket contenedor asociado. |
| `CO_CABE_CAJA` | `int` | Cabecera de Caja asociada. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CAJA_TICK` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla sirve como puente entre tickets y registros del modulo Caja. |

---

## Tabla: `H_CALC_TEMP`

### Descripcion funcional
Tabla usada en Legasys para almacenar calculos temporales de servicios. Permite guardar cantidades, montos y valores intermedios asociados a un usuario antes de consolidar la operacion final.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CALC_TEMP` | `int` | Identificador interno del calculo temporal. |
| `DE_SERV` | `varchar(190)` | Nombre o descripcion del servicio calculado. |
| `NU_CANT` | `int` | Cantidad considerada en el calculo. |
| `NU_MONT` | `decimal(11,2)` | Monto principal calculado. |
| `NU_REGI` | `decimal(11,2)` | Valor registral o complementario asociado al calculo. |
| `CO_USUA` | `int` | Usuario asociado al calculo temporal. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CALC_TEMP` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla parece usarse como soporte temporal para procesos de calculo o liquidacion dentro de Legasys. |

---

## Tabla: `H_CERT_SUPE`

### Descripcion funcional
Tabla usada en Legasys para registrar informacion de certificados asociados a un ticket de servicio. Permite almacenar persona, apoderado, numero de formato, partida y fechas vinculadas al certificado.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CERT_SUPE` | `bigint` | Identificador interno del certificado. |
| `CO_TICK_SERV` | `bigint` | Ticket de servicio asociado. |
| `CO_TICK_SERV_SUB` | `int` | Subservicio asociado, si aplica. |
| `NO_PERS` | `varchar(200)` | Nombre de la persona asociada al certificado. |
| `DE_OBSE` | `text` | Observaciones del certificado. |
| `NO_APOD` | `varchar(250)` | Nombre del apoderado asociado. |
| `NU_FORM` | `varchar(30)` | Numero de formato o formulario. |
| `FE_EMIS` | `date` | Fecha de emision. |
| `NU_PART` | `varchar(20)` | Numero de partida asociado. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CERT_SUPE` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla parece asociada a certificados especializados dentro de flujos notariales de Legasys. |

---

## Tabla: `H_CIER_CAJA_CHIC`

### Descripcion funcional
Tabla usada en Legasys para registrar aperturas y cierres de caja chica. Permite controlar saldos, gastos, reposiciones, usuarios responsables y estado del cierre.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CIER_CAJA_CHIC` | `int` | Identificador interno del cierre de caja chica. |
| `CO_COMP` | `int` | Codigo de la notaria o compania. |
| `NU_ANIO` | `int` | Anio asociado al registro. |
| `FE_APER` | `date` | Fecha de apertura. |
| `CO_USUA_APER` | `int` | Usuario que abrio la caja chica. |
| `FE_CIER` | `date` | Fecha de cierre. |
| `CO_USUA_CIER` | `int` | Usuario que cerro la caja chica. |
| `NU_SALD_INIC` | `decimal(11,2)` | Saldo inicial. |
| `NU_TOTA_REPO` | `decimal(11,2)` | Total repuesto. |
| `NU_GAST` | `decimal(11,2)` | Total de gastos. |
| `NU_SALD_FINA` | `decimal(11,2)` | Saldo final. |
| `CO_USUA_CREA` | `int` | Usuario que creo el registro. |
| `TS_USUA_CREA` | `datetime` | Fecha y hora de creacion. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `smallint` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CIER_CAJA_CHIC` | Clave principal de la tabla. |
| Referenciada por | `P_CAJA_CHIC` | `CO_CIER_CAJA_CHIC` | La tabla `P_CAJA_CHIC` referencia esta tabla mediante la columna `CO_CIER_CAJA_CHIC`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Es una tabla operativa importante para la administracion de caja chica en Legasys. |
| Funcional | Permite controlar apertura, cierre, gastos, reposiciones y saldos finales. |

---

## Tabla: `H_CLIE_JURI`

### Descripcion funcional
Tabla usada en Legasys para almacenar el detalle juridico de clientes. Complementa a `P_CLIE` con razon social, nombre comercial, partida y otros datos propios de personas juridicas.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CLIE` | `int unsigned` | Identificador del cliente, compartido con `P_CLIE`. |
| `CO_TDOC_IDEN` | `int` | Tipo de documento de identidad o registro asociado. |
| `RZ_SOCI` | `varchar(150)` | Razon social del cliente juridico. |
| `NO_COME` | `varchar(150)` | Nombre comercial del cliente. |
| `NU_PART` | `varchar(20)` | Numero de partida asociado. |
| `IN_EXTR` | `smallint` | Indicador complementario del cliente juridico. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CLIE` | Clave principal de la tabla. |
| Foreign Key | `CO_CLIE` | `CO_CLIE` | Referencia a `P_CLIE.CO_CLIE`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es clave para diferenciar y almacenar la informacion de clientes juridicos en Legasys. |

---

## Tabla: `H_CLIE_MAIL`

### Descripcion funcional
Tabla usada en Legasys para registrar correos electronicos de clientes. Permite asociar uno o varios mails a un cliente con control de estado.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CLIE_MAIL` | `int` | Identificador interno del correo del cliente. |
| `CO_CLIE` | `int` | Cliente asociado al correo. |
| `DE_MAIL` | `varchar(100)` | Correo electronico del cliente. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CLIE_MAIL` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla complementa la informacion de contacto de clientes dentro de Legasys. |

---

## Tabla: `H_CODO`

### Descripcion funcional
Tabla usada en Legasys para registrar codos o campos configurables asociados a documentos de firma y tipos de campo. Forma parte de la estructura dinamica que el sistema utiliza para modelar informacion documental.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CODO` | `int unsigned` | Identificador interno del registro. |
| `CO_TIPO_CAMP` | `int unsigned` | Tipo de campo asociado. |
| `CO_DOCU_FIRM` | `int unsigned` | Documento de firma asociado. |
| `CO_COMP` | `int unsigned` | Codigo de la notaria o compania. |
| `DE_CODO` | `varchar(100)` | Descripcion principal del campo o codo. |
| `NU_ORDE` | `int unsigned` | Orden de visualizacion o procesamiento. |
| `NC_CODO` | `int unsigned` | Codigo numerico complementario. |
| `IN_TIPO_CAMP` | `char(1)` | Indicador complementario del tipo de campo. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `date` | Fecha de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CODO` | Clave principal de la tabla. |
| Foreign Key | `CO_TIPO_CAMP` | `CO_TIPO_CAMP` | Referencia a `A_TIPO_CAMP_type.CO_TIPO_CAMP`. |
| Foreign Key | `CO_DOCU_FIRM` | `CO_DOCU_FIRM` | Referencia a `A_DOCU_FIRM.CO_DOCU_FIRM`. |
| Referenciada por | `R_CODO_KARD` | `CO_CODO` | La tabla `R_CODO_KARD` referencia esta tabla mediante la columna `CO_CODO`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es relevante para la configuracion de campos dinamicos y estructura documental en Legasys. |
| Funcional | `CO_TIPO_CAMP` conecta con el tipo de campo, y `CO_DOCU_FIRM` con el tipo documental de firma. |

---

## Tabla: `H_CONT_PRIC`

### Descripcion funcional
Tabla usada en Legasys para registrar informacion de contratos o contenidos principales asociados a un ticket de servicio. Permite almacenar datos de RUC, razon social, formulario y periodo.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CONT_PRIC` | `int` | Identificador interno del registro. |
| `CO_TICK_SERV` | `int` | Ticket de servicio asociado. |
| `NU_RUC` | `varchar(11)` | Numero de RUC asociado. |
| `NO_RAZO_SOCI` | `varchar(240)` | Razon social asociada. |
| `NU_FORM` | `varchar(20)` | Numero de formulario. |
| `FE_PERI` | `varchar(10)` | Periodo textual asociado. |
| `FE_PERI_INI` | `date` | Fecha de inicio del periodo. |
| `FE_PERI_FIN` | `date` | Fecha de fin del periodo. |
| `FE_PRES` | `date` | Fecha de presentacion. |
| `FE_ACTU` | `datetime` | Fecha de actualizacion o actuacion. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CONT_PRIC` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Parece almacenar informacion complementaria de contenido principal o contractual vinculada a tickets de servicio. |

---

## Tabla: `H_CUEN_BANC`

### Descripcion funcional
Tabla usada en Legasys para registrar cuentas bancarias por notaria y banco. Permite almacenar el numero de cuenta y su tipo para operaciones administrativas o financieras.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CUEN_BANC` | `int` | Identificador interno de la cuenta bancaria. |
| `CO_TIPO_CUEN_BANC` | `int` | Tipo de cuenta bancaria asociado. |
| `CO_COMP` | `int` | Codigo de la notaria o compania. |
| `CO_BANC_CAJA` | `int` | Banco de Caja asociado. |
| `NU_CUEN_BANC` | `varchar(50)` | Numero de cuenta bancaria. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CUEN_BANC` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es relevante para mantenimientos y configuraciones bancarias por notaria dentro de Legasys. |

---

## Tabla: `H_DATO_ENVI`

### Descripcion funcional
Tabla usada en Legasys para registrar datos de envio documental o entrega asociados a un ticket contenedor. Permite almacenar destinatario, tercero, direccion, contacto, tipo documental y datos economicos del envio.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DATO_ENVI` | `int` | Identificador interno del dato de envio. |
| `CO_TICK_CONT` | `int` | Ticket contenedor asociado. |
| `CO_PRES_ENVI_DIST` | `int` | Presentacion o distribucion asociada al envio. |
| `CO_USUA` | `int` | Usuario asociado al registro. |
| `NU_SEMI` | `int` | Numero secuencial asociado. |
| `CO_TIPO_DOCU` | `int` | Tipo de documento asociado. |
| `NO_CLIE` | `varchar(200)` | Nombre del cliente principal. |
| `NO_TIPO_DOCU` | `varchar(200)` | Nombre del tipo de documento principal. |
| `NU_DOCU_CLIE` | `varchar(200)` | Numero de documento del cliente principal. |
| `CO_TIPO_DOCU_TERC` | `int` | Tipo de documento del tercero. |
| `NO_CLIE_TERC` | `varchar(200)` | Nombre del tercero. |
| `NO_TIPO_DOCU_TERC` | `varchar(200)` | Nombre del tipo de documento del tercero. |
| `NU_DOCU_CLIE_TERC` | `varchar(200)` | Numero de documento del tercero. |
| `NO_CLIE_ENVI` | `varchar(100)` | Nombre del destinatario del envio. |
| `NO_TERC_ENVI` | `varchar(100)` | Nombre del tercero destinatario. |
| `DE_DIRE_ENVI` | `varchar(200)` | Direccion de envio. |
| `DE_REFE_ENVI` | `varchar(200)` | Referencia de la direccion de envio. |
| `NU_TELE_ENVI` | `varchar(15)` | Telefono de contacto del envio. |
| `NO_MAIL_ENVI` | `varchar(50)` | Correo de contacto del envio. |
| `NU_PREC_ENVI` | `decimal(15,2)` | Precio del envio. |
| `NO_DIST` | `varchar(50)` | Distrito del envio. |
| `IN_TERC_ENVI` | `int` | Indicador de tercero en el envio. |
| `NU_FOLI` | `varchar(10)` | Numero de folio asociado. |
| `NU_MINU` | `varchar(10)` | Numero de minuta asociado. |
| `IN_PROT` | `int` | Indicador relacionado a protocolo. |
| `IN_TEST` | `int` | Indicador relacionado a testimonio. |
| `DE_OBSE` | `varchar(100)` | Observaciones del envio. |
| `FE_IMPO` | `datetime` | Fecha de impresion o importacion. |
| `CO_USUA_MODI` | `int` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DATO_ENVI` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es relevante para entrega documental, mensajeria o despacho asociado a tickets en Legasys. |
| Funcional | Reune datos del cliente principal, tercero, direccion, documento y costo del envio. |

---

## Tabla: `H_DETA_CAJA`

### Descripcion funcional
Tabla usada en Legasys para registrar el detalle de conceptos cobrados en un comprobante de Caja. Permite almacenar servicio, concepto, cantidades, tarifas, IGV, totales y trazabilidad de modificacion.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DETA_CAJA` | `int unsigned` | Identificador interno del detalle de Caja. |
| `CO_CABE_CAJA` | `int unsigned` | Cabecera de Caja asociada. |
| `CO_PRES_TICK` | `int` | Presupuesto o presentacion del ticket asociada. |
| `CO_SERV_ALTE` | `int unsigned` | Servicio alterno asociado. |
| `NU_SECU` | `int unsigned` | Secuencia interna del detalle. |
| `NU_CANT` | `int unsigned` | Cantidad del detalle. |
| `MO_TARI` | `decimal(12,2)` | Monto tarifario o unitario. |
| `MO_CONC` | `decimal(12,2)` | Monto del concepto. |
| `PO_IGV` | `int unsigned` | Porcentaje de IGV aplicado. |
| `MO_IGV` | `decimal(10,2)` | Monto de IGV aplicado. |
| `MO_TOTA` | `decimal(12,2)` | Monto total del detalle. |
| `NU_CANT_CPTO` | `int` | Cantidad asociada al concepto. |
| `DE_DETA_CAJA` | `varchar(100)` | Nombre del servicio o detalle principal del comprobante. |
| `DE_DETA_CPTO` | `text` | Nombre del concepto o subconcepto detallado. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DETA_CAJA` | Clave principal de la tabla. |
| Foreign Key | `H_DETA_CAJA_ibfk_1` | `CO_CABE_CAJA` | Referencia a `P_CABE_CAJA.CO_CABE_CAJA`. |
| Index | `H_DETA_CAJA_FKIndex1` | `CO_CABE_CAJA` | Indice de apoyo para consultas por cabecera de Caja. |
| Index | `H_DETA_CAJA_index13269` | `CO_SERV_ALTE` | Indice de apoyo para consultas por servicio alterno. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Es una tabla central del modulo Caja porque guarda el detalle economico real de cada comprobante. |
| Funcional | En Legasys, `DE_DETA_CAJA` debe reflejar el nombre del servicio y `DE_DETA_CPTO` el concepto o subconcepto. |
| Funcional | Este detalle es clave para boletas, recibos y comprobantes donde el sistema muestra `servicio - concepto` cuando aplica. |

---

## Tabla: `H_CLIE_NATU`

### Descripcion funcional
Tabla usada en Legasys para almacenar el detalle natural de clientes. Complementa a `P_CLIE` con apellidos, nombres y documento de identidad propios de personas naturales.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CLIE` | `int unsigned` | Identificador del cliente, compartido con `P_CLIE`. |
| `AP_PATE` | `varchar(40)` | Apellido paterno del cliente. |
| `AP_MATE` | `varchar(40)` | Apellido materno del cliente. |
| `NO_CLIE` | `varchar(40)` | Nombre del cliente. |
| `CO_TDOC_IDEN` | `int unsigned` | Tipo de documento de identidad. |
| `NU_DOCU_IDEN` | `varchar(11)` | Numero de documento de identidad. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizo la ultima modificacion. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la ultima modificacion. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CLIE` | Clave principal de la tabla. |
| Foreign Key | `CO_CLIE` | `CO_CLIE` | Referencia a `P_CLIE.CO_CLIE`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es clave para diferenciar y almacenar la informacion de clientes naturales en Legasys. |

---

## Tabla: `H_CLIE_TELF`

### Descripcion funcional
Tabla usada en Legasys para registrar telefonos de clientes. Permite asociar uno o varios numeros telefonicos a un cliente con control de estado.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CLIE_TELF` | `int` | Identificador interno del telefono del cliente. |
| `CO_CLIE` | `int` | Cliente asociado al telefono. |
| `NU_TELF` | `varchar(100)` | Numero telefonico del cliente. |
| `IN_ESTA` | `char(1)` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CLIE_TELF` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla complementa la informacion de contacto de clientes dentro de Legasys. |

---

## Tabla: `H_ERRO_CNL`

### Descripcion funcional
Tabla usada en Legasys para registrar los errores ocurridos durante la comunicación o envío al Colegio de Notarios (CNL). Permite almacenar el detalle del error, el usuario, el servicio afectado y el módulo en el que se originó.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ERRO_CNL` | `int` | Identificador interno del error CNL. |
| `CO_TICK_SERV` | `int` | Ticket de servicio asociado al error. |
| `CO_TICK_CONT` | `int` | Ticket contenedor asociado. |
| `CO_USUA` | `int` | Usuario asociado al evento de error. |
| `DE_ERRO` | `varchar(190)` | Descripción o mensaje del error reportado. |
| `IN_TIPO` | `int` | Tipo o categoría del error. |
| `IN_MODU` | `int` | Módulo donde ocurrió el error. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la última modificación o del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ERRO_CNL` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla sirve para llevar un registro o log de fallos en integraciones con CNL en Legasys, útil para soporte y trazabilidad. |

---

## Tabla: `H_ESCA_RRPP`

### Descripcion funcional
Tabla usada en Legasys para registrar escaneos o imágenes relacionadas a Registros Públicos. Permite asociar una imagen o URL de escaneo a un seguimiento u a una carpeta de ticket.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ESCA_RRPP` | `int` | Identificador interno del escaneo RRPP. |
| `CO_SGMT_ORLC` | `int` | Seguimiento ORLC asociado. |
| `CO_CARP_TICK` | `int` | Carpeta de ticket asociada. |
| `IM_ESCA` | `varchar(100)` | Imagen o nombre de archivo del escaneo. |
| `URL_ESCA` | `varchar(250)` | URL o ruta de acceso al escaneo. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la última modificación. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ESCA_RRPP` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Permite mantener referencias a documentos o escaneos vinculados a trámites de Registros Públicos dentro del sistema. |

---

## Tabla: `H_ESTA_PAGO_LINE`

### Descripcion funcional
Tabla usada en Legasys para registrar el historial de estados de pagos en línea. Permite trazar los cambios de estado de una cabecera de pago y almacenar las respuestas (JSON) del proveedor o pasarela.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_HIST_PAGO_LINE` | `int` | Identificador interno del historial de pago. |
| `CO_CABE_PAGO_LINE` | `int` | Cabecera de pago en línea asociada. |
| `CO_ESTA_PAGO_LINE` | `int` | Estado del pago asociado. |
| `DE_OBSE` | `varchar(500)` | Observaciones del cambio de estado. |
| `TX_JSON` | `longtext` | Payload o respuesta en JSON del estado (ej. respuesta de la pasarela). |
| `CO_USUA_CREA` | `int` | Usuario que creó el registro. |
| `TS_USUA_CREA` | `datetime` | Fecha y hora de creación. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_HIST_PAGO_LINE` | Clave principal de la tabla. |
| Foreign Key | `CO_CABE_PAGO_LINE` | `CO_CABE_PAGO_LINE` | Referencia a `P_CABE_PAGO_LINE.CO_CABE_PAGO_LINE`. |
| Foreign Key | `CO_ESTA_PAGO_LINE` | `CO_ESTA_PAGO_LINE` | Referencia a `A_ESTA_PAGO_LINE.CO_ESTA_PAGO_LINE`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta tabla es fundamental para la trazabilidad de transacciones de pago electrónico, auditando cada respuesta de la pasarela. |

---

## Tabla: `H_FACT_ELEC`

### Descripcion funcional
Tabla usada en Legasys para registrar la información y el estado de la facturación electrónica ante SUNAT. Almacena las respuestas, comprobantes, hash, código de barras y enlaces a los documentos generados (PDF, XML, CDR).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_FACT_ELEC` | `int` | Identificador interno de facturación electrónica. |
| `CO_CABE_CAJA` | `int` | Cabecera de caja asociada. |
| `CO_CABE_NOTA` | `int` | Cabecera de nota de crédito/débito asociada. |
| `NU_SERIE` | `varchar(5)` | Número de serie del comprobante electrónico. |
| `DE_JSON` | `varchar(300)` | Datos en JSON relacionados con la facturación. |
| `NU_NUME` | `int` | Número correlativo del comprobante. |
| `NO_ENLA` | `varchar(200)` | Enlace principal de consulta o documento. |
| `NU_KEY` | `varchar(500)` | Clave, token o identificador del proveedor/SUNAT. |
| `DE_ACEP_SUNA` | `varchar(500)` | Estado o mensaje de aceptación de SUNAT. |
| `DE_DESC_SUNA` | `varchar(500)` | Descripción detallada de respuesta SUNAT. |
| `DE_NOTA_SUNA` | `varchar(500)` | Nota o advertencia devuelta por SUNAT. |
| `DE_RESP_SUNA` | `varchar(500)` | Respuesta general SUNAT. |
| `DE_SOAP_SUNA` | `varchar(500)` | Trama SOAP o identificador de envío. |
| `NU_DIGE_VALU` | `varchar(500)` | Digest Value (Hash del documento). |
| `DE_CODI_BARR` | `varchar(500)` | Código de barras o su representación en texto. |
| `DE_ENLA_PDF` | `varchar(150)` | Enlace directo al archivo PDF. |
| `DE_ENLA_XML` | `varchar(150)` | Enlace directo al archivo XML. |
| `DE_ENLA_CDR` | `varchar(150)` | Enlace directo al CDR (Constancia de Recepción). |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_FACT_ELEC` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Contiene toda la información técnica y de validación necesaria para los comprobantes electrónicos exigidos por SUNAT. |

---

## Tabla: `H_GRUP_RUC`

### Descripcion funcional
Tabla usada en Legasys para agrupar números de RUC o empresas vinculadas a un mismo grupo corporativo o económico.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_GRUP_RUC` | `int` | Identificador interno de la agrupación de RUC. |
| `CO_GRUP` | `int` | Grupo principal al que pertenece el RUC. |
| `NU_RUC` | `varchar(11)` | Número de RUC asociado. |
| `NO_RAZO_SOCI` | `varchar(200)` | Razón social asociada al RUC. |
| `CO_USUA_MODI` | `int` | Usuario que realizó la última modificación. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la última modificación. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_GRUP_RUC` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Sirve para organizar empresas que forman parte de consorcios o grupos empresariales. |

---

## Tabla: `H_JSON_TRAM`

### Descripcion funcional
Tabla clave en Legasys para registrar la trazabilidad e historial de consultas de Legasys IA. Permite almacenar el JSON de respuesta cruda de servicios externos (como Minuta IA o análisis de Medio de Pago), identificadores externos y vincularlo al ticket.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_JSON_TRAM` | `int` | Identificador interno del registro JSON. |
| `CO_COMP` | `int` | Código de la notaría o compañía. |
| `CO_TIPO_API` | `int` | Define el tipo de API (ej: `1` = Minuta IA, `2` = Medio de pago). |
| `CO_TICK_SERV` | `int` | Ticket de servicio asociado. |
| `ID_MINU` | `varchar(30)` | Se reutiliza para guardar el identificador devuelto por el servicio externo (ej. id_consulta o id_escaneo). |
| `DE_JSON` | `text` | Payload JSON crudo con el resultado del análisis o escaneo. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la modificación. |
| `CO_USUA_MODI` | `int` | Usuario que ejecutó la consulta o acción. |
| `IN_ESTA` | `int` | Estado del registro dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_JSON_TRAM` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Es central para el proyecto `LEGASYS IA` en Minutario Digital. `CO_TIPO_API` determina la procedencia y `ID_MINU` guarda el ID del proceso externo. Además, sirve como base para reportes IA. |

---

## Tabla: `H_LOG_API`

### Descripcion funcional
Tabla usada en Legasys como bitácora general para registrar llamadas e interacciones API. Permite almacenar el payload JSON de la consulta, vincular el token de API usado y el ticket contenedor relacionado.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_LOG_API` | `int` | Identificador interno del log de API. |
| `CO_TOKE_API` | `int` | Token API asociado a la petición. |
| `CO_TICK_CONT` | `int` | Ticket contenedor asociado. |
| `NO_JSON_API` | `text` | Payload o contenido JSON de la petición/respuesta API. |
| `IN_TIPO` | `int` | Tipo de evento o categoría de la llamada API. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la transacción o registro. |
| `IN_ESTA` | `int` | Estado del log dentro del sistema. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_LOG_API` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Sirve para auditar la actividad e intercambio de datos con clientes u otros servicios externos que consumen APIs internas. |

---

## Tabla: `H_LOG_FACT`

### Descripcion funcional
Tabla usada en Legasys para registrar eventos simples o logs operativos vinculados estrictamente al proceso de facturación.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_LOG_FACT` | `int` | Identificador interno del log de facturación. |
| `DE_DESC` | `varchar(250)` | Descripción o mensaje del evento de facturación. |
| `CO_USUA_MODI` | `int` | Usuario que generó o estuvo involucrado en el evento. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora del evento. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_LOG_FACT` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Bitácora básica para problemas, advertencias o rastreos rápidos en el flujo de facturación. |

---

## Tabla: `H_MAIL_TICK`

### Descripcion funcional
Tabla usada en Legasys para registrar los correos electrónicos vinculados a un ticket.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_MAIL_TICK` | `int` | Identificador interno del correo de ticket. |
| `CO_TICK_CONT` | `int` | Ticket contenedor asociado. |
| `NU_SEMI` | `int` | Número secuencial asociado. |
| `CO_USUA` | `int` | Usuario asociado al registro. |
| `NO_NOMB` | `varchar(100)` | Nombre asociado al correo. |
| `DE_MAIL` | `varchar(1000)` | Dirección de correo electrónico. |
| `IN_TIPO` | `char(1)` | Tipo de correo o destino. |
| `IN_ESTA` | `char(1)` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_MAIL_TICK` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Permite llevar el registro y trazabilidad de los destinatarios de correo de un ticket contenedor. |

---

## Tabla: `H_MARC_PLAN`

### Descripcion funcional
Tabla usada en Legasys para definir marcadores dinámicos (codos) asociados a plantillas documentales.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_MARC_PLAN` | `int unsigned` | Identificador interno del marcador de plantilla. |
| `CO_PLAN` | `int unsigned` | Plantilla asociada. |
| `CO_CODO` | `int unsigned` | Identificador del codo o campo dinámico asociado. |
| `NO_MARC` | `varchar(50)` | Nombre del marcador en la plantilla (ej: `[[MARCADOR]]`). |
| `NO_COLU` | `varchar(50)` | Nombre de la columna de origen de los datos. |
| `NO_TABL` | `varchar(50)` | Nombre de la tabla de origen de los datos. |
| `NO_COLU_A` | `varchar(50)` | Nombre de la columna alterna o relacionada. |
| `NO_TABL_A` | `varchar(50)` | Nombre de la tabla alterna o relacionada. |
| `TI_DATO` | `char(1)` | Tipo de dato del marcador. |
| `NO_FUNC` | `varchar(160)` | Nombre de función asociada para procesamiento. |
| `IN_ESTA` | `char(1)` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_MARC_PLAN` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Es vital para el motor documental (Twig/DOCX), ya que relaciona un marcador de Word con los datos de una tabla/columna del sistema o con un codo de Legasys. |

---

## Tabla: `H_MOVI_CRED`

### Descripcion funcional
Tabla usada en Legasys para registrar los movimientos financieros relacionados a notas de crédito en Caja.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_MOVI_CRED` | `int unsigned` | Identificador interno del movimiento de crédito. |
| `CO_CABE_CAJA` | `int unsigned` | Cabecera de caja asociada. |
| `MO_NETO` | `decimal(12,2)` | Monto neto del movimiento. |
| `MO_PAGA` | `decimal(12,2)` | Monto pagado o aplicado. |
| `IN_ESTA` | `char(1)` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_MOVI_CRED` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Parte del módulo de caja. Relaciona comprobantes con movimientos de compensación, devoluciones o crédito. |

---

## Tabla: `H_OPCI_SIST`

### Descripcion funcional
Tabla usada en Legasys para configurar las opciones del menú y sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_OPCI_SIST` | `int` | Identificador interno de la opción del sistema. |
| `CO_PRI_OPCI_SIST` | `int` | Opción padre o principal (jerarquía del menú). |
| `NO_ENLA_OPCI_SIST` | `varchar(200)` | Nombre o ruta legacy del enlace. |
| `NO_ENLA_LARA` | `varchar(200)` | Ruta o nombre de ruta para Laravel. |
| `NO_OPCI_SIST` | `varchar(50)` | Nombre visible de la opción en el menú. |
| `DE_ENLA_OPCI_SIST` | `text` | Descripción o icono de la opción. |
| `NU_ORDE` | `smallint` | Orden de visualización de la opción. |
| `NU_MEDI_VENT` | `varchar(10)` | Medidas de la ventana, en interfaces legacy. |
| `IN_TIPO_OPCI` | `char(1)` | Tipo de opción (módulo, enlace externo, popup). |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |
| `CO_USUA_MODI` | `int` | Usuario que realizó la modificación. |
| `IN_ESTA` | `char(1)` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_OPCI_SIST` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Fundamental para el control de acceso y el renderizado dinámico del menú principal del sistema. |

---

## Tabla: `H_OPER_TEMP`

### Descripcion funcional
Tabla temporal utilizada en Legasys para registrar o pre-liquidar operaciones y conceptos antes de ser guardados en el ticket final o en caja.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_OPER_TEMP` | `int unsigned` | Identificador interno de la operación temporal. |
| `CO_SERV_ALTE` | `int unsigned` | Servicio alterno asociado. |
| `CO_CPTO` | `int` | Concepto asociado. |
| `CO_SERV_CPTO_TARI` | `int` | Tarifa de concepto de servicio asociada. |
| `NU_CANT` | `int unsigned` | Cantidad del concepto. |
| `NU_CAJA` | `int` | Caja asociada (si aplica). |
| `NU_BIOM_RENI` | `int` | Número de identificaciones biométricas (RENIEC). |
| `MO_PRES` | `decimal(10,2)` | Monto de presupuesto parcial. |
| `DE_DETA` | `varchar(50)` | Detalle o glosa de la operación. |
| `MO_TARI` | `decimal(10,2)` | Tarifa unitaria. |
| `FE_CREA_TICK` | `date` | Fecha de simulación/creación. |
| `CO_USUA` | `int` | Usuario que está realizando la simulación u operación. |
| `NU_SEMI` | `int unsigned` | Número secuencial interno. |
| `NU_SUB_SEMI` | `int` | Subnúmero secuencial. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_OPER_TEMP` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Muy utilizada en flujos de "Pre-liquidación" o presupuestos donde la información debe visualizarse o calcularse sin estar vinculada a un ticket definitivo. |

---

## Tabla: `H_PIC_PRTC`

### Descripcion funcional
Tabla usada en Legasys para registrar participantes en el módulo PIC (Procesos Integrales o carpetas PIC). Funciona como tabla cabecera para derivar si el participante es natural (`H_PIC_PRTC_NATU`), jurídico (`H_PIC_PRTC_JURI`) o representante (`H_PIC_REPR`).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PIC_PRTC` | `int unsigned` | Identificador interno del participante PIC. |
| `CO_PIC` | `int unsigned` | Proceso o carpeta PIC asociada. |
| `CO_TIPO_PRTC` | `int unsigned` | Tipo de participación (ej. solicitante, interviniente). |
| `CO_TIPO_PERS` | `int unsigned` | Tipo de persona (natural o jurídica). |
| `NC_PIC_PRTC` | `varchar(100)` | Código o identificador alternativo del participante. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |
| `IN_ESTA` | `char(1)` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PIC_PRTC` | Clave principal de la tabla. |
| Foreign Key | `CO_PIC` | `CO_PIC` | Referencia a `P_PIC.CO_PIC`. |
| Referenciada por | `H_PIC_PRTC_JURI` | `CO_PIC_PRTC` | Es referenciada por `H_PIC_PRTC_JURI.CO_PIC_PRTC`. |
| Referenciada por | `H_PIC_PRTC_NATU` | `CO_PIC_PRTC` | Es referenciada por `H_PIC_PRTC_NATU.CO_PIC_PRTC`. |
| Referenciada por | `H_PIC_REPR` | `CO_PIC_PRTC` | Es referenciada por `H_PIC_REPR.CO_PIC_PRTC`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Actúa de manera polimórfica junto con sus tablas hijas. Si `CO_TIPO_PERS` determina que es persona jurídica, se debe leer la información extendida en `H_PIC_PRTC_JURI`. |

---

## Tabla: `H_PIC_PRTC_JURI`

### Descripcion funcional
Tabla que almacena la información específica de un participante jurídico en el módulo PIC. Se conecta uno a uno con `H_PIC_PRTC`.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PIC_PRTC` | `int unsigned` | Identificador del participante PIC (Clave y FK hacia `H_PIC_PRTC`). |
| `NU_RUC` | `varchar(11)` | Número de RUC de la persona jurídica. |
| `RZ_SOCI` | `varchar(150)` | Razón social de la empresa. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |
| `IN_ESTA` | `char(1)` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PIC_PRTC` | Clave principal de la tabla. |
| Foreign Key | `CO_PIC_PRTC` | `CO_PIC_PRTC` | Referencia a `H_PIC_PRTC.CO_PIC_PRTC`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Extiende a `H_PIC_PRTC` proporcionando atributos de negocio propios de empresas. |

---

## Tabla: `H_PIC_PRTC_NATU`

### Descripcion funcional
Tabla que almacena la información específica de un participante natural (persona) en el módulo PIC. Se conecta uno a uno con `H_PIC_PRTC`.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PIC_PRTC` | `int unsigned` | Identificador del participante PIC (Clave y FK hacia `H_PIC_PRTC`). |
| `AP_PATE` | `varchar(50)` | Apellido paterno. |
| `AP_MATE` | `varchar(50)` | Apellido materno. |
| `NO_PRTC` | `varchar(50)` | Nombres de la persona natural. |
| `CO_TDOC_IDEN` | `int unsigned` | Tipo de documento de identidad. |
| `NU_DOCU_IDEN` | `varchar(11)` | Número de documento de identidad. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |
| `IN_ESTA` | `char(1)` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PIC_PRTC` | Clave principal de la tabla. |
| Foreign Key | `CO_PIC_PRTC` | `CO_PIC_PRTC` | Referencia a `H_PIC_PRTC.CO_PIC_PRTC`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Extiende a `H_PIC_PRTC` con atributos biográficos de la persona (nombres, apellidos, documento). |

---

## Tabla: `H_PODE_FUER_REGI`

### Descripcion funcional
Tabla usada en Legasys para registrar información de poderes, pensiones o trámites especiales que deben procesarse fuera del ámbito registral habitual o bajo reglas de poderes fuera de registro.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PODE_FUER_REGI` | `int unsigned` | Identificador interno del poder/trámite especial. |
| `CO_TICK_SERV` | `bigint unsigned` | Ticket de servicio asociado. |
| `CO_TICK_SERV_SUB` | `int` | Subservicio asociado. |
| `FE_EMIS` | `date` | Fecha de emisión. |
| `MO_PENS` | `decimal(15,2)` | Monto de pensión (si aplica). |
| `FE_TERM` | `date` | Fecha de término o vigencia. |
| `NU_PLAZ` | `varchar(20)` | Plazo de vigencia (texto). |
| `DE_OBSE` | `text` | Observaciones especiales. |
| `CO_ASEG` | `varchar(12)` | Código de asegurado o número referencial. |
| `MO_LACT` | `decimal(15,2)` | Monto por lactancia. |
| `MO_SEPE` | `decimal(15,2)` | Monto por sepelio. |
| `MO_MATE` | `decimal(15,2)` | Monto por maternidad. |
| `DE_PRES` | `varchar(200)` | Descripción de la presentación o prestador. |
| `NU_PRES` | `int(10) unsigned zerofill` | Número secuencial o de presentación. |
| `CO_USUA_MODI` | `int(10) unsigned zerofill` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PODE_FUER_REGI` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Guarda metadatos vitales para trámites notariales específicos como cobro de pensiones o subsidios por EsSalud y poderes para fines previsionales. |

---

## Tabla: `H_PRES_TICK`

### Descripcion funcional
Tabla usada en Legasys para guardar el detalle del presupuesto y la liquidación vinculada a un ticket de servicio en Operaciones o Legal. Registra los importes a cobrar, los conceptos liquidados y si ya fueron pagados en caja.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PRES_TICK` | `int unsigned` | Identificador interno del presupuesto/liquidación del ticket. |
| `CO_TICK_SERV` | `int unsigned` | Ticket de servicio asociado. |
| `CO_TICK_CONT` | `int` | Ticket contenedor asociado. |
| `CO_TIPO_CPTO` | `int unsigned` | Tipo de concepto. |
| `CO_CPTO` | `int` | Concepto asociado en la liquidación. |
| `MO_IMPO_TICK` | `decimal(14,2)` | Monto de importe total liquidado. |
| `MO_TRAN_TICK` | `decimal(14,2)` | Monto transaccional liquidado. |
| `IN_PAGO` | `char(1)` | Indicador de si el concepto ya fue pagado. |
| `FE_PAGO` | `date` | Fecha en la que fue cobrado en caja. |
| `NU_CANT` | `int unsigned` | Cantidad del concepto liquidado. |
| `NU_BIOM_RENI` | `int` | Número de identificaciones biométricas (RENIEC) contabilizadas. |
| `CO_SERV_CPTO_TARI` | `int unsigned` | Referencia a la relación servicio-concepto-tarifa (R_SERV_CPTO_TARI). |
| `DE_DETA_CPTO` | `varchar(100)` | Glosa o detalle textual del concepto. |
| `DE_DETA_CAJA` | `varchar(100)` | Glosa o detalle utilizado para caja. |
| `IN_SUSP` | `int` | Indicador de suspensión. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que modificó la liquidación. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |
| `IN_ESTA` | `char(1)` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PRES_TICK` | Clave principal de la tabla. |
| Foreign Key | `CO_TICK_SERV` | `CO_TICK_SERV` | Referencia a `R_TICK_SERV.CO_TICK_SERV`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Es el puente crítico entre el Kardex (Trámite) y la Caja. Representa la "Liquidación" del ticket. Según las reglas del módulo Legal, cuando un kardex cambia de servicio base, sus registros en `H_PRES_TICK` pasan a `IN_ESTA = 0`. |

---

## Tabla: `H_PRTC_DIRE`

### Descripcion funcional
Tabla usada en Legasys para almacenar las direcciones asociadas a un participante.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PRTC_DIRE` | `int` | Identificador interno de la dirección del participante. |
| `CO_TIPO_DIRE` | `int unsigned` | Tipo de dirección (ej: Domicilio, Fiscal, etc.). |
| `CO_TIPO_RESI` | `int` | Tipo de residencia. |
| `CUP` | `int unsigned` | Código Único de Participante asociado. |
| `NS_DIRE` | `int unsigned` | Número secuencial de la dirección para el CUP. |
| `CO_UBIG` | `varchar(6)` | Ubigeo de la dirección. |
| `DE_DIRE` | `varchar(200)` | Dirección completa. |
| `NU_TELF` | `varchar(20)` | Número de teléfono asociado a la dirección. |
| `DE_MAIL` | `varchar(50)` | Correo electrónico de contacto. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que realizó la última modificación. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de la última modificación. |
| `IN_ESTA` | `char(1)` | Estado del registro. |
| `IN_VIP_DIRE` | `int` | Indicador de dirección destacada o principal. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PRTC_DIRE` | Clave principal de la tabla. |
| Foreign Key | `CO_TIPO_DIRE` | `CO_TIPO_DIRE` | Referencia a `A_TIPO_DIRE_type.CO_TIPO_DIRE`. |
| Foreign Key | `CUP` | `CUP` | Referencia a `P_PRTC.CUP`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Un participante (CUP) puede tener múltiples direcciones. El sistema suele considerar la de `NS_DIRE = 1` o `IN_VIP_DIRE` como principal. |

---

## Tabla: `H_PRTC_JURI`

### Descripcion funcional
Tabla usada en Legasys para almacenar la información de atributos específicos de un participante jurídico (empresa/entidad). Extiende el registro base de `P_PRTC`.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PRTC_JURI` | `int unsigned` | Identificador interno. |
| `CO_TIPO_EMPR` | `int unsigned` | Tipo de empresa (S.A.C., E.I.R.L., etc.). |
| `CO_NACI` | `int unsigned` | Nacionalidad de la empresa. |
| `CUP` | `int unsigned` | Código Único de Participante asociado. |
| `CO_TIPO_BENE_JURI` | `int` | Tipo de beneficiario jurídico. |
| `CO_TIPO_PERS_UIF` | `int` | Tipo de persona para UIF. |
| `CO_PAIS_NACI` | `int` | País de constitución. |
| `CO_PAIS_RESI` | `int` | País de residencia comercial. |
| `NS_PRTC` | `int` | Número secuencial del participante. |
| `RZ_SOCI` | `varchar(500)` | Razón Social. |
| `NU_RUC` | `varchar(20)` | Número de RUC. |
| `NU_PART` | `varchar(50)` | Número de partida registral. |
| `ID_NACI` | `char(1)` | Identificador de nacionalidad. |
| `CO_TIPO_CIIU` | `int` | Código CIIU (Actividad Económica). |
| `DE_OBJ_SOC` | `varchar(40)` | Objeto social principal. |
| `CO_OFIC_REGI_SID` | `int` | Oficina registral de inscripción. |
| `CO_ASEV_OFIC` | `int` | Auxiliar oficina (Cumplimiento/UIF). |
| `CO_ASEV_RESI` | `int` | Auxiliar residencia. |
| `CO_ASEV_OBLI` | `int` | Auxiliar obligados. |
| `CO_ASEV_FAMI` | `int` | Auxiliar familiar. |
| `CO_ZONA_REGI` | `int unsigned` | Zona registral. |
| `CO_ORIG_UIF` | `int` | Origen de fondos UIF. |
| `DE_ORIG_UIF` | `varchar(100)` | Detalle del origen de fondos. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |
| `IN_ESTA` | `char(1)` | Estado del registro. |
| `IN_VIP_PRTC` | `int` | Indicador de participante frecuente/VIP. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PRTC_JURI` | Clave principal de la tabla. |
| Foreign Key | `CO_TIPO_EMPR` | `CO_TIPO_EMPR` | Referencia a `A_TIPO_EMPR_type.CO_TIPO_EMPR`. |
| Foreign Key | `CO_NACI` | `CO_NACI` | Referencia a `A_NACI_type.CO_NACI`. |
| Foreign Key | `CUP` | `CUP` | Referencia a `P_PRTC.CUP`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Mantiene la data corporativa y de cumplimiento regulatorio (UIF) de las personas jurídicas que participan en trámites. |

---

## Tabla: `H_PRTC_NATU`

### Descripcion funcional
Tabla usada en Legasys para almacenar la información de atributos específicos de un participante natural. Extiende el registro base de `P_PRTC`.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PRTC_NATU` | `int` | Identificador interno. |
| `CO_DETA_RENI` | `int` | Referencia a consulta RENIEC. |
| `CO_ESTA_CIVI` | `int unsigned` | Estado Civil. |
| `CO_INDI_OCUP` | `int unsigned` | Ocupación principal. |
| `CO_INDI_GENE` | `int unsigned` | Género / Sexo. |
| `CUP` | `int unsigned` | Código Único de Participante asociado. |
| `CO_TDOC_IDEN` | `int unsigned` | Tipo de documento de identidad. |
| `CO_TIPO_PERS_UIF` | `int` | Tipo de persona para UIF. |
| `CO_INDI_PEP` | `int` | Indicador de Persona Expuesta Políticamente (PEP). |
| `DE_PEP` | `varchar(200)` | Detalle PEP. |
| `NS_PRTC` | `int unsigned` | Número secuencial del participante. |
| `NU_DOCU_IDEN` | `varchar(25)` | Número de documento de identidad. |
| `AP_PATE` | `varchar(50)` | Apellido paterno. |
| `AP_MATE` | `varchar(50)` | Apellido materno. |
| `NO_PERS` | `varchar(120)` | Nombres. |
| `DE_OCUP` | `varchar(250)` | Descripción de la ocupación. |
| `DE_PROF` | `varchar(200)` | Descripción de la profesión. |
| `DE_MAIL` | `varchar(100)` | Correo electrónico de contacto. |
| `DE_OBSE` | `varchar(100)` | Observaciones. |
| `CUP_CONY` | `int unsigned` | CUP del cónyuge. |
| `NS_CUP_CONY` | `int unsigned` | Secuencia del cónyuge. |
| `NS_DIRE_CONY` | `int unsigned` | Secuencia de la dirección del cónyuge. |
| `CUP_RUEG` | `bigint` | CUP del firmante a ruego (si aplica). |
| `NS_CUP_RUEG` | `int unsigned` | Secuencia del ruego. |
| `NS_DIRE_RUEG` | `int unsigned` | Secuencia de la dirección del ruego. |
| `CO_TIPO_INCA` | `int unsigned` | Tipo de incapacidad. |
| `NU_PART` | `varchar(50)` | Número de partida (ej. para representantes naturales o patrimonio familiar). |
| `CO_ZONA_REGI` | `int unsigned` | Zona registral. |
| `NU_ASIE` | `varchar(10)` | Asiento registral. |
| `DE_CARG` | `varchar(80)` | Cargo (si aplica). |
| `DE_NACI` | `varchar(70)` | Nacionalidad. |
| `IN_FIRM` | `char(1)` | Indicador de si firma (para impedimentos). |
| `IN_BIEN_SEPA` | `char(1)` | Indicador de separación de bienes. |
| `NU_TELE_MOVI` | `varchar(50)` | Teléfono móvil. |
| `NU_RUC` | `varchar(11)` | Número de RUC (si emite recibos/facturas). |
| `CO_PAIS_EMIS` | `int` | País emisor del documento. |
| `CO_PAIS_NATU` | `int` | País de nacimiento. |
| `CO_PAIS_RESI` | `int` | País de residencia. |
| `FE_NACI_UIF` | `date` | Fecha de nacimiento. |
| `CO_CARG_SUNA` | `smallint` | Cargo SUNAT. |
| `CO_TIPO_OCUP` | `int` | Tipo de ocupación. |
| `CO_TIPO_PROF` | `int` | Tipo de profesión. |
| `CO_TIPO_CARG` | `int` | Tipo de cargo. |
| `NO_TIPO_CARG` | `varchar(100)` | Nombre del cargo. |
| `DE_INST_UIF` | `varchar(120)` | Institución (PEP). |
| `CO_ASEV_RESI` | `int` | Auxiliar residencia UIF. |
| `CO_ASEV_OBLI` | `int` | Auxiliar obligados UIF. |
| `CO_ASEV_OFIC` | `int` | Auxiliar oficina UIF. |
| `NO_CONY` | `varchar(50)` | Nombres del cónyuge. |
| `AP_PATE_CONY` | `varchar(50)` | Apellido paterno cónyuge. |
| `AP_MATE_CONY` | `varchar(50)` | Apellido materno cónyuge. |
| `CO_ORIG_UIF` | `int` | Origen de fondos UIF. |
| `DE_ORIG_UIF` | `varchar(150)` | Detalle del origen de fondos UIF. |
| `CO_ASEV_DECL` | `int` | Auxiliares UIF. |
| `CO_ASEV_HABI` | `int` | Auxiliares UIF. |
| `CO_ASEV_IMPU` | `int` | Auxiliares UIF. |
| `CO_ASEV_FAMI` | `int` | Auxiliares UIF. |
| `CO_ASEV_YO` | `int` | Auxiliares UIF. |
| `NO_NOMB_FAMI` | `varchar(100)` | Nombres de familiar (PEP). |
| `NO_CARG_FAMI` | `varchar(50)` | Cargo de familiar (PEP). |
| `CO_PAIS_FAMI` | `int` | País de familiar. |
| `NU_BIOM_RENI` | `int` | Número de veces con biometría. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |
| `IN_ESTA` | `char(1)` | Estado del registro. |
| `IN_VIP_PRTC` | `int` | Indicador VIP/Frecuente. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PRTC_NATU` | Clave principal de la tabla. |
| Foreign Key | `CO_ESTA_CIVI` | `CO_ESTA_CIVI` | Referencia a `A_ESTA_CIVI.CO_ESTA_CIVI`. |
| Foreign Key | `CO_INDI_OCUP` | `CO_INDI_OCUP` | Referencia a `A_INDI_OCUP_type.CO_INDI_OCUP`. |
| Foreign Key | `CO_INDI_GENE` | `CO_INDI_GENE` | Referencia a `A_INDI_GENE_type.CO_INDI_GENE`. |
| Foreign Key | `CUP` | `CUP` | Referencia a `P_PRTC.CUP`. |
| Foreign Key | `CO_TDOC_IDEN` | `CO_TDOC_IDEN` | Referencia a `A_TDOC_IDEN.CO_TDOC_IDEN`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Según las reglas recientes (AGENTS.md), los representantes naturales también persisten su sexo/género en `CO_INDI_GENE` de esta tabla. |

---

## Tabla: `H_PRTC_TICK`

### Descripcion funcional
Tabla usada en Legasys para relacionar o cruzar participantes (`CO_PRTC_TRAM`) con un ticket contenedor/servicio y definir al firmante principal.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PRTC_TICK` | `int` | Identificador interno. |
| `CO_RELA_PRTC` | `int unsigned` | Relación del participante. |
| `CO_TICK_SERV` | `int unsigned` | Ticket de servicio asociado. |
| `CO_TIPO_PRTC` | `int unsigned` | Tipo de participación. |
| `CO_PRTC_TRAM` | `int unsigned` | Participante en el trámite. |
| `CO_USUA_FIRM` | `int unsigned` | Usuario o sistema asociado a la firma. |
| `CUP` | `int unsigned` | Código Único de Participante asociado. |
| `NS_PRTC` | `int unsigned` | Número secuencial del participante. |
| `NO_CORT` | `varchar(100)` | Nombre corto o referencia. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PRTC_TICK` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Ayuda a relacionar el flujo de participantes y sus calidades dentro de un servicio específico. |

---

## Tabla: `H_REPO_ESTA`

### Descripcion funcional
Tabla usada en Legasys para configurar o parametrizar el orden y módulo de estados de reportes dentro del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_REPO_ESTA` | `int` | Identificador del reporte de estado. |
| `CO_SERV_CONT` | `varchar(500)` | Referencia de los servicios o contenedores abarcados. |
| `DE_REPO_ESTA` | `varchar(100)` | Descripción o nombre del estado de reporte. |
| `CO_MODU` | `int` | Módulo del sistema asociado. |
| `NU_ORDE` | `int` | Orden en el cual se debe presentar. |
| `IN_ESTA` | `char(1)` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_REPO_ESTA` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Sirve para categorizar o estructurar filtros de reportes gerenciales según estados. |

---

## Tabla: `H_REPO_PRIC`

### Descripcion funcional
Tabla usada en Legasys para guardar registros temporales o reportes consolidados vinculados al contenido principal (`CO_CONT_PRIC`).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_REPO_PRIC` | `int` | Identificador interno. |
| `CO_CONT_PRIC` | `int` | Referencia al contenido principal. |
| `CO_TICK_SERV` | `int` | Ticket de servicio asociado. |
| `FE_REPO_PRIC` | `date` | Fecha del reporte. |
| `CO_USUA_MODI` | `int` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |
| `IN_ESTA` | `int` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_REPO_PRIC` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Parte de la generación y exportación de reportes de contenido notarial. |

---

## Tabla: `H_REPR_SUB`

### Descripcion funcional
Tabla usada en Legasys para registrar sub-representaciones o apoderamientos en cadena.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_REPR_SUB` | `int` | Identificador interno. |
| `CUP` | `int` | CUP del representado o delegante. |
| `CUP_REPR` | `int` | CUP del sub-representante o delegado. |
| `CO_USUA_MODI` | `int` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |
| `IN_ESTA` | `int` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_REPR_SUB` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Aborda la casuística donde un representante legal designa a otro representante (ej. sub-apoderados). |

---

## Tabla: `H_REPR_TRAM`

### Descripcion funcional
Tabla usada en Legasys para registrar los representantes legales o apoderados que actúan en nombre de un participante específico en un trámite o ticket.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_REPR_TRAM` | `int unsigned` | Identificador interno. |
| `CO_PRTC_TRAM` | `int unsigned` | Participante principal dentro del trámite al cual se representa. |
| `CUP_REPR` | `int unsigned` | CUP del representante. |
| `NS_CUP_REPR` | `int unsigned` | Secuencia del representante. |
| `NS_DIRE_REPR` | `int unsigned` | Dirección del representante. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_REPR_TRAM` | Clave principal de la tabla. |
| Foreign Key | `CO_PRTC_TRAM` | `CO_PRTC_TRAM` | Referencia a `R_PRTC_TRAM.CO_PRTC_TRAM`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Crucial en flujos donde personas jurídicas o naturales incapacitadas necesitan que un tercero firme y actúe por ellos en el trámite. |

---

## Tabla: `H_REPR_TRAM_VIP`

### Descripcion funcional
Tabla usada en Legasys para mantener el historial o designaciones de representantes frecuentes (VIP) vinculados a un CUP corporativo o natural para facilitar autocompletados en futuros trámites.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PRTC_TRAM_VIP` | `int` | Identificador interno. |
| `CUP` | `int` | CUP principal (ej. el banco o la constructora). |
| `CUP_REPR` | `int` | CUP del representante habitual. |
| `NS_CUP_REPR` | `int` | Secuencia. |
| `NS_DIRE_REPR` | `int` | Dirección habitual del representante. |
| `IN_ESTA` | `int` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PRTC_TRAM_VIP` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Mejora el UX permitiendo que en la carga de representantes para grandes empresas el sistema proponga apoderados previamente configurados. |

---

## Tabla: `H_REQU_SERV`

### Descripcion funcional
Tabla usada en Legasys para registrar los requisitos documentales (checklist) asociados a un servicio notarial.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_REQU_SERV` | `int unsigned` | Identificador interno. |
| `CO_COMP` | `int unsigned` | Compañía / Notaría. |
| `CO_SERV` | `int unsigned` | Servicio al cual se asocia el requisito. |
| `CO_REQU` | `int` | Código del requisito (documento necesario). |
| `NU_ORDE` | `int unsigned` | Orden de visualización del requisito. |
| `IN_ESTA` | `char(1)` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_REQU_SERV` | Clave principal de la tabla. |
| Foreign Key | `CO_COMP` | `CO_COMP` | Referencia a `A_COMP.CO_COMP`. |
| Foreign Key | `CO_SERV` | `CO_SERV` | Referencia a `P_SERV.CO_SERV`. |
| Foreign Key | `CO_REQU` | `CO_REQU` | Referencia a `A_REQU.CO_REQU`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Usado para indicar a los clientes o asistentes qué documentos (ej: Partida de matrimonio, Copia de DNI) deben presentar para ingresar un trámite específico. |

---

## Tabla: `H_SALD_TRAM`

### Descripcion funcional
Tabla usada en Legasys para llevar el control acumulado de los balances (Saldos) asociados a un trámite notarial. Contiene los totales de presupuesto, facturado, cancelado y saldo a favor o deudor en distintos ámbitos (Notaría, Registral, SUNAT).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_SALD_TRAM` | `int` | Identificador interno del saldo del trámite. |
| `CO_TICK_SERV` | `int` | Ticket de servicio asociado (Kardex). |
| `CO_TICK_CONT` | `int` | Ticket contenedor asociado. |
| `MO_PRES_NOTA` | `decimal(11,2)` | Monto de presupuesto (Honorarios Notariales). |
| `MO_FACT_NOTA` | `decimal(11,2)` | Monto facturado (Honorarios Notariales). |
| `MO_CANC_NOTA` | `decimal(11,2)` | Monto cancelado/pagado (Honorarios Notariales). |
| `MO_SALD_NOTA` | `decimal(11,2)` | Saldo pendiente (Honorarios Notariales). |
| `MO_PRES_REGI` | `decimal(11,2)` | Monto de presupuesto (Derechos Registrales). |
| `MO_FACT_REGI` | `decimal(11,2)` | Monto facturado (Derechos Registrales). |
| `MO_CANC_REGI` | `decimal(11,2)` | Monto cancelado/pagado (Derechos Registrales). |
| `MO_SALD_REGI` | `decimal(11,2)` | Saldo pendiente (Derechos Registrales). |
| `MO_INGR_SUNA` | `decimal(11,2)` | Montos de ingreso para pagos SUNAT. |
| `MO_EGRE_SUNA` | `decimal(11,2)` | Montos de egreso (pagos ejecutados) en SUNAT. |
| `MO_SALD_SUNA` | `decimal(11,2)` | Saldo retenciones/pagos SUNAT. |
| `IN_ESTA` | `int` | Estado del registro. |
| `CO_USUA_MODI` | `int` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_SALD_TRAM` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Importantísimo para evitar la facturación por debajo de lo cobrado o el cierre de trámites con saldos deudores en caja. Agrupa conceptos según su naturaleza económica (Notarial vs Registral). |

---

## Tabla: `H_SERV_ALTE`

### Descripcion funcional
Tabla usada en Legasys para registrar los "servicios alternos" o alias de un servicio principal.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_SERV_ALTE` | `bigint` | Identificador interno del servicio alterno. |
| `CO_SERV` | `int unsigned` | Servicio principal base asociado. |
| `DE_SERV_ALTE` | `varchar(150)` | Descripción o nombre del servicio alterno. |
| `CO_COMP` | `int unsigned` | Compañía o notaría. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |
| `IN_ESTA` | `char(1)` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_SERV_ALTE` | Clave principal de la tabla. |
| Foreign Key | `CO_SERV` | `CO_SERV` | Referencia a `P_SERV.CO_SERV`. |
| Referenciada por | `R_TICK_SERV` | `CO_SERV_ALTE` | Es referenciada por `R_TICK_SERV.CO_SERV_ALTE`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Permite tener variantes visibles de un servicio que conservan las mismas reglas base. El servicio alterno se persiste en el kardex y puede cambiarse sin resetear la data siempre que el servicio base (`CO_SERV`) sea el mismo. |

---

## Tabla: `H_SGMT_CALIF`

### Descripcion funcional
Tabla usada en Legasys para registrar el historial de observaciones y calificaciones de un seguimiento o trámite.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_SGMT_CALIF` | `int unsigned` | Identificador interno. |
| `CO_SITU_TRAM` | `int unsigned` | Situación de trámite asociada. |
| `CO_TICK_SERV` | `int unsigned` | Ticket de servicio. |
| `NU_SECU` | `int unsigned` | Secuencia de calificación. |
| `DE_OBSE` | `text` | Texto de la observación o calificación. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que modificó. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_SGMT_CALIF` | Clave principal de la tabla. |
| Foreign Key | `CO_SITU_TRAM` | `CO_SITU_TRAM` | Referencia a `A_SITU_TRAM_type.CO_SITU_TRAM`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Sirve para dejar registro de las distintas calificaciones (ej. observados o tachas) que un trámite pueda recibir durante su flujo notarial o registral. |

---

## Tabla: `H_SGMT_LOG`

### Descripcion funcional
Tabla usada en Legasys para mantener una bitácora técnica y de auditoría detallada (logs a nivel de sistema).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_SGMT_LOG` | `int` | Identificador interno. |
| `CO_USUA` | `int` | Usuario asociado al log. |
| `NO_TABL` | `varchar(20)` | Nombre de la tabla afectada. |
| `CO_INDI_TABL` | `int` | Indicador o registro afectado de la tabla. |
| `NU_IP` | `varchar(20)` | Dirección IP de la solicitud. |
| `FE_SGMT_LOG` | `datetime` | Fecha y hora del log. |
| `DE_SGMT_LOG` | `text` | Detalle o mensaje técnico del log. |
| `DE_NOMB_ARCH` | `varchar(200)` | Nombre del archivo o script que originó el log. |
| `NU_LINE_ARCH` | `int` | Línea de código fuente. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_SGMT_LOG` | Clave principal de la tabla. |
| Foreign Key | `CO_USUA` | `CO_USUA` | Referencia a `P_USUA.CO_USUA`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Destinada a diagnóstico de errores y auditorías granulares (incluyendo archivo y línea de código fuente) de transacciones importantes en el seguimiento. |

---

## Tabla: `H_SGMT_ORLC`

### Descripcion funcional
Tabla usada en Legasys para llevar el control principal del "Seguimiento en Oficinas Registrales (ORLC)". Almacena el número de título registral, partida, montos liquidados, devoluciones, tachas e información financiera registral del trámite.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_SGMT_ORLC` | `int unsigned` | Identificador interno. |
| `CO_TITU_BOT` | `int` | Código del bot de extracción registral. |
| `CO_OFIC_REGI` | `int unsigned` | Oficina Registral. |
| `CO_SITU_TRAM` | `int unsigned` | Situación del trámite. |
| `CO_TICK_SERV` | `int unsigned` | Ticket de servicio. |
| `CO_VENT_RRPP` | `int` | Ventanilla SUNARP/RRPP. |
| `CO_TIPO_TERC` | `int` | Tipo de tercero asociado. |
| `CO_CARP_TICK` | `int` | Carpeta asociada al ticket. |
| `NU_CANT_TERC` | `int` | Cantidad de terceros. |
| `NU_SECU` | `int unsigned` | Secuencia. |
| `NU_TITU` | `varchar(20)` | Número de título registral. |
| `FE_SITU` | `date` | Fecha de la situación actual. |
| `NO_RGST` | `varchar(100)` | Nombre del registrador. |
| `NU_PART` | `varchar(50)` | Número de partida registral. |
| `NU_ASIE` | `varchar(20)` | Asiento registral. |
| `FE_VENC` | `date` | Fecha de vencimiento. |
| `FE_ACCI` | `date` | Fecha de acción. |
| `MO_LIQU` | `decimal(14,2)` | Monto liquidado en RRPP. |
| `DE_OBSE` | `varchar(3000)` | Observaciones. |
| `DE_MENS_CLIE` | `text` | Mensaje al cliente. |
| `FE_ULTI_SUBS` | `date` | Fecha de última subsanación. |
| `AA_TITU` | `varchar(4)` | Año del título. |
| `MO_DEVO` | `decimal(14,2)` | Monto de devolución. |
| `MO_MAYO_DERE` | `decimal(14,2)` | Monto de mayor derecho. |
| `FE_DEVO_NOTA` | `date` | Fecha de devolución notarial. |
| `FE_DEVO_TACH` | `date` | Fecha de devolución por tacha. |
| `NU_CHEQ_BANC` | `varchar(30)` | Número de cheque bancario. |
| `MO_PRES` | `decimal(14,2)` | Monto de presupuesto registral. |
| `MO_INSC` | `decimal(14,2)` | Monto de inscripción. |
| `CO_REGI_SUNA` | `int unsigned` | Referencia registral de SUNARP/SUNAT. |
| `MO_TACH` | `decimal(14,2)` | Monto por tacha. |
| `FE_CALI_REGI` | `date` | Fecha de calificación. |
| `DE_RECI_SUNA` | `varchar(30)` | Recibo de SUNARP/SUNAT. |
| `NO_SERV_REGI` | `varchar(200)` | Nombre del servicio registral. |
| `IM_ESCA` | `varchar(50)` | Imagen escaneada. |
| `IM_ESQU_SUNA` | `longblob` | Esquema/documento de SUNARP. |
| `IN_INFO_USUA` | `char(1)` | Indicador de información al usuario. |
| `NU_DIAS_ALTE` | `int` | Días alternos. |
| `FE_INFO_USUA` | `datetime` | Fecha de información al usuario. |
| `IN_REGI_REVI` | `int` | Indicador de revisión. |
| `FE_INIC_TRAM_CHEQ` | `date` | Fecha de inicio cheque. |
| `NO_TITU_TRAS` | `varchar(20)` | Título de traslación. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que modificó. |
| `IN_MODU` | `int` | Módulo. |
| `IN_CTRL` | `int` | Indicador de control. |
| `IN_TIVE` | `int` | Indicador de tipo de ventanilla. |
| `IN_ORDE_GIRO` | `int` | Orden de giro. |
| `IN_ESTA` | `char(1)` | Estado del registro. |
| `IN_API` | `int` | Indicador si proviene de API. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_SGMT_ORLC` | Clave principal de la tabla. |
| Foreign Key | `CO_OFIC_REGI` | `CO_OFIC_REGI` | Referencia a `A_OFIC_REGI.CO_OFIC_REGI`. |
| Foreign Key | `CO_SITU_TRAM` | `CO_SITU_TRAM` | Referencia a `A_SITU_TRAM_type.CO_SITU_TRAM`. |
| Foreign Key | `CO_TICK_SERV` | `CO_TICK_SERV` | Referencia a `P_TRAM.CO_TICK_SERV`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Base del módulo de seguimiento de títulos (RRPP/SUNARP). Centraliza la liquidación registral (mayor derecho, tacha, devoluciones). |

---

## Tabla: `H_SGMT_TRAM`

### Descripcion funcional
Tabla usada en Legasys para registrar el historial de las "etapas de trámite" (`CO_ETAP_TRAM`) por las que ha atravesado un ticket.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_SGMT_TRAM` | `int unsigned` | Identificador interno. |
| `CO_ETAP_TRAM` | `int unsigned` | Etapa de trámite. |
| `CO_TICK_SERV` | `int unsigned` | Ticket de servicio. |
| `NU_SECU` | `int unsigned` | Secuencia. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que registró la etapa. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación/cambio de etapa. |
| `IN_ESTA` | `char(1)` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_SGMT_TRAM` | Clave principal de la tabla. |
| Foreign Key | `CO_ETAP_TRAM` | `CO_ETAP_TRAM` | Referencia a `A_ETAP_TRAM_type.CO_ETAP_TRAM`. |
| Foreign Key | `CO_TICK_SERV` | `CO_TICK_SERV` | Referencia a `P_TRAM.CO_TICK_SERV`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Registra la cronología exacta (y quién lo hizo) de los cambios de etapa o flujo operativo de un expediente. |

---

## Tabla: `H_SUB_SERV`

### Descripcion funcional
Tabla usada en Legasys para registrar subservicios o divisiones de un servicio principal en el módulo de Operaciones. Cada subservicio puede amarrar un `CO_TARI` (tarifa base).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_SUB_SERV` | `int` | Identificador interno del subservicio. |
| `CO_SERV` | `int` | Servicio base asociado. |
| `CO_COMP` | `int` | Notaría o compañía. |
| `CO_TARI` | `int` | Tarifa asociada. |
| `CO_TIPO_TARI` | `int` | Tipo de tarifa. |
| `DE_SUB_SERV` | `varchar(100)` | Descripción del subservicio. |
| `DC_SUB_SERV` | `varchar(50)` | Descripción corta. |
| `NO_SUB_GRUP` | `varchar(200)` | Nombre de agrupación de subservicio. |
| `NU_ORDE` | `int` | Orden visual en el catálogo. |
| `IN_ESTA` | `char(1)` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_SUB_SERV` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Según las reglas recientes (AGENTS.md), el mantenimiento de subservicios en Operaciones permite listar conceptos (`P_CPTO`) activos, ya que los subservicios pueden impactar en la liquidación de conceptos relacionados (`H_SUB_SERV.CO_CPTO` se ha agregado o está por agregarse al modelo conceptual general para cruces en caja). |

---

## Tabla: `H_TEMP_TITU`

### Descripcion funcional
Tabla usada en Legasys como búfer o repositorio temporal para consultas de estado de títulos a SUNARP (a través del Bot o integración API).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TEMP_TITU` | `int` | Identificador interno. |
| `CO_TICK_SERV` | `int` | Ticket de servicio. |
| `CO_TITU_BOT` | `int` | Referencia al bot de consulta. |
| `NU_TITU` | `varchar(40)` | Número del título. |
| `NU_KARD` | `varchar(40)` | Número de kardex asociado. |
| `AA_TITU` | `varchar(40)` | Año del título. |
| `CO_SGMT_ORLC` | `int` | Seguimiento ORLC vinculado. |
| `IN_ESTA` | `int` | Estado del registro. |
| `IN_MODU` | `int` | Módulo. |
| `IN_MAIL` | `int` | Indicador si se envió correo. |
| `IM_CORR` | `longblob` | Archivo o comprobante temporal. |
| `IN_API` | `int` | Indicador de fuente (API). |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TEMP_TITU` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Contiene datos en crudo extraídos vía scraping/API para ser posteriormente revisados o consolidados en `H_SGMT_ORLC`. |

---

## Tabla: `H_TICK_ACTO_SID`

### Descripcion funcional
Tabla usada en Legasys para asociar un ticket de servicio con un "Acto Registral SID" (Sistema de Intermediación Digital).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TICK_ACTO_SID` | `int` | Identificador interno. |
| `CO_TICK_SERV` | `int` | Ticket de servicio. |
| `CO_ACTO_REGI_SID` | `varchar(20)` | Código del Acto SID (SUNARP). |
| `CO_USUA_MODI` | `int` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |
| `IN_ESTA` | `int` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TICK_ACTO_SID` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Sirve de puente para generar presentaciones SID vinculando el expediente interno con los catálogos del Registro Público. |

---

## Tabla: `H_TICK_SOLI`

### Descripcion funcional
Tabla usada en Legasys para registrar información referencial o solicitudes financieras vinculadas a un ticket.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TICK_SOLI` | `int` | Identificador interno. |
| `CO_TICK_SERV` | `int` | Ticket de servicio. |
| `NU_SOLI` | `varchar(40)` | Número o código de la solicitud. |
| `NU_MONT` | `double` | Monto referencial. |
| `FE_CONS` | `datetime` | Fecha de consulta o emisión. |
| `CO_USUA_MODI` | `int` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |
| `IN_ESTA` | `int` | Estado del registro. |
| `IN_PAGA` | `int` | Indicador de pago. |
| `IN_EXIS` | `int` | Indicador de existencia o validación. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TICK_SOLI` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Se utiliza en procesos donde una liquidación o ticket requiere la autorización previa de una solicitud o ticket externo asociado. |

---

## Tabla: `H_TIPO_DEPO`

### Descripcion funcional
Tabla usada en Legasys como catálogo para los tipos de depósitos o transacciones bancarias aceptadas en los flujos de pago o liquidación.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TIPO_DEPO` | `int` | Identificador interno. |
| `CO_FORM_PAGO_CAJA` | `int` | Forma de pago en caja. |
| `CO_TIPO_MONE` | `int` | Moneda del depósito. |
| `DE_TIPO_DEPO` | `varchar(100)` | Descripción del tipo de depósito. |
| `DC_TIPO_DEPO` | `varchar(50)` | Descripción corta. |
| `IN_ESTA` | `char(1)` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TIPO_DEPO` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Actúa como un catálogo/maestro asociado a caja y cuentas bancarias, permitiendo clasificar si el pago se realizó por transferencia, cheque gerencia, depósito efectivo, etc. |

---

## Tabla: `H_TRAM_CERT`

### Descripcion funcional
Tabla usada en Legasys para registrar la información de certificaciones vinculadas a un trámite (certificaciones de reproducciones, copias certificadas de actas, etc.).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TRAM_CERT` | `bigint` | Identificador interno. |
| `CO_TICK_SERV` | `bigint` | Ticket de servicio asociado. |
| `CO_TICK_SERV_SUB` | `int` | Subservicio asociado. |
| `NU_ANIO` | `int unsigned` | Año del libro o acta. |
| `DE_LIBR_ACTA` | `varchar(160)` | Descripción del libro o acta. |
| `RZ_SOCL` | `varchar(200)` | Razón social asociada al libro. |
| `NO_SOLI` | `varchar(200)` | Nombre del solicitante. |
| `DE_DIRE` | `varchar(200)` | Dirección del solicitante. |
| `IN_ESTA` | `char(1)` | Estado del registro. |
| `NU_CERTI` | `varchar(30)` | Número de certificado. |
| `FE_ACTA_ANTE` | `date` | Fecha del acta anterior. |
| `FE_ACTA_POST` | `date` | Fecha del acta posterior. |
| `FE_LEGA_LIBR` | `date` | Fecha de legalización del libro. |
| `NU_FOJA_FIN` | `varchar(60)` | Foja final. |
| `NU_FOJA_ANTE_FIN` | `varchar(6)` | Foja anterior a la final. |
| `NU_FOJA_POST_FIN` | `varchar(6)` | Foja posterior a la final. |
| `NU_FOJA_INIC` | `varchar(60)` | Foja inicial. |
| `NU_FOJA_ANTE_INI` | `varchar(6)` | Foja anterior a la inicial. |
| `NU_FOJA_POST_INI` | `varchar(6)` | Foja posterior a la inicial. |
| `NO_ACTA_ANTE` | `varchar(160)` | Nombre/descripción acta anterior. |
| `NO_ACTA_POST` | `varchar(160)` | Nombre/descripción acta posterior. |
| `NO_CIUD_NOTA` | `varchar(40)` | Ciudad del notario (origen). |
| `NO_LIBR_ACTA` | `varchar(160)` | Nombre literal del libro. |
| `NO_NOTA_COPI` | `varchar(80)` | Notario que expidió la copia original. |
| `NU_DNI_SOLI` | `varchar(8)` | DNI del solicitante. |
| `CO_UBIG` | `varchar(6)` | Ubigeo. |
| `FE_ACTA` | `date` | Fecha del acta. |
| `FE_COPI_CERTI` | `date` | Fecha de la copia certificada. |
| `NU_FIRM` | `int unsigned` | Número de firmas a certificar. |
| `NU_FOLI` | `int unsigned` | Número de folios. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TRAM_CERT` | Clave principal de la tabla. |
| Foreign Key | `CO_TICK_SERV` | `CO_TICK_SERV` | Referencia al ticket de servicio. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Soporta las múltiples casuísticas notariales para dar fe de partes o copias de libros corporativos, requiriendo validación de legalizaciones previas (fojas y notarios anteriores). |

---

## Tabla: `H_TRAM_CERT_DOMI`

### Descripcion funcional
Tabla usada en Legasys para registrar certificaciones domiciliarias o constancias de supervivencia/supervivencia con constatación domiciliaria.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TRAM_CERT_DOMI` | `bigint` | Identificador interno. |
| `CO_TICK_SERV` | `bigint` | Ticket de servicio. |
| `CO_TICK_SERV_SUB` | `int` | Subservicio asociado. |
| `CO_TIPO_CONS_NOTA` | `int` | Tipo de constatación notarial. |
| `FE_CERT` | `date` | Fecha de la certificación. |
| `HO_CERT` | `varchar(10)` | Hora de inicio de la certificación. |
| `NO_CORR` | `varchar(400)` | Nombre de las personas que corroboran (testigos/vecinos). |
| `DE_OBSE` | `text` | Observaciones. |
| `DE_DOMI` | `varchar(300)` | Domicilio constatado. |
| `CO_UBIG` | `int` | Ubigeo del domicilio. |
| `DE_ACTA_CONS` | `text` | Descripción libre del acta de constatación. |
| `NO_INTE` | `varchar(250)` | Nombre del interviniente/solicitante. |
| `NU_DOCU_INTE` | `varchar(20)` | Documento del interviniente. |
| `NO_CARG_INTE` | `varchar(400)` | Cargo o relación del interviniente. |
| `NO_DEFI_CONS` | `varchar(250)` | Nombre de quién realiza/firma constatación. |
| `HO_CERT_FIN` | `varchar(10)` | Hora de finalización. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TRAM_CERT_DOMI` | Clave principal de la tabla. |
| Foreign Key | `CO_TICK_SERV` | `CO_TICK_SERV` | Referencia al ticket de servicio. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Soporta el servicio extra-protocolar de Constataciones Domiciliarias, donde el personal de la notaría acude a validar si una persona reside o vive en el inmueble indicado. |

---

## Tabla: `H_TRAM_DIRE`

### Descripcion funcional
Tabla usada en Legasys para registrar bienes o direcciones involucradas en el trámite (inmuebles, vehículos, muebles, etc.) y los metadatos asociados a su transferencia o gravamen (PDT, predial, alcabala).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TRAM_DIRE` | `bigint` | Identificador interno del bien. |
| `CO_CLAS_BIEN` | `int unsigned` | Clase de bien (mueble, inmueble). |
| `CO_TIPO_BIEN` | `int unsigned` | Tipo de bien específico. |
| `CO_TICK_SERV` | `bigint` | Ticket de servicio. |
| `CO_TICK_SERV_SUB` | `int` | Subservicio asociado. |
| `CO_NACI` | `int unsigned` | Nacionalidad (si aplica al registro del bien). |
| `CO_PAIS` | `int unsigned` | País. |
| `CO_ASEV_IMPU` | `int` | Auxiliar impuestos. |
| `CO_ASEV_DECL` | `int` | Auxiliar declaración. |
| `CO_ASEV_HABI` | `int` | Auxiliar habitabilidad. |
| `CO_MEDI_PAGO` | `int` | Medio de pago. |
| `CO_ZONA_REGI` | `int` | Zona Registral del bien. |
| `CO_TIPO_INSC` | `int` | Tipo de inscripción registral. |
| `CO_TIPO_PRED` | `int` | Tipo de predio (Urbano/Rústico). |
| `IN_DECL_JURA` | `char(1)` | Indicador de si presenta Declaración Jurada (Autoavalúo). |
| `IN_CASA_HABI` | `char(1)` | Indicador de Casa Habitación (Exoneración Alcabala). |
| `CO_ASEV_PAGO` | `int` | Auxiliar de pago. |
| `DE_DIRE` | `varchar(80)` | Dirección del inmueble. |
| `FE_ADQU_BIEN` | `date` | Fecha en que el enajenante adquirió el bien. |
| `MO_PAGO_CNTA` | `decimal(10,2)` | Monto o pago a cuenta del impuesto. |
| `NU_PRED` | `int unsigned` | Número de predio o suministro. |
| `DE_OTRO_BIEN` | `varchar(200)` | Descripción libre de otro tipo de bien. |
| `NU_PART_REGI` | `varchar(20)` | Número de partida registral del bien. |
| `NU_FORM_1662` | `varchar(20)` | N° formulario SUNAT 1662 (Pago impuestos). |
| `CO_UBIG` | `varchar(6)` | Ubigeo del bien. |
| `FE_MINU_ENEJ` | `date` | Fecha de minuta de enajenación. |
| `CO_TIPO_MUEB` | `int` | Tipo de mueble (si clase es mueble). |
| `DE_BIEN` | `varchar(150)` | Descripción general del bien. |
| `NU_CONS_PAGO` | `varchar(50)` | Número de constancia de pago de alcabala/predial. |
| `FE_CONS_PAGO` | `date` | Fecha de la constancia de pago. |
| `IN_ESTA` | `int` | Estado del registro. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TRAM_DIRE` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Según las reglas del Kardex, pasa a `IN_ESTA = 0` al cambiar de servicio base porque los datos del inmueble (alcabala, predial) dependen estrictamente del tipo de contrato o servicio brindado. |

---

## Tabla: `H_TRAM_FIRM`

### Descripcion funcional
Tabla usada en Legasys para controlar el estado de firma (cuándo, a qué hora, validación biométrica) de cada participante dentro de un trámite específico.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TRAM_FIRM` | `bigint` | Identificador interno. |
| `CO_RELA_PRTC` | `int unsigned` | Relación del participante (Vendedor, Comprador). |
| `CO_TICK_SERV` | `int unsigned` | Ticket de servicio. |
| `CO_TIPO_PRTC` | `int unsigned` | Tipo de participante. |
| `CO_PRTC_TRAM` | `int unsigned` | Participante del trámite. |
| `CO_USUA_FIRM` | `int unsigned` | Usuario/operador que certifica la firma. |
| `CUP` | `int unsigned` | CUP asociado. |
| `NS_PRTC` | `int unsigned` | Secuencia del participante. |
| `FE_FIRM` | `date` | Fecha en la que firmó. |
| `HO_FIRM` | `time` | Hora exacta de firma. |
| `IN_DATA_OK` | `char(1)` | Indicador de si la data o biometría está OK. |
| `NS_ORDE` | `int unsigned` | Orden en el que firman. |
| `IM_PDF_FIRM` | `longblob` | Archivo o imagen de la firma (si aplica captura digital). |
| `CO_USUA_MODI` | `int unsigned` | Usuario que modificó. |
| `PO_PART` | `decimal(10,3)` | Porcentaje de participación (ej. societario o condómino). |
| `IN_TIPO_PRTC` | `varchar(3)` | Tipo de persona (NAT/JUR). |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TRAM_FIRM` | Clave principal de la tabla. |
| Foreign Key | `CO_RELA_PRTC` | `CO_RELA_PRTC` | Referencia a `A_RELA_PRTC.CO_RELA_PRTC`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Clave en el módulo Legal para determinar si un instrumento ya puede autorizarse (cierre de firmas) y auditar en qué momento físico firmó cada interviniente. |

---

## Tabla: `H_TRAM_GRAV`

### Descripcion funcional
Tabla usada en Legasys para detallar gravámenes, hipotecas, préstamos u obligaciones financieras registradas en el instrumento notarial.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TRAM_GRAV` | `bigint` | Identificador interno. |
| `CO_TICK_SERV` | `int unsigned` | Ticket de servicio. |
| `CO_TICK_SERV_SUB` | `int` | Subservicio asociado. |
| `TI_HIPO` | `int unsigned` | Tipo de hipoteca. |
| `MO_DEUD` | `decimal(14,2)` | Monto de la deuda u obligación. |
| `MO_GRAV` | `decimal(14,2)` | Monto del gravamen/hipoteca. |
| `NU_PART_REGI` | `varchar(20)` | Partida registral afectada. |
| `TI_MONE_TAVA` | `varchar(20)` | Moneda de la tasación/valor. |
| `FE_TERM` | `date` | Fecha de término del gravamen. |
| `FE_INIC` | `date` | Fecha de inicio. |
| `TO_TASA_INTE` | `varchar(50)` | Tasa de interés (TCEA/TEA). |
| `TI_MONE_GRAV` | `int(10) unsigned zerofill` | Moneda del gravamen. |
| `TI_MONE_DEUD` | `int unsigned` | Moneda de la deuda. |
| `TI_MONE_RNTA` | `int unsigned` | Moneda de renta (si aplica). |
| `DE_PRDA` | `varchar(200)` | Descripción de pérdida o seguro. |
| `MO_TASA_VALO` | `decimal(14,2)` | Monto valor de tasación del bien. |
| `MO_RNTA` | `decimal(14,2)` | Monto de renta o armada. |
| `TI_MNTO_GRAV` | `int unsigned` | Tipo de monto gravado. |
| `TI_MNTO_DEUD` | `int unsigned` | Tipo de monto deuda. |
| `FE_GRAV` | `date` | Fecha de constitución. |
| `DE_FORM_EJEC` | `text` | Forma de ejecución pactada. |
| `CO_DURA` | `int unsigned` | Duración pactada (código). |
| `DE_PACT_ESPE` | `varchar(500)` | Pactos especiales. |
| `TO_TASA_COMI` | `varchar(50)` | Tasas de comisiones asociadas. |
| `DE_ANOS` | `int unsigned` | Plazo en años. |
| `DE_MESE` | `int unsigned` | Plazo en meses. |
| `DE_DIAS` | `int unsigned` | Plazo en días. |
| `TI_VIGE_GARA` | `int unsigned` | Vigencia de garantía. |
| `TI_FIJA_VALO` | `int unsigned` | Método de fijación de valor. |
| `TI_OBLI` | `int unsigned` | Tipo de obligación garantizada. |
| `TI_DOCU_LEGA` | `int unsigned` | Documento legal base. |
| `FE_CONS_ACTO` | `date` | Fecha de constitución del acto. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TRAM_GRAV` | Clave principal de la tabla. |
| Foreign Key | `CO_TICK_SERV` | `CO_TICK_SERV` | Referencia al ticket de servicio. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Maneja metadatos extensivos para hipotecas bancarias, levantamientos y prendas, nutriendo variables del motor DOCX para armado de minutas estandarizadas. |

---

## Tabla: `H_TRAM_LEGA_LIBR`

### Descripcion funcional
Tabla usada en Legasys para registrar los atributos específicos de los trámites de "Legalización de Libros" y sus continuaciones.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TRAM_LEGA_LIBR` | `bigint` | Identificador interno. |
| `CO_TICK_SERV` | `bigint` | Ticket de servicio. |
| `CO_TICK_SERV_SUB` | `int` | Subservicio asociado. |
| `NU_CABE_CAJA` | `varchar(20)` | Comprobante de pago vinculado (si es directo). |
| `RZ_EMPR` | `varchar(200)` | Razón social propietaria del libro. |
| `NU_PAGI_FOLI` | `int unsigned` | Número de páginas o folios del libro. |
| `NU_SECU_FOLI` | `varchar(3)` | Tipo (Folio Simple, Folio Doble). |
| `NU_RUC` | `varchar(14)` | RUC de la empresa. |
| `FE_LEGA` | `date` | Fecha de legalización. |
| `FE_LEGA_ANTE` | `date` | Fecha de legalización del libro anterior. |
| `FE_RECO` | `date` | Fecha de recojo. |
| `IN_HOJA` | `char(1)` | Indicador si son hojas sueltas o libro empastado. |
| `NU_RANG_INIC` | `varchar(8)` | Numeración de hoja inicial. |
| `NU_RANG_ALTE` | `varchar(12)` | Numeración final esperada (antiguo). |
| `DE_COME` | `text` | Comentarios del acta o pérdida de libro previo. |
| `DE_OBSE` | `text` | Observaciones generales. |
| `IN_OPER` | `char(1)` | Estado de operación. |
| `DE_DENO_LIBR` | `varchar(300)` | Denominación completa del libro. |
| `NO_PERS` | `varchar(50)` | Nombre de persona de contacto o representante. |
| `NU_RANG_FIN` | `int unsigned` | Folio o rango final actual. |
| `CO_TIPO_LIBR` | `int unsigned` | Tipo de libro (Actas, Matrícula, Diario, Mayor). |
| `CO_TIPO_FOLI` | `int unsigned` | Código del tipo de folio. |
| `NU_LIBR_LETR` | `varchar(30)` | Número de tomo o libro en texto (ej. Tomo Dos). |
| `CO_NUM_LIBR` | `int unsigned` | Número consecutivo del libro. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TRAM_LEGA_LIBR` | Clave principal de la tabla. |
| Foreign Key | `CO_TICK_SERV` | `CO_TICK_SERV` | Referencia al ticket de servicio. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Maneja validaciones críticas (ej. no se puede aperturar el tomo 3 sin haber cerrado el tomo 2). Central en el módulo de Operaciones Notariales y reportes de índices a SUNAT/Colegio de Notarios. |

---

## Tabla: `H_TRAM_OBSE`

### Descripcion funcional
Tabla usada en Legasys para registrar observaciones documentales, búsqueda de antecedentes o informes adjuntos de rechazo dentro de un trámite (ej. prevención de lavado de activos).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TRAM_OBSE` | `int unsigned` | Identificador interno. |
| `IN_TRAM_OBSE` | `char(3)` | Tipo o categoría de la observación. |
| `CO_TICK_SERV` | `int unsigned` | Ticket de servicio. |
| `NU_SECU` | `int unsigned` | Secuencia. |
| `FE_TRAM_OBSE` | `datetime` | Fecha en la que se generó la observación. |
| `CO_TDOC_IDEN` | `int` | Tipo de documento del implicado. |
| `NU_DOCU_IDEN` | `varchar(11)` | Número de documento del implicado. |
| `NO_BUSQ` | `varchar(100)` | Término o nombre consultado. |
| `DE_OBSE` | `text` | Texto de la observación o hallazgo (ej. Coincidencia en listas PEP). |
| `IM_DOCU` | `longblob` | Evidencia en PDF o imagen (reporte). |
| `NO_EXTE_DOCU` | `varchar(5)` | Extensión del archivo adjunto. |
| `IM_DOCU_ADJU` | `varchar(20)` | Referencia de archivo externo o adjunto. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que registró. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de registro. |
| `IN_ESTA` | `char(1)` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TRAM_OBSE` | Clave principal de la tabla. |
| Foreign Key | `CO_TICK_SERV` | `CO_TICK_SERV` | Referencia al ticket de servicio. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Importante en el área de cumplimiento (Compliance Notarial), donde los asesores adjuntan resultados de listas de riesgo, debida diligencia u observaciones que pausan un trámite. |

---

## Tabla: `H_TRAM_TRAF`

### Descripcion funcional
Tabla usada en Legasys para llevar los datos económicos y transaccionales principales de un instrumento de transferencia (Transferencias, Compra-Ventas, Donaciones, etc.).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TRAM_TRAF` | `bigint` | Identificador interno. |
| `CO_TICK_SERV` | `bigint` | Ticket de servicio. |
| `CO_TICK_SERV_SUB` | `int` | Subservicio asociado. |
| `MO_TOTA_VENT` | `decimal(16,2)` | Monto total de la operación/venta. |
| `TI_FORM_PAGO` | `int unsigned` | Código de forma de pago. |
| `PO_CUOT_IDEA` | `decimal(7,2)` | Porcentaje de cuotas ideales (acciones/derechos). |
| `NU_PART_REGI` | `varchar(40)` | Partida registral transferida. |
| `MO_VALO_BIEN` | `decimal(16,2)` | Monto autovalúo o valor fiscal del bien. |
| `TI_TRAF` | `int unsigned` | Tipo de transferencia/operación. |
| `TI_MONE_VNTA` | `int unsigned` | Moneda de la venta. |
| `FE_TRAF` | `date` | Fecha de la transferencia. |
| `CO_TIPO_MONE` | `int unsigned` | Moneda (catalogo general). |
| `FE_ACTA` | `date` | Fecha de acta (si aplica remate/vehicular). |
| `FE_MINU` | `date` | Fecha de la minuta privada. |
| `CO_OPOR_PAGO` | `varchar(3)` | Oportunidad del pago (Al contado, a plazos). |
| `CO_FORM_PAGO` | `int` | Forma de pago. |
| `CO_ORIG_UIF` | `int` | Origen de fondos UIF asociado a la transacción. |
| `FE_INIC` | `date` | Fecha inicial de pago. |
| `FE_TERM` | `date` | Fecha de fin de pago o plazo. |
| `CO_ASEV` | `varchar(1)` | Indicador de control aseverado. |
| `DE_OPOR_PAGO` | `varchar(80)` | Descripción libre de la forma/oportunidad de pago. |
| `IN_ESTA` | `int` | Estado del registro. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TRAM_TRAF` | Clave principal de la tabla. |
| Foreign Key | `CO_TICK_SERV` | `CO_TICK_SERV` | Referencia al ticket de servicio. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Según las reglas del Kardex, esta tabla pasa a `IN_ESTA = 0` si se cambia el servicio base del trámite, ya que las condiciones del precio, moneda y formas de pago varían según el acto jurídico. Además, es una fuente directa para el llenado de los formularios obligatorios de Prevención de Lavado de Activos. |

---

## Tabla: `H_TRAM_VEHI`

### Descripcion funcional
Tabla usada en Legasys para registrar toda la información técnica, física y registral de un vehículo que forma parte de un trámite (como transferencias vehiculares o prendas).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TRAM_VEHI` | `bigint` | Identificador interno. |
| `CO_TICK_SERV` | `bigint` | Ticket de servicio asociado. |
| `CO_TICK_SERV_SUB` | `int` | Subservicio asociado. |
| `CO_ASEV_PAGO` | `int` | Auxiliar de pago. |
| `NU_PLAC` | `varchar(30)` | Número de placa del vehículo. |
| `DE_CLAS` | `varchar(60)` | Clase de vehículo. |
| `NU_ANIO` | `varchar(8)` | Año de fabricación/modelo. |
| `DE_MARC` | `varchar(80)` | Marca. |
| `NU_SERI` | `varchar(80)` | Número de serie/VIN. |
| `DE_COLO` | `varchar(80)` | Color del vehículo. |
| `NU_MOTO` | `varchar(50)` | Número de motor. |
| `DE_MODE` | `varchar(100)` | Modelo del vehículo. |
| `DE_CARR` | `varchar(50)` | Carrocería. |
| `NU_FOLI` | `int unsigned` | Número de folio registral. |
| `DE_OBSE` | `text` | Observaciones. |
| `NU_POLI` | `varchar(50)` | Número de póliza. |
| `DE_COMB` | `varchar(100)` | Tipo de combustible. |
| `DE_POTE` | `varchar(20)` | Potencia del motor. |
| `NU_CILI` | `varchar(10)` | Cilindrada. |
| `CA_PESO` | `varchar(20)` | Peso neto. |
| `CA_PESO_BRUTO` | `varchar(20)` | Peso bruto. |
| `NU_ASIE` | `varchar(5)` | Cantidad de asientos. |
| `DE_LONG` | `varchar(20)` | Longitud. |
| `DE_ANCH` | `varchar(20)` | Ancho. |
| `DE_ALT` | `varchar(20)` | Altura. |
| `NU_PASA` | `varchar(5)` | Cantidad de pasajeros. |
| `NU_PUER` | `varchar(5)` | Cantidad de puertas. |
| `NU_RUED` | `varchar(5)` | Cantidad de ruedas. |
| `NU_EJES` | `varchar(5)` | Cantidad de ejes. |
| `NU_TARJ` | `varchar(12)` | Número de Tarjeta de Identificación Vehicular (TIV). |
| `CO_ENTI` | `int unsigned` | Entidad registral. |
| `FE_EMI` | `date` | Fecha de emisión de tarjeta. |
| `FE_FORM` | `date` | Fecha de formulario notarial. |
| `NU_FORM` | `varchar(30)` | Número de formulario notarial. |
| `ID_TARJ` | `varchar(2)` | ID de tarjeta. |
| `ID_PLAC` | `varchar(2)` | ID de placa. |
| `MODI_RAZ` | `varchar(120)` | Motivo de la modificación. |
| `CA_COLO` | `varchar(20)` | Categoría color. |
| `CA_MOTO` | `varchar(12)` | Categoría motor. |
| `CA_CILI` | `varchar(10)` | Categoría cilindrada. |
| `CA_COMB` | `varchar(100)` | Categoría combustible. |
| `CA_CARR` | `varchar(50)` | Categoría carrocería. |
| `DE_PESO_SECO` | `varchar(20)` | Peso seco. |
| `CA_EJES` | `varchar(5)` | Categoría ejes. |
| `CA_RUED` | `varchar(5)` | Categoría ruedas. |
| `ID_RECT` | `varchar(120)` | ID de rectificación. |
| `CA_OTRO` | `varchar(120)` | Otras características. |
| `ID_CLAS` | `varchar(60)` | ID de clasificación. |
| `NU_EXPE` | `varchar(10)` | Expediente. |
| `FE_EXP` | `date` | Fecha de expediente. |
| `DE_PROC` | `varchar(60)` | Procedencia o país de fabricación. |
| `NU_SOAT` | `varchar(30)` | Número de SOAT. |
| `FE_SOAT` | `date` | Fecha de vencimiento SOAT. |
| `NU_RECI_IMP` | `varchar(12)` | Número de recibo impuesto vehicular. |
| `FE_RECI_IMP` | `date` | Fecha de recibo impuesto. |
| `MO_RECI_IMP` | `decimal(14,2)` | Monto impuesto vehicular. |
| `FE_ACTA_ANTE` | `date` | Fecha de acta anterior. |
| `NU_CHASIS` | `varchar(50)` | Número de chasis. |
| `CO_CLAS` | `int unsigned` | Código de clase. |
| `CA_UTIL` | `varchar(5)` | Carga útil. |
| `CA_CARG_UTIL` | `varchar(5)` | Categoría carga útil. |
| `NU_PART` | `varchar(11)` | Número de partida registral. |
| `CO_ZONA_REGI` | `int unsigned` | Zona registral. |
| `CO_OFIC_REGI` | `int` | Oficina registral. |
| `CO_COMP_SEGU` | `int unsigned` | Compañía de seguros (SOAT). |
| `CO_TIPO_MONE` | `int` | Moneda de valoración. |
| `NU_VALO_VEHI` | `decimal(11,2)` | Valor referencial del vehículo. |
| `IN_ESTA` | `char(1)` | Estado del registro. |
| `ID_COLOR` | `varchar(20)` | ID interno de color. |
| `ID_MOTOR` | `varchar(20)` | ID interno de motor. |
| `ID_CARRO` | `varchar(20)` | ID interno de carrocería. |
| `ID_EJES` | `varchar(20)` | ID interno de ejes. |
| `ID_OTROS` | `varchar(20)` | ID de otros componentes. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |
| `IN_IMPO` | `int` | Indicador de importación. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TRAM_VEHI` | Clave principal de la tabla. |
| Foreign Key | `CO_TICK_SERV` | `CO_TICK_SERV` | Referencia al ticket de servicio. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Según las reglas del Kardex, esta tabla pasa a `IN_ESTA = 0` al cambiar el servicio base. Sus columnas capturan exactamente la estructura requerida para presentar Formularios Notariales Vehiculares ante SUNARP. |

---

## Tabla: `H_USUA_SESI`

### Descripcion funcional
Tabla usada en Legasys para registrar el historial o log de inicio de sesión de los usuarios del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_USUA_SESI` | `int` | Identificador de la sesión. |
| `CO_USUA` | `int` | Identificador del usuario. |
| `NU_IP` | `varchar(100)` | Dirección IP desde donde se inició sesión. |
| `IN_ESTA` | `int` | Estado del registro (ej. login activo o histórico). |
| `TS_USUA_MODI` | `datetime` | Fecha y hora del registro/modificación. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_USUA_SESI` | Clave principal de la tabla. |
| Foreign Key | `CO_USUA` | `CO_USUA` | Referencia a `P_USUA.CO_USUA` (Tabla principal de usuarios). |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Útil para control de concurrencia y auditorías de seguridad en la plataforma. |

---

## Tabla: `H_VIST_PREV`

### Descripcion funcional
Tabla usada en Legasys para registrar vistas previas de pre-liquidaciones o presupuestos vinculados a un ticket antes de que se aprueben o envíen formalmente a caja.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_VIST_PREV` | `int` | Identificador interno. |
| `CO_TICK_CONT` | `int` | Ticket contenedor asociado. |
| `CO_PRES_TICK` | `int` | Presupuesto asociado. |
| `CO_SERV` | `int` | Servicio asociado. |
| `CO_TIPO_CPTO` | `int` | Tipo de concepto (Notarial/Registral). |
| `NU_CANT` | `int` | Cantidad presupuestada. |
| `NO_DESC` | `varchar(200)` | Descripción o detalle manual del concepto. |
| `MO_PRES` | `decimal(11,2)` | Monto presupuesto unitario. |
| `MO_PAGO` | `decimal(11,2)` | Monto total a pagar. |
| `CO_USUA_MODI` | `int` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |
| `TS_USUA_ANUL` | `datetime` | Fecha y hora de anulación. |
| `IN_ESTA` | `int` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_VIST_PREV` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Parte de la etapa de "Presupuestación". Suele limpiarse o anularse una vez que la pre-liquidación se formaliza en `H_PRES_TICK`. |

---

## Tabla: `H_WHAT_TICK`

### Descripcion funcional
Tabla usada en Legasys para registrar los metadatos de las notificaciones o mensajes de WhatsApp vinculados a un ticket.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_WHAT_TICK` | `int` | Identificador interno. |
| `CO_TICK_CONT` | `int` | Ticket contenedor. |
| `NU_WHAT` | `varchar(10)` | Número de celular (WhatsApp). |
| `DE_PLAN` | `varchar(200)` | Plantilla o mensaje utilizado. |
| `CO_USUA_MODI` | `int` | Usuario que registró/envió. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de envío. |
| `IN_ESTA` | `int` | Estado del envío/registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_WHAT_TICK` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Registro de contacto de notificaciones automatizadas de estados de trámite vía la integración de WhatsApp. |

---

## Tabla: `P_ALIA_TABL`

### Descripcion funcional
Tabla maestra de sistema (diccionario de datos) que define los alias, nombres amigables y descripciones de las tablas funcionales del sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `NO_TABL` | `varchar(50)` | Nombre real de la tabla en base de datos. |
| `DE_TABL` | `varchar(100)` | Descripción o nombre amigable. |
| `TI_TABL` | `int unsigned` | Tipo/categoría de tabla. |
| `IN_MULT` | `char(1)` | Indicador de múltiple. |
| `DE_TRAM_LINE` | `text` | Descripción o vinculación en trámites en línea. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `NO_TABL` | Clave principal de la tabla. |
| Referenciada por | `H_ALIA_COLM` | `NO_TABL` | Es referenciada por `H_ALIA_COLM.NO_TABL`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Alimenta las herramientas internas de generación de reportes, constructor Twig o motor de plantillas, donde el usuario final necesita leer un nombre amigable de tabla en vez del nombre técnico. |

---

## Tabla: `P_CABE_CAJA`

### Descripcion funcional
Tabla principal/maestra del módulo de Caja. Almacena las cabeceras de los comprobantes de pago (Boletas, Facturas, Recibos) emitidos por la notaría.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CABE_CAJA` | `int unsigned` | Identificador interno del comprobante. |
| `CO_SEMI_TDOC` | `int unsigned` | Semilla o serie del tipo de documento. |
| `CO_TICK_CONT` | `int unsigned` | Ticket contenedor (Kardex) asociado. |
| `CO_COMP` | `int` | Compañía / Notaría. |
| `CO_FORM_PAGO_CAJA` | `int unsigned` | Forma de pago en caja. |
| `CO_TIPO_MONE` | `int unsigned` | Moneda del comprobante. |
| `CO_TIPO_MONE_VUEL` | `int` | Moneda del vuelto. |
| `CO_TIPO_MONE_EFEC` | `int` | Moneda del efectivo entregado. |
| `CO_CLIE` | `int` | Código de cliente (Facturado a). |
| `CO_CLIE_MAIL` | `int` | Indicador de correo del cliente. |
| `CO_CLIE_MAIL_ENVI` | `int` | Indicador si correo fue enviado. |
| `CO_GRUP` | `int` | Grupo o empresa asociada. |
| `CO_GRUP_PAGO` | `int` | Grupo que asume el pago. |
| `CO_FUNC_CLIE` | `int unsigned` | Funcionario del cliente (contacto). |
| `CO_FUNC_PROD` | `int` | Funcionario productor/abogado. |
| `CO_TIEM_PAGO` | `int` | Tiempo/plazo de pago. |
| `CO_TIPO_RETE` | `int` | Tipo de retención. |
| `NU_CABE_CAJA` | `varchar(20)` | Número o correlativo del comprobante. |
| `NU_ORDE_REFE` | `varchar(20)` | Número de orden de referencia. |
| `NU_CODI_REFE` | `varchar(50)` | Código de referencia. |
| `NU_VOUC_BANC` | `varchar(100)` | Número de voucher bancario. |
| `FE_CABE_CAJA` | `date` | Fecha de emisión del comprobante. |
| `NU_CAMB_VENT` | `decimal(11,3)` | Tipo de cambio venta. |
| `PO_DESC` | `int unsigned` | Porcentaje de descuento. |
| `MO_BRUT` | `decimal(12,2)` | Monto bruto. |
| `MO_NETO` | `decimal(12,2)` | Monto neto/total a pagar. |
| `MO_VUEL` | `decimal(12,2)` | Monto del vuelto. |
| `MO_EFEC` | `decimal(12,2)` | Monto en efectivo entregado. |
| `MO_COMI_TARJ` | `decimal(11,2)` | Comisión de tarjeta. |
| `MO_COMI_CAJA` | `decimal(11,2)` | Comisión de caja. |
| `PO_IGV` | `int unsigned` | Porcentaje IGV. |
| `MO_IGV` | `decimal(10,2)` | Monto IGV calculado. |
| `MO_INAF_IGV` | `decimal(11,2)` | Monto inafecto a IGV. |
| `MO_DEUD_PAGO` | `decimal(12,2)` | Monto deuda pendiente. |
| `MO_PRE_PAGO` | `decimal(12,2)` | Monto pre-pago o adelanto. |
| `DE_MEMO` | `text` | Memo o detalle interno. |
| `NO_CLIE_FINA` | `text` | Nombre de cliente final / tercero. |
| `NO_OTRO_DATO` | `varchar(250)` | Otra referencia o glosa en comprobante. |
| `NO_NOMB_SOLI` | `varchar(250)` | Nombre del solicitante. |
| `MO_RESE` | `decimal(12,2)` | Monto reservado. |
| `IN_INPOR` | `char(1)` | Indicador de importación. |
| `IN_REGI_CHEQ` | `char(1)` | Indicador de registro de cheque. |
| `IN_ENVI_COBR` | `char(1)` | Indicador si se envía a cobranza. |
| `FE_ACEP_COBR` | `date` | Fecha de aceptación de cobranza. |
| `FE_ACCI_CAJA` | `date` | Fecha de acción en caja. |
| `FE_VENC_COBR` | `date` | Fecha vencimiento de cobro. |
| `CO_CABE_CAJA_VINC` | `int` | Comprobante vinculado (ej. anticipo). |
| `CO_CABE_CAJA_RELA` | `int` | Comprobante relacionado (ej. nota crédito). |
| `NU_DETR_SUNA` | `varchar(10)` | Número de detracción SUNAT. |
| `NU_CABE_CAJA_AUX` | `varchar(20)` | Número auxiliar. |
| `NO_OBSE_CAJA` | `text` | Observaciones en caja. |
| `IN_ESTA_CAJA` | `int` | Estado del comprobante en caja (Ej. Pagado, Anulado). |
| `CO_CABE_SUB_CAJA` | `int` | Referencia de sub-caja. |
| `CO_USUA_ANUL` | `int unsigned` | Usuario que anuló. |
| `TS_USUA_ANUL` | `datetime` | Fecha y hora de anulación. |
| `CO_USUA_ACTI` | `int` | Usuario que activó/autorizó. |
| `TS_USUA_ACTI` | `datetime` | Fecha de activación. |
| `CO_USUA_ANUL_2` | `int` | Usuario segunda anulación/extorno. |
| `TS_USUA_ANUL_2` | `datetime` | Fecha segunda anulación. |
| `CO_USUA_MODI` | `int unsigned` | Usuario creador/emisor. |
| `TS_USUA_MODI` | `datetime` | Fecha de creación/emisión. |
| `IN_ESTA` | `char(1)` | Estado general de la tabla. |
| `IN_REVI` | `int` | Indicador de revisión. |
| `IN_RECH` | `int` | Indicador de rechazo. |
| `FE_REVI` | `datetime` | Fecha de revisión. |
| `IN_PAGO_DETR` | `int` | Indicador de pago de detracción. |
| `IN_ELEC` | `int` | Indicador si es comprobante electrónico. |
| `IM_PAGO` | `longblob` | Archivo adjunto del pago (voucher). |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CABE_CAJA` | Clave principal de la tabla. |
| Foreign Key | `CO_SEMI_TDOC` | `CO_SEMI_TDOC` | Referencia a `A_SEMI_TDOC.CO_SEMI_TDOC`. |
| Referenciada por | Múltiples | `CO_CABE_CAJA` | Es referenciada por `H_DETA_CAJA`, `H_SUB_CAJA`, `P_CABE_NOTA`, `P_CABE_SUB_CAJA`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Núcleo del módulo financiero de Legasys. Interactúa estrechamente con facturación electrónica y gestión de ingresos. |

---

## Tabla: `P_CABE_NOTA`

### Descripcion funcional
Tabla usada en Legasys para registrar las cabeceras de Notas de Crédito y Notas de Débito.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CABE_NOTA` | `int` | Identificador interno. |
| `CO_CABE_CAJA` | `int unsigned` | Comprobante de origen afectado. |
| `CO_SEMI_TDOC` | `int` | Semilla o serie de la nota. |
| `CO_MOTI_NOTA` | `int` | Motivo de emisión de la nota (Catálogo SUNAT). |
| `CO_FORM_PAGO_CAJA` | `int` | Forma de pago. |
| `CO_CABE_CAJA_REGE` | `int` | Comprobante regenerado o reemplazo. |
| `FE_CABE_NOTA` | `datetime` | Fecha de emisión de la nota. |
| `FE_VENC_COBR` | `date` | Fecha de vencimiento si aplica. |
| `NU_CABE_NOTA` | `varchar(20)` | Número o correlativo de la nota. |
| `MO_BRUT` | `decimal(12,2)` | Monto bruto de la nota. |
| `MO_IGV` | `decimal(12,2)` | Monto IGV afectado. |
| `MO_NETO` | `decimal(12,2)` | Monto neto final. |
| `DE_OBSE_NOTA` | `text` | Sustento o glosa de la nota. |
| `CO_USUA_MODI` | `int` | Usuario que emitió. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de emisión. |
| `IN_ESTA` | `char(1)` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CABE_NOTA` | Clave principal de la tabla. |
| Foreign Key | `CO_CABE_CAJA` | `CO_CABE_CAJA` | Referencia a `P_CABE_CAJA.CO_CABE_CAJA`. |
| Referenciada por | `H_ERRO_USUA` | `CO_CABE_NOTA` | Es referenciada por `H_ERRO_USUA.CO_CABE_NOTA`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Gestiona las devoluciones, anulaciones parciales o totales de comprobantes previamente emitidos en `P_CABE_CAJA`. |

---

## Tabla: `P_CABE_PAGO_LINE`

### Descripcion funcional
Tabla principal usada en Legasys para registrar y orquestar órdenes de "Pago en Línea" (pasarelas de pago, Niubiz, Culqi).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CABE_PAGO_LINE` | `int` | Identificador interno. |
| `CO_COMP` | `int` | Compañía o notaría. |
| `CO_TICK_CONT` | `int` | Ticket o Kardex vinculado. |
| `CO_CLIE` | `int` | Cliente que paga. |
| `CO_GRUP` | `int` | Grupo. |
| `CO_TIPO_MONE` | `int` | Moneda del pago (Soles, Dólares). |
| `CO_ESTA_PAGO_LINE` | `int` | Estado del pago en pasarela (Creado, Pagado, Expirado). |
| `CO_TDOC` | `int` | Tipo de documento generado. |
| `NU_OPER_PAGO_LINE` | `varchar(30)` | Número de orden interno. |
| `CL_PAGO_LINE` | `varchar(255)` | Identificador único/hash (URL segura). |
| `FE_EMIS_PAGO_LINE` | `date` | Fecha de creación del link. |
| `FE_VENC_PAGO_LINE` | `date` | Fecha de expiración del link de pago. |
| `TS_ENVI_PAGO_LINE` | `datetime` | Fecha de envío al cliente. |
| `TS_APER_PAGO_LINE` | `datetime` | Fecha de apertura (click del cliente). |
| `TS_PAGA_PAGO_LINE` | `datetime` | Fecha en la que la pasarela confirma el pago. |
| `MO_TOTA_PAGO_LINE` | `decimal(11,2)` | Monto total a cobrar al cliente. |
| `MO_PAGA_PAGO_LINE` | `decimal(11,2)` | Monto efectivamente pagado. |
| `MO_COMI_PAGO_LINE` | `decimal(11,2)` | Comisión retenida por la pasarela. |
| `DE_CONC_PAGO_LINE` | `varchar(250)` | Concepto o detalle del link de pago. |
| `DE_OBSE_PAGO_LINE` | `varchar(500)` | Observaciones internas. |
| `CO_CULQ_OPER` | `varchar(100)` | ID de operación externa en la pasarela. |
| `CO_CULQ_CHAR` | `varchar(100)` | ID del cargo en pasarela (Charge ID). |
| `CO_CULQ_ORDR` | `varchar(100)` | ID de orden en pasarela. |
| `DE_CULQ_STAT` | `varchar(100)` | Estado textual retornado por la pasarela. |
| `TX_CULQ_RESP` | `longtext` | Payload crudo JSON de la respuesta de la pasarela. |
| `IN_ESTA` | `int` | Estado del registro. |
| `CO_USUA_CREA` | `int` | Usuario que generó el link. |
| `TS_USUA_CREA` | `datetime` | Fecha de creación. |
| `CO_USUA_MODI` | `int` | Usuario que modificó o concilió. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CABE_PAGO_LINE` | Clave principal de la tabla. |
| Unique | `CL_PAGO_LINE` | `CL_PAGO_LINE` | Identificador único del enlace. |
| Foreign Key | `CO_ESTA_PAGO_LINE` | `CO_ESTA_PAGO_LINE` | Referencia a `A_ESTA_PAGO_LINE.CO_ESTA_PAGO_LINE`. |
| Referenciada por | Múltiples | `CO_CABE_PAGO_LINE` | Es referenciada por `H_CAJA_PAGO_LINE`, `H_DETA_PAGO_LINE`, `H_ESTA_PAGO_LINE`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Permite enviar enlaces (links) a los clientes para que abonen por tarjeta o billetera móvil, actualizando automáticamente el estado y registrando el pago en caja. |

---

## Tabla: `P_CAJA_EGRE`

### Descripcion funcional
Tabla usada en Legasys para registrar los "Egresos de Caja", sean gastos operativos de la notaría, entregas a rendir, o pagos de servicios registrales/terceros vinculados a un Kardex.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CAJA_EGRE` | `int` | Identificador interno. |
| `CO_TICK_CONT` | `int` | Ticket o trámite vinculado (si aplica). |
| `CO_CPTO_EGRE` | `int` | Concepto de egreso (Catálogo). |
| `CO_TIPO_MONE` | `int` | Moneda del egreso. |
| `CO_USUA` | `int` | Usuario/trabajador que solicita/recibe. |
| `CO_BANC` | `int` | Banco asociado al pago. |
| `CO_PROV_CAJA` | `int` | Proveedor beneficiario. |
| `CO_COMP` | `int` | Compañía/Notaría que asume el gasto. |
| `CO_FORM_PAGO_CAJA` | `int` | Forma de pago del egreso. |
| `FE_CAJA_EGRE` | `date` | Fecha de salida del dinero. |
| `NU_FACT_PROV` | `varchar(20)` | N° Factura/Comprobante de sustento. |
| `CO_CUEN_BANC` | `int` | Cuenta bancaria de la notaría origen de fondos. |
| `NU_OPER_BANC` | `varchar(50)` | N° de operación bancaria. |
| `DE_OBSE` | `text` | Observaciones o detalle del gasto. |
| `NU_MONT_BRUT` | `decimal(11,2)` | Monto inicial/bruto solicitado. |
| `NU_MONT_VUEL` | `decimal(11,2)` | Monto devuelto a caja (rendición). |
| `NU_MONT` | `decimal(11,2)` | Monto real/neto del egreso ejecutado. |
| `CO_USUA_MODI` | `int` | Cajero o usuario que operó el egreso. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora del registro. |
| `IN_ESTA` | `char(1)` | Estado del egreso (Activo, Rendido, Anulado). |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CAJA_EGRE` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Clave para cuadrar el Arqueo de Caja diario, restando estos valores a los ingresos en efectivo/bancos. |

---

## Tabla: `P_CALE_ACTI`

### Descripcion funcional
Tabla usada en Legasys para registrar actividades, recordatorios, citas y tareas en el calendario interno para los usuarios.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CALE_ACTI` | `int` | Identificador interno. |
| `CO_TICK_SERV` | `int` | Ticket de servicio si está vinculado a un trámite. |
| `CO_TRAM_OBSE` | `int` | Si la actividad surge por una observación. |
| `CO_TIPO_ADVE` | `int` | Tipo de advertencia o evento. |
| `CO_TIPO_USUA` | `int` | Tipo de usuario destinatario. |
| `FE_CALE_ACTI` | `date` | Fecha de la actividad. |
| `HO_CALE_ACTI` | `time` | Hora programada. |
| `FE_ULTI_ENVI` | `date` | Fecha de último envío de notificación o alarma. |
| `DE_CALE_ACTI` | `text` | Detalle o nota de la actividad. |
| `TS_USUA_MODI` | `datetime` | Fecha de modificación. |
| `CO_USUA_MODI` | `int` | Usuario que creó la actividad. |
| `IN_ESTA` | `char(1)` | Estado (Pendiente, Realizado). |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CALE_ACTI` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Funciona como agenda o CRM interno para abogados o gestores registrales. |

---

## Tabla: `P_CLIE`

### Descripcion funcional
Tabla maestra usada en Legasys para almacenar el catálogo consolidado de "Clientes" (tanto personas naturales como jurídicas), utilizados principalemente en Caja/Facturación y como agrupadotes de carteras o convenios.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CLIE` | `int unsigned` | Identificador único de cliente. |
| `CO_COMP` | `int` | Notaría a la que pertenece. |
| `CO_USUA` | `int` | Usuario gestor asignado. |
| `CO_GRUP` | `int unsigned` | Grupo empresarial al que pertenece. |
| `CO_TIPO_CLIE` | `int` | Clasificación/Categoría del cliente. |
| `CO_TIEM_PAGO` | `int` | Plazos/Convenios de pago asociados. |
| `CO_COBR` | `int` | Tipo de cobranza o gestor de cobranza. |
| `DE_DIRE` | `varchar(200)` | Dirección fiscal. |
| `DE_DIRE_REFE` | `varchar(100)` | Referencia de dirección. |
| `NO_BUSQ` | `varchar(150)` | Nombre normalizado para búsqueda (MAYÚSCULAS). |
| `CO_UBIG` | `varchar(6)` | Ubigeo fiscal. |
| `CO_TIPO_PERS` | `int unsigned` | Tipo de persona (Natural/Jurídica). |
| `CO_TIPO_DIRE` | `int unsigned` | Tipo de dirección. |
| `NU_TELF` | `varchar(20)` | Teléfono principal. |
| `NU_TELF_2` | `varchar(20)` | Teléfono secundario. |
| `NU_FAX` | `varchar(50)` | Fax o anexo. |
| `NU_RUC` | `varchar(15)` | RUC o Documento (llave principal de facturación). |
| `DE_MAIL` | `varchar(70)` | Correo electrónico para facturación electrónica. |
| `IN_EXON_IMPU` | `char(1)` | Exonerado de impuestos (Entidades del Estado). |
| `IN_LINE_CRED` | `char(1)` | Tiene línea de crédito habilitada. |
| `IN_TIPO_CRED` | `int` | Tipo de crédito asignado. |
| `MO_LINE_CRED` | `decimal(15,2) unsigned` | Monto de línea de crédito aprobada. |
| `IN_NOTI_MAIL` | `smallint` | Suscrito a notificaciones. |
| `IN_TIPO_ADVE_CLIE` | `int` | Alertas al facturar (Cliente deudor, Problemático). |
| `NO_PERS_COBR` | `varchar(190)` | Contacto del área de pagos del cliente. |
| `DE_CARG` | `varchar(60)` | Cargo del contacto de cobranzas. |
| `NU_TELF_RESP` | `varchar(15)` | Teléfono del responsable. |
| `DE_CORR_COBR` | `varchar(150)` | Correo de contabilidad para enviar facturas. |
| `NU_DIAS_PAGO` | `int` | Condición de pago en días. |
| `DE_OBSE` | `text` | Observaciones. |
| `IN_APRO` | `int` | Aprobación por jefatura de caja/crédito. |
| `IN_FIRM_DIGI` | `int` | Convenio firma digital. |
| `CO_USUA_CREA` | `smallint` | Creado por. |
| `TS_USUA_CREA` | `datetime` | Fecha creación. |
| `CO_USUA_MODI` | `int unsigned` | Modificado por. |
| `TS_USUA_MODI` | `datetime` | Fecha de modificación. |
| `IN_ESTA` | `char(1)` | Estado (Activo/Inactivo). |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CLIE` | Clave principal de la tabla. |
| Foreign Key | `CO_GRUP` | `CO_GRUP` | Referencia a `P_GRUP.CO_GRUP`. |
| Referenciada por | Múltiples | `CO_CLIE` | Referenciada fuertemente por `H_CLIE_JURI`, `H_CLIE_NATU`, `P_TICK`, etc. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | OJO: A diferencia de `P_PRTC` que maneja "Participantes" (Comparecientes en el instrumento), `P_CLIE` maneja al "Pagador" (A nombre de quién sale la factura). A veces son la misma persona, pero funcionalmente están separados. |

---

## Tabla: `P_CPTO`

### Descripcion funcional
Tabla maestra de "Conceptos" tarifarios. Define la unidad básica cobrable en caja y presupuestos (ej: Fojas, Cartas Notariales, Honorarios de Transferencia, IGV, etc.).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CPTO` | `int unsigned` | Código único de concepto. |
| `CO_TIPO_CPTO` | `int unsigned` | Tipo de concepto (Derechos Notariales, Registrales, UIF, SUNAT). |
| `IN_CANT` | `int` | Requiere captura de cantidad (ej. Fotocopias = Sí, Honorario fijo = No). |
| `DE_CPTO` | `varchar(100)` | Descripción o nombre del concepto que sale en Boleta/Factura. |
| `DC_CPTO` | `varchar(15)` | Abreviatura o código corto. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que modificó el concepto. |
| `TS_USUA_MODI` | `datetime` | Fecha de modificación. |
| `IN_ESTA` | `char(1)` | Estado (Activo/Inactivo). |
| `IN_CHEC` | `int` | Aparece marcado/sugerido por defecto en liquidadores. |
| `IN_INAF_IGV` | `int` | Indicador si es concepto Inafecto o Exonerado de IGV (Ej. Tasa Registral SUNARP o Arbitrios). |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CPTO` | Clave principal de la tabla. |
| Foreign Key | `CO_TIPO_CPTO` | `CO_TIPO_CPTO` | Referencia a `A_TIPO_CPTO.CO_TIPO_CPTO`. |
| Referenciada por | `R_SERV_CPTO_TARI` | `CO_CPTO` | Es referenciada por las matrices tarifarias `R_SERV_CPTO_TARI`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Según las reglas recientes (AGENTS.md), los conceptos "Libres" usados en liquidación se agregan dinámicamente relacionándolos al servicio con tarifa 0. Además, `IN_INAF_IGV` es crítico porque un concepto mal configurado (Ej. Tasa SUNARP con IGV) causa rechazo en SUNAT. |

---

## Tabla: `P_DOCU_DIGI_QR`

### Descripcion funcional
Tabla maestra del módulo de "Documentos Digitales LEGASYS / QR". Gestiona la publicación de copias, traslados y certificaciones a la nube (AWS/S3) permitiendo la validación y firma digital notarial accesible desde un código QR público.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DOCU_DIGI_QR` | `int` | Identificador principal del documento digital. |
| `CO_COMP` | `int` | Notaría emisora. |
| `CO_TICK_CONT` | `int` | Ticket o carpeta contenedora. |
| `CO_TICK_SERV` | `int` | Servicio asociado. |
| `NU_KARD` | `varchar(20)` | Número de Kardex u operación notarial. |
| `NU_INST` | `varchar(20)` | Número de instrumento/escritura o certificación. |
| `DE_ACTO` | `varchar(255)` | Descripción o tipo de acto jurídico. |
| `DE_NOTA` | `varchar(255)` | Notario u oficio que emite. |
| `NO_CLIE` | `varchar(255)` | Nombre del solicitante o interviniente principal. |
| `DE_TDOC_CLIE` | `varchar(50)` | Tipo de documento del cliente. |
| `NU_DOCU_CLIE` | `varchar(30)` | N° documento del cliente. |
| `FE_INGR` | `datetime` | Fecha de ingreso del expediente. |
| `FE_ESCR` | `datetime` | Fecha de la escritura o instrumento. |
| `NU_CTRL` | `varchar(100)` | Código único de control visual o foja. |
| `CL_TOKE_PUBL` | `varchar(255)` | Hash o token JWT único para acceso público seguro. |
| `CL_URL_PUBL` | `varchar(500)` | URL directa generada para la validación del QR. |
| `NO_ARCHI_ORIG` | `varchar(255)` | Nombre original del documento subido. |
| `NO_ARCHI_FIRM` | `varchar(255)` | Nombre del archivo tras el proceso de firma. |
| `DE_RUTA_ARCHI_ORIG` | `varchar(500)` | Ruta local o S3 del archivo original. |
| `DE_RUTA_ARCHI_FIRM` | `varchar(500)` | Ruta local o S3 del archivo firmado/sellado. |
| `DE_HASH_ARCHI_FIRM` | `varchar(255)` | Checksum SHA256 para validación de integridad. |
| `DE_HASH_QR` | `varchar(255)` | Hash asociado al dibujo del QR. |
| `IN_REQU_FIRM_DIGI` | `tinyint(1)` | Indicador si este documento exige firma del notario. |
| `IN_FIRM_DIGI` | `tinyint(1)` | Estado: ¿Ya fue firmado digitalmente?. |
| `IN_PUBL` | `tinyint(1)` | Estado: ¿Está publicado y visible al público?. |
| `IN_ESTA_DOCU_DIGI` | `tinyint` | Estado del flujo documental (Generado, En Firma, Publicado). |
| `TX_OBSE` | `text` | Observaciones. |
| `TX_JSON_EXTRA` | `json` | Campo JSON dinámico para metadatos del tipo de servicio. |
| `FE_FIRM_DIGI` | `datetime` | Fecha en la que el notario estampó firma. |
| `FE_PUBL` | `datetime` | Fecha de liberación a la nube. |
| `CO_USUA_MODI` | `int` | Usuario que registró o subió el documento. |
| `TS_USUA_MODI` | `datetime` | Timestamp de última modificación. |
| `IN_ESTA` | `tinyint(1)` | Estado del registro (Anulación lógica). |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DOCU_DIGI_QR` | Clave principal de la tabla. |
| Unique | `CL_TOKE_PUBL` | `CL_TOKE_PUBL` | Token público único del documento. |
| Referenciada por | Múltiples | `CO_DOCU_DIGI_QR` | Es referenciada por `H_DOCU_DIGI_QR_ESTA` y `H_DOCU_DIGI_QR_PRTC`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Tabla CORE para el nuevo portal en la nube. Según `AGENTS.md`, la instalación local sincroniza a la nube no solo el alta, sino también los cambios de estado (ej: cuando el notario firma y `IN_FIRM_DIGI` pasa a 1). El PDF firmado en sí no se sincroniza automáticamente, pero sí sus metadatos (`DE_RUTA_ARCHI_FIRM`). |

---

## Tabla: `P_FOLI`

### Descripcion funcional
Tabla maestra usada en Legasys para registrar y gestionar el inventario de folios (papel notarial de seguridad) asignados a la notaría, controlando sus rangos o series.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_FOLI` | `int` | Identificador interno. |
| `CO_TIPO_FORM` | `int` | Tipo de formato (ej. Papel Notarial Extraprotocolar, Protocolar). |
| `NU_SERI_INIC` | `varchar(100)` | Serie alfanumérica inicial. |
| `NU_FOLI_INIC` | `varchar(100)` | Número de folio inicial del bloque. |
| `NU_FOJA` | `varchar(100)` | Número de foja vinculada. |
| `NU_SERI_FIN` | `varchar(100)` | Serie alfanumérica final. |
| `NU_FOLI_FIN` | `varchar(100)` | Número de folio final del bloque. |
| `IN_TIPO_FOLI` | `int` | Tipo de folio específico. |
| `CO_USUA_MODI` | `datetime` | Usuario que modificó (Tipo de dato erróneo en BD legacy). |
| `TS_USUA_MODI` | `int` | Timestamp de modificación (Tipo de dato erróneo en BD legacy). |
| `IN_ESTA` | `int` | Estado del registro (Activo, Agotado). |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_FOLI` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Gestiona las "resmas" de papel notarial para su posterior descuento a través de `H_DETA_FOLI` cada vez que se imprime un documento protocolar o extraprotocolar. |

---

## Tabla: `P_FORM_DOCU`

### Descripcion funcional
Tabla usada en Legasys para almacenar las plantillas binarias o formatos estáticos de documentos notariales (ej. escaneos de sellos o fondos de certificados).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_FORM_DOCU` | `int` | Identificador interno. |
| `CO_COMP` | `int` | Compañía/Notaría a la que pertenece. |
| `NO_FORM_DOCU` | `varchar(100)` | Nombre o descripción del formato. |
| `EX_FORM_DOCU` | `varchar(10)` | Extensión del archivo original (ej. JPG, PDF). |
| `IM_FORM_DOCU` | `longblob` | Archivo binario de la imagen o formato. |
| `IN_ESTA` | `int` | Estado (Activo/Inactivo). |
| `CO_USUA_MODI` | `int` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_FORM_DOCU` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | En desuso o uso restringido en la nueva arquitectura de Legasys, reemplazada paulatinamente por plantillas DOCX y rutas S3, pero mantenida para formatos legacy impresos. |

---

## Tabla: `P_GRUP`

### Descripcion funcional
Tabla maestra usada en Legasys para agrupar clientes bajo un mismo paraguas corporativo o consorcio (Grupo Empresarial).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_GRUP` | `int unsigned` | Identificador único del grupo. |
| `CO_COMP` | `int` | Compañía/Notaría. |
| `CO_USUA` | `int` | Usuario administrador o sectorista a cargo del grupo. |
| `NO_GRUP` | `varchar(100)` | Nombre del grupo empresarial. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |
| `IN_TIPO_GRUP` | `int` | Tipo de agrupación. |
| `IN_TEST_WEB` | `int` | Indicador de uso en testeo web o accesos web. |
| `IN_CARG_TEST` | `int` | Indicador de cargo o habilitación de test. |
| `IN_ESTA` | `char(1)` | Estado (Activo/Inactivo). |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_GRUP` | Clave principal de la tabla. |
| Referenciada por | Múltiples | `CO_GRUP` | Es referenciada por `P_CLIE` y `R_GRUP_CLIE`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Vital en la facturación y cobranzas, ya que permite ver la deuda o volumen transaccional consolidado de todas las empresas (P_CLIE) que pertenecen a un mismo holding o consorcio constructor/inmobiliario. |

---

## Tabla: `P_INSE`

### Descripcion funcional
Tabla usada en Legasys como catálogo o diccionario de "Insertos" predefinidos para la generación de minutas y escrituras.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_INSE` | `int` | Identificador interno. |
| `CO_COMP` | `int` | Notaría que posee el inserto. |
| `DE_INSE` | `varchar(150)` | Nombre o título del inserto (ej. Inserto SUNAT, Inserto UIF). |
| `NO_TEXT_INSE` | `text` | Contenido de texto del inserto. |
| `CO_USUA_MODI` | `int` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |
| `IN_ESTA` | `int` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_INSE` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Sirve para inyectar cláusulas legales estáticas u obligatorias en los documentos notariales procesados por el motor documental. |

---

## Tabla: `P_NOTI`

### Descripcion funcional
Tabla usada en Legasys para registrar las "Notificaciones de Sistema" o alertas dirigidas a usuarios internos (campanita de notificaciones de la aplicación web).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_NOTI` | `int` | Identificador interno. |
| `CO_TICK_CONT` | `int` | Ticket o trámite vinculado que generó la alerta. |
| `CO_TICK_SERV` | `int` | Servicio asociado a la notificación. |
| `IN_MODU` | `int` | Módulo del sistema del cual proviene. |
| `DE_NOTI` | `text` | Texto descriptivo de la notificación. |
| `URL_NOTI` | `text` | URL de acción al hacer clic en la alerta. |
| `CO_USUA` | `int` | Usuario destinatario de la notificación. |
| `FE_NOTI` | `datetime` | Fecha y hora en la que se generó la alerta. |
| `IN_TIPO` | `int` | Tipo de notificación (Info, Error, Warning, Success). |
| `IN_REVI` | `int` | Indicador de si ya fue leída/revisada por el usuario (0=No, 1=Sí). |
| `IN_ESTA` | `int` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_NOTI` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Es la tabla que alimenta el menú superior de notificaciones para los usuarios de la notaría, útil para flujos de trabajo asíncronos o alertas de aprobaciones pendientes. |

---

## Tabla: `P_PAGO_DOCU`

### Descripcion funcional
Tabla usada en Legasys para almacenar el detalle documental de un pago (como referencias de cheques, transferencias, bouchers), usada de forma satelital a las transacciones de caja.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PAGO_DOCU` | `int` | Identificador interno. |
| `CO_FORM_PAGO_CAJA` | `int` | Forma de pago en caja. |
| `CO_TIPO_MONE` | `int` | Moneda del pago. |
| `CO_TIPO_TARJ` | `int` | Tipo de tarjeta (si aplica). |
| `CO_BANC_CAJA` | `int` | Banco asociado a la transacción. |
| `FE_PAGO_DOCU` | `date` | Fecha del documento de pago. |
| `NU_PAGO` | `decimal(12,2)` | Monto del pago asociado al documento. |
| `NU_CUEN` | `varchar(100)` | Número de cuenta bancaria. |
| `NU_CHEQ` | `varchar(100)` | Número de cheque bancario. |
| `NU_TARJ` | `varchar(100)` | 4 últimos dígitos u ofuscación de la tarjeta. |
| `NU_VAUC` | `varchar(100)` | Número de operación o voucher. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de registro/modificación. |
| `CO_USUA_MODI` | `int` | Usuario que registró/modificó. |
| `IN_ESTA` | `char(1)` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PAGO_DOCU` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Almacena el desglose de los medios de pago bancarizados para conciliación contable. |

---

## Tabla: `P_PIC`

### Descripcion funcional
Tabla maestra "Parte, Índice y Certificado (PIC)". Sirve como bandeja central para la gestión, emisión y archivo de los partes notariales, testimonios o copias certificadas derivados de los instrumentos notariales, y su posterior envío a RRPP (Registros Públicos).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PIC` | `int unsigned` | Identificador principal del registro PIC. |
| `CO_ORIG_PIC` | `int unsigned` | Origen (ej. Escritura Pública, Acta Extraprotocolar). |
| `CO_CLAS_PIC` | `int unsigned` | Clasificación o naturaleza del PIC. |
| `CO_COMP` | `int unsigned` | Notaría que expide. |
| `CO_ENTI` | `int unsigned` | Entidad de destino (ej. SUNARP, Ministerio de RR.EE.). |
| `CO_DEPA` | `int unsigned` | Departamento o subdivisión interna de origen. |
| `FE_PIC` | `date` | Fecha de expedición del parte/testimonio. |
| `IM_PIC` | `varchar(50)` | Identificador o ruta de la imagen o PDF principal. |
| `DE_ARCH` | `longblob` | Archivo binario incrustado (Uso limitado/Legacy). |
| `DE_TIPO` | `varchar(150)` | Extensión o tipo mime del archivo. |
| `DE_PIC` | `text` | Descripción o glosa del Parte/Certificado. |
| `CO_SERV_ALTE` | `int unsigned` | Servicio alterno asociado. |
| `DE_REFE` | `varchar(100)` | Referencia libre (ej. Nombre del mensajero o gestor). |
| `CO_USUA_MODI` | `int unsigned` | Usuario responsable. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |
| `IN_ESTA` | `char(1)` | Estado del PIC (Expedido, Presentado a RRPP, Anulado). |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PIC` | Clave principal de la tabla. |
| Foreign Key | `CO_ORIG_PIC` | `CO_ORIG_PIC` | Referencia a `A_ORIG_PIC.CO_ORIG_PIC`. |
| Foreign Key | `CO_CLAS_PIC` | `CO_CLAS_PIC` | Referencia a `A_CLAS_PIC.CO_CLAS_PIC`. |
| Foreign Key | `CO_COMP` | `CO_COMP` | Referencia a `A_COMP.CO_COMP`. |
| Foreign Key | `CO_ENTI` | `CO_ENTI` | Referencia a `A_ENTI_PIC.CO_ENTI`. |
| Foreign Key | `CO_DEPA` | `CO_DEPA` | Referencia a `A_DEPA.CO_DEPA`. |
| Referenciada por | `H_PIC_PRTC` | `CO_PIC` | Es referenciada por `H_PIC_PRTC.CO_PIC`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Base del módulo PIC (o Despacho Notarial). Aquí se orquestan los documentos finales (Testimonios y Partes) que salen hacia Registros Públicos, Bancos o los propios clientes, manteniendo un control estricto (Kardex de salida). |

---

## Tabla: `P_PRTC`

### Descripcion funcional
Tabla maestra de "Participantes" (Comparecientes, Otorgantes, Intervinientes). Sirve como índice principal para conectar los datos de filiación de una persona/empresa en los instrumentos notariales.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CUP` | `int unsigned` | Código Único de Participante (Llave primaria). |
| `CO_TIPO_PERS` | `int unsigned` | Tipo de persona (Natural o Jurídica). |
| `NS_ULTI_PRTC` | `int unsigned` | Secuencial de última versión de datos personales. |
| `NS_ULTI_DIRE` | `int unsigned` | Secuencial de última versión de dirección. |
| `NO_CORT` | `varchar(500)` | Nombre completo o Razón Social (Denominación corta/búsqueda). |
| `DE_CORR` | `varchar(200)` | Correo electrónico principal de contacto. |
| `IM_FIRMA` | `longblob` | Imagen de firma escaneada o biométrica. |
| `IN_ESTA` | `char(1)` | Estado del participante. |
| `IN_VIP` | `int` | Indicador si es un participante VIP. |
| `CO_USUA_VIP` | `int` | Usuario que lo marcó como VIP. |
| `FE_USUA_VIP` | `date` | Fecha de marcación como VIP. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CUP` | Clave principal de la tabla. |
| Foreign Key | `CO_TIPO_PERS` | `CO_TIPO_PERS` | Referencia a `A_TIPO_PERS_type.CO_TIPO_PERS`. |
| Referenciada por | Múltiples | `CUP` | Es referenciada ampliamente por `H_PRTC_DIRE`, `H_PRTC_JURI`, `H_PRTC_NATU`, `R_PRTC_TRAM`, etc. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Diseño polimórfico. Solo guarda la "Cáscara". Los datos reales y específicos residen en `H_PRTC_NATU` (si es persona natural) o `H_PRTC_JURI` (si es empresa), amarrados por el `CUP`. |

---

## Tabla: `P_SERV`

### Descripcion funcional
Tabla maestra de "Servicios" o actos jurídicos ofrecidos por la Notaría. Es el corazón del sistema, ya que dicta las reglas de negocio, plantillas y precios de cada trámite.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_SERV` | `int unsigned` | Código único de servicio. |
| `CO_TIPO_ACTO_JURI` | `int` | Categoría del acto jurídico. |
| `DE_SERV` | `varchar(100)` | Descripción o nombre completo del servicio. |
| `DC_SERV` | `varchar(30)` | Descripción corta o abreviatura. |
| `CO_ACTO_JURI` | `varchar(4)` | Código estandarizado del acto. |
| `DE_OBSE` | `text` | Observaciones o requisitos. |
| `CO_CLAS` | `varchar(2)` | Clasificación interna. |
| `ID_SUNA` | `char(1)` | Exige pase por SUNAT (PDT Notarios). |
| `ID_SAT` | `char(1)` | Exige pase por SAT (Impuesto Alcabala/Vehicular). |
| `ID_UIF` | `char(1)` | Reportable a UIF (Prevención Lavado de Activos). |
| `ID_DEUD` | `char(1)` | Bloquea si cliente tiene deuda. |
| `ID_CUAN` | `char(1)` | Requiere cuantía (precio o tasación del bien) obligatoria. |
| `ID_CERT` | `int` | Exige identificación biométrica/certificados obligatorios. |
| `ID_IMPU` | `char(1)` | Sujeto a impuestos notariales específicos. |
| `CO_MODU` | `int unsigned` | Módulo al que pertenece (Legal, Operaciones, etc.). |
| `CO_REGI_SUNA` | `int unsigned` | Equivalencia en SUNAT. |
| `CO_REGI_NOTA` | `int unsigned` | Equivalencia en Colegio de Notarios. |
| `CO_REGI_PDT` | `char(2)` | Código en PDT SUNAT. |
| `CO_REGI_UIF` | `varchar(3)` | Código de acto para ROEL/UIF. |
| `IN_IPNP_UIF` | `varchar(5)` | Parámetro UIF específico. |
| `IN_UMBR_UIF` | `char(1)` | Valida umbral mínimo para reporte UIF. |
| `CO_ACTO_REGI` | `varchar(5)` | Código de acto registral SUNARP. |
| `CO_LIBR_REGI` | `int unsigned` | Libro Registral SUNARP asociado. |
| `DE_TRAM_LINE` | `text` | Descripción para trámite en línea. |
| `IN_INGR_PRTC` | `char(1)` | Habilita ingreso de participantes. |
| `IN_BLOQ_CAJA` | `int` | Bloquea trámite si no está pagado en caja. |
| `IN_IMPR_CAJA` | `int` | Imprime ticket de caja automáticamente. |
| `IN_GENE_MINU` | `int` | Servicio genera minuta automáticamente. |
| `IN_TIPO_ADVE_SERV` | `int` | Lanza advertencia específica al generar. |
| `IN_OTOR` | `int` | Número mínimo de otorgantes. |
| `IN_BENE` | `int` | Número mínimo de beneficiarios/adquirentes. |
| `IN_ACLA` | `int` | Indicador si permite aclaratorias. |
| `IN_CUAN_PAGO` | `int` | Validación de cuantía vinculada al pago. |
| `CO_USUA_MODI` | `int unsigned` | Usuario que modificó. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |
| `IN_ESTA` | `char(1)` | Estado (Activo/Inactivo). |
| `IN_PART_ELEC` | `char(1)` | Habilita Parte Electrónico SUNARP. |
| `IN_ENVI_INFO` | `int` | Habilita el envío masivo de información. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_SERV` | Clave principal de la tabla. |
| Foreign Key | `CO_MODU` | `CO_MODU` | Referencia a `A_MODU_type.CO_MODU`. |
| Foreign Key | `CO_REGI_NOTA` | `CO_REGI_NOTA` | Referencia al catálogo de actos de la Junta de Decanos. |
| Referenciada por | Múltiples | `CO_SERV` | Es referenciada por `H_REQU_SERV`, `H_SERV_ALTE`, `P_TRAM`, `R_SERV_CPTO_TARI`, etc. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Según las reglas del Kardex, cambiar el `P_SERV` principal de un trámite en borrador ocasiona que todas sus tablas dependientes (`H_TRAM_TRAF`, `H_PRES_TICK`, etc.) pasen a `IN_ESTA = 0` para forzar la recarga de la plantilla de precios y reglas del nuevo servicio. |

---

## Tabla: `P_TARI`

### Descripcion funcional
Tabla catálogo de Tarifas y Precios aplicados a los diferentes conceptos que conforman un servicio.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TARI` | `int unsigned` | Identificador interno. |
| `MO_IMPO` | `decimal(8,2)` | Monto o importe de la tarifa. |
| `CO_USUA_MODI` | `int unsigned` | Usuario creador/modificador. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |
| `IN_ESTA` | `char(1)` | Estado de la tarifa. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TARI` | Clave principal de la tabla. |
| Referenciada por | `R_SERV_CPTO_TARI` | `CO_TARI` | Es referenciada por `R_SERV_CPTO_TARI.CO_TARI`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Legasys relaciona el `P_SERV` con el `P_CPTO` usando la matriz tarifaria, cuyo precio base lo da `P_TARI`. Para conceptos libres de precio 0.00, se debe crear la relación a una tarifa existente equivalente a cero o crearla si no existe. |

---

## Tabla: `P_TICK`

### Descripcion funcional
Tabla maestra "Ticket / Orden de Trabajo". Agrupa y consolida todos los servicios (`P_TRAM`), documentos, facturas y tareas operativas asociadas a una misma solicitud o cliente en un solo lugar.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TICK_CONT` | `int unsigned` | Identificador único del contenedor de ticket. |
| `CO_CLIE` | `int unsigned` | Cliente o solicitante principal. |
| `CO_ABOG_EXTE` | `int unsigned` | Abogado externo asociado al cliente. |
| `CO_MODU` | `int unsigned` | Módulo por defecto (Legal/Operaciones). |
| `CO_TDOC` | `int` | Tipo de documento para facturación base. |
| `CO_FORM_PAGO_CAJA` | `int` | Forma de pago predeterminada. |
| `CO_CLIE_MAIL` | `int` | Correo a usar para notificaciones del ticket. |
| `CO_CLIE_TELF` | `int` | Teléfono de contacto del ticket. |
| `CO_GRUP` | `int` | Grupo empresarial responsable. |
| `CO_FUNC_CLIE` | `int` | Funcionario del cliente (contacto directo). |
| `CO_FUNC_PROD` | `int` | Funcionario de la notaría responsable. |
| `CO_TIPO_PROY` | `int` | Tipo de proyecto (Masivo/Especial). |
| `IN_LINE_CRED` | `smallint` | Indica si el ticket usará línea de crédito. |
| `CO_PRES_TERC` | `int` | Prestador o tercero involucrado. |
| `NU_KARD` | `varchar(30)` | Número oficial de KARDEX notarial. |
| `FE_CREA_KARD` | `datetime` | Fecha oficial de apertura de KARDEX. |
| `FE_CREA_TICK` | `datetime` | Fecha de creación interna en sistema. |
| `NU_MINU` | `varchar(12)` | Número de minuta asociada (si aplica a todo el ticket). |
| `FE_MINU` | `date` | Fecha de la minuta principal. |
| `NU_ESCR` | `varchar(12)` | Número de escritura pública asociada. |
| `FE_ESCR` | `date` | Fecha de la escritura. |
| `DE_PROC` | `varchar(200)` | Procedencia del expediente. |
| `DE_EXPE` | `varchar(100)` | Número de expediente físico/bancario. |
| `CO_ABOG_EXTR` | `int` | Abogado externo secundario. |
| `NO_ABOG_EXTE` | `varchar(190)` | Nombre manual del abogado externo. |
| `NO_ORDE_TRAB` | `varchar(90)` | Número de orden de trabajo (Bancos). |
| `CO_USUA_ABOG` | `int unsigned` | Abogado de la notaría asignado al ticket. |
| `CO_USUA_DIGI` | `int unsigned` | Digitador/Asistente asignado. |
| `CO_COMP` | `int unsigned` | Notaría matriz. |
| `ID_IMPU` | `char(1)` | Afectación de impuestos. |
| `IN_MAIL` | `char(1)` | Autoriza envío de correos. |
| `DE_MAIL_NOTI` | `varchar(200)` | Correo de notificación. |
| `DE_CELU_NOTI` | `varchar(10)` | Celular de notificación. |
| `IN_TIPO_PAGO` | `int` | Tipo de pago preferencial. |
| `CO_USUA_MODI` | `int unsigned` | Usuario creador/modificador. |
| `TS_USUA_MODI` | `datetime` | Fecha de modificación. |
| `IN_ESTA` | `char(1)` | Estado del ticket (Activo/Anulado/Terminado). |
| `IN_NUEV` | `char(1)` | Indicador de recién creado. |
| `IN_EDIT` | `char(1)` | Indicador de edición actual (Bloqueo lógico). |
| `IN_COBR_DISP` | `char(1)` | Bandera de cobranza disponible. |
| `IN_COBR_ACUM` | `char(1)` | Bandera de cobro acumulado. |
| `IN_COBR_RAPI` | `char(1)` | Habilita caja rápida. |
| `IN_TRAN` | `char(1)` | Indicador de transferencia o migración. |
| `IN_CHEC_VB` | `char(1)` | Indicador de Visto Bueno (Abogado). |
| `FE_CHEC_VB` | `datetime` | Fecha del Visto Bueno. |
| `IN_PAGO_CAJA` | `smallint` | Estado de pago general en caja. |
| `IN_ENVI_DOMI` | `int` | Requiere envío de documentos a domicilio. |
| `IN_PDF_COMP` | `int` | PDF completado y disponible. |
| `TELF_ENVI_DOMI` | `varchar(15)` | Teléfono para el currier. |
| `NU_ORDE_PERU_NOTA` | `int` | ID Orden Perú Notario. |
| `NU_LOTE_PERU_NOTA` | `int` | ID Lote Perú Notario. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TICK_CONT` | Clave principal de la tabla. |
| Foreign Key | `CO_TICK_CONT` | `CO_TICK_CONT` | Referencia a `P_TICK_CONT.CO_TICK_CONT`. |
| Foreign Key | `CO_CLIE` | `CO_CLIE` | Referencia a `P_CLIE.CO_CLIE`. |
| Referenciada por | `R_TICK_SERV` | `CO_TICK_CONT` | Es referenciada por `R_TICK_SERV.CO_TICK_CONT`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | "El Ticket" es la carpeta física del cliente, pero en versión digital. Puede contener 1 solo servicio (ej. 1 Kardex de Compraventa) o 10 servicios (ej. 10 Legalizaciones en Operaciones). Al guardar/crear un ticket, los datos del cliente se normalizan forzosamente a MAYÚSCULAS en los campos de captura (regla de módulo). |

---

## Tabla: `P_TICK_CONT`

### Descripcion funcional
Tabla generadora o secuenciador principal de los contenedores de Tickets para la notaría. Separa los correlativos anuales.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TICK_CONT` | `int unsigned` | Identificador interno absoluto. |
| `CO_TIPO_SUCU` | `int unsigned` | Sucursal (Sede de la notaría). |
| `CO_COMP` | `int unsigned` | Compañía/Notaría. |
| `NU_ANIO` | `int unsigned` | Año de apertura del ticket. |
| `NU_TICK` | `int unsigned` | Correlativo autogenerado anual. |
| `NU_ORDE` | `varchar(50)` | Número de orden formal compuesto. |
| `CO_TICK_CONT_ORIG` | `int` | Ticket origen (si fue clonado o desglosado). |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TICK_CONT` | Clave principal de la tabla. |
| Referenciada por | `P_TICK` | `CO_TICK_CONT` | Es referenciada por la cabecera operativa `P_TICK`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Evita que los tickets de distintas notarías (o sucursales en un futuro) choquen en numeración, manteniendo un correlativo local limpio por año. |

---

## Tabla: `P_TOKE_API`

### Descripcion funcional
Tabla usada en Legasys para registrar llaves (API Tokens) otorgados a clientes B2B (bancos, concesionarias) para que puedan inyectar trámites vía API externa.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TOKE_API` | `int` | Identificador interno. |
| `NO_RESP_API` | `varchar(250)` | Nombre del desarrollador o responsable de la empresa. |
| `NO_TOKE_API` | `varchar(200)` | Token JWT o Hash estático provisto. |
| `CO_COMP` | `int` | Notaría que provee el acceso. |
| `CO_CLIE` | `int` | Cliente empresarial amarrado al token. |
| `CO_GRUP` | `int` | Grupo amarrado. |
| `CO_ABOG` | `int` | Abogado default al que caerán los trámites. |
| `IN_ESTA` | `int` | Estado del token (Activo, Revocado). |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TOKE_API` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Utilizado por la API REST de interconexión con sistemas bancarios o inmobiliarios para crear tickets masivos en la cola de Legasys sin intervención humana. |

---

## Tabla: `P_TRAM`

### Descripcion funcional
Tabla maestra de "Trámite / Servicio específico". Es el KARDEX propiamente dicho o la línea de servicio contratada por el cliente dentro de su Ticket.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TICK_SERV` | `int unsigned` | Código único de Kardex/Servicio. |
| `CO_COLA_TICK` | `int` | Ubicación o prioridad en la cola de atención. |
| `NU_ANIO_TRAM` | `int unsigned` | Año de la solicitud de trámite. |
| `NU_ANIO_CONT` | `year` | Año contable asignado. |
| `NU_TRAM` | `int unsigned` | Correlativo interno o N° de Kardex. |
| `IN_KARD` | `char(1)` | Indicador si generó número de Kardex oficial. |
| `NU_CTRL` | `varchar(30)` | Código único de control notarial (Uso interno). |
| `CO_COMP` | `int unsigned` | Notaría encargada. |
| `IN_NUEV` | `char(1)` | Indicador de trámite recién abierto. |
| `IN_EDIT` | `char(1)` | En uso o edición (Semáforo lógico). |
| `CO_SERV` | `int unsigned` | Servicio asociado (`P_SERV`). |
| `NU_INST` | `int unsigned` | Número de instrumento o escritura. |
| `FE_ESCR_TRAM` | `date` | Fecha oficial de la escritura. |
| `NU_MINU_INTE` | `varchar(100)` | Número de minuta u oficio ingresado. |
| `FE_MINU_TRAM` | `date` | Fecha de la minuta base. |
| `CO_REGI_NOTA` | `int unsigned` | Acto notarial del colegio de notarios. |
| `CO_VENT_RRPP` | `int` | Ventanilla SUNARP asignada. |
| `CO_OFIC_REGI_SUNA` | `int` | Oficina registral de SUNARP. |
| `NU_FORM` | `varchar(30)` | Formulario notarial. |
| `CO_SEMI_INST` | `int unsigned` | Semilla o serie del instrumento. |
| `IN_MINU` | `char(1)` | Tramite requiere minuta. |
| `IN_ACLA` | `int` | Es un trámite aclaratorio o rectificación. |
| `IN_ESTA_CNL` | `int` | Estado ante el Colegio de Notarios de Lima. |
| `IN_PART_DIGI` | `int` | Requiere presentación por Parte Digital. |
| `IN_ENVI_PART_DIGI` | `int` | Fue enviado por Parte Digital. |
| `NU_SOLI_INCRI_SUNA` | `varchar(20)` | N° Solicitud Inscripción SUNARP. |
| `CO_ETAP_TRAM` | `int unsigned` | Etapa actual del flujo notarial (Borrador, Firmas, Terminado). |
| `CO_SITU_TRAM` | `int` | Situación (Concluido, Anulado, Observado). |
| `NU_FOLI` | `int` | Cantidad de folios del instrumento. |
| `FE_CONC` | `datetime` | Fecha de conclusión. |
| `IN_EMIT_PART` | `int` | Permite o emitió partes. |
| `CO_COMP_SUST` | `int` | Notaría que sustituye/aclara (si aplica). |
| `MO_SALD_REGI` | `decimal(11,2)` | Saldo o déficit registral a favor/en contra. |
| `IN_FIRM_DIGI` | `int` | Estado firma digital notario. |
| `IN_TIPO_UIF` | `int` | Estado de verificación por Lavado de Activos. |
| `IN_POSI_QR` | `int` | Posicionamiento del sello QR. |
| `IN_TERM_COLA_TICK` | `int` | Finalizó en su cola de despacho. |
| `IN_APRO_ROBO` | `int` | Aprobado por proceso automatizado/Robótica. |
| `IN_SID_SUNA` | `int` | Marcado para envío por SID-SUNARP. |
| `IN_REVI` | `int` | Estado de revisión de matriz. |
| `IN_ENVI_CORR` | `int` | Enviado correo de culminación. |
| `IN_OBSE_PERU_NOTA` | `int` | Estado observación en Colegio Notarios. |
| `IN_BIEN_FUTU` | `int` | Compraventa es sobre bien futuro. |
| `IN_APRO_REGI` | `int` | Aprobación por registros públicos. |
| `IN_TIPO_COMP_FINA` | `int` | Estado en base de datos financiera. |
| `IN_ARCH` | `int` | Enviado a Archivo Central / Bóveda. |
| `IN_MUNI_IA` | `int` | Procesado por IA Legasys. |
| `IN_VALI` | `int` | Validación biométrica. |
| `CO_USUA_MODI` | `int unsigned` | Modificado por. |
| `TS_USUA_MODI` | `datetime` | Última actualización. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TICK_SERV` | Clave principal de la tabla. |
| Unique | `NU_CTRL` | `NU_CTRL` | Número de control único. |
| Foreign Key | `CO_TICK_SERV` | `CO_TICK_SERV` | Referencia puente de `R_TICK_SERV.CO_TICK_SERV`. |
| Referenciada por | Múltiples | `CO_TICK_SERV` | Centro absoluto del módulo Legal y Operaciones. Referenciada por `H_DOCU_EXTE`, `H_SGMT_ORLC`, `R_PRTC_TRAM`, tablas vehiculares, etc. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Este registro representa a la escritura pública o al trámite extraprotocolar en vida. Nota clave sobre `FE_ESCR_TRAM`: A pesar del nombre, en Legasys este valor se obtiene dinámicamente desde los campos configurables (`H_CODO.CO_TIPO_CAMP = 4`) durante la edición del borrador, no depender únicamente de este campo rígido de tabla. |

---

## Tabla: `P_USUA`

### Descripcion funcional
Tabla maestra de "Usuarios", que contiene al personal administrativo, cajeros, abogados y notarios que utilizan e inician sesión en el sistema Legasys.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_USUA` | `int` | Código único de usuario. |
| `CO_TIPO_USUA` | `int unsigned` | Rol o tipo de usuario (Admin, Cajero, Abogado, Notario). |
| `CO_COMP` | `int unsigned` | Notaría a la que pertenece. |
| `CO_TIPO_AREA` | `int` | Área funcional donde trabaja. |
| `CO_GRUP_USUA` | `int` | Grupo al que pertenece. |
| `ID_USUA` | `varchar(20)` | Nombre de usuario o slug de inicio de sesión. |
| `CL_USUA` | `varchar(50)` | Contraseña (Legacy format, ofuscado/MD5). |
| `NO_USUA` | `varchar(150)` | Nombres y Apellidos completos. |
| `NU_TOKE_CELU` | `varchar(50)` | Token OTP para validación celular. |
| `DE_DIRE` | `varchar(150)` | Dirección domiciliaria. |
| `CO_UBIG` | `varchar(6)` | Ubigeo de domicilio. |
| `DE_MAIL` | `varchar(50)` | Correo corporativo del trabajador. |
| `DE_CELU` | `varchar(12)` | Celular. |
| `DE_TELE` | `varchar(12)` | Teléfono fijo. |
| `NU_RUC` | `varchar(12)` | RUC del trabajador. |
| `NU_DNI` | `varchar(10)` | DNI del trabajador. |
| `FE_NACI` | `date` | Fecha de nacimiento. |
| `IN_INIC_USUA` | `char(3)` | Iniciales para firmas o sellos en documentos. |
| `IN_ENVI_FOTO` | `char(1)` | Indicador si proporcionó foto/firma. |
| `IN_ACTI` | `int` | Estado del usuario Activo/Inactivo. |
| `IN_NOTA` | `int` | Indicador si este usuario "Es el Notario". |
| `FE_ACTU_ACTI` | `datetime` | Último login o actualización. |
| `CO_USUA_MODI` | `int unsigned` | Creador del usuario. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de creación/edición. |
| `IN_ESTA` | `char(1)` | Estado en base de datos. |
| `CL_USUA_HASH` | `varchar(255)` | Contraseña segura en formato Bcrypt/Argon. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_USUA` | Clave principal de la tabla. |
| Foreign Key | `CO_TIPO_USUA` | `CO_TIPO_USUA` | Referencia a `A_TIPO_USUA_type.CO_TIPO_USUA`. |
| Referenciada por | Múltiples | `CO_USUA` | Es referenciada por todo el sistema para logs, como en `H_SGMT_LOG.CO_USUA`, y asignaciones. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | La tabla contiene usuarios de todas las notarías que usan la instancia SaaS. Por ello, el módulo `mantenimiento/usuarios` debe abrir SIEMPRE filtrando por el `CO_COMP` de la sesión actual por seguridad. (Ojo: `CO_TIPO_USUA = 4` autoriza a cambiar servicios principales del Kardex). |

---

## Tabla: `R_ABOG_ASIS`

### Descripcion funcional
Tabla relacional que asigna (mapea) a los abogados principales con sus asistentes, digitadores o procuradores a cargo.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ABOG_ASIS` | `int` | Identificador interno de la relación. |
| `CO_USUA_ABOG` | `int` | Identificador del Abogado (de `P_USUA`). |
| `CO_USUA_ABOG_ASIS` | `int` | Identificador del Asistente/Digitador (de `P_USUA`). |
| `IN_TIPO` | `smallint` | Tipo de dependencia/relación jerárquica. |
| `CO_USUA_MODI` | `int` | Administrador que generó la relación. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de vinculación. |
| `IN_ESTA` | `smallint` | Estado de la relación (Activa/Inactiva). |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ABOG_ASIS` | Clave principal de la tabla. |
| Foreign Key | `CO_USUA_ABOG` | `CO_USUA_ABOG` | Referencia a `P_USUA.CO_USUA`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Utilizada en el módulo de distribución de Kardex para sugerir o restringir qué digitador puede ver, redactar o corregir los borradores (`H_DOCU_EXTE`) asignados a la bandeja de un abogado en específico. |

---

## Tabla: `R_ACLA_TRAM`

### Descripcion funcional
Tabla relacional usada en Legasys para vincular un trámite (Kardex) nuevo que nace como "Aclaratoria" o "Rectificación" con el instrumento o escritura original al que está afectando.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ACLA_TRAM` | `int` | Identificador interno. |
| `CO_TICK_SERV` | `int` | Trámite/Kardex actual (Aclaratoria). |
| `CO_TICK_SERV_SUB` | `int` | Subservicio asociado. |
| `CO_COMP` | `int` | Notaría actual. |
| `CO_COMP_ACLA` | `int` | Notaría de origen del documento a aclarar (puede ser otra). |
| `NU_INST` | `varchar(20)` | Número de instrumento/escritura a aclarar. |
| `FE_INST` | `varchar(20)` | Fecha del instrumento original. |
| `CO_USUA_MODI` | `int` | Usuario que registró el vínculo. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de vinculación. |
| `IN_ESTA` | `int` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ACLA_TRAM` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Permite al notario dejar constancia de que la escritura presente no es independiente, sino que subsana errores materiales u omisiones de un instrumento previo (`NU_INST`). |

---

## Tabla: `R_CABE_DETR`

### Descripcion funcional
Tabla relacional para asociar pagos de detracciones (SUNAT) a los comprobantes de caja emitidos que superan los umbrales legales.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CABE_DETR` | `int` | Identificador interno. |
| `CO_CABE_CAJA` | `int` | Comprobante de pago principal. |
| `IN_PAGO_DETR` | `int` | Estado de pago de la detracción. |
| `CO_USUA_MODI` | `int` | Usuario que registró el depósito. |
| `TS_USUA_MODI` | `datetime` | Fecha de modificación. |
| `IN_ESTA` | `int` | Estado del registro. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CABE_DETR` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Clave para el cierre contable mensual y evitar multas de SUNAT por servicios gravados que superan los topes normativos en notaría. |

---

## Tabla: `R_CAJA_COBR`

### Descripcion funcional
Tabla relacional para la gestión de "Cobranzas" de comprobantes emitidos a crédito.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CAJA_COBR` | `int` | Identificador interno. |
| `CO_CABE_CAJA` | `int` | Comprobante o factura por cobrar. |
| `CO_COBR` | `int` | Cobrador o gestor de cartera asignado. |
| `CO_FUNC_CLIE` | `int` | Contacto del cliente encargado del pago. |
| `FE_CAJA_COBR` | `date` | Fecha programada o realizada de la cobranza. |
| `CO_USUA_MODI` | `int` | Usuario que registró la gestión. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |
| `IN_ESTA` | `char(1)` | Estado (Pendiente, Gestionado). |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CAJA_COBR` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Permite llevar trazabilidad de las llamadas o gestiones a clientes morosos antes del pago definitivo. |

---

## Tabla: `R_CAJA_FORM_PAGO`

### Descripcion funcional
Tabla relacional para desglosar o "hacer split" de las formas de pago de un mismo comprobante en Caja.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CAJA_FORM_PAGO` | `int` | Identificador interno. |
| `CO_CABE_CAJA` | `int unsigned` | Comprobante de pago principal (`P_CABE_CAJA`). |
| `CO_FORM_PAGO_CAJA` | `int unsigned` | Forma de pago parcial (Efectivo, Tarjeta, Depósito). |
| `CO_BANC_CAJA` | `int unsigned` | Banco receptor (si es depósito). |
| `CO_CUEN_BANC` | `int` | Cuenta bancaria notarial. |
| `CO_TIPO_TARJ` | `int` | Tipo o marca de tarjeta (Visa, MC). |
| `NU_PAGO` | `varchar(12)` | Monto pagado con esta forma específica. |
| `FE_CABE_CAJA` | `date` | Fecha del comprobante. |
| `FE_PAGO` | `date` | Fecha en la que ingresó este abono específico. |
| `IN_TIPO_CAJA` | `smallint` | Tipo de caja receptora. |
| `CO_USUA_CREA` | `int` | Cajero que cobró. |
| `TS_USUA_CREA` | `datetime` | Timestamp del cobro. |
| `NU_TARJ` | `varchar(12)` | Últimos dígitos de tarjeta. |
| `IN_ESTA` | `smallint` | Estado de la porción de pago. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CAJA_FORM_PAGO` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Crucial para la liquidación de caja. Por ejemplo: Un comprobante de 1000 soles puede tener 2 registros aquí (500 en efectivo y 500 en tarjeta), permitiendo el cuadre exacto por medio de pago al final del turno. |

---

## Tabla: `R_CAJA_PAGO`

### Descripcion funcional
Tabla relacional que asocia los pagos documentados (`P_PAGO_DOCU`) con el comprobante de caja final.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CAJA_PAGO` | `int` | Identificador interno. |
| `CO_PAGO_DOCU` | `int` | Documento de pago (Voucher/Cheque). |
| `CO_CABE_CAJA` | `int` | Comprobante de caja. |
| `CO_COBR` | `int` | Referencia de cobranza. |
| `MO_PAGO` | `decimal(15,2)` | Monto imputado al comprobante. |
| `TS_USUA_MODI` | `datetime` | Fecha de imputación. |
| `CO_USUA_MODI` | `int` | Usuario vinculador. |
| `IN_ESTA` | `char(1)` | Estado. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CAJA_PAGO` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Permite "partir" un solo depósito bancario gigante (`P_PAGO_DOCU`) y distribuirlo o saldar múltiples facturas (`P_CABE_CAJA`). |

---

## Tabla: `R_CARP_TICK`

### Descripcion funcional
Tabla relacional usada para estructurar los archivos, minutas u oficios adjuntos al expediente virtual o "Carpeta" del ticket.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CARP_TICK` | `int` | Identificador de archivo. |
| `CO_TICK_SERV` | `int` | Trámite/Servicio al que pertenece. |
| `CO_SGMT_ORLC` | `int` | Seguimiento o estado de origen. |
| `CO_UPDA_DIGI` | `int` | Vinculación a repositorio digital de IA. |
| `NU_ANIO` | `varchar(4)` | Año de subida. |
| `NU_MES` | `varchar(2)` | Mes de subida. |
| `NU_DIA` | `varchar(2)` | Día de subida. |
| `DE_CARP_TICK` | `varchar(200)` | Nombre o título del documento. |
| `EX_CARP_TICK` | `varchar(100)` | Extensión del archivo original (PDF, DOCX). |
| `PE_CARP_TICK` | `varchar(100)` | Tamaño o peso del archivo. |
| `FI_TEMP_ARCH` | `longblob` | Archivo binario temporal (Legacy). |
| `CO_USUA_MODI` | `int` | Usuario que subió el documento. |
| `TS_USUA_MODI` | `datetime` | Timestamp de subida. |
| `IN_ESTA` | `int` | Estado del archivo. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CARP_TICK` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Es el archivador digital interno de la notaría para adjuntar DNIs, Partidas, Planos y Minutas base al flujo de trabajo del Abogado. |

---

## Tabla: `R_CLIE_TARI`

### Descripcion funcional
Tabla relacional para asignar listas de precios personalizadas, convenios o descuentos especiales a un cliente empresarial.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CLIE_TARI` | `int unsigned` | Identificador interno. |
| `CO_TIPO_TARI` | `int unsigned` | Tipo de tarifa o convenio de precios. |
| `CO_CLIE` | `int unsigned` | Cliente beneficiado (`P_CLIE`). |
| `IN_ESTA` | `char(1)` | Estado de vigencia del convenio. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CLIE_TARI` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Permite sobreescribir la tarifa normal (`P_TARI`) al momento de liquidar y presupuestar si el cliente (Ej. un Banco o Constructora) tiene precios pactados por volumen. |

---

## Tabla: `R_CODO_KARD`

### Descripcion funcional
Tabla relacional para almacenar el valor capturado de los campos dinámicos (Controles de Documento - `H_CODO`) para un Kardex/Trámite específico.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_CODO_KARD` | `int unsigned` | Identificador interno. |
| `CO_CODO` | `int unsigned` | El campo o control dinámico asociado. |
| `CO_TICK_SERV` | `int unsigned` | El Kardex o trámite donde se captura. |
| `NU_KARD` | `varchar(30)` | Número oficial del Kardex. |
| `VA_CONC` | `varchar(100)` | El valor digitado o seleccionado por el usuario. |
| `TS_USUA_MODI` | `date` | Fecha de captura. |
| `CO_USUA_MODI` | `int unsigned` | Usuario digitador. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_CODO_KARD` | Clave principal de la tabla. |
| Foreign Key | `CO_CODO` | `CO_CODO` | Referencia al esquema dinámico `H_CODO`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Regla crítica: Esta tabla actúa como metadata extendida del Kardex. Por ejemplo, según AGENTS.md, la fecha real de la escritura (`FE_ESCR_TRAM`) o el monto de la transferencia muchas veces se resuelve cruzando el valor de `VA_CONC` para el `H_CODO.CO_TIPO_CAMP = 4`. Es vital para el motor Twig a la hora de inyectar variables al DOCX. |

---

## Tabla: `R_DESP_NOTA`

### Descripcion funcional
Tabla relacional para el control del "Despacho Notarial", gestionando la salida física o electrónica de Partes, Testimonios y Boletas desde la Notaría hacia su destino (gestores, clientes, courier).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DESP_NOTA` | `int` | Identificador interno. |
| `CO_TICK_SERV` | `int` | Trámite finalizado. |
| `CO_ETAP_TRAM` | `int` | Etapa de finalización. |
| `CO_DETA_CAJA` | `int` | Detalle de caja asociado (Pago del despacho). |
| `CO_USUA` | `int` | Usuario encargado del despacho. |
| `FE_DESP_NOTA` | `date` | Fecha de salida. |
| `HO_DESP_NOTA` | `varchar(10)` | Hora de salida. |
| `FE_IMPO` | `datetime` | Fecha de impresión del testimonio/parte. |
| `FE_WHAT` | `datetime` | Fecha de notificación al cliente. |
| `DE_OBSE` | `text` | Observaciones al entregar. |
| `FE_ESCR` | `date` | Fecha escritura (Referencia). |
| `FE_CIER_FIRM` | `date` | Fecha en la que concluyeron las firmas. |
| `NU_FOLI` | `varchar(10)` | Foja/Folio donde inicia. |
| `NU_MINU` | `varchar(10)` | Minuta asociada. |
| `NU_TOKE` | `varchar(150)` | Token seguro de entrega o seguimiento. |
| `IN_PART` | `int` | Indicador si se despacha "Parte Registral". |
| `IN_TEST` | `int` | Indicador si se despacha "Testimonio". |
| `IN_COPI` | `int` | Indicador si se despacha "Copia Simple". |
| `NU_SOLI_REG` | `varchar(30)` | Número de solicitud registral (si va a SUNARP). |
| `IN_LEGA` | `int` | Indicador de legalización. |
| `IN_ENVI` | `int` | Indicador de enviado por Courier. |
| `IN_APRO` | `int` | Aprobación de salida por jefatura. |
| `FE_APRO` | `datetime` | Fecha de aprobación. |
| `CO_USUA_APRO` | `int` | Usuario que aprobó salida. |
| `IN_APROB` | `int` | Verificación final (Check). |
| `IN_ESTA` | `int` | Estado del despacho (Entregado, En tránsito, Devuelto). |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DESP_NOTA` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esta es la última etapa del ciclo de vida del trámite, donde el producto notarial final se entrega físicamente al cliente o se envía electrónicamente mediante el módulo PIC o correo. |

---

## Tabla: `R_DESP_REGI`

### Descripcion funcional
Tabla relacional para el control del "Despacho Registral" (Presentaciones a SUNARP y Municipalidades), incluyendo control de saldos y tachas.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DESP_REGI` | `int unsigned` | Identificador interno. |
| `CO_SITU_TRAM` | `int unsigned` | Situación (Liquidado, Inscrito, Tachado, Observado). |
| `CO_TICK_SERV` | `int unsigned` | Kardex asociado. |
| `CO_REGI_SUNA` | `int unsigned` | Registro/Libro de SUNARP. |
| `CO_CABE_CAJA` | `int unsigned` | Factura de notaría que sustentó el pago registral. |
| `CO_VENT_RRPP` | `int unsigned` | Ventanilla SUNARP u Oficina. |
| `CO_ENVI_DESP` | `int` | Gestor registral de la notaría que llevó el título. |
| `CO_OFIC_REGI` | `int` | Sede Registral (Ej. Zona IX - Lima). |
| `CO_DETA_CAJA` | `int` | Detalle específico facturado al cliente. |
| `CO_TIPO_CHEQ` | `int` | Tipo de cheque gerencia si se usó para pago de derechos. |
| `CO_MOVI_REGI` | `int` | Movimiento contable registral interno. |
| `FE_DESP_REGI` | `date` | Fecha de presentación en RRPP. |
| `FE_CIER_FIRM` | `date` | Fecha de cierre de firmas (requisito SUNARP). |
| `NU_TITU` | `varchar(20)` | N° de Título generado por SUNARP al ingresar. |
| `NU_SALD_PEND` | `decimal(15,2)` | Saldo pendiente por pagar o liquidar de derechos. |
| `NU_PAGA` | `decimal(12,2)` | Derechos de presentación pagados. |
| `NU_PAGO_MAYO` | `decimal(12,2)` | Derechos de inscripción o mayor valor. |
| `NU_PAGO_PRES` | `decimal(12,2)` | Monto presupuesto inicial para RRPP. |
| `NU_SALDO` | `decimal(12,2)` | Saldo a devolver al cliente (Vuelto registral). |
| `NU_SOLI` | `varchar(20)` | Número de solicitud. |
| `IN_CRED_CAJA` | `int` | Fue cubierto por crédito de notaría. |
| `IN_ESTA_AREA_RRPP` | `int` | Estado en la sección del registrador público. |
| `CO_USUA` | `int` | Usuario que registró la presentación. |
| `TS_USUA` | `datetime` | Fecha del registro. |
| `TS_USUA_ANUL` | `timestamp` | Fecha de anulación/desistimiento. |
| `TS_USUA_CARG_AUTO` | `datetime` | Fecha de cargo automático en SUNARP. |
| `CO_USUA_MODI` | `int` | Usuario modificador. |
| `CO_USUA_RESP` | `int` | Abogado responsable de subsanar observaciones de SUNARP. |
| `IN_ESTA` | `char(1)` | Estado en el sistema Legasys. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DESP_REGI` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Módulo súper crítico para la liquidación de saldos registrales (vueltos de SUNARP a clientes). Se alimenta cruzando datos con `H_SALD_TRAM`. |

---

## Tabla: `R_DESP_SID`

### Descripcion funcional
Tabla relacional exclusiva para el Despacho Registral electrónico vía la API de SID-SUNARP (Sistema de Intermediación Digital).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_DESP_SID` | `int` | Identificador interno. |
| `CO_TICK_SERV` | `int` | Trámite/Kardex enviado digitalmente. |
| `CO_DESP_REGI` | `int` | Enlace con la presentación registral estándar. |
| `NU_SOLI` | `varchar(20)` | Número de solicitud SID-SUNARP. |
| `FE_INGR` | `datetime` | Fecha y hora en la que la API SID acuse de recibo. |
| `FE_ERROR` | `datetime` | Fecha del error si la API de SUNARP falla o rebota. |
| `CO_USUA_MODI` | `int` | Usuario notario/abogado que firmó y envió al SID. |
| `TS_USUA_MODI` | `datetime` | Timestamp. |
| `IN_ESTA` | `int` | Estado del envío SID (Enviado, Aceptado, Fallido). |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_DESP_SID` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Controla la trazabilidad de los Partes Electrónicos. Trabaja de la mano con `H_TICK_ACTO_SID`. |

---

## Tabla: `R_ESCR_USUA`

### Descripcion funcional
Tabla relacional usada para auditar y controlar qué usuarios tienen el privilegio o la asignación de descargar/modificar una Escritura Pública específica.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_ESCR_USUA` | `int` | Identificador interno. |
| `CO_TICK_SERV` | `int` | Trámite o Escritura. |
| `CO_USUA` | `int` | Usuario asignado/involucrado en la matriz. |
| `IN_ESTA` | `char(1)` | Estado (Activo/Revocado). |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_ESCR_USUA` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Componente de seguridad interno para el bloqueo concurrente de las plantillas DOCX y control de quién "Checkouteó" el archivo de la escritura. |

---

## Tabla: `R_INSE_DIGI`

### Descripcion funcional
Tabla relacional que asocia los Insertos Notariales (`P_INSE`) con Tipos Documentales Digitales específicos para el módulo Legasys IA o la nube.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_INSE_DIGI` | `int` | Identificador interno. |
| `CO_INSE` | `int` | Código del inserto legal a inyectar. |
| `CO_TIPO_DIGI` | `int` | Tipo de documento digital asociado. |
| `CO_USUA_MODI` | `int` | Usuario modificador. |
| `TS_USUA_MODI` | `datetime` | Timestamp. |
| `IN_ESTA` | `int` | Estado. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_INSE_DIGI` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Utilizado por el motor documental Twig y la IA para saber qué cláusulas extra insertar al procesar la Minuta IA o el Medio de Pago (según `H_JSON_TRAM`). |

---

## Tabla: `R_INSE_SERV`

### Descripcion funcional
Tabla relacional matriz que vincula los Insertos (`P_INSE`) con un Servicio específico (`P_SERV`) para obligar o sugerir su uso en el instrumento notarial.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `R_INSE_SERV` | `int` | Identificador interno. |
| `CO_INSE` | `int` | Código del inserto. |
| `CO_SERV` | `int` | Código del servicio o acto (Ej. Compraventa, Sucesión). |
| `CO_USUA_MODI` | `int` | Usuario vinculador. |
| `TS_USUA_MODI` | `datetime` | Fecha vinculación. |
| `IN_ESTA` | `int` | Estado de vigencia obligatoria. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `R_INSE_SERV` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Ejemplo: Si `CO_SERV` es "Constitución de Empresa", esta tabla obliga a inyectar el inserto de "Declaración Jurada UIF" y "Pacto Social" automáticamente en el Twig del borrador. |

---

## Tabla: `R_INSE_TICK_SERV`

### Descripcion funcional
Tabla relacional operativa que deja constancia histórica de que un Inserto específico fue de hecho utilizado e inyectado en un Kardex o Trámite concreto.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_INSE_TICK_SERV` | `int` | Identificador interno. |
| `CO_INSE_DOCU` | `int` | Código del inserto documental utilizado. |
| `CO_TICK_SERV` | `int` | Kardex / Trámite. |
| `IN_ESTA` | `char(1)` | Estado de inyección en el documento final. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_INSE_TICK_SERV` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Sirve para auditoría, validando que el abogado o motor Twig no se "olvidó" de aplicar las cláusulas requeridas por `R_INSE_SERV` antes de que se autoricen las firmas finales. |

---

## Tabla: `R_PERM_CAJA`

### Descripcion funcional
Tabla relacional de seguridad y roles financieros. Establece qué usuarios (Cajeros) están autorizados a operar sobre qué Cajas físicas/lógicas de la notaría, y con qué medios de pago.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PERM_CAJA` | `int` | Identificador interno. |
| `CO_CAJA` | `int` | Identificador de la caja física o agencia virtual. |
| `CO_USUA` | `int` | Usuario/Cajero autorizado. |
| `IN_FORM_PAGO` | `smallint` | Forma de pago autorizada (Ej. Algunos cajeros solo manejan tarjetas, no efectivo). |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de asignación. |
| `CO_USUA_MODI` | `int` | Administrador/Jefe de Caja que dio el permiso. |
| `IN_ESTA` | `char(1)` | Estado (Permiso Activo/Revocado). |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PERM_CAJA` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Restricción clave en el login de caja. Si el usuario intenta emitir un comprobante o liquidar y no tiene un registro `IN_ESTA=1` aquí, el sistema bloquea el módulo financiero para él. |

---

## Tabla: `R_PERM_USUA`

### Descripcion funcional
Tabla relacional para el control de acceso y asignación de permisos (RBAC - Role Based Access Control) entre Tipos de Usuario (`A_TIPO_USUA`) y Opciones del Sistema.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PERM_USUA` | `int` | Identificador interno. |
| `CO_TIPO_USUA` | `int` | Tipo o perfil del usuario (Ej. Administrador, Abogado). |
| `CO_OPCI_SIST` | `int` | Módulo o vista autorizada. |
| `TS_USUA_MODI` | `datetime` | Fecha y hora de modificación. |
| `CO_USUA_MODI` | `int` | Administrador que asignó el permiso. |
| `IN_ESTA` | `char(1)` | Estado de habilitación (Permitido/Denegado). |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PERM_USUA` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Define dinámicamente qué menús e interfaces se renderizan para el usuario en el frontend y bloquea accesos no autorizados a nivel de middleware. |

---

## Tabla: `R_PRTC_BIEN`

### Descripcion funcional
Tabla relacional para asociar a los Participantes (Comparecientes) con un Bien específico (Inmueble, Vehículo) dentro de un trámite, definiendo su porcentaje de partición o cuota ideal.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PRTC_BIEN` | `int` | Identificador interno. |
| `CO_PRTC_TRAM` | `int` | Participante dentro del trámite. |
| `CO_TRAM_DIRE` | `int` | Bien inmueble (Dirección). |
| `CO_TICK_SERV` | `int` | Trámite o Kardex. |
| `CO_TICK_SERV_SUB` | `int` | Subservicio asociado. |
| `NU_SECU` | `int` | Orden secuencial de los copropietarios. |
| `PO_PART` | `decimal(10,3)` | Porcentaje de participación sobre el bien (Ej. 50.000%). |
| `IN_ESTA` | `int` | Estado de la asociación. |
| `CO_USUA_MODI` | `int` | Usuario que vinculó el bien. |
| `TS_USUA_MODI` | `timestamp` | Fecha de vinculación. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PRTC_BIEN` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Fundamental en Contratos de Compraventa de Acciones y Derechos, Anticipos de Legítima o Sucesiones donde múltiples personas adquieren o disponen porcentajes exactos de un mismo inmueble. |

---

## Tabla: `R_PRTC_SERV`

### Descripcion funcional
Tabla relacional de configuración. Define cuáles son los "Tipos de Participantes" (`A_TIPO_PRTC`: Vendedor, Comprador, Otorgante, Apoderado) válidos y obligatorios para un Servicio Notarial (`P_SERV`) específico.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PRTC_SERV` | `int unsigned` | Identificador interno. |
| `CO_TIPO_PRTC` | `int unsigned` | Tipo de intervención (Ej. Vendedor). |
| `CO_SERV` | `int unsigned` | Servicio/Kardex (Ej. Compraventa de Inmueble). |
| `CO_TIPO_SUNA` | `varchar(2)` | Equivalencia para el PDT Notarios SUNAT. |
| `CO_TIPO_PERS` | `int` | Tipo de persona admitida (Natural/Jurídica). |
| `CO_TIPO_CNL` | `varchar(3)` | Equivalencia para el índice del Colegio de Notarios. |
| `NU_ORDE` | `int unsigned` | Orden de visualización en pantalla. |
| `NU_MINI_PRTC_CNL` | `int` | Cantidad mínima requerida de este tipo. |
| `IN_ESTA` | `char(1)` | Estado de vigencia de la regla. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PRTC_SERV` | Clave principal de la tabla. |
| Foreign Key | `CO_TIPO_PRTC` | `CO_TIPO_PRTC` | Referencia a `A_TIPO_PRTC.CO_TIPO_PRTC`. |
| Foreign Key | `CO_SERV` | `CO_SERV` | Referencia a `P_SERV.CO_SERV`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Dicta la estructura lógica del trámite. Al cambiar el `P_SERV` base en Legal, se reinician los tipos de participantes del Kardex basándose en esta tabla. |

---

## Tabla: `R_PRTC_TRAM`

### Descripcion funcional
Tabla relacional operativa que inscribe la participación material de una Persona/Empresa (`P_PRTC`) dentro de un Trámite/Kardex (`P_TRAM`), sellando su rol y porcentajes generales.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PRTC_TRAM` | `int unsigned` | Identificador de participación. |
| `CO_TICK_SERV` | `int unsigned` | Kardex donde interviene. |
| `CUP` | `int unsigned` | Código del participante base. |
| `NS_PRTC` | `int unsigned` | Secuencial de los datos personales (fotografía del momento). |
| `NS_DIRE` | `int unsigned` | Secuencial de su dirección. |
| `PO_PART` | `decimal(5,2)` | Porcentaje general de participación en el contrato. |
| `NU_PART` | `int unsigned` | Número de participaciones/acciones que adquiere o cede. |
| `MO_PART` | `decimal(12,2)` | Monto o valor monetario de su participación. |
| `CO_TIPO_MONE_PART` | `int` | Moneda de su participación económica. |
| `NU_PART_UIF` | `decimal(15,2)` | Umbral de partición reportado a UIF. |
| `CO_TIPO_PRTC` | `int unsigned` | El rol que juega (Comprador, Vendedor, etc.). |
| `IN_TITU_PART` | `char(1)` | Indicador si es el titular principal. |
| `IN_CLIE` | `char(1)` | Indicador si también asume el rol de Cliente/Pagador. |
| `IN_PART` | `int` | Fue incluido en el Parte Registral. |
| `ID_API` | `int` | ID cruzado con API biométrica RENIEC. |
| `ID_API_CONY` | `int` | ID cruzado del cónyuge con RENIEC. |
| `IN_ESTA` | `int` | Estado del participante en el Kardex (1 = Activo, 0 = Eliminado/Anulado). |
| `CO_USUA_MODI` | `int unsigned` | Usuario que lo agregó al trámite. |
| `TS_USUA_MODI` | `datetime` | Fecha de agregación. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PRTC_TRAM` | Clave principal de la tabla. |
| Foreign Key | `CO_TICK_SERV` | `CO_TICK_SERV` | Referencia a `P_TRAM.CO_TICK_SERV`. |
| Foreign Key | `CUP` | `CUP` | Referencia a `P_PRTC.CUP`. |
| Referenciada por | `H_REPR_TRAM` | `CO_PRTC_TRAM` | Referenciada por la tabla de representantes legales/apoderados (`H_REPR_TRAM`). |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | "La Intervención". Al redactar el instrumento, Twig lista a los otorgantes iterando sobre esta tabla. Nótese el snapshot (`NS_PRTC`, `NS_DIRE`): Si la persona actualiza su DNI años después, este Kardex histórico seguirá apuntando a los datos (estado civil, dirección) que tenía en el momento exacto de la firma. |

---

## Tabla: `R_PRTC_TRAM_SUB`

### Descripcion funcional
Tabla relacional para operaciones compuestas. Asocia al participante no solo al Kardex General (`P_TRAM`), sino específicamente a un Acto Secundario o Subservicio dentro del mismo Kardex.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PRTC_TRAM_SUB` | `int` | Identificador interno. |
| `CO_PRTC_TRAM` | `int` | Participación principal del interviniente. |
| `CO_PRTC_SERV` | `int` | Tipo de intervención. |
| `NU_PART_UIF` | `decimal(15,2)` | Porcentaje reportable UIF. |
| `PO_PART` | `decimal(5,2)` | Porcentaje fraccionado. |
| `MO_PART` | `decimal(12,2)` | Monto valorizado. |
| `CO_TIPO_MONE_PART` | `int` | Moneda. |
| `CO_TICK_SERV_SUB` | `int` | Identificador del Subservicio (Ej. Cancelación de Hipoteca). |
| `IN_ESTA` | `int` | Estado. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PRTC_TRAM_SUB` | Clave principal de la tabla. |
| Foreign Key | Múltiples | `CO_PRTC_TRAM`, `CO_PRTC_SERV` | Vinculación a las tablas maestras de participación. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Esencial para el reporte PLD/UIF en escrituras donde un mismo documento contiene una "Compraventa" (donde X es comprador) y una "Constitución de Hipoteca" (donde X es deudor hipotecario). Permite disgregar sus roles y montos en cada acto. |

---

## Tabla: `R_REGI_NOTA`

### Descripcion funcional
Tabla relacional de configuración que dicta cómo una Notaría (`CO_COMP`) específica decide operar o configurar un Servicio Notarial (`CO_REGI_NOTA` / `CO_SERV`). Permite customizar márgenes, fuentes e interlineados para la impresión en papel de seguridad.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_REGI_SERV` | `int` | Identificador interno. |
| `CO_COMP` | `int` | Empresa / Notaría. |
| `CO_REGI_NOTA` | `int` | Servicio o Categoría Notarial. |
| `IN_KARD` | `varchar(20)` | Nomenclatura o serie de Kardex aplicable. |
| `IN_REIN_INST` | `int` | Permite reinicio de instrumento por año. |
| `IN_GENE_INST` | `int` | Autogenera N° de Escritura. |
| `IN_MULT_TRAM` | `int` | Permite actos múltiples en un solo ticket. |
| `IN_INGR_PRTC` | `int` | Requiere captura de participantes obligatoria. |
| `NU_CUEN_INGR` | `varchar(250)` | Cuenta bancaria default para este servicio. |
| `DE_TIPO_LETR_MINU` | `varchar(100)` | Fuente tipográfica para el documento impreso (Ej. Arial, Times). |
| `NU_TAMA_LETR_MINU` | `int` | Tamaño de letra (pt). |
| `DE_INTE_LINE_MINU` | `varchar(100)` | Tipo de interlineado (Simple, 1.5). |
| `NU_INTE_LINE_MINU` | `decimal(11,2)` | Valor numérico del interlineado. |
| `DE_MARG_MINU` | `varchar(100)` | Márgenes laterales configurados. |
| `CO_USUA_MODI` | `int` | Administrador modificador. |
| `TS_USUA_MODI` | `datetime` | Fecha actualización. |
| `IN_ESTA` | `int` | Estado de la configuración. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_REGI_SERV` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Configuración técnica del procesador DOCX de Legasys. Evita desconfiguraciones del papel notarial o márgenes rotos al exportar el instrumento para impresión. |

---

## Tabla: `R_REGI_TABS`

### Descripcion funcional
Tabla relacional del generador UI Legacy. Mapea qué "Pestañas" o Tabs dinámicos (Ej. "Datos del Vehículo", "Datos del Inmueble") deben activarse visualmente según el Servicio seleccionado.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_REGI_TABS` | `int` | Identificador interno. |
| `CO_TABS` | `int` | Identificador de la Pestaña/Módulo UI. |
| `CO_SERV` | `varchar(200)` | Servicio o lista de servicios vinculados. |
| `NO_TABL` | `varchar(20)` | Nombre lógico de la tabla de datos a llenar. |
| `IN_ESTA` | `char(1)` | Estado (Mostrar/Ocultar). |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_REGI_TABS` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Permite inyectar componentes HTML específicos en la pantalla de "Atención de Ticket" sin quemarlos en el código duro. Si el servicio es un traspaso vehicular, activa el Tab de características de motor/chasis. |

---

## Tabla: `R_SERV_COLM`

### Descripcion funcional
Tabla relacional de metadata dinámica (Diccionario de Datos UI). Define qué campos (Columnas) debe renderizar Legasys para capturar datos variables (CODO) según el servicio elegido.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_SERV_COLM` | `int unsigned` | Identificador interno. |
| `NO_TABL` | `varchar(50)` | Nombre interno de la tabla lógica asociada. |
| `CO_ALIA_COLM` | `int unsigned` | Alias de la columna. |
| `CO_SERV` | `int unsigned` | Servicio asociado. |
| `NO_COLM` | `varchar(50)` | Nombre base de la columna (Ej. FE_ESCR). |
| `DE_COLM_PERS` | `varchar(50)` | Label o Etiqueta personalizada para la interfaz. |
| `IN_OBLI` | `char(1)` | Indicador de llenado obligatorio (Require). |
| `NU_POSI` | `int unsigned` | Posición u orden visual en pantalla. |
| `IN_NULO` | `char(1)` | Admite valor nulo. |
| `IN_BUSQ` | `char(1)` | Columna se puede usar para búsquedas y filtros. |
| `IN_MOST_WEB` | `char(1)` | Mostrar en el portal web público. |
| `IN_MOST_INTR` | `char(1)` | Mostrar en la intranet (Abogados). |
| `IN_MOST_SUNA` | `char(1)` | Requerido para reporte SUNAT. |
| `TI_FORM_SALI` | `varchar(50)` | Formato o máscara de salida (Date, Currency). |
| `NU_ORDE_TABL` | `int unsigned` | Ordenación lógica de tabla. |
| `VA_DEFE_SERV` | `varchar(50)` | Valor por defecto (Default Value). |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_SERV_COLM` | Clave principal de la tabla. |
| Foreign Key | `CO_ALIA_COLM` | `CO_ALIA_COLM` | Referencia al esquema `H_ALIA_COLM`. |
| Foreign Key | `CO_SERV` | `CO_SERV` | Referencia a `P_SERV.CO_SERV`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Parte del motor de Vistas Dinámicas de Legasys. Evita crear decenas de tablas para capturar información específica. Aquí se configura que la "Transferencia Vehicular" pida "Placa" (obligatorio) y "Color" (opcional). |

---

## Tabla: `R_SERV_CPTO_TARI`

### Descripcion funcional
Tabla relacional financiera **crítica**. Ensambla o vincula el Servicio (`P_SERV`) con los Conceptos que lo conforman (`P_CPTO`) y la Tarifa predeterminada (`P_TARI`) a cobrar en liquidación y caja.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_SERV_CPTO_TARI` | `int unsigned` | Identificador interno. |
| `CO_COMP` | `int` | Notaría propietaria del ensamble tarifario. |
| `CO_CPTO` | `int unsigned` | Concepto cobrable (Ej. Derechos Notariales). |
| `CO_TARI` | `int unsigned` | Tarifa monetaria asociada. |
| `CO_SERV` | `int unsigned` | Servicio padre (Ej. Compraventa). |
| `CO_TIPO_TARI` | `int` | Categoria de tarifa (Base, Promocional, Especial). |
| `NU_ORDE` | `int` | Orden visual para el despliegue del presupuesto. |
| `CO_USUA_MODI` | `int unsigned` | Administrador modificador. |
| `TS_USUA_MODI` | `datetime` | Fecha actualización. |
| `IN_ESTA` | `char(1)` | Estado de vigencia tarifaria. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_SERV_CPTO_TARI` | Clave principal de la tabla. |
| Foreign Key | Múltiples | `CO_CPTO`, `CO_TARI`, `CO_SERV` | Une los tres catálogos principales del sistema financiero. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | **Regla de Caja**: Esta es la Plantilla de Precios. Cuando el módulo de liquidación se abre, carga en pantalla los conceptos cuyo `IN_ESTA=1` pertenezcan al `P_SERV` del ticket. El orden de los ítems en la boleta visible debe respetar `NU_ORDE`. Si se agrega un concepto "Libre", el sistema lo guarda aquí (con Tarifa 0.00) tras bambalinas para permitir el cobro. |

---

## Tabla: `R_SERV_NOTA`

### Descripcion funcional
Tabla relacional para personalizar el comportamiento del Servicio según la Notaría, similar a `R_REGI_NOTA` pero enfocada en la habilitación del trámite en sí.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_SERV_NOTA` | `int` | Identificador interno. |
| `CO_COMP` | `int` | Notaría. |
| `CO_SERV` | `int` | Servicio Notarial. |
| `IN_KARD` | `varchar(5)` | Genera Kardex. |
| `IN_REIN_INST` | `int` | Reinicio anual de instrumentos. |
| `IN_GENE_INST` | `int` | Generación automática. |
| `IN_MULT_TRAM` | `int` | Admite múltiples actos. |
| `CO_USUA_MODI` | `int` | Usuario modificador. |
| `TS_USUA_MODI` | `datetime` | Timestamp. |
| `IN_ESTA` | `int` | Estado de disponibilidad en la notaría. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_SERV_NOTA` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Una Notaría (en el contexto SaaS) puede no ofrecer todos los `P_SERV` existentes en la matriz global. Si `IN_ESTA = 0`, el servicio no aparecerá en el combo del Módulo Legal para esa sucursal. |

---

## Tabla: `R_SERV_PLAN`

### Descripcion funcional
Tabla relacional que conecta un Servicio (`P_SERV`) con su Plantilla DOCX (`P_PLAN`) base u original para la redacción del borrador notarial.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_SERV_PLAN` | `int unsigned` | Identificador interno. |
| `CO_SERV` | `int unsigned` | Servicio/Trámite notarial. |
| `CO_PLAN` | `int unsigned` | Archivo Plantilla de Word o Texto HTML (`P_PLAN`). |
| `CO_DOCU_FIRM` | `int` | Plantilla asociada a las fojas de firma. |
| `CO_USUA_MODI` | `int unsigned` | Creador de la regla. |
| `TS_USUA_MODI` | `date` | Timestamp. |
| `IN_ESTA` | `char(1)` | Estado de vigencia de la plantilla. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_SERV_PLAN` | Clave principal de la tabla. |
| Foreign Key | `CO_SERV` | `CO_SERV` | Referencia a `P_SERV`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | "El Molde". Cuando un abogado abre el Kardex, el motor Twig lee esta relación, recupera el Word base asignado, inyecta las variables `[[NOMBRES]]` del cliente y genera el `H_DOCU_EXTE` (Borrador Editable). |

---

## Tabla: `R_SUB_SERV_TICK`

### Descripcion funcional
Tabla relacional para el desglose operativo. Vincula los "Subservicios" (Actos secundarios) al contenedor general del Ticket (`CO_TICK_CONT`) para la facturación detallada.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_SUB_SERV_TICK` | `int` | Identificador interno. |
| `CO_SUB_SERV` | `int` | Código del sub-acto prestado (Ej. Fotocopias, Legalización de Firma Adicional). |
| `CO_TICK_CONT` | `int` | Ticket operativo general. |
| `CO_USUA` | `int` | Usuario que registró el gasto/servicio. |
| `NU_SEMI` | `int` | Semilla o serie de papel gastado. |
| `NU_SUB_SEMI` | `int` | Sub-serie o control menor. |
| `NU_CANT` | `int` | Cantidad prestada (Ej. 10 fotocopias). |
| `MO_IMPO` | `decimal(11,2)` | Monto o importe a sumar al presupuesto. |
| `IN_ESTA` | `char(1)` | Estado del cobro/ejecución. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_SUB_SERV_TICK` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Fundamental en Operaciones (Ticket Rápido) para ir acumulando pequeños cobros (`H_SUB_SERV`) en una sola cuenta por pagar (`MO_IMPO`) vinculada al Ticket. |

---

## Tabla: `R_TICK_CNXO`

### Descripcion funcional
Tabla relacional para establecer Conexiones ("Conexos") entre distintos Tickets. Útil cuando un trámite es prerrequisito de otro o cuando varios tickets pertenecen al mismo proyecto inmobiliario.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TICK_CNXO` | `int` | Identificador interno. |
| `CO_TICK_CONT_ORIG` | `int` | Ticket Padre / Principal. |
| `CO_TICK_CONT_CNXO` | `int` | Ticket Hijo / Secundario vinculado. |
| `CUP` | `int` | Participante en común (si aplica). |
| `IN_TIPO` | `int` | Tipo de vinculación (Ej. Pre-requisito, Desglose, Agrupación). |
| `TS_USUA_MODI` | `datetime` | Fecha del enlace. |
| `CO_USUA_MODI` | `int` | Usuario vinculador. |
| `IN_ESTA` | `char(1)` | Estado (Vinculado/Separado). |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TICK_CNXO` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Ejemplo de negocio: Si se hace un "Levantamiento de Hipoteca" (Ticket B) para poder "Vender un Inmueble" (Ticket A), esta tabla permite visualizar en el Kardex A que primero debe cerrarse el proceso B. |

---

## Tabla: `R_TICK_SERV`

### Descripcion funcional
Tabla relacional de puente crítico. Vincula el Contenedor (Ticket - `P_TICK`) con el Servicio prestado (Kardex - `P_TRAM`), además de registrar atributos específicos del momento de esa vinculación.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TICK_SERV` | `int unsigned` | Identificador interno (Llave primaria y puente principal de `P_TRAM`). |
| `CO_TICK_CONT` | `int unsigned` | Contenedor Ticket Padre. |
| `CO_SERV_ALTE` | `bigint` | Servicio Notarial Alterno / Equivalente. |
| `CO_TOKE_API` | `int` | Token API que originó la inserción (Si fue B2B). |
| `NU_CANT` | `int unsigned` | Cantidad de actos solicitados. |
| `MO_TARI` | `decimal(8,2)` | Tarifa negociada en ese momento. |
| `NU_DOCU` | `varchar(60)` | N° de documento de referencia del cliente. |
| `NU_SECU_TEST` | `int` | Secuencial de testimonio expedido. |
| `NU_SECU_SND` | `int unsigned` | Secuencial de Sistema Notarial Digital. |
| `IN_ENVI_MAIL` | `char(1)` | Correo enviado. |
| `IN_FIRM_COMP` | `char(1)` | Firmas completas. |
| `FE_FIRM_COMP` | `date` | Fecha en la que concluyeron las firmas. |
| `FE_ENVI_MAYO` | `date` | Fecha de envío al colegio o registro mayor. |
| `IN_ENVI_CNL` | `int` | Enviado al Colegio de Notarios de Lima. |
| `CO_USUA_MODI` | `int unsigned` | Usuario vinculador. |
| `TS_USUA_MODI` | `datetime` | Fecha vinculación. |
| `IN_ESTA` | `char(1)` | Estado de la vinculación. |
| `IN_MIGR` | `int` | Indica si el registro provino de una migración legacy. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TICK_SERV` | Clave principal de la tabla. |
| Foreign Key | `CO_TICK_CONT` | `CO_TICK_CONT` | Referencia a `P_TICK.CO_TICK_CONT`. |
| Foreign Key | `CO_SERV_ALTE` | `CO_SERV_ALTE` | Referencia a `H_SERV_ALTE.CO_SERV_ALTE`. |
| Referenciada por | Múltiples | `CO_TICK_SERV` | Es la llave principal para `P_TRAM`, `H_PRES_TICK`, y `Z_KARD_ESCR`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Actúa como el nexo entre el cajero (Ticket) y el abogado (Kardex/Trámite). El `CO_TICK_SERV` generado aquí es el que viaja a `P_TRAM` como su Primary Key (Identidad 1 a 1). |

---

## Tabla: `R_TICK_SERV_SUB`

### Descripcion funcional
Tabla relacional para vincular un Kardex (`CO_TICK_SERV`) con sus Subservicios u operaciones secundarias (Ej. Transferencia Vehicular + Certificado Policial).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TICK_SERV_SUB` | `int` | Identificador interno. |
| `CO_TICK_SERV` | `int` | Trámite Padre / Kardex. |
| `CO_SERV` | `int` | Servicio asociado al sub-acto. |
| `CO_USUA_MODI` | `int` | Usuario modificador. |
| `TS_USUA_MODI` | `datetime` | Timestamp. |
| `IN_ESTA` | `int` | Estado del sub-servicio. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TICK_SERV_SUB` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Similar a `R_SUB_SERV_TICK` pero amarrado directamente al Kardex en lugar de a la caja general del Ticket. |

---

## Tabla: `R_UPDA_DIGI`

### Descripcion funcional
Tabla relacional del Repositorio Digital de Legasys. Vincula los binarios, metadatos y enlaces de la nube generados por el motor de IA o Archivo Central con un Kardex específico.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_UPDA_DIGI` | `int` | Identificador de repositorio digital. |
| `CO_TICK_SERV` | `int` | Kardex asociado. |
| `CO_DL939_PAGO` | `int` | Enlace a Medio de Pago DL939 (Si aplica). |
| `CO_TIPO_DIGI` | `int` | Tipo de documento (Minuta, Voucher, DNI). |
| `CO_CARP_TICK` | `int` | Relación con el archivo físico del Ticket. |
| `IN_UPDA_DIGI` | `int` | Estado de subida. |
| `IM_UPDA_DIGI` | `longblob` | Binario del archivo (Legacy mode). |
| `URL_UPDA_DIGI` | `text` | Ruta relativa o URL Cloud (S3/Storage) del archivo. |
| `DE_UPDA_DIGI` | `varchar(100)` | Descripción o etiqueta. |
| `NO_EXTE_DIGI` | `varchar(150)` | Extensión original (jpg, pdf). |
| `CO_USUA_MODI` | `int` | Operador / Abogado. |
| `TS_USUA_MODI` | `datetime` | Fecha de carga. |
| `CO_USUA_ELIM` | `int` | Usuario que borró. |
| `TS_USUA_ELIM` | `datetime` | Fecha borrado lógico. |
| `IN_ESTA` | `int` | Estado del archivo (Activo/Borrador/Eliminado). |
| `IN_BOT` | `int` | Procesado por BOT/IA Legasys automáticamente. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_UPDA_DIGI` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | "Bandeja de Entradas IA". Cuando Legasys IA escanea una minuta o un medio de pago bancario, el resultado (JSON y PDF) recae aquí. También sirve para asociar PDFs de medios de pago a `H_DL939_PAGO`. |

---

## Tabla: `R_VEHI_DESP_REGI`

### Descripcion funcional
Tabla relacional para el Despacho Registral de Trámites Vehiculares. Asocia un vehículo específico de la transferencia con la presentación a SUNARP (Cambio de tarjeta de propiedad).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_VEHI_DESP_REGI` | `int` | Identificador interno. |
| `CO_TICK_SERV` | `int` | Kardex vehicular. |
| `CO_TRAM_VEHI` | `int` | Placa/Vehículo involucrado (`H_TRAM_VEHI`). |
| `CO_DESP_REGI` | `int` | Despacho registral (`R_DESP_REGI`). |
| `CO_USUA_MODI` | `int` | Usuario que armó el paquete. |
| `TS_USUA_MODI` | `datetime` | Fecha de armado. |
| `IN_ESTA` | `int` | Estado del envío. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_VEHI_DESP_REGI` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Necesaria porque un solo Kardex notarial de Transferencia puede vender/traspasar múltiples vehículos (flotillas), y cada vehículo podría generar un título independiente en SUNARP. |

---

## Tablas: `T_PDT_...` (Declaraciones PDT SUNAT)

### Descripcion funcional
Familia de tablas Temporales/Transaccionales (`T_PDT_ACTOS`, `T_PDT_BIENES`, `T_PDT_FORM_1662`, `T_PDT_OTORGANTES`, `T_PDT_PAGO`) que actúan como caché o "Staging Area" para la generación del archivo plano (.txt) del Programa de Declaración Telemática (PDT) de Operaciones de Notarios exigido por SUNAT.

### Columnas principales destacadas (General)
- `CO_TICK_SERV`: El trámite u operación notarial.
- `NUM_ESCRITURA` / `FEC_NUMERACION`: Identidad notarial de la escritura.
- `ACTO` / `TIPO_BIEN` / `UBIGEO`: Códigos estandarizados por SUNAT (Catálogo Anexo).
- `MON_PAGADO` / `VALOR`: Importes cuantificados de la transacción.
- `TIPO_DOCU` / `NUM_DOCU` / `TIPO_PERSO`: Datos normalizados de los otorgantes.
- `IN_MIGRA`: Flag que indica si el registro ya fue exportado al archivo TXT de SUNAT.

### Claves e indices
Todas tienen una Primary Key autoincremental simple (Ej. `CO_PDT_ACTOS`, `CO_PDT_BIENES`).

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Mensualmente, la notaría debe reportar a SUNAT todas las escrituras translativas de dominio, constitución de empresas, poderes, etc. Legasys "aplana" la complejidad de su esquema y vuelca los datos aquí con los códigos exigidos por la administración tributaria para generar los reportes de manera rápida y sin castigar al motor base. |

---

## Tabla: `T_PERS_SOSP_UIF`

### Descripcion funcional
Tabla "Lista Negra" o de Personas Sospechosas. Módulo de Prevención de Lavado de Activos (PLD/UIF).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_PERS_SOSP_UIF` | `int` | Identificador interno. |
| `CO_TIPO_SOSP` | `int` | Categoría (Ej. PEP, Lista OFAC, Investigado). |
| `CO_TICK_SERV` | `int` | Kardex donde el sistema detectó a la persona. |
| `NU_INST` | `int` | Número de instrumento observado. |
| `FE_ESCR` | `date` | Fecha de escritura observada. |
| `NU_KARD` | `varchar(10)` | KARDEX observado. |
| `DE_SERV` | `varchar(100)` | Acto notarial que intentó realizar. |
| `NO_PRTC` | `varchar(100)` | Nombre completo del sospechoso o empresa fachada. |
| `DE_TIPO_PRTC` | `varchar(50)` | Rol que intentó jugar (Ej. Comprador). |
| `DE_OBSE` | `varchar(200)` | Motivo de inclusión / Alerta temprana generada. |
| `IN_ESTA` | `char(1)` | Estado de la alerta UIF (Activa, Descartada). |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_PERS_SOSP_UIF` | Clave principal de la tabla. |
| Foreign Key | `CO_TIPO_SOSP` | `CO_TIPO_SOSP` | Referencia al catálogo de tipos de alertas. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Cuando el oficial de cumplimiento cruza listas ONU/OFAC, si hay una coincidencia (Hit), el sistema alerta y bloquea el trámite, reportando la incidencia en esta tabla para el envío del ROS (Reporte de Operaciones Sospechosas) a la SBS. |

---

## Tabla: `V_BIEN_CNL`

### Descripcion funcional
Tabla de Vistas o Diccionarios Auxiliares para el módulo de reportes hacia el Colegio de Notarios de Lima (CNL).

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_BIEN_CNL` | `int` | Identificador interno. |
| `CO_ACTO_JURI` | `varchar(30)` | Acto jurídico. |
| `CO_TIPO_BIEN` | `varchar(120)` | Tipo de bien reportado. |
| `CO_MEDI_PAGO` | `varchar(100)` | Medio de pago utilizado. |
| `CO_FORM_PAGO` | `varchar(200)` | Forma de pago. |
| `CO_OPOR_PAGO` | `varchar(200)` | Oportunidad del pago (Al contado, Diferido). |
| `CO_CLAS_BIEN` | `varchar(100)` | Clasificación del bien mueble/inmueble. |
| `NU_MONT_TRAN` | `decimal(11,2)` | Monto transado. |
| `IN_OTOR` | `int` | Otorgantes. |
| `IN_BENE` | `int` | Beneficiarios. |
| `IN_FIDU` | `int` | Fiduciarios. |
| `IN_OPOR_PAGO` | `varchar(50)` | Variable estática. |
| `IN_CUAN_OPER` | `varchar(50)` | Cuantía operación. |
| `IN_TIPO_CUAN_OPER` | `int` | Tipo cuantía. |
| `IN_MEDI_PAGO_OPER` | `varchar(50)` | Variable estática. |
| `IN_TIPO_MEDI_PAGO_OPER` | `int` | Tipo medio. |
| `IN_ESTA` | `int` | Estado. |
| `CO_USUA_MODI` | `int` | Modificador. |
| `TS_USUA_MODI` | `datetime` | Fecha. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_BIEN_CNL` | Clave principal de la tabla. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | Se utiliza para el Módulo de Envío OCP (Órgano Centralizado de Prevención) de las Juntas de Decanos. Contiene "Traducciones" de los catálogos internos de Legasys hacia los códigos fijos que exige la OCP. |

---

## Tabla: `Z_KARD_ESCR`

### Descripcion funcional
Tabla "Bóveda" o Contenedor Final Binario de la Escritura Pública en Legasys. Guarda las versiones congeladas de los PDFs y plantillas que conforman el instrumento.

### Columnas
| Columna | Tipo de dato | Descripcion |
|---|---|---|
| `CO_TICK_SERV` | `int unsigned` | Kardex asociado (Primary Key compartida). |
| `CO_DOCU_FIRM` | `int unsigned` | Identificador documental de las firmas. |
| `CO_PLAN` | `int` | Identificador de plantilla Word usada (`P_PLAN`). |
| `IN_TIPO_GENE` | `char(1)` | Tipo de generación (Automática Twig, Subida manual). |
| `IM_DOCU_ESCR` | `longblob` | Binario de la Escritura Pública "Matriz". |
| `CO_DOCU_ESCR` | `int` | Enlace externo a la Matriz si está en Storage S3. |
| `IM_DOCU_TEST` | `longblob` | Binario del Testimonio generado. |
| `CO_DOCU_TEST` | `int` | Enlace externo al Testimonio. |
| `IM_DOCU` | `longblob` | Binario de Borrador final (DOCX). |
| `CO_DOCU` | `int` | Enlace externo al Borrador. |
| `IM_PART_PDF` | `longblob` | Binario del Parte Registral para SUNARP (Firmado digitalmente). |
| `IM_DOCU_PDF` | `longblob` | Binario alternativo PDF. |
| `IM_SOLI_PDF` | `longblob` | Solicitud de inscripción PDF. |
| `CO_DOCU_PDF` | `int` | Enlace externo al Parte. |
| `IM_MINU` | `longblob` | Binario de la Minuta original adjunta. |
| `CO_MINU` | `int` | Enlace externo a la Minuta. |
| `IM_DOCU_DIGI` | `longblob` | Copia de seguridad en la nube. |
| `CO_DOCU_DIGI` | `int` | Enlace nube de seguridad. |
| `TS_GENE_ESCR` | `datetime` | Fecha y hora de congelamiento/generación final. |
| `IN_CIER` | `char(1)` | Indicador de Cierre de Instrumento (Inmutable). |
| `IN_QR_FIRM` | `int` | Código QR embebido en firmas. |
| `IN_TOKE_SEGU` | `varchar(32)` | Hash MD5/SHA de integridad del documento. |
| `CO_USUA_MODI` | `int unsigned` | Notario/Abogado que selló el archivo. |
| `TS_USUA_MODI` | `datetime` | Última modificación en bóveda. |

### Claves e indices
| Tipo | Nombre | Columna(s) | Detalle |
|---|---|---|---|
| Primary Key | `PRIMARY` | `CO_TICK_SERV` | Clave principal de la tabla compartida 1 a 1 con el trámite. |
| Foreign Key | `CO_TICK_SERV` | `CO_TICK_SERV` | Referencia inversa hacia `R_TICK_SERV.CO_TICK_SERV`. |

### Observaciones
| Tipo | Detalle |
|---|---|
| Funcional | **El Archivo Central**. En arquitecturas legacy, esta tabla guardaba archivos enteros de Word y PDF (pesados) en columnas `longblob` (lo que explicaba el crecimiento exponencial de la BD MySQL). Actualmente, si `CO_DOCU_xxx` (ej. `CO_DOCU_ESCR`) tiene valor, indica que el archivo está migrado al sistema de archivos (`storage/app/...`) y la base de datos se mantiene limpia. Es la fuente de la verdad para la impresión de testimonios. |
