# my_warehouse

My Warehouse

## Estrutura de um Banco de Dados para um Almoxarifado de Laboratório

**Entendendo as Necessidades**

Identificar as principais entidades e seus relacionamentos que compõem o sistema de almoxarifado de um laboratório. A partir dessa análise, podemos propor uma estrutura de banco de dados que atenda às necessidades de gestão do almoxarifado.

**Entidades e Atributos Propostos**

**1. Produtos**
**2. Fornecedores**
**3. Compras**
**4. Itens da Compra**
**5. Consumo Interno**
**6. Sugestões de Compra**

**Relacionamentos:**

* Um fornecedor pode ter muitos produtos.
* Uma compra pode ter muitos produtos (tabela de junção).
* Um produto pode ser consumido várias vezes.
* Um produto pode ter várias sugestões de compra.

**Considerações Adicionais:**

* **Prazos de Entrega:** Essa informação pode ser armazenada na tabela de compras, associada ao fornecedor ou ao produto, dependendo da granularidade desejada.
* **Plano de Consumo e Projeção de Gastos:** Essas informações podem ser armazenadas em tabelas separadas ou em campos adicionais nas tabelas de produtos ou sugestões de compra.
* **Perdas:** Uma tabela específica para registrar as perdas, com informações como data, produto, quantidade e motivo, pode ser útil.
* **Qualificação de Fornecedores:** Essa informação pode ser armazenada em uma tabela separada ou em um campo específico na tabela de fornecedores.
