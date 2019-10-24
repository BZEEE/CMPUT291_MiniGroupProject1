-- Data prepared by Brandon Zukowski, bbjzukows@ualberta.ca
-- Published on Oct 23rd, 2019

insert into persons values ('Ned', 'Stark', '2012-01-01', 'Winterfell , Westeros', 'Kingslanding, Westeros', '780-0010-0001');
insert into persons values ('Bran', 'Stark', '2012-02-02', 'Winterfell , Westeros', 'Kingslanding, Westeros', '780-0010-0891');
insert into persons values ('Arya', 'Stark', '2012-03-03', 'Winterfell , Westeros', 'Kingslanding, Westeros', '780-0010-0111');
insert into persons values ('Sansa', 'Stark', '2012-04-04', 'Winterfell , Westeros', 'Kingslanding, Westeros', '780-0010-2301');
insert into persons values ('Rob', 'Stark', '2012-05-05', 'Winterfell , Westeros', 'Kingslanding, Westeros', '780-0780-0001');
insert into persons values ('John', 'Snow', '2012-06-06', 'Winterfell , Westeros', 'Kingslanding, Westeros', '780-0610-2401');
insert into persons values ('Tyrian', 'Lannister', '2012-07-07', 'Winterfell , Westeros', 'Kingslanding, Westeros', '780-0110-0871');
insert into persons values ('Jamie', 'Lannister', '2012-08-08', 'Winterfell , Westeros', 'Kingslanding, Westeros', '780-6810-4531');
insert into persons values ('Daenerys', 'Targaryan', '2012-09-09', 'Winterfell , Westeros', 'Kingslanding, Westeros', '780-0114-5901');


-- create Users
insert into users values ('ns1', 'GoT1', 'o', 'Ned', 'Stark', 'Winterfell');
insert into users values ('as2', 'GoT2', 'a', 'Arya', 'Stark', 'Winterfell');
insert into users values ('rs3', 'GoT3', 'o', 'Rob', 'Stark', 'Winterfell');
insert into users values ('ss4', 'GoT4', 'a', 'Sansa', 'Stark', 'Winterfell');
insert into users values ('bs5', 'GoT5', 'o', 'Bran', 'Stark', 'Winterfell');
insert into users values ('tl6', 'GoT6', 'a', 'Tyrian', 'Lannister', 'Winterfell');
insert into users values ('jl7', 'GoT7', 'o', 'Jamie', 'Lannister', 'Winterfell');
insert into users values ('dt8', 'GoT8', 'a', 'Daenerys', 'Targaryan', 'Winterfell');
insert into users values ('js9', 'GoT9', 'a', 'John', 'Snow', 'Winterfell');



-- Partner names can be given in any order (as can be noted)
insert into marriages values (200, '2019-07-13', 'Winterfell, Westeros', 'John', 'Snow', 'Daenerys', 'Targaryan');

insert into vehicles values ('U100', 'Chevrolet', 'Camaro', 1969, 'red');
insert into vehicles values ('U101', 'Mercedes', 'SL 230', 1964, 'black');
insert into vehicles values ('U102', 'Chevrolet', 'Camaro', 1969, 'red');
insert into vehicles values ('U103', 'Mercedes', 'SL 230', 1964, 'black');

insert into vehicles values ('U104', 'Lamborghini', 'Aventadpr', 2018, 'black');

insert into registrations values (0, '2008-05-26','2021-05-25', 'Winter Is Coming','U100', 'John', 'Snow');
insert into registrations values (1, '2009-01-16','2022-01-15', 'Winter Is Coming','U101', 'Ned', 'Stark');
insert into registrations values (3, '2010-05-26','2021-05-25', 'Winter Is Coming','U102', 'Bran', 'Stark');
insert into registrations values (4, '2010-01-16','2022-01-15', 'Winter Is Coming','U103', 'Arya', 'Stark');

insert into registrations values (5, '2012-05-26','2021-05-25', 'Winter Is Coming','U104', 'Jamie', 'Lannister');
insert into registrations values (6, '2013-01-16','2022-01-15', 'Winter Is Coming','U104', 'Tyrian', 'Lannister');
insert into registrations values (7, '2014-05-26','2021-05-25', 'Winter Is Coming','U104', 'Rob', 'Stark');
insert into registrations values (8, '2015-01-16','2022-01-15', 'Winter Is Coming','U104', 'Sansa', 'Stark');
insert into registrations values (9, '2016-05-26','2021-05-25', 'Winter Is Coming','U104', 'Daenerys', 'Targaryan');

