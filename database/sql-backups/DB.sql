DROP SCHEMA IF EXISTS eventos;
CREATE SCHEMA IF NOT EXISTS eventos;
USE eventos;

CREATE TABLE IF NOT EXISTS cidades(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome_cidade VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS artistas(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    telefone VARCHAR(16) NOT NULL,
    email VARCHAR(50) NOT NULL,
    pagina_web VARCHAR(100) NOT NULL DEFAULT "Não Informada"
);

CREATE TABLE IF NOT EXISTS tipo_eventos(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    tipo VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS precos(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    cachê DOUBLE NOT NULL,
    
    artista_id INT NOT NULL,
    CONSTRAINT fk_artitas_precos
		FOREIGN KEY(artista_id)
        REFERENCES artistas(id),
        
	tipo_evento_id INT NOT NULL,
    CONSTRAINT fk_tipo_eventos_precos
		FOREIGN KEY(tipo_evento_id)
        REFERENCES tipo_eventos(id)
);

CREATE TABLE IF NOT EXISTS eventos(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    data_evento DATETIME NOT NULL,
    localizacao VARCHAR(100) NOT NULL,
    valor_ingresso DOUBLE NOT NULL,
    publico_maximo INT NOT NULL,
            
	tipo_evento_id INT NOT NULL,
    CONSTRAINT fk_tipo_eventos_eventos
		FOREIGN KEY(tipo_evento_id)
        REFERENCES tipo_eventos(id),
        
	cidade_id INT NOT NULL,
    CONSTRAINT fk_cidades_eventos
		FOREIGN KEY(cidade_id)
        REFERENCES cidades(id),
        
	publico_presente INT DEFAULT (publico_maximo)
);

CREATE TABLE IF NOT EXISTS artistas_eventos(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    
    artista_id INT NOT NULL,
    CONSTRAINT fk_artitas_artistas_eventos
		FOREIGN KEY(artista_id)
        REFERENCES artistas(id),
        
	evento_id INT NOT NULL,
    CONSTRAINT fk_eventos_artistas_eventos
		FOREIGN KEY(evento_id)
        REFERENCES eventos(id)
);

CREATE TABLE IF NOT EXISTS despesas(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    marketing DOUBLE NOT NULL,
    
    evento_id INT NOT NULL,
    CONSTRAINT fk_eventos_despesas
		FOREIGN KEY(evento_id)
        REFERENCES eventos(id)
);

CREATE TABLE IF NOT EXISTS artistas_despesas(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    hospedagem DOUBLE NOT NULL,
    
    preco_id INT NOT NULL,
    CONSTRAINT fk_precos_artistas_despesas
		FOREIGN KEY(preco_id)
        REFERENCES precos(id),
	
	despesa_id INT NOT NULL,
    CONSTRAINT fk_despesas_artistas_despesas
		FOREIGN KEY(despesa_id)
        REFERENCES despesas(id),

	cachê DOUBLE
);

CREATE TABLE IF NOT EXISTS receitas(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    
    evento_id INT NOT NULL,
    CONSTRAINT fk_eventos_receitas
		FOREIGN KEY(evento_id)
        REFERENCES eventos(id),
        
    renda DOUBLE
);

CREATE TABLE IF NOT EXISTS lucros(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    
    evento_id INT NOT