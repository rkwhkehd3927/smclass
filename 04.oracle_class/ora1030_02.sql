-- 타입
-- 문자형, 숫자형, 날짜형
-- char, varchar2, nchar, nvarchar2, long, clob
-- char: 한글문자 입력 시, 3byte 사용
-- varchar2(6): 한글 2글자 입력
-- nvarchar2(5): 한글 5자리까지 입력 가능 - 2byte

-- number
-- date: 초까지 입력, timestamp: 밀리세컨드까지 입력

select '홍길동' from dual;
-- length 문자 길이
select length('홍길동') from dual;

-- 이름의 길이로 역순 정렬
select name, length(name) n from students order by name;

-- lengthb: byte 크기
select lengthb('홍길동') from dual;

-- 합계가 200점 이상이면서, 번호는 10 이상 50 이하, 이름의 2번째 자리에 e가 들어가 있는 학생을 출력
select * from students;
select * from students where total>=200 and no>=10 and no<=50 and name like '_e%';


select * from students where total>=200;
-- select * from 테이블
select * from ( select * from students where total>=200) where name like '_e%' and no>=30;

rollback;

select no,name,total,rank() from students order by total desc;

-- 등수함수 rank() over(기준점) 입력, no 중복이 없음. 유일키, 기본키, 프라이머리(primary key)
select no,name,total,rank() over(order by total desc) ranks from students;
select ranks from (select no, rank() over(order by total desc) ranks from students;

select no, name, total, rank from students order by total desc;

-- 수정: update
update students a 
set rank=(
select ranks from(select no,rank() over(order by total desc)ranks from students) b
where a.no=b.no);

update students a 
set rank=1
where a.no=101;

select * from studetns order by rank;

rollback;

select no,rank() over(order by total desc) as ranks from students;
update students
set rank = 1
where no = 101;

update students
set rank = 2
where no = 100;

update students
set rank = 3
where no = 3;

-- 사원번호가 높은 순으로 등수를 생성하시오.
-- 사원번호,이름,등수 출력
select employee_id,emp_name, rank() over(order by employee_id desc) ranks from employees;

--drop table emp2;
-- employees 테이블을 emp2 테이블로 복사
create table emp2 as select * from employees;

select rank() over(order by employee_id desc) from employees;
desc emp2;
-- 테이블 컬럼 추가
alter table emp2 add rank number(4);
desc emp2;
select * from emp2;

-- rank() 등수를 rank에 입력
update emp2 e set rank =(
select ranks from(select employee_id, rank() over(order by employee_id desc)ranks from employees) e2
where e.employee_id = e2.employee_id
);

select employee_id from emp2;

-- 컬럼의 순서를 변경
-- emp_name 뒤에 rank 컬럼을 배치 (가운데를 다 숨김처리)
-- desc emp2;
-- invisible: 숨김처리
alter table emp2 modify EMAIL invisible;
alter table emp2 modify PHONE_NUMBER invisible;
alter table emp2 modify HIRE_DATE invisible;
alter table emp2 modify SALARY invisible;
alter table emp2 modify MANAGER_ID invisible;
alter table emp2 modify COMMISSION_PCT invisible;
alter table emp2 modify RETIRE_DATE invisible;
alter table emp2 modify DEPARTMENT_ID invisible;
alter table emp2 modify JOB_ID invisible;
alter table emp2 modify CREATE_DATE invisible;
alter table emp2 modify UPDATE_DATE invisible;

-- visible: 다시 나타내기
alter table emp2 modify EMAIL visible;
alter table emp2 modify PHONE_NUMBER visible;
alter table emp2 modify HIRE_DATE visible;
alter table emp2 modify SALARY visible;
alter table emp2 modify MANAGER_ID visible;
alter table emp2 modify COMMISSION_PCT visible;
alter table emp2 modify RETIRE_DATE visible;
alter table emp2 modify DEPARTMENT_ID visible;
alter table emp2 modify JOB_ID visible;
alter table emp2 modify CREATE_DATE visible;
alter table emp2 modify UPDATE_DATE visible;

alter table emp2 modify rank invisible;
alter table emp2 modify rank visible;
select * from emp2;

-- 컬럼 삭제

desc emp2;

alter table emp2 drop column EMAIL;
alter table emp2 drop column PHONE_NUMBER;
alter table emp2 drop column HIRE_DATE;
alter table emp2 drop column SALARY;
alter table emp2 drop column COMMISSION_PCT;
alter table emp2 drop column RETIRE_DATE;
alter table emp2 drop column DEPARTMENT_ID;
alter table emp2 drop column CREATE_DATE;
alter table emp2 drop column UPDATE_DATE;


alter table emp2 add DEPARTMENT_NAME varchar2(80);

-- 현재 부서명이 없음
select * from emp2;
desc emp2;
-- 부서명은 departments에 있음
select * from departments;
select department_id,department_name from emp2;
select department_id,department_name from departments;

-- 부서명 입력
update emp2 e set e.department_name = (
select d from (select department_id,department_name d from departments) e2
where e.department_id = e2.department_id
);

select department_name from emp2;

--drop table stu;
-- 테이블 복사
create table stu as select * from students;
desc stu;
alter table stu drop column avg;

select * from stu;
-- total 컬럼, avg 컬럼, rank 컬럼 추가
alter table stu add total number(3);
alter table stu add AVG number;
alter table stu add RANK number(3);
desc stu;

alter table stu modify sdate invisible;
alter table stu modify sdate visible;

-- 합계, 평균 추가
update stu set total= kor+eng+math, avg= (kor+eng+math)/3;

-- rank 입력

-- rank()
select total, rank() over(order by total desc) ranks from stu;

update stu s set rank=(
select ranks from (select no,rank() over(order by total desc) ranks from stu) s2
where s.no = s2.no
);

select * from stu order by rank;

commit;


----------- 날짜함수
-- 현재 날짜: sysdate
select sysdate from dual;
select sysdate-1 from dual;
select sysdate+30 from dual;

create table datetable (
no number(4),
predate date,
today date,
nextdate date
);

-- 회원가입 1달치, 6개월, 1년
insert into datetable values(
1,sysdate-30,sysdate,sysdate+180
);

select no,predate,today 가입일, nextdate 만료일 from datetable;

select * from member;
select id,name,mdate,sysdate ,round(sysdate-mdate) from member
where sysdate>=mdate+180;

-- 입사일 현재날짜와 입사일 몇일 지났는지 출력하시오.
-- employees, hire_date
select sysdate-hire_date, round(sysdate-hire_date),emp_name from employees;
-- round: 달도 반올림 가능, 15일 이상이면 다음달로 넘어감, 미만이면 버림
select hire_date,round(hire_date,'month') from employees;
-- 일의 숫자를 1로 초기화
select hire_date,trunc(hire_date,'month') from employees;

-- 입사일, 현재일 기준의 달수
select hire_date,sysdate, months_between(sysdate,hire_date) from employees;
-- months_between: 두 일자 가운데 지나간 달수를 알려줌
select hire_date,sysdate,round(months_between(sysdate,hire_date)) 달수 ,round(sysdate-hire_date) 일수 from employees;

-- add_months 3개월 추가
select hire_date,add_months(hire_date,3) from employees;

-- next_day: 다음주 수요일 날짜를 알려줌
select sysdate,next_day(sysdate,'수요일') from dual;

select sysdate,next_day(sysdate,'토요일') from dual;

-- last_date: 그 달의 마지막 날짜를 알려줌
select hire_date, last_day(hire_date) from employees;
select sysdate,last_day(sysdate) from dual;

-- 형변환 함수
select sysdate from dual;
select to_char(sysdate,'yyyy/mm/dd hh24:mi:ss' from dual;

select hire_date from employees;
select hire_date,to_char(hire_date,'yyyy-mm-dd') from employees;

-- 입력타입은 날짜형이 되어야 함
select to_char('24/01/01','yyyy-mm-dd') from dual;

select * from member where id='aaa' and pw='1111';

select * from member;
update member set id='abc',pw='1111',name='황혜진',email='ddd@naver.com'
where id='Trineman';

select * from member where id='eee';