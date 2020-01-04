create database healthcare_db;
use healthcare_db;


create external table health_care(id int,
gender string,
age int,
hypertension int,
heart_disease int,
ever_married string,
work_type string,
Residence_type string,
avg_glucose_level float,
bmi float,
smoking_status string,
stroke int)
row format delimited fields terminated by ','
location '/health_project/'
tblproperties ("skip.header.line.count"="1");




create table work_type_disease_perc_all as select t1.work_type,(t1.total/t2.all_total)*100
from
(select work_type,count(*) total
from health_care
where heart_disease = 1
group by work_type) as t1 join (
select count(*) all_total
from health_care
where heart_disease = 1
) as t2;


create table gender_by_perc as 
select gender,(t1.total/t2.all_total)*100
from
(select gender,count(*) total
from health_care
group by gender) as t1 join(
select count(*) all_total
from health_care
) as t2;


create table work_type_disease_perc_rural as select t1.work_type,(t1.total/t2.all_total)*100
from(
select work_type,count(*) total
from health_care
where residence_type = 'Rural' and heart_disease = 1
group by work_type) as t1
join (
select count(*) all_total
from health_care
where residence_type = 'Rural' and heart_disease = 1
) as t2;






