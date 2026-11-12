-- Questão 1
SELECT uf,
        COUNT(*) 						AS qtd_clientes
FROM clientes_banco
WHERE data_referencia = '2024-01-15'
GROUP BY uf
ORDER BY qtd_clientes DESC
LIMIT 5;

-- Questão 2
SELECT nome, saldo
FROM clientes_banco
WHERE data_referencia = '2024-04-15'
ORDER BY saldo DESC
LIMIT 1;

-- Questão 3
SELECT COUNT(DISTINCT id_cliente) 		AS qtd_clientes_diferentes
FROM clientes_banco;

-- Questão 4 
SELECT ROUND(AVG(renda_mensal), 2)		AS renda_media_prime
FROM clientes_banco
WHERE segmento = 'Prime'
AND data_referencia BETWEEN '2024-12-01' AND '2024-12-31';

-- Questão 5
SELECT profissao,
		COUNT(*) 						AS profissao_clientes
FROM clientes_banco
WHERE data_referencia BETWEEN '2024-12-01' AND '2024-12-31'
GROUP BY profissao
ORDER BY profissao_clientes DESC
LIMIT 3;

-- Questão 6
SELECT data_referencia,
		COUNT(*) 						AS qtd_contas_bloqueadas
FROM clientes_banco
WHERE status_conta = 'Bloqueada'
GROUP BY data_referencia
ORDER BY qtd_contas_bloqueadas DESC
LIMIT 1;

-- Questão 7
SELECT cidade,
		ROUND(AVG(saldo), 2)			AS saldo_medio_cidade
FROM clientes_banco
WHERE data_referencia BETWEEN '2024-09-01' AND '2024-09-30'
GROUP BY cidade	
HAVING COUNT(*) >= 50
ORDER BY saldo_medio_cidade DESC
LIMIT 1;

-- Questão 8
SELECT SUM(saldo)						AS soma_saldo_private
FROM clientes_banco
WHERE segmento = 'Private'
AND data_referencia BETWEEN '2024-12-01' AND '2024-12-31';

-- Questão 9
SELECT agencia,
		COUNT(*)						AS qtd_clientes_agencia
FROM clientes_banco
WHERE data_referencia BETWEEN '2024-12-01' AND '2024-12-31'
GROUP BY agencia
ORDER BY qtd_clientes_agencia DESC
LIMIT 1;

-- Questão 10
SELECT data_referencia,
		SUM(saldo) 					AS maior_saldo_clientes
FROM clientes_banco
GROUP BY data_referencia
ORDER BY maior_saldo_clientes DESC
LIMIT 1;

-- Questão 11
SELECT COUNT(DISTINCT id_cliente)					AS qtd_contas_encerradas
FROM clientes_banco
WHERE status_conta = 'Encerrada'
AND data_referencia BETWEEN '2024-01-01' AND '2024-12-31';


-- Questão 12
SELECT ROUND(AVG(score_credito), 2) 		AS score_medio_df
FROM clientes_banco
WHERE uf = 'DF'
AND data_referencia BETWEEN '2024-06-01' AND '2024-06-30';

-- Questão 13
SELECT COUNT(*) 							AS qtd_clientes
FROM clientes_banco
WHERE data_referencia BETWEEN '2024-03-01' AND '2024-03-31'
AND score_credito >= 700
AND possui_cartao = false;

-- Questão 14
SELECT canal_preferido,
        COUNT(*) 							AS qtd_clientes
FROM clientes_banco
WHERE data_referencia BETWEEN '2024-12-01' AND '2024-12-31'
GROUP BY canal_preferido
ORDER BY qtd_clientes DESC;

-- Questão 15
SELECT COUNT(DISTINCT id_cliente) 			AS qtd_clientes_novos_2024
FROM clientes_banco
WHERE data_abertura BETWEEN '2024-01-01' AND '2024-12-31';

-- Questão 16
SELECT tipo_conta,
        ROUND(AVG(saldo), 2)				AS saldo_medio
FROM clientes_banco
WHERE data_referencia BETWEEN '2024-12-01' AND '2024-12-31'
GROUP BY tipo_conta
ORDER BY saldo_medio DESC;

-- Questão 17
SELECT MAX(limite_credito) AS maior_limite_varejo
FROM clientes_banco
WHERE segmento = 'Varejo'
AND data_referencia BETWEEN '2024-12-01' AND '2024-12-31';

-- Questão 18
SELECT sexo,
        COUNT(*) 							AS qtd_clientes
FROM clientes_banco
WHERE data_referencia BETWEEN '2024-12-01' AND '2024-12-31'
AND possui_investimento = true
GROUP BY sexo
ORDER BY qtd_clientes DESC;

-- Questão 19
SELECT uf,
		COUNT(*)						AS qtd_clientes_uf
FROM clientes_banco
WHERE data_referencia BETWEEN '2024-12-01' AND '2024-12-31'
GROUP BY uf
HAVING COUNT(*) < 13
ORDER BY qtd_clientes_uf ASC;

-- Questão 20
SELECT COUNT(*)						AS clientes_nasc_60
FROM clientes_banco
WHERE data_referencia BETWEEN '2024-12-01' AND '2024-12-31'
AND data_nascimento < '1960-01-01';

