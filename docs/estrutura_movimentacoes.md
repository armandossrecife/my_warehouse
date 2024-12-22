## Movimentações do estoque

**Usuários:**
* **usuarioId:** Identificador único para cada usuário (chave primária).
* **nome:** Nome do usuário.

**Lotes:**
* **loteId:** Identificador único para cada lote (chave primária).
* **loteValidade:** Data de validade do lote.

**Fabricantes:**
* **id:** Identificador único para cada fabricante (chave primária).
* **FabricanteDescricao:** Descrição do fabricante.

**Itens:**
* **itemId:** Identificador único para cada item (chave primária).
* **itemDescricao:** Descrição do item.
* **tipo:** Tipo do item (caractere único).
* **tipoItem:** Tipo específico do item.
* **especificacao:** Especificação do item.
* **loteQuantidade:** Quantidade do item no lote.
* **data:** Data de registro do item.
* **precoMedio:** Preço médio do item.
* **valorTotal:** Valor total do item.
* **loteId:** Identificador do lote associado ao item (chave estrangeira referenciando a tabela Lotes).
* **usuarioId:** Identificador do usuário associado ao item (chave estrangeira referenciando a tabela Usuarios).
* **fabricanteId:** Identificador do fabricante associado ao item (chave estrangeira referenciando a tabela Fabricantes).

**Observações-chave:**

* A tabela **Itens** é a tabela central, armazenando informações detalhadas sobre cada item, incluindo suas características, quantidade, preço e associações com outras tabelas.
* O uso de **chaves estrangeiras** estabelece relacionamentos entre a tabela Itens e as tabelas Lotes, Usuarios e Fabricantes, garantindo a integridade dos dados e permitindo a recuperação eficiente de dados.

## Detalhamento:

**Estrutura do Banco de Dados:**

Este conjunto de tabelas descreve uma base de dados que pode ser usada para gerenciar informações sobre produtos (itens) e suas relações com usuários, lotes e fabricantes.

* **Tabela Usuarios:** Armazena informações básicas sobre os usuários do sistema, como um identificador único (usuarioId) e o nome do usuário.
* **Tabela Lotes:** Armazena informações sobre lotes de produtos, incluindo um identificador único (loteId) e a data de validade do lote.
* **Tabela Fabricantes:** Armazena informações sobre os fabricantes dos produtos, com um identificador único (id) e uma descrição do fabricante.
* **Tabela Itens:** É a tabela principal e armazena detalhes sobre cada item, como descrição, tipo, quantidade, preço, data de registro e, o mais importante, as relações com outras tabelas. As chaves estrangeiras (loteId, usuarioId e fabricanteId) ligam cada item a um lote específico, um usuário específico e um fabricante específico.

**Relações entre as Tabelas:**

As chaves estrangeiras criam um relacionamento entre as tabelas, permitindo que você, por exemplo:

* Descubra todos os itens de um determinado lote.
* Veja todos os itens comprados por um usuário específico.
* Encontrar todos os itens fabricados por um determinado fabricante.

**Tipos de Dados:**

O tipo de dado DECIMAL(10,2) é usado para armazenar valores monetários, como o preço médio e o valor total de um item. Isso significa que esses valores podem ter até 10 dígitos no total, com 2 dígitos após o ponto decimal, o que é comum para representar valores monetários.

**Em resumo:**

Esta estrutura de banco de dados fornece uma forma organizada de armazenar e gerenciar informações sobre produtos, seus fabricantes, os usuários que os compram e os lotes aos quais pertencem. As chaves estrangeiras garantem a integridade dos dados e as relações entre as tabelas permitem realizar consultas complexas e obter informações valiosas sobre os dados armazenados.