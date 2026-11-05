-- CRIANDO TABELA DE CATEGORIAS
CREATE TABLE categorias (
	id_categoria SERIAL PRIMARY KEY NOT NULL,
	nome_categoria VARCHAR(40) NOT NULL
);

-- CRIANDO TABELA CLIENTES
CREATE TABLE clientes (
	id_cliente SERIAL PRIMARY KEY NOT NULL,
	nome_cliente VARCHAR(80) NOT NULL
);

-- CRIANDO TABELA DE PRODUTOS
CREATE TABLE produtos (
	id_produto SERIAL PRIMARY KEY NOT NULL,
	nome_produto VARCHAR(80),
	preco DECIMAL(8,2),
	id_categoria INTEGER NOT NULL,
		CONSTRAINT fk_produtos_categorias
			FOREIGN KEY (id_categoria) REFERENCES categorias (id_categoria)
);

-- criando a tabela de pedidos
CREATE TABLE pedidos (
	id_pedido SERIAL PRIMARY KEY NOT NULL,
	data DATE NOT NULL,
	id_cliente INTEGER NOT NULL,
		CONSTRAINT fk_pedidos_clientes
			FOREIGN KEY(id_cliente) REFERENCES clientes (id_cliente)
);

-- criando a associativa item_pedido
CREATE TABLE item_pedido (
	id_pedido INTEGER NOT NULL,
	id_produto INTEGER NOT NULL,
	quantidade INTEGER,
		CONSTRAINT pk_item_pedido PRIMARY KEY(id_pedido, id_produto),
		CONSTRAINT fk_item_pedido_pedidos
			FOREIGN KEY (id_pedido) REFERENCES pedidos (id_pedido),
		CONSTRAINT fk_item_pedido_produtos
			FOREIGN KEY (id_produto) REFERENCES produtos (id_produto)
);

-- 1) LIMPA OS DADOS E REINICIA OS IDs
TRUNCATE TABLE item_pedido, pedidos, produtos, clientes, categorias RESTART IDENTITY CASCADE;

-- 2) POPULANDO CATEGORIAS
INSERT INTO categorias (nome_categoria) VALUES
	('Eletrônicos'),
	('Informática'),
	('Livros'),
	('Papelaria'),
	('Casa e Cozinha'),
	('Esportes');

-- 3) POPULANDO CLIENTES
INSERT INTO clientes (nome_cliente) VALUES
	('Ana Souza'),
	('Bruno Lima'),
	('Carla Mendes'),
	('Daniel Rocha'),
	('Eduarda Alves'),
	('Felipe Costa'),
	('Giovana Martins'),
	('Henrique Dias');

-- 4) POPULANDO PRODUTOS
INSERT INTO produtos (nome_produto, preco, id_categoria) VALUES
	('Smartphone X10', 1899.90, 1),
	('Fone de Ouvido Bluetooth', 149.90, 1),
	('Smart TV 43 polegadas', 2299.00, 1),
	('Notebook 15 polegadas', 3499.00, 2),
	('Mouse sem fio', 59.90, 2),
	('Teclado mecânico', 289.90, 2),
	('Monitor 24 polegadas', 799.00, 2),
	('Dom Casmurro', 39.90, 3),
	('Algoritmos: Teoria e Prática', 189.00, 3),
	('Caderno universitário', 24.90, 4),
	('Kit de canetas coloridas', 19.90, 4),
	('Mochila escolar', 129.90, 4),
	('Jogo de panelas antiaderente', 249.90, 5),
	('Cafeteira elétrica', 179.90, 5),
	('Bola de futebol', 89.90, 6),
	('Tênis de corrida', 349.90, 6);

-- 5) POPULANDO PEDIDOS
INSERT INTO pedidos (data, id_cliente) VALUES
	('2026-09-02', 1),
	('2026-09-05', 2),
	('2026-09-10', 3),
	('2026-09-15', 1),
	('2026-09-20', 4),
	('2026-10-01', 5),
	('2026-10-04', 6),
	('2026-10-09', 2),
	('2026-10-14', 7),
	('2026-10-21', 8),
	('2026-10-28', 3),
	('2026-11-03', 5);

-- 6) POPULANDO ITEM_PEDIDO
INSERT INTO item_pedido (id_pedido, id_produto, quantidade) VALUES
	(1, 1, 1),
	(1, 2, 2),
	(2, 4, 1),
	(2, 5, 1),
	(3, 8, 3),
	(3, 10, 2),
	(4, 6, 1),
	(4, 7, 1),
	(5, 13, 1),
	(5, 14, 1),
	(6, 3, 1),
	(7, 15, 2),
	(7, 16, 1),
	(8, 9, 1),
	(8, 11, 4),
	(9, 12, 1),
	(9, 2, 1),
	(10, 1, 1),
	(10, 5, 2),
	(11, 7, 2),
	(11, 6, 1),
	(12, 16, 1),
	(12, 15, 1);

-- 7) CONFERINDO O RESULTADO
SELECT p.id_pedido,
       p.data,
       c.nome_cliente,
       pr.nome_produto,
       cat.nome_categoria,
       i.quantidade,
       pr.preco,
       (i.quantidade * pr.preco) AS subtotal
FROM pedidos p
JOIN clientes c ON c.id_cliente = p.id_cliente
JOIN item_pedido i ON i.id_pedido = p.id_pedido
JOIN produtos pr ON pr.id_produto = i.id_produto
JOIN categorias cat ON cat.id_categoria = pr.id_categoria
ORDER BY p.id_pedido, pr.nome_produto;






