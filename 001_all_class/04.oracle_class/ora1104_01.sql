create table emp02(
empno number(4) not null,
ename varchar2(30) not null,
job varchar2(9), -- null 가능
deptno number(2) -- null 가능
);

insert into emp02 values(
1,'홍길동','clerk',2);

insert into emp02 values(
2,'유관순',null,null); -- 하지만 무결성 제약 조건에 null 이 들어가는 것은 좋지 않음

insert into emp02 values(
3,'이순신',null,null);

-- drop table board2;

create table emp02(
empno number(4) unique, -- null 가능, 중복은 불가능
ename varchar2(30) not null,
job varchar2(9), -- null 가능
deptno number(2) -- null 가능
); 

insert into emp02 values(
1,'홍길동','clerk',2);

insert into emp02 values(
2,'유관순',null,null);

insert into emp02 values(
3,'이순신',null,null);

insert into emp02 values(
null,'강감찬',null,null);

-- unique: error, 중복 불가능
insert into emp02 values(
2,'김구',null,null);

select * from emp02;

delete emp02 where empno is null; -- null 값 삭제
commit;

-- 제약조건 변경 alter: unique -> not null
alter table emp02 modify empno not null;

-- not null, pk_emp02_empno: 별칭
alter table emp02 add constraint pk_emp02_empno primary key(empno);

alter table emp02 drop constraint pk_emp02_empno;



create table emp02(
empno number(4) primary key, -- null 가능, 중복은 불가능
ename varchar2(30) not null,
job varchar2(9), -- null 가능
deptno number(2) -- null 가능
); 

drop table mem;

create table mem(
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(100) default '무명',
gender varchar2(6) check(gender in('Male','Femail')) -- check: male,female,MALE,FEMALE 입력시 error
);

insert into mem values(
'aaa','1111','홍길동','Male'
);

insert into mem values(
'bbb','1111','유관순','female'
);

commit;

select * from board;

create table board2(
bno number(4) primary key,
btitle varchar2(1000) not null,
id varchar2(30),
constraint fk_board2_id foreign key(id) references mem(id) 
);


-- 부모테이블의 aaa삭제 시, 자식 테이블의 aaa글이 모두 삭제
delete mem where id='aaa';

select * from board2;

-- 외래키로 등록시, 부모키에 해당 값이 없으면 에러
insert into board2 values(
1,'제목1','aaa'
);

-- 외래키 삭제
alter table board2 drop constraint fk_board2_id;

-- 부모키 삭제 시, 외래키로 등록된 값들을 모두 삭제
alter table board2
add constraint fk_board2_id foreign key (id)
references mem(id) on delete cascade; -- on delete

-- default: on delete restricted 부모키 삭제시, 외래키에 등록된 값이 있으면, 삭제가 되지 않음.
-- on delete set null: 부모키 삭제 시, 외래키로 등록된 값을 삭제는 하지 않고, 해당되는 컬럼값만 null 처리

-- 부모테이블의 aaa삭제 시, 자식 테이블의 aaa글이 모두 삭제
delete mem where id='aaa';

select * from mem;

drop table mem;
select * table board2;

create table mem(
id varchar2(30) primary key,
pw varchar2(100) not null,
name varchar2(100),
deptno number(4)
);

insert into mem values(
'aaa','1111','홍길동',10);

insert into mem values(
'bbb','1111','유관순',20);

rollback;

insert into mem values(
'ccc','1111','이순신',30);

-- 10 '총무부', 20 '인사부', 30 '마케팅'

select id,pw,name,deptno,
decode(deptno,
10, '총무부',
20, '인사부',
30, '마케팅'
) from mem;

-- case
select id,pw,anme,deptno,
case
when deptno=10 then '총무부'
when deptno=20 then '인사부'
when deptno=30 then '마케팅'
end as deptName
from mem;
 
select * from employees;

select job_id from employees;

-- clerk: 월급의 5% 인상, rep 10%, management 15%
-- 1. clerk, rep, man 인 사람 출력
select job_id from employees;
-- substr(d,1,3): d에서 1번째부터 3개까지 잘라오기
select substr(job_id,4) j_id from employees where lower(substr(job_id,4)) in ('clerk','rep','man');
select substr(job_id,4) j_id from employees where substr(job_id,4) in ('CLERK','REP','MAN');

-- 1.05 = 5%, 1.1 = 10%, 1.15 = 15% 인상
select substr(job_id,4) j_id, salary, 
decode(substr(job_id,4),
'CLERK',salary*1.05,
'REP',salary*1.1,
'MAN',salary*1.15) sal from employees where substr(job_id,4) in ('CLERK','REP','MAN');

create table lavel_data (
	id VARCHAR2(50) primary key,
	lavel number(1) not null
);


--drop table level_data;
-- 1:100 포인트, 2:1000 포인트, 3:5000 포인트, 4:10000 포인트, 5:20000 포인트
-- point


-- 1,2,3: 5000 포인트, 4,5: 20000 포인트
select id, lavel, 
decode (lavel,
1,100,
2,1000,
3,5000,
4,10000,
5,20000)|| 'point' as point from lavel_data;

select id, lavel, case
when lavel>=1 and lavel<=3 then 5000
when lavel>=4 then 20000
end  point
from lavel_data;

select * from students;

-- avg: 90점 이상 A, 80점 이상 B, 70점 이상 C, 60점 이상 D, 그외 F
-- result
select * from students;
select name, avg, case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
when avg<=59 then 'F'
end result
from students;

-- 테이블 전체 복사
create table stu as select * from students;

-- 컬럼 추가
select * from stu;

alter table stu add result varchar2(2);


select * from stu;

select name, avg, case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
when avg<60 then 'F'
end result
from students;

-- 테이블 stu의 result 컬럼에 위의 결과를 추가
update stu set result = 
case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
when avg<60 then 'F'
end;

select * from stu;

-- 파이썬에서 if문을 구현해서 처리
-- rank() over: 순위를 구현하는 함수
select no,name,total, rank() over(order by total desc) from stu order by no;

-- rank() over(): 같은 순위일 경우 중복 순위 개수만큼 다음 순위값을 증가하여 출력
-- dense_rank(): 중복순위가 존재해도 순차적으로 다음 순위 표시
select no,name,total, dense_rank() over(order by total desc) from stu;
select rank() over(order by total desc) as ra from stu;


select ranks from (select rank() over(order by total desc) ranks from stu);
-- 순위를 rank 컬럼에 추가
-- rank 등수 입력 처리
update stu a set rank = (
select ranks from(select no, rank() over(order by total desc) as ranks from stu) b
where b.no=a.no -- 중요
);

select * from stu;
select no, rank() over (order by total desc) as ranks from stu;


-- case
-- salary 5000 이하: 월급 15% 인상, 5000~8000: 10% 인상, 8000 이상: 5% 인상하여 출력
select emp_name, salary, case
when salary<=5000 then salary*1.15
when salary>=5000 and salary<=8000 then salary*1.1
when salary>=8000 then salary*1.05
end y_salary
from employees;

-- emp_name 대문자 D가 포함되어 있으면 salary 10% 인상, M이 포함되어 있으면 5% 인상, 그외는 인상 0%
-- like 사용하기
select emp_name, salary, case
when emp_name like '%D%' then salary*1.1
when emp_name like '%M%' then salary*1.05
else salary
end e_salary
from employees;

select * from employees;
select department_id,commission_pct from employees
where commission_pct is not null;

-- 커미션이 있는 사원수를 출력
select count(*),commission_pct from employees
where commission_pct is not null group by commission_pct;

-- 부서별 사원수
select count(*),department_id from employees group by department_id order by department_id;

-- 부서별 평균 월급 출력
select department_id,avg(salary) from employees group by department_id;

-- 그룹함수 비교연산 having
-- 부서별 평균 월급이 7000보다 높은 사원수 출력
select department_id,avg(salary),count(salary) from employees group by department_id
having avg(salary)>=7000;

-- 부서별 평균 월급이 5000 이하인 부서별 인원수를 출력
-- 그룹함수는 having 절에 조건문을 사용해야함. where절에는 사용불가
select department_id, count(salary) from employees
group by department_id 
having avg(salary)<=5000;

-- 부서별 사람 찾기
select department_id,count(*) from employees group by department_id;


select avg(salary) from employees; -- 전체 평균 월급: 6461.83...
-- 부서별 평균 월급보다 적게 받는 부서별 사원수 출력 (엥?) 

select department_id,count(*) from employees a
where salary < (
select salarys from(
select department_id,avg(salary) salarys from employees 
group by department_id) b
where a.department_id = b.department_id)
group by department_id
order by department_id;  -- ㅁㅊ 개어려워 너무 어려워 ★ 중요



select department_id,count(*) from employees 
where salary < (select avg(salary) from employees)
group by department_id;

-- 13,000 , 6,000
select salary from employees where department_id = 20;
select salary from employees where department_id = 60;

select avg(salary) from employees where department_id = 30; -- 4150

-- 부서의 최대급여와 최소급여를 출력하되, 최대급여가 5000 이상인 부서만 출력하시오.
-- 그룹함수이기 대문에 where 말고 having 으로 조건문 걸기
select department_id,max(salary), min(salary) from employees
having max(salary) >= 5000 group by department_id order by department_id desc;

-- 학번, 이름, 전화번호, 주소, 성별, 학년, 학기, 국어, 영어, 수학, 합계, 평균 등수
-- 1001,홍길동,010,서울,남자,1,1,100,100,100,300,1
-- 1001,홍길동,010,서울,남자,1,2,90,90,90,270,8
-- 1001,홍길동,010,서울,남자,1,3,95,95,95,285,15


-- 부서명 departments
select * from departments;

-- donald OCnonnell 의 부서명을 알고싶어요 (쿼리문을 두개 돌려야함)
select emp_name,department_id from employees
where emp_name = 'Donald OConnell'; -- 50

select department_id,department_name from departments
where department_id = 50; -- 배송부

-- join을 사용해야 두개의 쿼리를 1개의 쿼리로 구성 가능해짐
-- join
-- 1. cross join
-- 2. inner join
-- 3. outer join
-- 4. self join

-- ★ cross join: 특별한 키워드 없이 두개의 테이블을 검색하는 것
select * from employees; -- 107
select * from departments; -- 27 * 107 = 2889

select count(*) from employees, departments; -- 2889
select * from employees, departmetns;

-- ★ inner join: equi join - 같은 컬럼을 가지고 비교해서 두개의 테이블을 검색 
select emp_name,a.dempartment_id,department_name 
from employees a, departments b
where a.department_id = b.department_id; -- (+): outer join

select bno,btitle,bcontent,id from board;

-- 101 * 4 = 404
select bno,btitle,bcontent,a.id,email,phone,bgroup,bstep,bindent,bhit,bdate,bfile 
from member a, board b
where a.id=b.id;

select * from jobs;

-- inner join: 사원번호, 사원명, job_id, job_title 출력
select employee_id,emp_name,a.job_id,job_title 
from employees a,jobs b
where a.job_id=b.job_id and a.job_id = 'SH_CLERK';

-- 사원번호, 사원명, 부서번호, 부서명, job_id, job_title 출력
select * from departments;
select * from employees;
select * from jobs;
select employee_id,emp_name, a.department_id, department_name, a.job_id, job_title
from employees a, departments b, jobs c
where a.job_id=c.job_id and a.department_id=b.department_id; -- 최종

-- member name
-- board 게시글
select * from board;
select bno,btitle,bcontent,a.name,bgroup,bstep,bindent,bhit,bdate,bfile from member a,board b
where a.id= b.id;

-- 사원번호, 사원명, 월급, 부서번호, 부서명
-- 평균 월급보다 적은 사원 출력
select employee_id, emp_name, salary,a.department_id, department_name
from employees a, departments b
where a.department_id = b.department_id 
and salary < (select avg(salary)from employees);

-- 부서별 평균 월급보다 월급이 적은 사원 출력
-- 1. 전체 사원번호, 사원명, 월급, 부서번호, 부서명

-- 부서별 평균 월급
select department_id,avg(salary) from employees group by department_id;

-- 어려워 어려워어려워ㅠㅠ ★
select employee_id, emp_name, salary,a.department_id,department_name
from employees a, departments b
where a.department_id = b.department_id 
and salary < ( -- 부서별 평균보다 작은 월급
select salarys from -- 부서별 평균 월급을 salarys 에 넣기
(select department_id,avg(salary) salarys from employees group by department_id) c -- 부서별 평균 월급
where a.department_id = c.department_id);

---

select * from employees;
select * from departments;
select * from jobs;


-- job_id가 CLERK 인 사원의 사원명, 사원번호, 부서명, 부서번호, 직급번호, 직급명 출력
select emp_name,employee_id,department_name,a.department_id,a.job_id,job_title
from employees a, departments b, jobs c
where a.department_id=b.department_id and a.job_id= c.job_id
and substr(a.job_id,4) in ('CLERK','MAN');

-----

select salary from employees order by salary;
-- 2000~4000 E, 4000~6000 D, 6000~8000 C, 8000~10000 B, 10000~100000 A등급
create table salgrade(
grade varchar2(10),
losal number(6),
hisal number(6)
);

insert into salgrade values(
'E등급',2000,4000
);
insert into salgrade values(
'D등급',4001,6000
);
insert into salgrade values(
'C등급',6001,8000
);
insert into salgrade values(
'B등급',8001,10000
);
insert into salgrade values(
'A등급',10001,100000
);

-- drop table salgrade;
select * from salgrade;

-- salary 옆에 등급 넣기
-- 등급 in salgrade
-- salgrade, employees 둘 사이에 같은 컬럼이 없음
-- 그래서 non-equi join을 사용해 테이블을 join 해야함
-- non_equi join: 같은 컬럼이 없는 두 테이블 간에, 두 테이블의 값을 비교하여 출력
select salary from employees;
select emp_name,salary,grade
from employees,salgrade -- 107 * 5 = 535
where salary between losal and hisal; -- losal, hisal 둘을 비교하여 출력,

-- non-equi join 을 활용하여 students total A,B,C,D,F 등급을 출력
-- 100~90 A, 89~80 B, 79~70 C, 69~60 D, 60점 미만 F
-- 생성할 테이블명: stu_grade/ grade,lototal,hitotal
-- name, avg, grade 출력

-- drop table stu_grade;
create table stu_grade(
grade varchar2(10), -- A,A등급
loavg number(5,2), -- 59.99
hiavg number(5,2) 
);



insert into stu_grade values(
'A등급',90,100
);

insert into stu_grade values(
'B등급',80,89.99
);

insert into stu_grade values(
'C등급',70,79.99
);

insert into stu_grade values(
'D등급',60,69.99
);

insert into stu_grade values(
'F등급',0,59.99
);

select * from stu_grade;
select * from students;

select name, avg, grade
from students, stu_grade
where avg between loavg and hiavg;

-- alter table stu_grade rename column lototal to loavg;
-- alter table stu_grade rename column hitotal to hiavg;

select * from stu;


update stu set result = '';
commit;

-- stu에 stu_grade 등급값을 result 로 넣기
-- result 결과값을 non_equi join 을 사용해서 입력
-- name, total, grade 출력
select * from stu;
desc stu;
alter table stu modify result varchar2(20);
-- A등급(등급이라는 글자를 넣으려면 7~10 byte 필요)
alter table stu modify result varchar2(10); -- 10 byte 로 변경, A-2,등-3,급-3byte


select name,total,avg,grade
from stu,stu_grade
where avg between loavg and hiavg; -- 등급 출력

-- ★ 힝 어려워 ㅠㅠㅠ
update stu a set result = (
select results from(
select no,grade as results
from stu,stu_grade
where avg between loavg and hiavg) b
where a.no = b.no
); -- result 에 등급값 넣기


commit;

select name, total, avg, result from stu;

-- ★ self join: 자신의 테이블 2개를 join 하여 결과값 출력
select employee_id,emp_name,manager_id from employees;
select employee_id,emp_name from employees
where employee_id = 124; -- Kevin Mourgos

select a.employee_id, a.emp_name, a.manager_id, b.emp_name 
from employees a, employees b
where a.manager_id = b.employee_id and a.manager_id=124;





-----

select * from students;
desc students;