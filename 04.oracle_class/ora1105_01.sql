-- join
-- inner join - equi join, non-equi-join,self join, outer join

-- 사원번호, 사원명, 부서번호 in employees / 부서명 in departments 를 출력하시오
select employee_id,emp_name,a.department_id,department_name from employees a, departments b
where a.department_id = b.department_id;

select * from stu_grade;
select * from students;

-- non-equi-join: 두 테이블 간 동일한 컬럼없이 데이터를 가져오는 방법
-- avg 값을 가지고(?), 다른 컬럼을 다른 테이블에서 가져와 출력
select * from students, stu_grade 
where avg between loavg and hiavg;

-- self join 자신의 테이블을 2번 호출
-- a.employee_id = 198, a.manager_id = 124, 의 이름을 b.emp_name 에 가져오는 것
select a.employee_id,a.emp_name,a.manager_id,b.emp_name from employees a, employees b
where a.manager_id = b.employee_id; 

select * from stu_grade;
select * from stu;

-- 컬럼 삭제
alter table stu drop column result;

-- 컬럼 추가
alter table stu add result varchar2(10);

-- avg 컬럼을 가지고, stu_grade를 활용하여 값을 result에 모두 입력

select no, avg, grade, result
from stu, stu_grade
where avg between loavg and hiavg
order by avg; -- 등급 출력

-- update stu set result = 1;

update stu a set result = ( -- 업데이트할 stu 의 별칭을 a로 두고
select results from(
select no, grade as results
from stu,stu_grade
where avg between loavg and hiavg) b -- 넣으려는 result(등급)를 출력한 식의 stu를 b
where a.no = b.no -- a의 no와, b의 no가 같은 곳에 result 넣기
);

select * from stu;

-- non-equi join update 구문
select grades from ( -- 등급만 출력
select no,grade as grades
from stu,stu_grade
where avg between loavg and hiavg); -- update 안에 넣을 구문이 잘 출력되는지가 중요

update stu a set result = (
select grades from ( -- 등급만 출력
select no,grade as grades
from stu,stu_grade
where avg between loavg and hiavg
) b
where a.no = b.no);

-- rank()
select * from students;
select * from stu;
update stu set rank = 0;

-- rank()의 결과값을 rank 컬럼에 모두 입력
select no, name, avg, rank() over(order by avg desc) as ranks from stu;
--update stu set rank = 1;
update stu a set rank = (
select ranks from( -- 안에 출력할 값을 ranks로 감싸기
select no, rank() over(order by avg desc) as ranks from stu 
)b -- 항상 안에 출력하고 싶은 값의 명령어를 먼저 써보기
where a.no = b.no);

---------
-- 107개: manager_id가 null 일때 ceo로 출력
select employee_id,emp_name,manager_id from employees;
 
-- null 을 제외한 개수: 106, 포함하면 107개
select count(manager_id) from employees
where manager_id is not null;

-- null 값이면 0 출력, ceo
select nvl(manager_id,0) from employees; -- 0 출력
select nvl(manager_id,'CEO') from employees; -- 타입이 달라서 ERROR
-- to_char로 타입 변경후 출력
select nvl(to_char(manager_id),'CEO')manager_id from employees; 

-- self join, manager_id 와 매니저 이름 출력
-- self join - 106개(null 제외) : 이러면 월급이 안나가버림ㅋㅎ null 도 출력시키고 싶어!
-- null도 출력시키려면 outer join을 해야함
-- ★ outer join - (+): 해당 컬럼에 null 값이 존재할 시 null 값을 포함해서 출력
select a.employee_id,a.emp_name,a.manager_id,b.emp_name,a.salary
from employees a, employees b
-- (+): a.manager_id에 null이 있으면 b.employee_id에 추가해서 출력시켜줘!
where a.manager_id = b.employee_id(+); 

select * from employees
where emp_name = 'Martha Sullivan';

-- 사원번호, 사원명, 부서번호, 부서명 출력
-- outer join, employees의 부서번호가 null 인 것도 출력
select employee_id, emp_name, a.department_id, department_name
from employees a,departments b
where a.department_id = b.department_id(+);

-- ★ ansi cross join
select * from employees cross join departments;
-- cross join
select * from employees, departments;

-- ★ ansi inner join
select a.department_id,department_name
from employees a inner join departments b
on a.department_id = b.department_id;

-- ansi join using: 따로 a,b 등 별칭을 설정해주지 않아도 알아서 찾음
select department_id,department_name
from employees inner join departments
using (department_id);

-- ★ ansi join: natural join - 두개의 공통부분의 컬럼이 있으면 자동으로 인식하여 검색
select department_id,department_name
from employees natural join departments;

-- equi-join
select department_id,department_name 
from employees a, departments b
where a.department_id = b.department_id;


-- outer join(left,right,full)
select a.department_id,department_name
from employees a left outer join departments b
on a.department_id = b.department_id;

-- Oracle outer-join: 양쪽 컬럼 모두에 (+) 붙이면 error
-- ( 알고 싶은 값의 반대편에 (+) 붙이기? )
select employee_id,emp_name,a.department_id,department_name
from employees a, departments b
--          left            right
where a.department_id = b.department_id(+);

------------------------------
------------------------------


-- union

select * from students;

select * from students
where total>=250; -- 24개
 
select * from students
where name like '%a%'; -- 35개

-- union: 49개(중복 제외) 원래,24+35=59개
-- union all: 중복 허용
select * from students
where total >= 250
union
select * from students
where name like '%a%';

select * from students
where total>=250 or name like '%a%';

-- union: 동일 테이블, 다른 테이블 모두 사용 가능, 컬럼의 타입만 동일하면 모두 출력
-- 컬럼 개수 및 타입이 동일해야함
-- 조건 1: 위쪽 쿼리문과 아래쪽 쿼리문의 컬럼 개수가 동일
-- 조건 2: 타입 무조건 일치
select employee_id,emp_name from employees;
select no,name from students;

-- 자유게시판 freeboard, 공지사항 notice, 이벤트 event, 종합게시판 totalboard 등을
-- 통합적으로 검색해서 출력하고 싶을 때 union
select employee_id,emp_name from employees
union
select no,name from students;

select employee_id,emp_name,no,name
from employees,students;


-- Employees에 없는 Departments의 부서 검색 -> 부서번호, 부서이름
select department_id,department_name -- 존재하는 것만 출력
from departments a
where not exists -- : ~는 제외하고
( select 1 from employees b where a.department_id = b.department_id );
-- 1은 의미없음
select distinct department_id from employees;

-- Employees department_id가 50인 사원 검색 -> 부서번호, 부서이름
-- Employees에 5000 <= salary <= 8000 인 사원의 부서번호, 부서이름
-- 두 개를 union ( 뭔가 망한듯 )
select a.department_id,department_name,salary
from employees a,departments b 
where a.department_id = b.department_id and a.department_id = 50
union
select a.department_id,department_name,salary
from employees a,departments b 
where a.department_id = b.department_id and salary>=5000 and salary<=8000;

-- Employees department_id가 50인 사원 검색 -> 부서번호, 부서이름
-- Employees에 없는 Departments의 부서 검색 -> 부서번호, 부서이름
-- 두 개를 union
select a.department_id,department_name
from employees a,departments b 
where a.department_id = b.department_id and a.department_id = 50
union
select department_id,department_name -- 존재하는 것만 출력
from departments a
where not exists -- : ~는 제외하고
( select 1 from employees b where a.department_id = b.department_id );


desc member; -- name,mdate
desc students; -- name,sdate
-- union
select name,mdate from member
union
select name,sdate from students;

select * from board2;
--drop table board2;

create table board2 (
	bno number(4),
	btitle VARCHAR2(1000),
	bcontent clob,
	id VARCHAR2(30),
	bgroup number(4),
	bstep number(4),
	bindent number(4),
	bhit number(4),
	bdate DATE,
	bfile VARCHAR2(100)
);

commit;
select * from board2 order by bno;
-- 8,11,12,16,21,22,25,29,35,38,44,46,57,61,66,74,88,95,96,98 삭제
delete board2 where bno=98;

select * from board2
where bno between 1 and 20; -- 1~20번일 뿐 20개를 가져오진 않음

-- rownum: 번호를 새롭게 부여해서 가져옴
select rownum,bno,btitle,bdate from board2
order by bdate desc, btitle asc;

-- rownum: 번호가 순서대로 정렬됨, 서브쿼리 사용
-- 1~20(between 1 and 20) 불러오기는 되지만 2~ (2부터) 불러오기는 불가능
-- 가능하게 하려면 아래와 같이 서브쿼리로 계속 잡아줘야함
select rnum,bno,btitle from
(select rownum rnum,bno,btitle 
from( select bno, btitle from board2 order by bdate desc))
where rownum between 11 and 20;

-- row_number() over(): 정렬 후, 번호 부여
-- 얘도 2 이후부터 가져오려면 계속 서브쿼리로 만들어야함
select rnum,bno,btitle,bdate 
from( select row_number() over(order by bdate desc) rnum,bno,btitle,bdate from board2 )
where rnum between 11 and 20;

-- a.*
select * 
from( select row_number() over(order by bdate desc) rnum, a.* from board2 a )
where rnum between 11 and 20;
select bno, * from board2; -- error
select bno, a.* from board2 a; -- 이렇게 해야함

-- 모든 컬럼을 출력하시오
-- row_number() 사용, 11~20 출력
select *
from(select row_number() over(order by bdate desc) rnum, a.* from board2 a)
where rnum between 11 and 20;

-- rownum 사용, 11~20 출력
-- rownum 바깥으로 빼기, 그래야 번호를 순서대로 잘 부여할 수 있음
select * from( select rownum rnum, a.* 
from( select * from board2 order by bdate desc) a )
where rnum between 11 and 20;

-- rownum, 11~20 출력
select * from( select rownum rnum, a.* -- 테이블을 넣어야하는데 대신 아래 식 넣기
from( select no,name,avg,rank() over(order by avg desc) ranks from students ) a
where ranks between 11 and 20);

-- row_number() over() 사용, 11~20 출력
select *
from ( select row_number() over(order by avg desc) rnum, 
rank() over(order by avg desc), a. * from students a)
where rnum between 21 and 30;

-- rank() 값 rank 컬럼에 입력
update students a set rank = (
select ranks
from (select no,rank() over(order by avg desc) ranks from students) b
where a.no=b.no);

select * from students;
commit;

-- ★ view
-- 상담원: 사원들 전화를 가지고 사원들에게 마케팅 하려고 함
-- 100명에게 사원 테이블 오픈을 제공해달라고 요청 from 마케팅 팀
-- 직원가 100만원 90% 10만원 아이폰 16
select * from employees;

-- 실제 테이블이 생성된 건 아님, 가상의 테이블 생성(필요한 정보만 볼 수 있는),
-- (e.g. 정사원들이 아닌 상담원들이 볼 수 있는 가상의 카피본: 민감한 정보들 포함 X)
-- employees_view
create or replace view employees_view
as
select employee_id,emp_name,email,phone_number,hire_date
from employees;

select * from employees_view;

-- 사원번호, 사원명, 이메일, 폰번호, 입사일, 부서번호, 부서명 등이 출력 가능한
-- 가상의 view 생성 create
create or replace view emp_view
as
select employee_id,emp_name,email,phone_number,hire_date,
a.department_id,department_name
from employees a, departments b
where a.department_id=b.department_id;

select * from emp_view;
-- view 삭제
--drop view emp_view;

select * from employees;
select * from employees_view;

-- view column comment(주석-설명문) 추가
comment on column employees_view.employee_id is '사원번호에 해당됩니다.';
-- comment 주석 확인
select * from user_col_comments;
-- table comment 주석 확인
select * from user_tab_comments;

create or replace view emp_view
as
select employee_id as e_id,emp_name as e_name from employees_view;


--drop table emp02;

create table emp02(
employee_id number(6),
emp_name varchar2(80),
hire_date date,
salary number(8,2),
department_id number(6)
);

desc emp02;
-- employees 안의 데이터 emp02 로 복붙
insert into emp02(employee_id,emp_name,hire_date,salary,department_id)
select employee_id,emp_name,hire_date,salary,department_id from employees;

select * from emp02;
-- view 생성
-- with read only: select 만 가능
create or replace view emp02_view
as
select employee_id,emp_name,hire_date
from emp02;

-- view select 
select * from emp02_view order by employee_id;

-- 단순 view: 1개의 테이블로 구성된 것
-- insert,update,delete 가능, not null 등 제약조건이 되어 있으면 insert 불가할 수도 있음
-- view 에서 값을 수정 후 commit 하면 emp02(기존 본체 테이블)에도 적용됨
-- 전부 적용되는 것은 아니고 막거나 허용 가능
-- 복합 view: 2개 이상 테이블 join, 함수사용, group by 같은 경우는 insert, update, delete 불가

-- employee_id 가 101 인 사람의 이름을 홍길동으로 변경
update emp02_view set emp_name = '홍길동'
where employee_id = 101;

commit;
select * from emp02;

insert into emp02_view values(
207,'유관순',sysdate);

alter table emp02 modify salary number(8,2) not null;

----------

-- 학생성적프로그램
select * from students;
-- no: seq
-- 입력 필요 데이터: name, kor, eng, math
-- total: 오라클에서 입력
-- avg: 오라클에서 입력
-- rank: 오라클에서 입력
-- sdate: sysdate 오라클에서 입력

-- insert into students values(students_seq.nextval,name,kor,eng,math,kor+eng+math,
--(kor+eng+math)/3,sysdate);

select students_seq.currval from dual;
commit;

-- students 테이블의 no 중 가장 큰 수는?
select max(no) from students;

select * from students;

-- avg 소수점 2자리 까지만 출력
-- no,name,kor,eng,math,total,avg,rank,sdate
select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students;

-- a가 포함되어 있는 이름 검색
select * from students
where name like '%a%';

select * from students
order by name desc;

update students a set rank = ( 
select ranks from(
select no,name,kor,eng,math,total,round(avg,2),rank() over(order by avg desc) as ranks, 
to_char(sdate,'yyyy-mm-dd') from students) b 
where a.no=b.no);
commit;