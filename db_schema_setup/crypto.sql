PGDMP  +                    |            crypto    16.0    16.0 
    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    25658    crypto    DATABASE     }   CREATE DATABASE crypto WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Singapore.1252';
    DROP DATABASE crypto;
                airflow_user    false                        2615    25659    crypto    SCHEMA        CREATE SCHEMA crypto;
    DROP SCHEMA crypto;
                airflow_user    false            �            1259    26255    crypto_price    TABLE       CREATE TABLE crypto.crypto_price (
    pk_crypto_price_id bigint NOT NULL,
    usd character varying(30),
    jpy character varying(30),
    eur character varying(30),
    sgd character varying(30),
    hkd character varying(30),
    "timestamp" timestamp without time zone
);
     DROP TABLE crypto.crypto_price;
       crypto         heap    pg_database_owner    false    6            �            1259    26258 #   crypto_price_pk_crypto_price_id_seq    SEQUENCE     �   CREATE SEQUENCE crypto.crypto_price_pk_crypto_price_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 :   DROP SEQUENCE crypto.crypto_price_pk_crypto_price_id_seq;
       crypto          pg_database_owner    false    216    6            �           0    0 #   crypto_price_pk_crypto_price_id_seq    SEQUENCE OWNED BY     k   ALTER SEQUENCE crypto.crypto_price_pk_crypto_price_id_seq OWNED BY crypto.crypto_price.pk_crypto_price_id;
          crypto          pg_database_owner    false    217            Q           2604    26259    crypto_price pk_crypto_price_id    DEFAULT     �   ALTER TABLE ONLY crypto.crypto_price ALTER COLUMN pk_crypto_price_id SET DEFAULT nextval('crypto.crypto_price_pk_crypto_price_id_seq'::regclass);
 N   ALTER TABLE crypto.crypto_price ALTER COLUMN pk_crypto_price_id DROP DEFAULT;
       crypto          pg_database_owner    false    217    216            S           2606    26264    crypto_price crypto_price_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY crypto.crypto_price
    ADD CONSTRAINT crypto_price_pkey PRIMARY KEY (pk_crypto_price_id);
 H   ALTER TABLE ONLY crypto.crypto_price DROP CONSTRAINT crypto_price_pkey;
       crypto            pg_database_owner    false    216           