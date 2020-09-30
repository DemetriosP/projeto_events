create database if not exists evento;
use evento;

create table if not exists funcionario
(idfuncionario char(8) not null,
nome varchar(255) not null,
senha varchar(255) not null,
telefone char(11),
email varchar(100) unique not null,
cargo varchar(255) not null,
setor varchar(255) not null,
primary key(idfuncionario));

create table if not exists cliente
(idcpf_cnpj	char(14) not null,
nome varchar(255) not null,
senha varchar(255)  not null,
email varchar(100) unique not null,
data_nascimento date not null,
telefone char(11) not null,
cep char(10) not null,
cidade varchar(255) not null,
endereco varchar(255) not null,
bairro varchar(255) not null,
primary key(idcpf_cnpj));
 
create table if not exists ambiente
(idambiente int auto_increment not null,
localizacao varchar(255) not null,
descricao varchar(255)  not null,
ocupacao_min char(3) not null,
ocupacao_max char(3) not null,
situacao varchar(255) default 'Disponivel',
idfuncionario char(8) not null,
primary key(idAmbiente),
foreign key (idfuncionario) references funcionario(idfuncionario));
 
create table if not exists item
(iditem int auto_increment not null,
data_inclusao date unique not null,
descricao varchar(255)  not null,
categoria varchar(255) not null,
titulo	varchar(255) not null,
tecnica varchar(255),
dimensao varchar(255),
autor varchar(255) not null,
valor decimal(8,2),
imagem blob,
situacao varchar(255) default 'Disponivel',
idfuncionario char(8) not null,
idAmbiente int not null,
primary key(iditem),
foreign key (idfuncionario) references funcionario(idfuncionario),
foreign key (idambiente) references ambiente(idambiente));
 
create table if not exists solicitacao
(idsolicitacao int auto_increment not null,
localizacao varchar(255) not null,
tipo_evento varchar(255) not null,
data_evento date not null,
formato_evento	varchar(255) not null,
item varchar(255),
hora_inicial time not null,
hora_final time not null,
ocupacao char(3) not null,
situacao varchar(255) default 'Aguardando Aprovação',
idcpf_cnpj char(14) not null,
idambiente int not null,
idfuncionario char(8),
idpagamento int,
primary key(idsolicitacao),
foreign key (idambiente) references ambiente(idambiente),
foreign key (idcpf_cnpj) references cliente(idcpf_cnpj),
foreign key (idfuncionario) references funcionario(idfuncionario),
foreign key (idpagamento) references pagamento(idpagamento));

create table if not exists pagamento
(idpagamento int auto_increment not null,
numero_cartao char(16) unique not null,
titular varchar(255)  not null,
validade char(5) not null,
cvv char(3) not null,
parcelas char(2) not null,
primary key(idpagamento));

select * from cliente;
select * from item;
select * from solicitacao;
select * from funcionario;
select * from pagamento;
select * from ambiente;

insert into funcionario
values ('12345678','David Busch','12345678','11988336321',
'david.busch@pinacoteca.com.br','Aux Administrativo','Administrativo'),
       ('87654321','Lucas Andreucci','87654321','19993776436',
       'lucas.andreucci@pinacoteca.com.br','Gerente Administrativo','Administrativo'); 


insert into cliente
values ('00340730005','Victor Paravatti','11223344','victor.paravatti@gmail.com',
'1996-03-21','11986955632','987654000','Pinhalzinho','Rua do Canavial, 59','Parque das Gazelas'),
       ('05804287028','Demetrios Pantaleão','44332211','demetrios.pantaleao@gmail.com',
       '1977-08-26','11958696321','654321000','Tuiuti','Rua dos Mangueiras, 87','Capinzeiro do Boi Gordo');

insert into ambiente
values (1,'Pina Luz','Pátio interno coberto com 220m² e pé direito de 16m','50','250',default,'12345678'),
       (2,'Pina Estação','Pátio interno coberto com 220m², pé direito de 16m e obras de arte permanentes','50','150',default,'87654321');	

insert into item
values (1,'2020-09-18','Adquirido, em 1950, pelo Governo do Estado de São Paulo e, atualmente, pertence ao Acervo da Pinacoteca do Estado de São Paulo.',
		'Escultura','Atleta em descanso, 1896 - 1978',null,'88 x 127 x 72,5 cm','João Batista Ferri',null,'atleta_em_descanso.jpg',default,'12345678',1),
		(2,'2020-09-19','Transferido do Museu Paulista, atualmente pertence ao Acervo da Pinacoteca do Estado de São Paulo.','Pintura',
		'Caipira Picando o Fumo - 1893','Óleo sobre tela','150 x 210 cm','Almeida Junior',null,'caipira_picando_fumo.jpg',default,'87654321',2); 

insert into solicitacao
values (1,'Pina Luz','Jantar','2020-09-20','Corporativo','Santa Ceia', '19:00:00','23:00:00','75',default,'00340730005',1,'12345678','12345678'),
       (2,'Pina Estação','Coquetel','2020-09-21','Academico','Monaliza','16:20:00','21:00:00','120',default,'05804287028',2,'87654321','87654321'); 
       
insert into pagamento
values (1,'5499850790951557','Victor Paravatti','1127','583','24'),
       (2,'4929608417255361','Demetrios Pantaleao','0926','658','11'); 


#1 EXIBE AS DATAS DOS EVENTOS E SEUS RESPECIVOS LOCAIS
select a.local1,a.descricao, date_format(s.data_evento, '%d/ %m /%y') as 'Data do evento', 
s.ambiente, s.tipo_evento as 'Tipo do evento'
from ambiente a inner join solicitacao s
on a.idfuncionario=s.idfuncionario;


#2 EXIBE OS ITENS DO ACERVO, JUNTAMENTE COM OS FUNCIONÁRIOS QUE OS INCLUÍRAM
select i.titulo, i.descricao, i.autor, i.tecnica, f.nome, f.cargo
from item i left join funcionario f
on i.idfuncionario=f.idfuncionario;


#3 INSERÇÃO DE MAIS UM AMBIENTE DISPONÍVEL PARA LOCAÇÃO
insert into ambiente values ('00000003','Vintage','Pátio interno coberto com 250m²','50','300','12345678');


#4 MODIFICAÇÃO DE UMA DATA DE UMA LOCAÇÃO SOLICITADA
UPDATE solicitacao 
SET data_evento='04102020'
WHERE idsolicitacao='123456';


#5 INSERÇÃO DE NOVO ITEM NO ACERVO
insert into item
values ('12345679','20092020','Doado pelo MASP em 1962, atualmente, pertence ao Acervo da Pinacoteca do Estado de São Paulo.','Escultura','Bandeirantes, desbravando o Brasil, de 1903',null,'105x 150 x 90,5 cm','Benedito Calixto','50000.00','bandeirantes.jpg','12345678','00000003','05804287028');


#6 INSERÇÃO DE UMA NOVA SOLICITAÇÃO
insert into solicitacao
values ('123455','Pina Luz','Vintage','Vale a Pena Ver De Novo','181020','Cultural','12345679','17:00','22:00','250','87654321','05804287028','12345679');


#7 MOSTRA OS LOCAIS QUE COMEÇAM COM A LETA "V"
select * from ambiente where local1 like 'V%';


#8 MEDIA DE PESSOAS QUE COMPARECERÃO AOS EVENTOS DO DEMETRIOS
select c.nome, format(avg(s.ocupacao),2) as 'Média de pessoas que comparecerão aos eventos do Démetrios'
from cliente c inner join solicitacao s
on s.idcpf_cnpj=s.idcpf_cnpj
where c.nome like 'D%';


#9 INSERINDO VALOR NOS ÍTENS DA TABELA ITEM
UPDATE item
SET valor='23500.00'
WHERE iditem='87654321';

UPDATE item
SET valor='41526.68'
WHERE iditem='12345678';


# SOMA DOS VALORES DOS ITENS DO ACERVO
select sum(valor) as 'Valor total dos itens do acervo' from item;


# MÉDIA DOS VALORES DOS ITENS DO ACERVO
select format(avg(valor),2) as 'Média de valor dos itens do acervo' from item;


# EXIBINDO DADOS DE DUAS TABELAS DO ACERVO, DANDO PREFERENCIA À TABELA A ESQUERDA, INCLUSIVE OS CAMPOS NULOS
select i.titulo,i.descricao, i.autor, i.tecnica, a.local1
from item i left join ambiente a
on i.idAmbiente=a.idAmbiente;

SELECT idambiente, item, ocupacao, hora_inicial, hora_final, data_evento FROM solicitacao WHERE status_solicitacao = 'Aguardando Aprovação'