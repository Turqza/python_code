CREATE TABLE IF NOT EXISTS public.espacios_publicos
(
    id_space integer NOT NULL DEFAULT nextval('espacios_publicos_id_space_seq'::regclass),
    cod_localidad integer,
    id_provincia integer,
    id_departamento integer,
    created_at timestamp without time zone,
    categoria character varying(50) COLLATE pg_catalog."default",
    record_type character varying(50) COLLATE pg_catalog."default",
    provincia character varying(50) COLLATE pg_catalog."default",
    localidad character varying(200) COLLATE pg_catalog."default",
    nombre character varying(200) COLLATE pg_catalog."default",
    codigo_postal character varying(200) COLLATE pg_catalog."default",
    telefono character varying(200) COLLATE pg_catalog."default",
    email character varying(200) COLLATE pg_catalog."default",
    web character varying(200) COLLATE pg_catalog."default",
    fuente character varying(200) COLLATE pg_catalog."default",
    CONSTRAINT espacios_publicos_pkey PRIMARY KEY (id_space)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.espacios_publicos
    OWNER to postgres;
