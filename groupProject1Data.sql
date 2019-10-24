-- Data prepared by Brandon Zukowski, bbjzukows@ualberta.ca
-- Published on Oct 23rd, 2019

insert into persons values ('Ned', 'Stark', '2012-01-01', 'Winterfell , Westeros', 'Kingslanding, Westeros', '780-0010-0001');
insert into persons values ('Bran', 'Stark', '2012-02-02', 'Winterfell , Westeros', 'Kingslanding, Westeros', '780-0010-0891');
insert into persons values ('Arya', 'Stark', '2012-03-03', 'Winterfell , Westeros', 'Kingslanding, Westeros', '780-0010-0111');
insert into persons values ('Sansa', 'Stark', '2012-04-04', 'Winterfell , Westeros', 'Kingslanding, Westeros', '780-0010-2301');
insert into persons values ('Rob', 'Stark', '2012-05-05', 'Winterfell , Westeros', 'Kingslanding, Westeros', '780-0780-0001');
insert into persons values ('John', 'Snow', '2012-06-06', 'Winterfell , Westeros', 'Kingslanding, Westeros', '780-0610-2401');
insert into persons values ('Tyrian', 'Lanister', '2012-07-07', 'Winterfell , Westeros', 'Kingslanding, Westeros', '780-0110-0871');
insert into persons values ('Jamie', 'Lannister', '2012-08-08', 'Winterfell , Westeros', 'Kingslanding, Westeros', '780-6810-4531');
insert into persons values ('Daenerys', 'Targaryan', '2012-09-09', 'Winterfell , Westeros', 'Kingslanding, Westeros', '780-0114-5901');


-- create Users
insert into users value ('ns1', 'GoT1', 'o', 'Ned', 'Stark', "Winterfell")
insert into users value ('as2', 'GoT2', 'a', 'Arya', 'Stark', "Winterfell")
insert into users value ('rs3', 'GoT3', 'o', 'Rob', 'Stark', "Winterfell")
insert into users value ('ss4', 'GoT4', 'a', 'Sansa', 'Stark', "Winterfell")
insert into users value ('bs5', 'GoT5', 'o', 'Bran', 'Stark', "Winterfell")
insert into users value ('tl6', 'GoT6', 'a', 'Tyrian', 'Lannister', "Winterfell")
insert into users value ('jl7', 'GoT7', 'o', 'Jamie', 'Lannister', "Winterfell")
insert into users value ('dt8', 'GoT8', 'a', 'Daenerys', 'Targaryan', "Winterfell")
insert into users value ('js8', 'GoT9', 'a', 'John', 'Snow', "Winterfell")



-- Partner names can be given in any order (as can be noted)
insert into marriages values (200, '2019-07-13', 'Winterfell, Westeros', 'John', 'Snow', 'Daenerys', 'Targaryan');

insert into vehicles values ('U200', 'Chevrolet', 'Camaro', 1969, 'red');
insert into vehicles values ('U300', 'Mercedes', 'SL 230', 1964, 'black');

insert into registrations values (300, '1964-05-26','2021-05-25', 'Winter Is Coming','U200', 'John', 'Snow');
insert into registrations values (302, '1980-01-16','2022-01-15', 'Winter Is Coming','U300', 'Ned', 'Stark');

