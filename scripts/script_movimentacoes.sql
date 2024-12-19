CREATE TABLE Usuarios (
    usuarioId INT PRIMARY KEY,
    nome VARCHAR(100)
);

CREATE TABLE Lotes (
    loteId INT PRIMARY KEY,
    loteValidade DATE
);

CREATE TABLE Fabricantes (
    id INT PRIMARY KEY,
    FabricanteDescricao VARCHAR(100)
);

CREATE TABLE Itens (
    itemId INT PRIMARY KEY,
    itemDescricao VARCHAR(100),
    tipo CHAR(1),
    tipoItem VARCHAR(50),
    especificacao VARCHAR(100),
    loteQuantidade INT,
    data DATE,
    precoMedio DECIMAL(10,2),
    valorTotal DECIMAL(10,2),
    loteId INT,
    usuarioId INT,
    fabricanteId INT,
    FOREIGN KEY (loteId) REFERENCES Lotes(loteId),
    FOREIGN KEY (usuarioId) REFERENCES Usuarios(usuarioId),
    FOREIGN KEY (fabricanteId) REFERENCES Fabricantes(id)
);