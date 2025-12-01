CREATE SCHEMA IF NOT EXISTS `moustass_db` DEFAULT CHARACTER SET utf8;

CREATE TABLE IF NOT EXISTS `moustass_db`.`users` (
  `idusers` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `role` VARCHAR(45) NOT NULL,
  `password_hash` VARCHAR(45) NOT NULL,
  `1st_password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idusers`),
  UNIQUE INDEX `idusers_UNIQUE` (`idusers` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `moustass_db`.`log_file` (
  `id_log_file` INT NOT NULL AUTO_INCREMENT,
  `id_user` INT NOT NULL,
  `log_journal` DATETIME NOT NULL,
  `user_public_key` VARCHAR(2000) NOT NULL,
  `user_file_hash` VARCHAR(2000) NOT NULL,
  `signed_filed_hash` VARCHAR(2000) NOT NULL,
  PRIMARY KEY (`id_log_file`),
  INDEX `id_user_idx` (`id_user` ASC) VISIBLE,
  CONSTRAINT `id_user`
    FOREIGN KEY (`id_user`)
    REFERENCES `moustass_db`.`users` (`idusers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `moustass_db`.`log_auth` (
  `id_log_auth` INT NOT NULL AUTO_INCREMENT,
  `iduser` INT NOT NULL,
  `log_date` DATE NOT NULL,
  `log_time` DATETIME NOT NULL,
  `auth_attempt` INT NULL,
  PRIMARY KEY (`id_log_auth`),
  INDEX `iduser_idx` (`iduser` ASC) VISIBLE,
  CONSTRAINT `iduser`
    FOREIGN KEY (`iduser`)
    REFERENCES `moustass_db`.`users` (`idusers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
