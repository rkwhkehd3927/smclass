-- 그룹함수
-- sum: 합계, avg: 평균, count: 개수, min: 최소값, max: 최대값
-- median: 중앙값, count: 개수


select salary from employees;

select sum(salary) from employees;
select to_char(sum(salary),'999,999') from employees;

select avg(salary) from employees; -- 6461.831775700934579439252336448598130841
-- 소수점 2자리 반올림
select round(avg(salary),4) from employees; -- 6461.8318
select trunc(avg(salary),4) from employees; -- 6461.8317

select max(salary) from employees;
select min(salary) from employees;

--- 평균값보다 월급이 높은 사원을 출력
select avg(salary) from employees;
select count(salary) from employees where salary>=6461.83;
-- 평균값을 select 해서 입력함
select count(salary) from employees where salary >= (select avg(salary) from employees);

-- emp_name: 단일함수, avg: 그룹함수 / 둘을 같이 쓸 수 없음
select emp_name,avg(salary) from employees; -- error

-- 단일함수, 그룹함수 함께 사용할 수 없음
select department_id,max(salary) from employees; -- error

-- students 테이블 모든 학생의 kor 점수 합계, 평균, 최대값, 최소값을 구하시오
select kor from students;

-- median: 중앙값, count: 개수
select sum(kor),avg(kor),max(kor),min(kor),median(kor) from students;


-- 부서번호가 50, 사원들 월급의 합,평균,최대,최소값을 출력
select sum(salary),avg(salary),max(salary),min(salary),median(salary) from employees where department_id=50;

-- 부서번호 30
select sum(salary),avg(salary),max(salary),min(salary),median(salary) from employees where department_id=30;


-- group by: 단일함수를 출력하고 싶을때, 단일함수 입력
select department_id,max(salary) from employees group by department_id;

-- 그룹함수가 아닌데 굳이 그룹핑해서 출력하지 말 것!
select emp_name,salary from employees;

-- 107명의 평균
select avg(salary) from employees;
-- 단일 함수와 그룹 함수를 함께 사용하려면 group by 지정해야함
select department_id,round(avg(salary)),count(salary),max(salary) from employees group by department_id;

-- 평균월급보다 높은 사람 수를 출력
select count(salary) from employees where salary >= (select avg(salary) from employees);


-- 수학함수: abs-절대값, ceil-올림, floor-버림, round-반올림, trunc-절사, mod-나머지, power-제곱, sqrt-제곱근
-- 제곱
select power(2,2),2*2*2 from dual;

-- 문자,숫자형 타입 -> 날짜형 타입 변경 가능
-- 숫자, 날짜형 타입 -> 문자형 타입 변경 가능
-- 문자형 타입 -> 숫자형 타입 변경 가능 
-- 날짜형 타입 -> 숫자형 타입 변경 불가, 형태를 변경해서 문자형으로 변경한 후, 숫자형으로 변경가능 
select 20240101,to_date(20240101) from dual;
select '2',to_number('2') from dual;

select '20240101',to_number('20240101') from dual;
select to_number(to_date('20240101')) from dual; -- error

select sysdate,to_number(sysdate) from dual; -- error

-- 날짜형 -> 문자형 변환
select sysdate, to_number(to_char(sysdate,'yyyymmdd')) from dual; -- 20241031

-- 년 월 일 한글 입력방법
select sysdate, to_char(sysdate, 'yyyy"년"mm"월"dd"일" day') from dual; -- 2024년10월31일 목요일
select sysdate, to_char(sysdate, 'yyyy/mm/dd day') from dual;


-- 숫자형 타입: 사칙연산 계산해서 출력됨
select kor+eng from students;



-- 문자형 함수
select emp_name,email from employees;
-- 문자형 타입을 +를 사용하여 합치려고 하면 에러남
select emp_name+email from employees; -- error
-- ||, concat 함수
select emp_name||email from employees; -- 이게 더 빨라서 이걸 더 많이 씀
select concat(emp_name,email) from employees;
 
-- lower: 소문자 치환, upper: 대문자 치환, initcap: 첫글자 대문자 치환
select * from member where lower(name) = 'bryan';

select 'joHn',initcap('joHn'),lower('joHn'),upper('joHn') from dual;

-- lpad: 왼쪽 자리수 채우기
select 'john',lpad('john',10,'#'),rpad('john',10,'#') from dual;

-- rpad: 오른쪽 자리수 채우기
select 'john',rpad('john',10,'#') from dual;

-- trim: 앞,뒤 공백 없애기, ltrim: 왼쪽 공백 없애기, rtrim: 오른쪽 공백 없애기
select length(' aaa '), length(trim(' aaa ')) from dual;

-- replace: 치환
select ' a b c ', trim(' a b c ') from dual;
select length(' a b c '), length(trim(' a b c ')), length(replace(' a b c ','','')) from dual;

-- substr: 특정위치 자르기
select 'abcdefg', substr('abcdefg',0,3), substr('abcdefg',2,2) from dual; -- abcdefg / abc / bc

-- hire_date, employees
-- 입사일이 3,8,10월인 사원을 출력
select hire_date,substr(hire_date,4,2) from employees where substr(hire_date,4,2) in (3,8,10);

-- 7월 이상
select hire_date,substr(hire_date,4,2) from employees where substr(hire_date,4,2) > 7;

-- translate 치환
-- 각 글자에 해당되는 단어를 각 단어로 치환
-- 순서에 없는 변환글자는 삭제
select 'axyz', translate('abxdsdasdxyyzx','xy','ab') from dual; -- abadsdasdabbza: x는 a, y는 b로 바꿈
select 'axyz', replace('abxdsdasdxyyzx','xy','ab') from dual; -- abxdsdasdabyzx: xy 만 ab 로 바꿈

-- length(): 문자열 길이
-- students 테이블 name의 글자길이가 10자 이상인 학생만 출력
-- count는 검색되는 값의 개수
select name from students where length(name)>=10;

-- 사원 월급의 합, 평균 구하기
select sum(salary),round(avg(salary),2) from employees;

-- 영어점수의 합, 평균, 최대값, 최소값 구하기
select sum(eng), round(avg(eng),2), max(eng), min(eng) from students;

-- students 테이블에서 홍길동, "등록일: 2023년 12월 02일 x요일 등록!" 이런 식으로 출력
select name, to_char(sdate, '"등록일: "yyyy"년" mm"월" dd"일" day "등록!"') from students;