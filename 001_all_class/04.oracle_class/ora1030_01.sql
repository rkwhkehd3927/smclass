select sysdate from dual;

select sysdate-30,sysdate,sysdate+30 from dual;

-- employees 테이블 hire_date 컬럼
select hire_date-1,hire_date,hire_date+1 from employees;

-- 날짜 범위 검색 가능, 정렬 order by, asc: 순차정렬, desc: 역순정렬
select emp_name,hire_date from employees where hire_date>='02/01/01' and hire_date<='04/12/31';
select emp_name,hire_date from employees where hire_date>='02/01/01' and hire_date<='04/12/31' order by hire_date desc;
select emp_name,hire_date from employees where hire_date between '02/01/01' and '04/12/31' order by hire_date;

-- like
select emp_name from employees where emp_name like '___a%';

select emp_name from employees where emp_name like '%a_';


-- 정렬 desc - null 값을 젤 위쪽으로 올려줌, asc - null 값 젤 아래쪽
select department_id from employees order by department_id desc;

-- 월급(salary) 역순 정렬
select emp_name,salary from employees order by salary desc;

-- students 테이블에서 total 역순 정렬
select name,total from students order by total desc;

-- hire_date 기준, 순차정렬
select emp_name,hire_date from employees order by hire_date;

-- kor 기준, kor가 동일한 값일 때 eng도 역순 정렬
select name,kor,eng,math from students order by kor desc, eng desc;

-- 한국어 순차정렬: ㄱ,ㄴ,ㄷ... 역순정렬: ㅎ,ㅍ,ㅌ... (모든 언어 가능)
select name from students order by name;

-- 입사일이 빠른 순으로 정렬, 이름은 역순으로 정렬
select emp_name,hire_date from employees order by hire_date, emp_name desc;


-- abs 절대값
select -10 val,abs(-10) as abs from dual;

select kor,kor-eng,abs(kor-eng) abs from students order by abs desc;


-- floor 소수점 이하 버림
select 3.141592, floor(3.141592) from dual;
-- trunc: 버림, 자리수 지정 가능
select 34.5678,trunc(34.5678,2) from dual; -- 34.56
select 34.5678,trunc(34.5678,-1) from dual; -- 30

-- ceil 소수점 이하 올림
select 3.14592, ceil(3.141592) from dual; -- 4


-- round  반올림, 자리수 범위 지정
-- 소수점 첫째자리
select 34.5678, round(34.5678) from dual; -- 35

-- 소수점 둘째자리까지 출력, 셋째자리에서 반올림
select 34.5678, round(34.5678,2) from dual; -- 34.57

-- 양수 첫째자리에서 반올림, 소수점 자리수에서 앞쪽으로 한칸위치 반올림
select 34.5678, round(34.5678,-1) from dual; -- 30

-- mod: 나머지
select 27/2,mod(27,2) from dual;
select 30/3, mod(31,7) from dual; -- 3

-- 사원번호가 홀수인 사원을 출력
select employee_id,emp_name from employees where mod(employee_id,2) = 1 order by employee_id; -- 나누기 2가 1인 값들 다 출력

-- 최종 연봉(ysalary로 정의): 월급*12+(월급*12)*커미션, 소수점 2자리에서 반올림
-- nvl: null 이면 0으로 표시하기
-- 1381.86 - 달러 환율
select salary,round(salary*12+((salary*12)*nvl(commission_pct,0))*1381.86795,1) ysalary from employees;

-- 시퀀스: 자동으로 번호 부여
create sequence stu_seq
start with 1 -- 시작 1
increment by 1 -- 1씩 증가하기
minvalue 1 -- 최소값
maxvalue 9999 -- 최대값
nocycle
nocache;

select stu_seq.currval from dual; -- currval: 현재 값
select stu_seq.nextval from dual; -- nextval: 다음 값, 이전 값으로 돌아가는 방법은 없음

-- 게시판 테이블 생성
create table board(
bno number(4),
btitle varchar2(100),
bcontent varchar2(4000),
id varchar2(30),
bhit number(10),
bdate date
);

insert into board values(
1,'제목입니다.','내용입니다.','aaa',1,sysdate
);

insert into board values(
2,'제목입니다.2','내용입니다.2','bbb',1,sysdate
);

insert into board values(
stu_seq.nextval,'제목입니다.2','내용입니다.2','aaa',1,sysdate
);

select * from board;

create sequence board_seq
start with 14 -- 시작번호
increment by 1 -- 증감숫자
minvalue 1 -- 최소값
maxvalue 9999 -- 최대값
nocycle -- 1~9999 이상이 되면, 다시 1
nocache -- 메모리에 시퀀스값 미리 할당
;

desc board;
insert into board values(
board_seq.nextval,'제목14','내용14','aaa',1,sysdate);  -- 다시 1부터 시작 못함

select * from board

update board set btitle = '제목을 다시 변경' where bno=14;

commit;

drop table board;

create table board(
bno number(4),
btitle varchar2(100),
bcontent clob, -- 대용량 글자 타입
id varchar2(20),
bgroup number(4), -- 답변달기 그룹핑
bstep number(4), -- 답변달기 경우 순서 정의
bindent number(4), -- 답변달기 들여쓰기
bhit number(10), -- 조회수
bdate date -- 등록일
);

select board_seq.currval from dual;

insert into board values(
board_seq.nextval, '제목1','내용1','aaa',board_seq.currval,0,0,1,sysdate
);

select * from board;

-- 시퀀스 생성
-- students_seq.nextval
-- students 테이블 100 -> 101
-- 101,'홍길순',100,99,99,90,total,avg,rank,날짜
-- 1명을 입력하세요.

create sequence students_seq
start with 100
increment by 1
minvalue 1
maxvalue 9999
nocycle
nocache
;



insert into students values(
students_seq.nextval,'홍길순',99,99,90,99+99+90,(99+99+90)/3,0,sysdate
);

insert into students values(
students_seq.nextval,'홍길자',100,89,90,100+89+90,(100+89+90)/3,0,sysdate
);

select * from newstudents;

select no,name,kor,eng,math,total,round(avg,2),rank,sdate from students;
-- table students에 's' 라는 별칭 주어 출력하기
select s.*,round(avg,2) from students s;

select dept_seq.nextval from dual;

-- s_seq
-- 시작 1, 증분 1, 최대값 99999

create sequence s_seq
start with 1 
increment by 1
minvalue 1
maxvalue 99999
nocycle
nocache
;


-- 시퀀스 생성, nextval: 다음 시퀀스번호 생성, currval: 현재 시퀀스 번호 출력
select s_seq.nextval from dual;
select emp_seq.nextval from dual;
select emp_seq.currval from dual;

