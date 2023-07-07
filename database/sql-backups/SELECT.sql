SELECT * 
FROM estados;

SELECT C.id, C.nome_cidade, E.nome_estado 
FROM cidades AS C JOIN estados AS E ON C.estado_id = E.id;

SELECT * FROM artistas;

SELECT * FROM tipo_eventos;

SELECT P.id, P.cachê, A.nome, TE.tipo 
FROM precos AS P JOIN artistas AS A ON P.artista_id = A.id JOIN tipo_eventos AS TE ON P.tipo_evento_id = TE.id;

SELECT E.id, E.data_evento, E.localizacao, E.valor_ingresso, E.publico_maximo, E.publico_presente, TE.tipo, C.nome_cidade
FROM eventos AS E JOIN tipo_eventos AS TE ON E.tipo_evento_id = TE.id JOIN cidades AS C ON E.cidade_id = C.id;

SELECT AE.id, A.nome, E.data_evento, E.localizacao
FROM artistas_eventos AS AE JOIN artistas AS A ON AE.artista_id = A.id JOIN eventos AS E ON AE.evento_id = E.id;

SELECT D.id, D.marketing, E.data_evento, E.localizacao
FROM despesas AS D JOIN eventos AS E ON D.evento_id = E.id;

SELECT AD.id, AD.hospedagem, D.marketing, A.nome, P.cachê
FROM artistas_despesas AS AD JOIN precos AS P ON AD.preco_id = P.id JOIN despesas AS D ON AD.despesa_id = D.id JOIN artistas AS A ON P.artista_id = A.id;

SELECT R.id, R.renda, E.data_evento, E.localizacao
FROM receitas AS R JOIN eventos AS E ON R.evento_id = E.id;

SELECT L.id, L.lucro, E.data_evento, E.localizacao 
FROM lucros AS L JOIN eventos AS E ON L.evento_id = E.id;