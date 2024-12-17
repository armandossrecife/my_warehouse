CREATE TABLE Produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT,
    unidade_medida TEXT,
    fabricante TEXT,
    fornecedor INTEGER,
    valor_unitario REAL,
    estoque_minimo INTEGER,
    estoque_maximo INTEGER,
    localizacao TEXT,
    data_validade DATE,
    FOREIGN KEY(fornecedor) REFERENCES Fornecedores(id)
);

CREATE TABLE Fornecedores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cnpj TEXT,
    contato TEXT,
    endereco TEXT,
    qualificacao TEXT
);

CREATE TABLE Compras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_compra DATE,
    fornecedor INTEGER,
    valor_total REAL,
    forma_pagamento TEXT,
    nota_fiscal TEXT,
    FOREIGN KEY(Fornecedor) REFERENCES Fornecedores(id)
);

CREATE TABLE Itens_Compra (
    id_item INTEGER PRIMARY KEY AUTOINCREMENT,
    compra INTEGER,
    produto INTEGER,
    quantidade INTEGER,
    valor_unitario REAL,
    valor_total REAL,
    FOREIGN KEY(compra) REFERENCES Compras(id),
    FOREIGN KEY(produto) REFERENCES Produtos(id)
);

CREATE TABLE Consumo_Interno (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_consumo DATE,
    produto INTEGER,
    quantidade INTEGER,
    setor_solicitante TEXT,
    observacoes TEXT,
    FOREIGN KEY(produto) REFERENCES Produtos(id)
);

CREATE TABLE Sugestoes_Compra (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto INTEGER,
    quantidade_sugerida INTEGER,
    data_sugestao DATE,
    justificativa TEXT,
    FOREIGN KEY(produto) REFERENCES Produtos(id)
);