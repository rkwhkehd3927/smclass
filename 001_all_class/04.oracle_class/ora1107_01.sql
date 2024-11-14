-- 평균 80점 이상, 국어 90점 이상인 학생 출력

select * from students;
select name,kor,avg from students where avg>=80 and kor>=90;

-- 평균 60점 이상 또는 총점 100점 이상 출력
select name,avg,total from students where avg>=60 or total>=100;
