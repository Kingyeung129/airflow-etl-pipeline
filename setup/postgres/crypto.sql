--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

-- Started on 2024-06-02 02:07:21

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 6 (class 2615 OID 25659)
-- Name: crypto; Type: SCHEMA; Schema: -; Owner: airflow_user
--

CREATE SCHEMA crypto;


ALTER SCHEMA crypto OWNER TO airflow_user;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 216 (class 1259 OID 26255)
-- Name: crypto_price; Type: TABLE; Schema: crypto; Owner: pg_database_owner
--

CREATE TABLE crypto.crypto_price (
    pk_crypto_price_id bigint NOT NULL,
    usd character varying(30),
    jpy character varying(30),
    eur character varying(30),
    sgd character varying(30),
    hkd character varying(30),
    "timestamp" timestamp without time zone
);


ALTER TABLE crypto.crypto_price OWNER TO pg_database_owner;

--
-- TOC entry 217 (class 1259 OID 26258)
-- Name: crypto_price_pk_crypto_price_id_seq; Type: SEQUENCE; Schema: crypto; Owner: pg_database_owner
--

CREATE SEQUENCE crypto.crypto_price_pk_crypto_price_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE crypto.crypto_price_pk_crypto_price_id_seq OWNER TO pg_database_owner;

--
-- TOC entry 4840 (class 0 OID 0)
-- Dependencies: 217
-- Name: crypto_price_pk_crypto_price_id_seq; Type: SEQUENCE OWNED BY; Schema: crypto; Owner: pg_database_owner
--

ALTER SEQUENCE crypto.crypto_price_pk_crypto_price_id_seq OWNED BY crypto.crypto_price.pk_crypto_price_id;


--
-- TOC entry 4689 (class 2604 OID 26259)
-- Name: crypto_price pk_crypto_price_id; Type: DEFAULT; Schema: crypto; Owner: pg_database_owner
--

ALTER TABLE ONLY crypto.crypto_price ALTER COLUMN pk_crypto_price_id SET DEFAULT nextval('crypto.crypto_price_pk_crypto_price_id_seq'::regclass);


--
-- TOC entry 4691 (class 2606 OID 26264)
-- Name: crypto_price crypto_price_pkey; Type: CONSTRAINT; Schema: crypto; Owner: pg_database_owner
--

ALTER TABLE ONLY crypto.crypto_price
    ADD CONSTRAINT crypto_price_pkey PRIMARY KEY (pk_crypto_price_id);


-- Completed on 2024-06-02 02:07:21

--
-- PostgreSQL database dump complete
--

