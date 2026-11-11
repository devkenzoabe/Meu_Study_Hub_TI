-- Questão 1
SELECT COUNT(*)
FROM fato_vendas
WHERE id_cliente IS NULL;

-- Questão 2
SELECT COUNT(DISTINCT id_cliente) 
FROM fato_vendas;

-- Questão 3
SELECT SUM(valor_total)         AS faturamento_total
FROM fato_vendas
WHERE data_venda >= '2025-01-01';

-- Questão 4
SELECT DISTINCT marca
FROM dim_produto
WHERE categoria = 'Higiene'
ORDER BY marca;

-- Questão 5
SELECT AVG(valor_total)			AS valor_medio_aplicativo
FROM fato_vendas
WHERE canal = 'Aplicativo';

-- Questão 6
SELECT COUNT(*) 				AS qtd_bebidas_acima_10
FROM dim_produto
WHERE categoria = 'Bebidas'
 AND preco_tabela > 10

-- Questão 7
SELECT nome_produto, marca, preco_tabela
FROM dim_produto 
ORDER BY preco_tabela DESC, nome_produto ASC
LIMIT 1;

-- Questão 8
SELECT categoria,
	   COUNT(*) 				AS qtd_produtos
FROM dim_produto
GROUP BY categoria
ORDER BY qtd_produtos DESC, categoria ASC;

-- Questão 9
SELECT categoria,
	   AVG(preco_tabela)		AS valor_medio_categoria
FROM dim_produto
GROUP BY categoria
ORDER BY valor_medio_categoria DESC;

-- Questão 10
SELECT cidade,
	   COUNT(*)  				AS qtd_clientes
FROM dim_cliente
GROUP BY cidade 
HAVING COUNT(*) >= 60
ORDER BY qtd_clientes DESC, cidade ASC;

-- Questão 11
SELECT COUNT(*) 				AS clientes_sem_email
FROM dim_cliente
WHERE email IS NULL;

-- Questão 12
SELECT COUNT(*)					AS  clientes_f_nascidas_anos_90
FROM dim_cliente
WHERE sexo = 'F'
AND data_nascimento BETWEEN '1990-01-01' AND '1999-12-31';

-- Questão 13
SELECT COUNT(*)		 			AS clientes_primeiro_nome_ana
FROM dim_cliente
WHERE nome LIKE 'Ana %';
 
-- Questão 14
SELECT uf,
	   COUNT(*) 				AS qtd_lojas
FROM dim_loja
GROUP BY uf
HAVING COUNT(*) > 3
ORDER BY qtd_lojas DESC;
 
-- Questão 15
SELECT nome_loja, cidade, data_inauguracao
FROM dim_loja
WHERE data_inauguracao < '2007-01-01'
ORDER BY data_inauguracao ASC;
 
-- Questão 16
SELECT canal,
	   SUM(valor_total) 		AS faturamento
FROM fato_vendas
WHERE data_venda >= '2025-01-01'
AND data_venda <  '2026-01-01'
GROUP BY canal
ORDER BY faturamento DESC;
 
-- Questão 17
SELECT forma_pagamento,
       COUNT(*)        	 		AS qtd_linhas,
       SUM(valor_total) 		AS faturamento
FROM fato_vendas
WHERE canal = 'Loja física'
GROUP BY forma_pagamento
ORDER BY faturamento DESC;
 
-- Questão 18
SELECT id_produto, 
	   SUM(quantidade) 			AS unidades_vendidas
FROM fato_vendas
GROUP BY id_produto
ORDER BY unidades_vendidas DESC, id_produto ASC
LIMIT 10;
 
-- Questão 19
SELECT id_loja, 
       SUM(valor_total) 		AS faturamento
FROM fato_vendas
WHERE data_venda >= '2024-01-01'
AND data_venda <  '2025-01-01'
GROUP BY id_loja
ORDER BY faturamento DESC
LIMIT 5;
 
-- Questão 20
SELECT id_loja, 
	   COUNT(*) 				AS qtd_linhas
FROM fato_vendas
GROUP BY id_loja
HAVING COUNT(*) > 300
ORDER BY qtd_linhas DESC;
 
-- Questão 21
SELECT id_cliente, 
	   COUNT(*) 				AS qtd_linhas
FROM fato_vendas
WHERE id_cliente IS NOT NULL
GROUP BY id_cliente
HAVING COUNT(*) >= 70
ORDER BY qtd_linhas DESC, id_cliente ASC;
 
-- Questão 22
SELECT COUNT(*)                 AS linhas_com_desconto,
       ROUND(AVG(desconto), 2)  AS desconto_medio
FROM fato_vendas
WHERE desconto > 0;
 
-- Questão 23
SELECT MIN(valor_total) 		AS menor_valor,
       MAX(valor_total) 		AS maior_valor
FROM fato_vendas
WHERE data_venda >= '2025-12-01'
AND data_venda <  '2026-01-01';
 
-- Questão 24
SELECT COUNT(*)         		AS qtd_linhas,
       SUM(valor_total) 		AS faturamento_dia
FROM fato_vendas
WHERE data_venda = '2025-12-24';
 
-- Questão 25
SELECT id_venda,
       quantidade * preco_unitario 									AS valor_bruto,
       desconto,
       valor_total,
       ROUND(desconto / (quantidade * preco_unitario) * 100, 2) 	AS percentual_desconto
FROM fato_vendas
WHERE canal = 'Site'
AND data_venda >= '2025-01-01'
AND data_venda <  '2026-01-01'
AND desconto > 0
ORDER BY desconto / (quantidade * preco_unitario) DESC, id_venda ASC
LIMIT 10;