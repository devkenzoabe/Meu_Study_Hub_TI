CREATE TABLE planos (
	id_plano SERIAL PRIMARY KEY NOT NULL,
	preco DECIMAL(6,2) NOT NULL,
		CONSTRAINT ck_planos CHECK(preco > 0)
);

--- criando tabela de diretores
CREATE TABLE diretores (
	id_diretor SERIAL PRIMARY KEY NOT NULL,
	nome_diretor VARCHAR(60) NOT NULL
);

--- CRIANDO A TABELA DE GENEROS
CREATE TABLE generos (
	id_genero SERIAL PRIMARY KEY NOT NULL,
	nome VARCHAR(50) NOT NULL
);

-- CRIANDO A TABELA DE USUARIOS
CREATE TABLE usuarios (
	id_usuario SERIAL PRIMARY KEY NOT NULL,
	email_usuario VARCHAR(80) NOT NULL,
	id_plano INTEGER NOT NULL,
		CONSTRAINT fk_usuario_plano
			FOREIGN KEY(id_plano) REFERENCES planos (id_plano)
);

----- criando a tabela de filmes
CREATE TABLE filmes (
	id_filme SERIAL PRIMARY KEY NOT NULL,
	titulo VARCHAR(120) NOT NULL,
	ano INTEGER,
	id_genero INTEGER NOT NULL,
	id_diretor INTEGER NOT NULL,
		CONSTRAINT fk_generos_filmes
			FOREIGN KEY(id_genero) REFERENCES generos(id_genero),
		CONSTRAINT fk_diretor_filme
			FOREIGN KEY(id_diretor) REFERENCES diretores(id_diretor)
);

---- CRIANDO A TABELA ASSOCIATIVA NTRE FILMES E USUARIOS
CREATE TABLE assistidos (
	id_usuario INTEGER NOT NULL,
	id_filme INTEGER NOT NULL,
		CONSTRAINT pk_assistidos PRIMARY KEY(id_usuario, id_filme),
		CONSTRAINT fk_assistidos_usuarios
			FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario),
		CONSTRAINT fk_assistidos_filmes
			FOREIGN KEY (id_filme) REFERENCES filmes(id_filme)
);


--- INSERINDO REGISTROS DA IA EM STREAMING

-- 1. PLANOS
INSERT INTO planos (preco) VALUES
(19.90),
(29.90),
(49.90);


-- =====================================================
-- 2. DIRETORES
-- =====================================================

INSERT INTO diretores (nome_diretor) VALUES
('Christopher Nolan'),
('Steven Spielberg'),
('James Cameron'),
('Quentin Tarantino'),
('Martin Scorsese'),
('Peter Jackson'),
('Denis Villeneuve'),
('Greta Gerwig'),
('David Fincher'),
('Tim Burton'),
('Ridley Scott'),
('Alfred Hitchcock'),
('Stanley Kubrick'),
('Francis Ford Coppola'),
('Wes Anderson'),
('Bong Joon-ho'),
('Jordan Peele'),
('Sofia Coppola'),
('Guillermo del Toro'),
('Robert Zemeckis'),
('Ron Howard'),
('Ang Lee'),
('David Lynch'),
('Spike Lee'),
('Woody Allen'),
('Sam Mendes'),
('Alejandro González Iñárritu'),
('Taika Waititi'),
('Patty Jenkins'),
('George Lucas');


-- =====================================================
-- 3. GÊNEROS
-- =====================================================

INSERT INTO generos (nome) VALUES
('Ação'),
('Aventura'),
('Ficção Científica'),
('Drama'),
('Comédia'),
('Terror'),
('Suspense'),
('Fantasia'),
('Romance'),
('Animação'),
('Musical'),
('Documentário'),
('Crime'),
('Guerra'),
('Histórico'),
('Biografia'),
('Esporte'),
('Família'),
('Mistério'),
('Western');


-- =====================================================
-- 4. USUÁRIOS
-- 65 USUÁRIOS DISTRIBUÍDOS ENTRE 3 PLANOS
-- =====================================================

INSERT INTO usuarios (email_usuario, id_plano)
SELECT
    'usuario' || n || '@gmail.com',
    ((n - 1) % 3) + 1
FROM generate_series(1, 65) AS n;


-- =====================================================
-- 5. FILMES
-- =====================================================

INSERT INTO filmes (titulo, ano, id_genero, id_diretor) VALUES
('A Origem', 2010, 3, 1),
('Interestelar', 2014, 3, 1),
('Oppenheimer', 2023, 4, 1),
('Jurassic Park', 1993, 2, 2),
('E.T. O Extraterrestre', 1982, 3, 2),
('Titanic', 1997, 9, 3),
('Avatar', 2009, 3, 3),
('Pulp Fiction', 1994, 7, 4),
('Kill Bill', 2003, 1, 4),
('O Lobo de Wall Street', 2013, 4, 5),
('Os Infiltrados', 2006, 7, 5),
('O Senhor dos Anéis', 2001, 8, 6),
('O Hobbit', 2012, 8, 6),
('Duna', 2021, 3, 7),
('Blade Runner 2049', 2017, 3, 7),
('Barbie', 2023, 5, 8),
('Adoráveis Mulheres', 2019, 4, 8),
('Clube da Luta', 1999, 7, 9),
('Seven', 1995, 7, 9),
('Edward Mãos de Tesoura', 1990, 8, 10),
('Gladiador', 2000, 4, 11),
('Alien: O Oitavo Passageiro', 1979, 6, 11),
('Blade Runner', 1982, 3, 11),
('O Iluminado', 1980, 6, 13),
('2001: Uma Odisseia no Espaço', 1968, 3, 13),
('Laranja Mecânica', 1971, 7, 13),
('O Poderoso Chefão', 1972, 4, 14),
('Apocalypse Now', 1979, 4, 14),
('Drácula de Bram Stoker', 1992, 8, 14),
('O Grande Hotel Budapeste', 2014, 5, 15),
('A Vida Marinha com Steve Zissou', 2004, 5, 15),
('Parasita', 2019, 7, 16),
('Memórias de um Assassino', 2003, 7, 16),
('Corra!', 2017, 6, 17),
('Nós', 2019, 6, 17),
('Encontros e Desencontros', 2003, 4, 18),
('Maria Antonieta', 2006, 4, 18),
('O Labirinto do Fauno', 2006, 8, 19),
('A Forma da Água', 2017, 8, 19),
('De Volta para o Futuro', 1985, 3, 20),
('Forrest Gump', 1994, 4, 20),
('Náufrago', 2000, 4, 20),
('Uma Mente Brilhante', 2001, 4, 21),
('Apollo 13', 1995, 4, 21),
('O Segredo de Brokeback Mountain', 2005, 4, 22),
('As Aventuras de Pi', 2012, 8, 22),
('Cidade dos Sonhos', 2001, 7, 23),
('Veludo Azul', 1986, 7, 23),
('Faça a Coisa Certa', 1989, 4, 24),
('Malcolm X', 1992, 6, 24),
('Noivo Neurótico, Noiva Nervosa', 1977, 5, 25),
('Meia-Noite em Paris', 2011, 9, 25),
('Beleza Americana', 1999, 4, 26),
('1917', 2019, 4, 26),
('Birdman', 2014, 4, 27),
('O Regresso', 2015, 4, 27),
('Jojo Rabbit', 2019, 5, 28),
('Thor: Ragnarok', 2017, 1, 28),
('Mulher-Maravilha', 2017, 1, 29),
('Monster', 2003, 6, 29),
('Star Wars: Uma Nova Esperança', 1977, 3, 30),
('Star Wars: O Império Contra-Ataca', 1980, 3, 30),
('Indiana Jones e os Caçadores da Arca Perdida', 1981, 2, 30),
('O Resgate do Soldado Ryan', 1998, 4, 2),
('A Lista de Schindler', 1993, 4, 2),
('Psicose', 1960, 6, 12),
('Um Corpo que Cai', 1958, 7, 12),
('Os Bons Companheiros', 1990, 13, 5),
('Taxi Driver', 1976, 4, 5),
('Os Incríveis', 2004, 10, 2),
('Procurando Nemo', 2003, 10, 2),
('Wall-E', 2008, 3, 2),
('Cisne Negro', 2010, 4, 5),
('O Artista', 2011, 11, 15),
('La La Land', 2016, 11, 8),
('Whiplash', 2014, 4, 8),
('Bohemian Rhapsody', 2018, 16, 9),
('O Jogo da Imitação', 2014, 16, 9),
('O Discurso do Rei', 2010, 4, 26),
('Django Livre', 2012, 1, 4);


-- =====================================================
-- 6. FILMES ASSISTIDOS
-- 5 FILMES PARA CADA USUÁRIO
-- =====================================================

INSERT INTO assistidos (id_usuario, id_filme)
SELECT
    u.id_usuario,
    ((u.id_usuario * 7 + f.numero * 11) % 80) + 1
FROM usuarios u
CROSS JOIN generate_series(0, 4) AS f(numero);


-- =====================================================
-- 7. CONSULTAS PARA CONFERIR OS DADOS
-- =====================================================

SELECT * FROM planos;

SELECT * FROM diretores;

SELECT * FROM generos;

SELECT * FROM usuarios;

SELECT * FROM filmes;

SELECT * FROM assistidos;


-- =====================================================
-- 8. CONSULTA GERAL COM TODOS OS RELACIONAMENTOS
-- =====================================================

SELECT
    u.email_usuario,
    p.preco AS preco_plano,
    f.titulo AS filme,
    f.ano,
    g.nome AS genero,
    d.nome_diretor AS diretor
FROM assistidos a
INNER JOIN usuarios u
    ON a.id_usuario = u.id_usuario
INNER JOIN planos p
    ON u.id_plano = p.id_plano
INNER JOIN filmes f
    ON a.id_filme = f.id_filme
INNER JOIN generos g
    ON f.id_genero = g.id_genero
INNER JOIN diretores d
    ON f.id_diretor = d.id_diretor
ORDER BY u.id_usuario;














