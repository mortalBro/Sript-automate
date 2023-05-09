import csv

file_name = 'brand_details.csv'
file_name2 = 'sql_data.csv'
column_number = 1
check_dat=[]
data_in_data_base={}


with open(file_name, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        check_dat.append(str(row[1]))
    
with open(file_name2, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data_in_data_base[str(row[1])]=int(row[0])

present_id=[]
have_to_insert=[]
for i in check_dat:
    if i in data_in_data_base:
        present_id.append(data_in_data_base[i])
    else:
        have_to_insert.append(i)

# INSERT INTO `brand_details` (`id`, `brand_name`, `brand_name_old`, `target`, `achiv`, `category_id`) VALUES (NULL, 'CAVANDERS GOLD SAUNF 10S SQ', '', '5', '5', '1');
val="INSERT INTO `brand_details` (`id`, `brand_name`, `brand_name_old`, `target`, `achiv`, `category_id`) VALUES "
ans=""
for i in have_to_insert:
    ans+="(NULL,"+" '' "+"'"+i+"',"+"'5','5','1'),"
ans=ans[:-1]
final_query=val+ans+";"
# print(final_query)

# INSERT INTO `brand_details` (`id`, `brand_name`, `brand_name_old`, `target`, `achiv`, `category_id`) VALUES (NULL, '' 'CVFT 64','5','5','1'),(NULL, '' 'FOCUS PAN FT 10'S','5','5','1'),(NULL, '' 'FS PREMIER 64 FT 10'S','5','5','1'),(NULL, '' 'FS PRINCE 64FT','5','5','1'),;



# INSERT INTO promoter_details (manager_id, campaign_id, name, email, phone_no, asm_state, town, am_name, target, type, password, experiance, Education, status, route_active_date, route_id, distance, outlets, appversion, deviceversion, devicename, promoter_location, otp, ShowRoute, token, create_date, old_promoter, old_number, dashboard_visiable, change_date, otp_count, otp_attempt, attempt_nxttime, otpLastSentTime, is_block) 
# VALUES ('17', '81', 'Saalam', 'b33783', '7385133783', NULL, 'Hingoli', NULL, NULL, NULL, MD5('7385133783'), '1', 'mbs', '1', '2023-05-08', '12591', '5.211974047033464', '5', '2.6', '10', 'RMX2002', '', '3952', 'YES', 'e10adc3949ba59abbe56e057f20f883e', '2018-08-19 22:50:48', NULL, NULL, '2,4,5,6', NULL, '0', '0', NULL, NULL, '0');


file_name_3 = 'sec.csv'
cam_id=81
man_id=17
base_query="INSERT INTO promoter_details (manager_id, campaign_id, name, email, phone_no, asm_state, town, am_name, target, type, password, experiance, Education, status, route_active_date, route_id, distance, outlets, appversion, deviceversion, devicename, promoter_location, otp, ShowRoute, token, create_date, old_promoter, old_number, dashboard_visiable, change_date, otp_count, otp_attempt, attempt_nxttime, otpLastSentTime, is_block) VALUES "
last_query=""
with open(file_name_3, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        name=row[6]
        ph_no=row[5]
        if(len(str(ph_no))<6):
            emai="b12345"
        else:
            emai="b"+ph_no[5:]
        wd_tow=row[3]
        last_query+="('17', '80', '"+name+"', '"+emai+"', '"+ph_no+"', NULL, '"+wd_tow+"', NULL, NULL, NULL, MD5('7385133783'), '1', 'mbs', '1', '2023-05-08', '12591', '5.211974047033464', '5', '2.6', '10', 'RMX2002', '', '3952', 'YES', 'e10adc3949ba59abbe56e057f20f883e', '2018-08-19 22:50:48', NULL, NULL, '2,4,5,6', NULL, '0', '0', NULL, NULL, '0'),"

f_query=base_query+last_query[:-1]+";"
print(f_query)


