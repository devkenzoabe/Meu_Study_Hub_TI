-- CRIACAO DO DB BIBLIOTECA
CREATE DATABASE biblioteca;

-- CRIANDO A TABELA DE EDITORAS
CREATE TABLE editoras (
	id_editora SERIAL PRIMARY KEY,
	nome VARCHAR(60) NOT NULL UNIQUE
);

-- CRIANDO A TABELA DE AUTORES
CREATE TABLE autores (
	id_autor SERIAL PRIMARY KEY,
	nome VARCHAR(80) NOT NULL
);

-- CRIANDO A TABELA DE LIVROS
CREATE TABLE livros (
	id_livro SERIAL NOT NULL,
	nome_livro VARCHAR(100) NOT NULL,
	ano INTEGER,
	id_editora INTEGER NOT NULL,
	id_autor INTEGER NOT NULL,
		CONSTRAINT pk_livros
			PRIMARY KEY(id_livro),
		CONSTRAINT dominio_ano
			CHECK(ano BETWEEN 1950 AND 2026),
		CONSTRAINT fk_livros_editoras
			FOREIGN KEY(id_editora) REFERENCES editoras(id_editora),
		CONSTRAINT fk_livros_autores
			FOREIGN KEY(id_autor) REFERENCES autores(id_autor)
);

-- RENOMEIA COLUNA NOME_LIVRO
ALTER TABLE livros RENAME COLUMN nome_livro TO nome

-- CRIA A COLUNA ISBN
ALTER TABLE livros ADD COLUMN isbn CHAR(20)

-- EXCLUI A COLUNA ISBN DA TABELA DE LIVROS
ALTER TABLE livros DROP COLUMN isbn

-- POPULANDO A TABELA DE EDITORAS
INSERT INTO editoras (nome) VALUES
	('Companhia das Letras'),
	('Rocco'),
	('Intrínseca'),
	('Editora Aleph'),
	('HarperCollins Brasil'),
	('Penguin-Companhia'),
	('Editora Record'),
	('Martins Fontes');

-- POPULANDO A TABELA DE AUTORES
INSERT INTO autores (nome) VALUES
	('Machado de Assis'),
	('Clarice Lispector'),
	('George Orwell'),
	('J.K. Rowling'),
	('J.R.R. Tolkien'),
	('Isaac Asimov'),
	('Agatha Christie'),
	('Carlos Drummond de Andrade'),
	('Jorge Amado'),
	('Graciliano Ramos');

-- POPULANDO A TABELA DE LIVROS
INSERT INTO livros (nome, ano, id_editora, id_autor) VALUES
	('Dom Casmurro', 1999, 1, 1),
	('Memórias Póstumas de Brás Cubas', 2001, 1, 1),
	('A Hora da Estrela', 1998, 2, 2),
	('Perto do Coração Selvagem', 2000, 2, 2),
	('1984', 2009, 1, 3),
	('A Revolução dos Bichos', 2007, 1, 3),
	('Harry Potter e a Pedra Filosofal', 2000, 2, 4),
	('Harry Potter e a Câmara Secreta', 2000, 2, 4),
	('O Senhor dos Anéis: A Sociedade do Anel', 2019, 5, 5),
	('O Hobbit', 2019, 5, 5),
	('Eu, Robô', 2014, 4, 6),
	('Fundação', 2012, 4, 6),
	('Assassinato no Expresso do Oriente', 2015, 5, 7),
	('E Não Sobrou Nenhum', 2017, 5, 7),
	('Sentimento do Mundo', 2012, 1, 8),
	('Capitães da Areia', 2008, 1, 9),
	('Gabriela, Cravo e Canela', 2012, 1, 9),
	('Vidas Secas', 2013, 7, 10),
	('São Bernardo', 2008, 7, 10),
	('Angústia', 2010, 7, 10);

-- CONFERINDO O RESULTADO
SELECT l.id_livro,
       l.nome AS livro,
       a.nome AS autor,
       e.nome AS editora,
       l.ano
FROM livros l
JOIN autores a ON a.id_autor = l.id_autor
JOIN editoras e ON e.id_editora = l.id_editora
ORDER BY l.id_livro;