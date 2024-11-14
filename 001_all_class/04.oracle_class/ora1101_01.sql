-- 입사일의 마지막 날짜를 출력
-- 10/1 -> 10/31, 9/5 -> 9/30
-- last_day
select hire_date,last_day(hire_date) from employees; -- 그달의 마지막 날

-- 가입일
select sdate from students;

-- 가입일, 1년 후 날짜를 출력
select sdate, add_months(sdate,12) from students;
select sdate, add_months(sdate,-6) from students;

-- 현재일 기준으로 입력일이 6개월 이내인 회원만 출력
-- 11/1
select sdate from students where sdate>=add_months(sysdate,-6) order by sdate;

-- 년도 월별로 가입인원을 나눠서 출력하시오
select mdate from member order by mdate;

select last_day(mdate) md from member order by md;
select substr(last_day(mdate),1,5) md, count(mdate) from member group by last_day(mdate) order by md;

-- employees 테이블에서 부서별(department_id)인원을 출력하시오
select department_id, count(department_id) from employees group by department_id;

-- 그룹함수: sum,avg,count,min,max,median
create table emp3
as select * from employees;

select * from emp3;
create table emp4
as select * from employees where 1=2;

select * from emp4;
insert into emp4 select * from employees;
rollback;

insert into emp4(employee_id,emp_name,hire_date) select employee_id,emp_name,hire_date from employees;

-- insert, update, delete
-- commit, rollback

--------------------
-- 테이블
-- create: 생성, alter: 변경, drop: 삭제
--

-- alter add: 테이블에 컬럼 추가
select * from emp4;
alter table emp4 add(hire_date2 date);
desc emp4;

-- 컬럼 변경: 컬럼 안에 데이터가 있다면 제약조건, e.g. 65 길이의 문자가 있을 경우 50 으로 변경 안됨
alter table emp4 modify(email varchar2(70));
alter table emp4 modify(email varchar2(50));

select emp_name from emp4;
desc emp4;
-- 컬럼의 길이 확인 후 변경하기
alter table emp4 modify(emp_name varchar2(20));

-- 컬럼의 길이 확인
select max(length(emp_name)) from employees;
select length(emp_name) em from employees order by em desc;

-- 컬럼 타입 변경 -> 컬럼 안 데이터가 null 일때만 가능
-- 다른 타입의 경우 데이터를 null로 변경한 후 타입을 변경해야함
select * from emp4;
alter table emp4 modify email number(4);

alter table emp4 modify emp_name number(20); -- error

desc emp4;

-- employee_id 값을 email 컬럼에 복사
update emp4 set email = employee_id;
select * from emp4;

-- employee_id 값을 phone number 에 입력
-- phone number 문자형 타입, employee_id 숫자형 타입
update emp4 set phone_number = employee_id;
update emp4 set phone_number = '198a' where employee_id=198;

-- 문자형 타입을 숫자형 타입에 복사
-- 안에 있는 데이터가 모두 숫자형이기에 가능
-- 문자가 포함되어 있으면 불가능
update emp4 set manager_id = phone_number;

--rollback;

-- 컬럼 이름 변경
desc emp4;
alter table emp4 rename column phone_number to p_number;

-- 속성 변경 가능
alter table emp4 modify hire_date date null;
alter table emp4 modify hire_date date not null;

-- 컬럼 삭제
alter table emp4 drop column hire_date2;
desc emp4;

-- 테이블 삭제
drop table emp2;
drop table emp3;

-- 테이블 이름 변경
rename emp4 to emp44;

-------------

-- Primary_Key: 중복과 null 값이 불가능
-- unique: null은 가능, 중복은 불가능
-- not null: null 불가능. 중복 가능
-- default: 값이 입력되지 않았을 때의default 값 지정 가능
select * from departments;
-----------

-- drop table board;

create table bmember(
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30) not null,
nickname varchar2(30),
age number(3) default 0,
gender varchar2(6) check(gender in ('Male','Female')),
email varchar2(20),
bdate date default sysdate
);

desc bmember;
-- 입력
insert into bmember (id,pw,name,nickname,age,gender,email,bdate) 
values('aaa','1111','홍길동','길동스',20,'Male','aaa@aaa.com',sysdate);

-- age와 bdate 의 경우 따로 입력안해도 default 값이 자동으로 들어감
insert into bmember (id,pw,name,nickname,gender,email) 
values('bbb','2222','유관순','관순스','Female','bbb@bbb.com');

-- check: Male, Female 이 두가지 형태 외에는 입력 불가, 이 둘은 중복 가능
-- male,MALE,malE 등은 데이터 입력 불가
insert into bmember (id,pw,name,nickname,age,gender,email,bdate) 
values('ccc','3333','이순신','순신스',20,'Male','ccc@ccc.com',sysdate);

-- not null (빈 공백' '은 null 이 아니라 입력 가능): null 허용하지 않음, 중복 허용
insert into bmember (id,pw,name,nickname,age,gender,email,bdate) 
values('ddd','','강감찬','감찬스',20,'Male','ddd@ddd.com','2024/01/01');

-- primary key: 중복 불가, null 불가
insert into bmember (id,pw,name,nickname,age,gender,email,bdate) 
values('eee','','김구','구스',20,'Male','eee@eee.com','2024/02/21')

commit;

select * from bmember;

create table emp3(
empno number(4) unique,
ename varchar2(30) not null,
job varchar2(9),
deptno number(2)
);


insert into emp3 values(
1,'홍','01','01');

insert into emp3 values(
2,'유','02','02');

-- unique: null 값은 허용
insert into emp3(ename,job,deptno) values(
'이','03','03');

-- unique: 중복 불가
insert into emp3 values(
2,'강','04','04');


select * from member;
insert into member values(
'aaa','1111','홍길자','aaa@aaa.com','123-456-7890','Female','golf',sysdate);

commit;
-------------------

-- primary key 등록시 중복 및 null 값이 존재하면 안됨
-- primary key 추가, 수정
-- constraint id_pk: 이름 설정
desc member;
alter table member add constraint id_pk primary key (id);

-- primary key 삭제
alter table member drop constraint id_pk;

desc bmember;

create table board(
bno number(4)primary key,
btitle varchar2 (100) not null,
bcontent clob,
id varchar2(30),
bgroup number(4),
bstep number(4),
bindent number(4),
bhit number(4),
bdate date,
bfile varchar2(100));

insert into board values(
board_seq.nextval,'제목1','내용1','aaa',board_seq.currval,0,0,0,sysdate,'');

insert into board values(
board_seq.nextval,'제목2','내용2','bbb',board_seq.currval,0,0,0,sysdate,'');

insert into board values(
board_seq.nextval,'제목3','내용3','ccc',board_seq.currval,0,0,0,sysdate,'');

insert into board values(
board_seq.nextval,'제목4','내용4','ddd',board_seq.currval,0,0,0,sysdate,'');

insert into board values(
board_seq.nextval,'제목5','내용5','eee',board_seq.currval,0,0,0,sysdate,'');

commit;

select * from board;
------------------------------------

create table mem2 (
	id VARCHAR2(50),
	pw varchar2(4),
	name VARCHAR2(50),
	email VARCHAR2(50),
	phone VARCHAR2(50),
	gender VARCHAR2(50),
	hobby varchar2(50),
	mdate DATE
);
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('aaa', '1111', '홍길동', 'rsherville0@tinyurl.com', '324-226-8544', 'Male', 'golf', '2024-03-06');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('bbb', '1111', '유관순', 'mrubinlicht1@fotki.com', '475-964-8193', 'Female', 'book', '2024-08-18');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('ccc', '1111', '이순신', 'bchstney2@walmart.com', '541-891-0085', 'Female', 'run', '2024-08-16');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('ddd', '1111', '강감찬', 'cstubbes3@chron.com', '900-194-4605', 'Female', 'game', '2024-02-10');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('eee', '1111', '김구', 'tnacey4@list-manage.com', '727-883-1542', 'Female', 'golf', '2024-09-10');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Trineman', '6216', 'Riobard', 'rtrineman5@prweb.com', '140-720-7698', 'Male', 'book', '2024-09-03');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Towell', '5201', 'Bryan', 'btowell6@stumbleupon.com', '365-214-7874', 'Male', 'run', '2024-03-16');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Neagle', '4903', 'Horacio', 'hneagle7@nifty.com', '114-384-4352', 'Male', 'run', '2024-02-01');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Gresham', '4089', 'Valentine', 'vgresham8@quantcast.com', '547-694-3516', 'Female', 'swim', '2024-10-11');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('O''Dare', '6041', 'Doroteya', 'dodare9@dyndns.org', '102-500-7735', 'Female', 'game', '2024-07-29');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Doumic', '1343', 'Stepha', 'sdoumica@com.com', '745-998-5005', 'Female', 'game', '2024-08-08');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Allmann', '9173', 'Husein', 'hallmannb@imageshack.us', '122-775-3647', 'Male', 'book', '2024-01-01');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Tommis', '6716', 'Roderic', 'rtommisc@sourceforge.net', '673-244-8303', 'Male', 'book', '2024-07-09');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Bleaden', '4168', 'Drud', 'dbleadend@123-reg.co.uk', '838-544-2408', 'Male', 'golf', '2024-06-18');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('D''Aguanno', '7476', 'Wini', 'wdaguannoe@cyberchimps.com', '237-714-1340', 'Female', 'run', '2024-06-27');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Gegay', '8185', 'Bernette', 'bgegayf@yahoo.com', '982-358-5670', 'Female', 'golf', '2024-07-05');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Flea', '6937', 'Fidelity', 'ffleag@reverbnation.com', '602-708-0462', 'Female', 'run', '2024-01-18');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Shory', '1240', 'Robb', 'rshoryh@intel.com', '621-231-3542', 'Male', 'run', '2024-09-13');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Harm', '1438', 'Flinn', 'fharmi@yelp.com', '328-792-9216', 'Male', 'golf', '2023-12-05');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Poschel', '9693', 'Sterling', 'sposchelj@usnews.com', '499-462-1400', 'Male', 'swim', '2024-05-27');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Medford', '5717', 'Jacquenette', 'jmedfordk@epa.gov', '634-270-7550', 'Female', 'book', '2024-02-18');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Gianelli', '5559', 'Katherina', 'kgianellil@wikipedia.org', '967-878-2128', 'Female', 'game', '2024-05-18');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Kolodziejski', '5522', 'Danella', 'dkolodziejskim@jugem.jp', '110-354-1019', 'Female', 'golf', '2024-03-25');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Mildmott', '9678', 'Jule', 'jmildmottn@wix.com', '286-208-5611', 'Male', 'run', '2024-07-23');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Pietrowski', '6843', 'Ediva', 'epietrowskio@photobucket.com', '571-362-5389', 'Female', 'golf', '2023-12-30');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Chasemoore', '9290', 'Dunc', 'dchasemoorep@geocities.jp', '390-444-9215', 'Male', 'golf', '2024-03-27');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Overnell', '6410', 'Barth', 'bovernellq@cdbaby.com', '825-465-2790', 'Male', 'run', '2024-06-12');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Benford', '8906', 'Margette', 'mbenfordr@twitter.com', '210-839-4892', 'Female', 'swim', '2024-06-20');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Portman', '6013', 'Orson', 'oportmans@reverbnation.com', '258-285-2186', 'Male', 'golf', '2024-06-09');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Elflain', '7065', 'Trish', 'telflaint@intel.com', '319-787-3297', 'Female', 'golf', '2024-04-30');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Ockland', '7153', 'Deirdre', 'docklandu@sfgate.com', '895-501-5958', 'Female', 'run', '2023-12-03');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Le Floch', '5518', 'Linea', 'lleflochv@hp.com', '734-888-6261', 'Female', 'swim', '2024-01-24');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('McGaugan', '5439', 'Conny', 'cmcgauganw@imageshack.us', '376-451-4038', 'Male', 'game', '2023-11-08');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Lilburn', '6148', 'Shepherd', 'slilburnx@sina.com.cn', '250-173-1654', 'Male', 'swim', '2024-07-03');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Frew', '7401', 'Meaghan', 'mfrewy@unc.edu', '276-431-6409', 'Female', 'swim', '2023-12-04');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Myner', '1917', 'Lorrie', 'lmynerz@wikimedia.org', '550-264-0011', 'Male', 'book', '2024-10-06');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Knightsbridge', '2295', 'Elias', 'eknightsbridge10@dedecms.com', '906-789-7346', 'Male', 'swim', '2023-12-30');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Merwood', '6745', 'Georgy', 'gmerwood11@comcast.net', '904-984-7938', 'Male', 'golf', '2024-01-14');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Dewsbury', '1477', 'Bond', 'bdewsbury12@amazon.co.jp', '106-232-5734', 'Male', 'swim', '2024-02-02');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Kliche', '5468', 'Nevins', 'nkliche13@admin.ch', '608-113-7174', 'Male', 'game', '2024-06-22');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Fick', '7675', 'Panchito', 'pfick14@senate.gov', '430-438-4575', 'Male', 'book', '2024-03-12');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Danielczyk', '5661', 'Reinaldos', 'rdanielczyk15@irs.gov', '359-176-0405', 'Male', 'book', '2024-05-27');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Blazey', '8853', 'Lou', 'lblazey16@about.com', '729-460-3951', 'Male', 'run', '2024-04-12');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Godly', '6603', 'Pail', 'pgodly17@plala.or.jp', '190-426-8746', 'Male', 'run', '2024-06-02');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Attwoull', '3472', 'Cliff', 'cattwoull18@slideshare.net', '570-758-4710', 'Male', 'golf', '2024-08-10');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Chason', '5763', 'Terrie', 'tchason19@symantec.com', '650-189-0579', 'Female', 'run', '2024-03-11');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Noni', '2224', 'Jannel', 'jnoni1a@bloglovin.com', '871-506-4522', 'Female', 'book', '2024-01-04');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Graham', '3477', 'Mendy', 'mgraham1b@trellian.com', '887-280-4803', 'Male', 'swim', '2024-09-01');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Griffey', '8521', 'Raff', 'rgriffey1c@51.la', '947-561-4983', 'Male', 'swim', '2024-04-12');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Wretham', '3484', 'Laure', 'lwretham1d@ted.com', '183-800-2897', 'Female', 'book', '2023-11-07');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Sewart', '5890', 'Lodovico', 'lsewart1e@shareasale.com', '962-952-9409', 'Male', 'swim', '2024-05-25');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Leber', '3162', 'Cory', 'cleber1f@foxnews.com', '773-506-6136', 'Female', 'run', '2024-05-03');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Germain', '2786', 'Teodoor', 'tgermain1g@usda.gov', '287-887-6296', 'Male', 'book', '2024-09-25');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('O''Dooghaine', '4249', 'Jeni', 'jodooghaine1h@washingtonpost.com', '656-654-8738', 'Female', 'book', '2024-02-18');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Ralestone', '2620', 'Lenard', 'lralestone1i@w3.org', '692-797-1702', 'Male', 'book', '2024-09-07');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Yong', '8340', 'Kasey', 'kyong1j@seattletimes.com', '820-634-7148', 'Female', 'run', '2023-12-04');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Yukhov', '6010', 'Gallard', 'gyukhov1k@weather.com', '602-990-8790', 'Male', 'run', '2023-12-22');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Digman', '1555', 'Britt', 'bdigman1l@google.com', '997-747-6638', 'Female', 'game', '2023-11-04');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Rocks', '1647', 'Dane', 'drocks1m@latimes.com', '455-553-6937', 'Male', 'book', '2023-12-07');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Lewisham', '8757', 'Danni', 'dlewisham1n@addtoany.com', '597-704-9376', 'Female', 'swim', '2024-02-09');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('O''Spillane', '4868', 'Hamlen', 'hospillane1o@indiegogo.com', '584-856-0076', 'Male', 'golf', '2024-02-19');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Keoghane', '8511', 'Garrott', 'gkeoghane1p@accuweather.com', '655-285-1122', 'Male', 'game', '2024-01-23');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Gransden', '3139', 'Maire', 'mgransden1q@bloglines.com', '517-233-8716', 'Female', 'book', '2024-02-24');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Kobiera', '5689', 'Jaime', 'jkobiera1r@flickr.com', '325-635-7089', 'Female', 'run', '2023-11-16');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Craske', '6088', 'Isa', 'icraske1s@delicious.com', '903-771-5929', 'Male', 'golf', '2024-06-26');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Island', '9324', 'Terrance', 'tisland1t@cmu.edu', '569-238-3939', 'Male', 'golf', '2024-03-16');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Hazeldine', '9138', 'Glenn', 'ghazeldine1u@foxnews.com', '118-455-4847', 'Male', 'game', '2024-08-10');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Gutch', '8827', 'Davin', 'dgutch1v@jiathis.com', '602-127-7922', 'Male', 'book', '2024-07-06');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Pavlenkov', '8269', 'Elane', 'epavlenkov1w@cyberchimps.com', '172-572-0209', 'Female', 'game', '2023-12-27');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Kasman', '3887', 'Davita', 'dkasman1x@de.vu', '140-813-6914', 'Female', 'book', '2024-09-15');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Andraud', '6948', 'Gunter', 'gandraud1y@rambler.ru', '999-479-2224', 'Male', 'swim', '2024-03-10');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Mandrey', '9531', 'My', 'mmandrey1z@whitehouse.gov', '809-354-8112', 'Male', 'golf', '2024-04-17');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Teers', '1997', 'Lynda', 'lteers20@bigcartel.com', '831-197-8592', 'Female', 'golf', '2024-07-28');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('MacBey', '8775', 'Farand', 'fmacbey21@seesaa.net', '319-735-6030', 'Female', 'swim', '2024-06-05');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Bontoft', '2628', 'Blanca', 'bbontoft22@webnode.com', '818-469-6633', 'Female', 'run', '2024-09-25');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Gercken', '3185', 'Heinrik', 'hgercken23@webmd.com', '604-301-2929', 'Male', 'game', '2024-03-28');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Huzzay', '5857', 'Alf', 'ahuzzay24@sogou.com', '570-223-4310', 'Male', 'book', '2024-08-16');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Tredger', '7675', 'Sherwood', 'stredger25@bbc.co.uk', '527-871-8185', 'Male', 'run', '2024-06-01');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Canadine', '8566', 'Nicolis', 'ncanadine26@devhub.com', '800-674-8410', 'Male', 'golf', '2024-08-03');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Paireman', '7080', 'Nichol', 'npaireman27@msn.com', '668-411-8679', 'Female', 'run', '2024-01-01');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Powis', '6242', 'Mehetabel', 'mpowis28@surveymonkey.com', '271-883-5391', 'Female', 'book', '2024-09-18');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Walsh', '7311', 'Luther', 'lwalsh29@gmpg.org', '523-360-3018', 'Male', 'golf', '2024-09-18');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Pont', '4975', 'Edd', 'epont2a@nbcnews.com', '551-629-4794', 'Male', 'golf', '2024-02-22');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Osborne', '7007', 'Gauthier', 'gosborne2b@naver.com', '711-842-1931', 'Male', 'run', '2024-05-31');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Tinker', '8402', 'Andree', 'atinker2c@wp.com', '731-985-8198', 'Female', 'swim', '2023-12-23');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Persence', '7577', 'Obediah', 'opersence2d@elegantthemes.com', '549-594-4369', 'Male', 'run', '2024-05-28');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Boatwright', '1204', 'Ernie', 'eboatwright2e@printfriendly.com', '833-853-7804', 'Male', 'swim', '2024-01-18');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Kirkhouse', '6330', 'Pernell', 'pkirkhouse2f@soup.io', '412-173-6891', 'Male', 'book', '2024-06-12');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Ghidetti', '9376', 'Den', 'dghidetti2g@seattletimes.com', '165-768-1973', 'Male', 'run', '2024-10-21');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Keppel', '1397', 'Yolanthe', 'ykeppel2h@harvard.edu', '928-660-5279', 'Female', 'run', '2024-09-09');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Matteini', '7664', 'Zola', 'zmatteini2i@jalbum.net', '672-317-8567', 'Female', 'swim', '2024-05-28');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Malmar', '9156', 'Andriana', 'amalmar2j@ed.gov', '588-732-4548', 'Female', 'run', '2024-01-25');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Waplington', '7863', 'Tobiah', 'twaplington2k@dell.com', '996-187-6594', 'Male', 'game', '2024-07-11');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Cosyns', '2387', 'Lauri', 'lcosyns2l@edublogs.org', '943-340-9913', 'Female', 'game', '2024-04-05');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Atto', '5832', 'Had', 'hatto2m@mozilla.com', '624-750-8503', 'Male', 'game', '2024-06-07');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Bushell', '8202', 'Franz', 'fbushell2n@indiegogo.com', '274-938-6045', 'Male', 'game', '2024-03-06');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Glassford', '3189', 'Virgil', 'vglassford2o@usatoday.com', '361-318-5270', 'Male', 'run', '2024-05-23');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Aron', '3277', 'Freeland', 'faron2p@timesonline.co.uk', '724-482-5099', 'Male', 'game', '2024-08-25');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Tavner', '8684', 'Brig', 'btavner2q@webeden.co.uk', '366-125-0586', 'Male', 'run', '2024-05-14');
insert into mem2 (id, pw, name, email, phone, gender, hobby, mdate) values ('Shiliton', '5557', 'Sandi', 'sshiliton2r@abc.net.au', '407-488-9852', 'Female', 'book', '2024-01-11');


select * from mem2;
commit;

update mem2 set id='abc', pw='1111', name='황혜진', email='rkwhkehd3927@naver.com' where id='Trineman';

desc board;
select * from member;
--delete member;
--commit;

insert into member select * from mem2;
select * from member;

select * from board; -- 5개 BNO,BTITLE,BCONTENT,ID,BGROUP,BSTEP
select * from bmember; -- 5개

-- 5개만 ( 5개 * 5개 = 25개 )
select bno,btitle,bcontent,nickname,email,bgroup,bstep,bindent,bhit,bfile from board, bmember
where board.id = bmember.id; -- member id:primary key,board.id:foreign key

-- 두개의 테이블을 합쳐서 출력
select employee_id,emp_name,email,salary,employees.department_id,department_name from employees,departments
where employees.department_id = departments.department_id;

select department_id, department_name from departments where department_id = 50;

--------------------

desc board;

-- 테이블 create 할때, foreign key 생성
create table board2(
bno number(4) primary key, 
btitle varchar2(1000) not null,
id varchar2(30),
bcontent clob,
constraint fk_board2_id foreign key(id) references bmember(id)
);

-- 닉네임: id_fk, foreign key: id, bmember 테이블의 primary key: id 등록
alter table board add constraint id_fk foreign key(id) references bmember(id);

-- foreign key 삭제
alter table board drop constraint id_fk;

select * from board;
select * from bmember;

-- abc 글을 등록하면, 등록이 안됨
insert into board values(
board_seq.nextval,'제목6','내용6','abc',board_seq.currval,0,0,0,sysdate,'');

delete board where bno=7;
commit;

-- [foreign key에 등록된 id 삭제 방법]
-- bmember 테이블 id, foreign key로 board, board2에 등록
-- foreign key: 외래 키
-- 원본의 primary key 데이터를 지우려면, 원칙으로는 foreign key의 데이터를 모두 삭제해야 삭제가 됨
-- foreign key를 해제해야 삭제가능
-- primary key: 기본키
select * from bmember;
delete bmember where id = 'aaa';
delete board where id = 'aaa'; -- 얘를 먼저해야 바로 위 명령어가 실행가능'
rollback;

alter table board drop constraint id_fk;

-- foreign key로 등록되면, primary key 삭제 시 foreign key가 있으면 삭제 불가능
-- on delete cascade: primary key가 삭제되면, foreign key로 등록된 모든 글 삭제
alter table board add constraint id_fk foreign key (id) references bmember(id) on delete cascade;



-- 1. on delete restricted
-- 기본값: 미입력 시, 자식데이터가 있을 경우, 부모데이터가 삭제되지 않음
alter table board add constraint id_fk foreign key (id) references bmember(id);
select * from board;
-- 자식테이블
-- 위의 자식 테이블에서 aaa로 쓴 데이터를 먼저 삭제해야 id 삭제 가능 
delete bmember where id = 'aaa';
delete board where bno = 3;

-- 2. on delete cascade
-- 부모 데이터 삭제 시, 자식데이터까지 모두 삭제
alter table board add constraint id_fk foreign key (id) references bmember(id) on delete cascade;
-- 부모 데이터를 삭제하면, 자식데이터의 모든 글이 삭제됨
delete bmember where id = 'aaa';
select * from board;

-- 3. on delete set null
-- 부모 데이터 삭제시, 자식데이터 값 null
alter table board add constraint id_fk foreign key (id) references bmember(id) on delete set null;
-- 부모 데이터를 삭제하면 자식데이터의 해당 컬럼만 null로 변경되고, 데이터는 그대로 존재
delete bmember where id = 'aaa';
select * from board;



-- check 구문 
create table emp01(
empno number(4) primary key,
ename varchar2(30) not null,
salary number(7,2) check(salary between 2000 and 20000),
gender varchar2(10) check(gender in('Male','Female'))
);

-- check가 지정 되어 있는 컬럼에 추가
insert into emp01 values(
1,'홍길동',2500,'Male'
);
-- salary 범위를 벗어나면 에러
insert into emp01 values(
2,'유관순',20000,'Female'
);
--Male,Female 이외 단어 입력시 에러
insert into emp01 values(
3,'이순신',20000,'male'
);

-- default: insert 시 값이 입력되지 않을 시, 문자, 숫자, 날짜 넣을수 있음
create table emp02(
empno number(4) primary key,
ename varchar2(30) default '무명',
income number(4) default 0,
salary number(7,2) check(salary between 2000 and 20000),
gender varchar2(10) check(gender in ('Male','Female')),
edate date default sysdate
);

--
insert into emp02 (empno,salary,gender) values(
1,5000,'Male');

commit;


select * from emp02;

----------

create table mem(
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30) default '무명',
age number(3) default 0,
birth date,
gender varchar2(6) check(gender in('Male','Female')),
hobby varchar2(50) default 'game',
mdate date default sysdate
);

insert into mem values(
'aaa','1111','홍길동','24','2000/05/05','Male','golf',sysdate
);

insert into mem values(
'ccc','3333','이순신','23','2001/07/05','Male','game',sysdate
);

commit;

select * from students;

-- update mem set pw='3333' where id='ccc';


-- employees 테이블 부서번호가 50번인 사원수 가져오기
select count(department_id) from employees;


-- employees 테이블 부서번호가 50번인, 부서인원, 부서번호, 부서명 가져오기
select count(*) no,a.department_id dept, department_name deptname 
from employees a, departments b 
where a.department_id = b.department_id and a.department_id=50
group by a.department_id,department_name;


desc students;