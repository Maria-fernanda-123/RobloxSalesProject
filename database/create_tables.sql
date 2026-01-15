-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP DATABASE IF EXISTS mydb;
CREATE DATABASE mydb CHARACTER SET utf8mb4;
USE mydb;

-- -----------------------------------------------------
-- Table `mydb`.`sales`
-- -----------------------------------------------------
-- Plataformas
CREATE TABLE platforms (
    platform_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    selling_fee DECIMAL(5,2) NOT NULL,
    withdrawal_fee DECIMAL(5,2) NOT NULL
) ENGINE=InnoDB;

-- Itens
CREATE TABLE items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(100),
    purchase_price DECIMAL(10,2),
    sale_price DECIMAL(10,2),
    quantity INT
) ENGINE=InnoDB;

-- Vendas
CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    platform_id INT NOT NULL,
    item_id INT,
    description VARCHAR(100),
    quantity INT,
    unit_price DECIMAL(10,2),
    total_sale DECIMAL(10,2),
    selling_fee_amount DECIMAL(10,2),
    withdrawal_fee_amount DECIMAL(10,2),
    net_after_platform DECIMAL(10,2),
    sale_date DATE,
    FOREIGN KEY (platform_id) REFERENCES platforms(platform_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id)
) ENGINE=InnoDB;



