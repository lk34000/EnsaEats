DROP TABLE IF EXISTS client CASCADE ;

CREATE TABLE client(
    id_client serial PRIMARY KEY NOT NULL,
    nom text NOT NULL,
    prenom text NOT NULL,
    mdp text NOT NULL
);

INSERT INTO client(nom,prenom,mdp) VALUES
('Stofer','Lisa','le13lavie'),
('Pain','Guillaume','lyonnaisavie'),
('Kourtis','Leon','lol'),
('Varet','Tanguy','Albon'),
('Bamba','Mamadou','le_s')
;

DROP TABLE IF EXISTS adresse CASCADE ;

CREATE TABLE adresse(
    id_adresse serial PRIMARY KEY NOT NULL,
    ad_postale text NOT NULL,
    ville text NOT NULL,
    code_poste text NOT NULL,
    pays text NOT NULL
);

INSERT INTO adresse(ad_postale,ville,code_poste,pays) VALUES
('1 Rue louis armand','Bruz','35170','France'),
('4 Rue louis armand','Bruz','35170','France'),
('14 Rue de la Rabine','Bruz','35170','France'),
('7 Ctr Antoine de Saint-Exupéry,','Bruz','35170','France'),
('8 Rue du maine','Rennes','35000','France')
;

DROP TABLE IF EXISTS adresse_client CASCADE ;

CREATE TABLE adresse_client(
    id_adresse INT ,
    id_client INT
);

INSERT INTO adresse_client(id_adresse,id_client) VALUES
(1,1),
(2,2),
(3,3),
(4,4),
(5,5)
;


DROP TABLE IF EXISTS menu;
CREATE TABLE menu(
    id_menu serial PRIMARY KEY NOT NULL,
    nom_menu text NOT NULL,
    prix FLOAT NOT NULL,
    nomresto varchar(50) NOT NULL
);

INSERT INTO menu(nom_menu,prix,nomresto) VALUES
('Best_of',8,'McDonalds'),
('Maxi_Best_off',10,'McDonalds'),
('Mc_First',5,'McDonalds'),
('Happy_Meal',4,'McDonalds'),
('Salade',7,'McDonalds'),
('Brochette',16,'Table Rouge'),
('Mixed',19,'Table Rouge'),
('Sashimi',17,'Table Rouge'),
('Plateaux',35,'Table Rouge'),
('Margherita',8.8,'La Tomate'),
('Orientale',11.5,'La Tomate'),
('Napoletana',10,'La Tomate'),
('Pipo',11,'La Tomate'),
('La pesto',12.5,'La Tomate'),
('George Clooney',14.5,'La saint Georges'),
('George Michael',12,'La saint Georges'),
('Georges Clemenceau',11.9,'La saint Georges'),
('Georges Lautner',18.10,'La saint Georges'),
('George Perec',12.5,'La saint Georges'),
('George Harrison',14.9,'La saint Georges')
;

DROP TABLE IF EXISTS plat;
CREATE TABLE plat(
    id_plat serial PRIMARY KEY NOT NULL ,
    nom_plat text NOT NULL
)  ;

INSERT INTO plat(nom_plat) VALUES
('Petites Frites'),
('Moyennes Frites'),
('Grandes Frites'),
('Petite Boisson'),
('Moyenne Boisson'),
('Grande Boisson'),
('Hamburger'),
('Big Mac'),
('Mc Firts Poulet'),
('Jouet'),
('Salade Caesar'),
('Boisson'),
('Brochettes'),
('Sashimi'),
('Sushi'),
('Makis')
;



DROP TABLE IF EXISTS menu_plat CASCADE ;

CREATE TABLE menu_plat(
    id_menu INT ,
    id_plat INT
);

INSERT INTO menu_plat(id_menu,id_plat) VALUES
(1,2),
(1,5),
(1,8),
(2,3),
(2,6),
(2,8),
(3,2),
(3,5),
(3,9),
(4,1),
(4,4),
(4,7),
(4,10),
(5,11),
(5,5),
(6,12),
(6,13),
(7,12),
(7,13),
(7,14),
(8,12),
(8,14),
(8,12),
(8,13),
(8,14),
(8,15),
(8,16)
;


DROP TABLE IF EXISTS commande CASCADE;

CREATE TABLE commande(
    id_commande serial PRIMARY KEY NOT NULL,
    id_client int NOT NULL,
    nom_restaurant text NOT NULL
    );

INSERT INTO commande(id_client, nom_restaurant) VALUES
(3, 'Mcdonalds'),
(4, 'Table Rouge'),
(2, 'La saint Georges'),
(1, 'La Tomate' ),
(5, 'Mcdonalds');


DROP TABLE IF EXISTS contenu_commande CASCADE;

CREATE TABLE contenu_commande(
    id_commande int NOT NULL,
    id_menu int NOT NULL,
    quantite int NOT NULL);

INSERT INTO contenu_commande (id_commande, id_menu, quantite) VALUES
(1,3,1),
(1,1,1),
(2,9,1),
(2,7,2),
(3,17,1),
(4,14,2),
(5,4,1),
(5,3,2);
