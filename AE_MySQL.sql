-- Create the table
/*
create table ae_data(
ae_date date,
total_parcel_count int,
total_payout_amount decimal(19,18),
ae_time time
) */

-- -----------------------------------
-- use database and select all form table
/*
use atlas_earth_data;
select * from ae_data;
*/

-- -----------------------------------
-- EXAMPLE of one entry at a time
/*
insert into ae_data(ae_date, total_parcel_count, total_payout_amount, ae_time)
values('2025-07-14', 46, 1.570563935517269849, '19:08:00')
*/
