select * from member;

drop table member;

create table member (
	id VARCHAR2(50),
	pw varchar2(4),
	name VARCHAR2(50),
	email VARCHAR2(50),
	phone VARCHAR2(50),
	gender VARCHAR2(50),
	hobby varchar2(50),
	mdate DATE
);



update member set id='abc',pw='1111',name='아무개',email='rkwhkehd3927@naver.com' where id='abc';

update member set pw='2222' where id='Towell';

commit;
-----------------------------------------
select sysdate-1,sysdate,sysdate+1 from dual;

select hire_date,round(hire_date,'Month') from employees;

select hire_date,trunc(hire_date,'Month') from employees;

select add_months(trunc(sysdate,'month'),1) from dual;

-- vip 요금제로 변경을 하면 다음달부터 1일부터 혜택
select sysdate, add_months(trunc(sysdate,'month')) from dual;

-- 입사일 기준 다음달부터 1일부터 혜택을 주겠다고 함
-- 입사일 다음달 1일 출력
select hire_date, add_months(trunc(hire_date,'month'),1) from employees;

-- 입사일 기준 1년 후의 날짜 출력
select sysdate,add_months(sysdate,12) from dual;
select sysdate,sysdate+365,add_months(sysdate,12) from dual;

-- 입사일 기준 1년 후 날짜와, 1년 후 마지막 그달의 날짜를 출력
select hire_date,last_day(hire_date) from employees;
select hire_date,hire_date+365,last_day(hire_date+365) from employees;

-- 입력일 기준 1년 후 마지막 날짜가 24년,25년 8/31,9/30,10/31 인 학생들 모두 출력
select sdate from students
where sdate='25/09/30' or sdate='25/10/31';
select sdate,last_day(sdate+365) sdate2,last_day(add_months(sdate,12)) sdate3 from students
where last_day(sdate+365)in ('25/08/31','25/09/30','25/10/31') order by sdate2;

select sdate,extract(month from sdate),extract(year from last_day(sdate+365)) from students
where extract(month from last_day(sdate+365)) in (8,11,12);

-- extract 함수: 특정 년,월,일,시,분,초 만 분리해서 가져오는 함수
-- sysdate 년,월,일
select sysdate from dual;
select extract(year from sysdate) from dual; -- 2024
select extract(month from sysdate) from dual; -- 10
select extract(day from sysdate) from dual; -- 31

-- systimestamp 년월일시분초
select systimestamp from dual;
select extract(hour from systimestamp) from dual;
select extract(minute from systimestamp) from dual;
select extract(second from systimestamp) from dual;

-- substr 함수: 문자에서 시작 위치, 가져올 개수
select sysdate,substr(sysdate,4,2) from dual;

select sdate,last_day(sdate+365) sdate2 from students 
where substr(sdate,4,2) in (8,11,12) order by sdate2;


-- 날짜 -> 문자 to_char ## 날짜포맷
-- 문자 -> 날짜 to_date ## 날짜 사칙연산
-- 문자 -> 숫자 to_number ## 천단위, 숫자앞에 0을 표시, 통화표시
-- 숫자 -> 문자 to_char ## 천단위 표시, 천단위(,) 삭제해서 사칙연산


-- 날짜 형변환해서 날짜 포맷을 변경
-- date 타입 -> char 타입으로 변경해서 포맷
select sysdate from dual; -- 24/10/31
select sysdate,to_char(sysdate,'yyyy-mm-dd') from dual; -- 2024-10-31
select sysdate,to_char(sysdate,'yyyy-mm-dd hh24:mi:ss day') from dual; -- 2024-10-31 12:59:01 목요일
select sysdate,to_char(sysdate,'yyyy-mm-dd hh24:mi:ss dy') from dual; -- 2024-10-31 12:58:54 목
select sysdate,to_char(sysdate,'yyyy-mm-dd hh24:mi:ss mon') from dual; -- 2024-10-31 12:59:27 10월
select sysdate,to_char(sysdate,'yyyy-MON-dd hh24:mi:ss') from dual; -- 2024-10월-31 13:00:37
select sysdate,to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual; -- 2024-10-31 01:02:26
select sysdate,to_char(sysdate,'yyyy-mm-dd am hh:mi:ss day') from dual; -- 2024-10-31 오후 01:02:54 목요일

select hire_date,to_char(hire_date,'yyyy-mm-dd hh:mi:ss') from employees; -- 2007-06-21 12:00:00

-- students 테이블 sdate 2024/01/01
select sdate,to_char(sdate,'yyyy/mm/dd') from students;

select kor from students where kor=70;

-- 숫자 -> 문자타입으로 변경해서 포맷 천단위 표시 
select salary*1382.86*12 from employees; 
select to_char(salary*1382.86*12,'000,000,999,999') from employees;

select to_char(12,'0000') from dual; -- 0012
select 12 from dual;



--drop table chartable2;

create table chartable(
no number(4),
kor number(10),
kor_char varchar2(10),
kor_mark varchar2(10)
);

create table chartable2(
no number(4),
kor number(10),
kor_char varchar2(10),
kor_mark varchar2(10)
);


insert into chartable2 values(
3, 3000000, 3000000, 3000000
);

-- 숫자형 타입은 숫자앞에 0 있어도 표시가 되지 않음. 문자형 타입만 가능
-- 천단위 표시는(,) 숫자형 타입에 입력이 안됨. 문자형 타입만 가능
insert into chartable2 values(
4, 003000000, 03000000, '003000000'
);

-- number,number,str-number 타입을 넣어도 입력, str
-- 문자형 타입에는 숫자형 타입 가능
insert into chartable values(
1,10000,to_char(1000000, '0000000'),to_char(1000000, '0,000,000')
);


insert into chartable values(
3, 30000, 30000, 30000
);


-- 숫자형타입, 문자형(숫자)타입은 사칙연산 가능
-- 숫자형 타입과 문자 천단위 표시(,) 숫자타입은 사칙연산 불가능, 천단위 표시는 문자형 타입
-- (문자형 타입(숫자)에 특수문자가 섞여있으면 사칙연산 불가. kor_mark 여기에 123,456,789 이렇게생긴게들어있음)
-- 숫자형 타입+문자(숫자형) 타입 = 두타입 결과값 출력됨
select kor+kor_char from chartable;
select kor+kor_mark from chartable;

desc chartable; -- number,varchar2
desc chartable2; -- 모든 타입 number


select * from chartable;
select * from chartable2;

commit;

-- 2일 이후의 날짜를 출력
-- '20241031'+2 그냥 이렇게 쓰면 31일에 2가 추가돼서 33일 이렇게 뜸.
-- 그래서 to_date를 써야 함
select '20241031',to_date('24-10-31')+2,sysdate+2 from dual;
select sysdate,sysdate+2 from dual;

select to_date('20241031')+2 from dual;

select to_date(20231031) from dual;

-- number형 타입 -> 날짜형 타입
select sysdate - to_date(20231101) from dual;
-- 문자형 타입 - > 날짜형 타입
select sysdate - to_date('20231101') from dual;


-------------------------------

-- 문자형 타입 -> 숫자형 타입
-- 천단위 문자형타입 -> 천단위 제외 숫자형 타입
select to_number('20,000','999,999') from dual;

-- 문자형 천단위 타입 -> 숫자형 타입 변환
select kor,to_number(kor_mark,'999,999,999') from chartable;
-- 숫자형 타입이기에 사칙연산 가능
select kor+to_number(kor_mark,'999,999,999') from chartable;

-- delete chartable;

insert into chartable values(
1,10000,'0010000','1,000,000'
);

select department_id from employees;
select department_id from employees where department_id is null;

select commission_pct from employees where commission_pct is not null;

-- 월급 * 커미션을 계산하시오
select salary+salary * nvl(commission_pct,0) from employees; -- nvl: null value, 값이 null이면 뒤에 값 표시하기

-- null 경우: 0 표시
select emp_name,nvl(department_id,0) from employees;
-- null 경우: CEO 표시, 숫자형을 문자형으로 타입 변경
select emp_name,nvl(to_char(department_id),'ceo') from employees;
