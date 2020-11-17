# rental_house_pricing

## Overview
This is final project for Basic Machine Learning at VinBDI

## Requirement
* Scrapy

## Raw data
https://drive.google.com/drive/u/0/folders/1-Yo5BWsVeleylpayKqEuI_-RFvMX6Pvx

## Website
* https://phongtro123.com/
* https://batdongsan.com.vn/
* https://nha.chotot.com/
* https://thuephongtro.com/
* https://alonhadat.com.vn

## Entity to extract
* Giá (triệu/tháng)
* Location: (string) Chuỗi địa chỉ
* Dis_central: (float) Khoảng cách tới trung tâm HN (làm tròn theo theo phường), Nominatim -> Hải
* Size: (float) Diện tích phòng (m2)
* Size_total_bool: (bool) Diện tích là tổng diện tích? (Trong description có từ khóa tổng diện tích hoặc tương tự, thì trường Diện tích trong bài đăng là ko đáng tin)
* Kind: (Category) Loại Phòng = [ccmn, phòng trọ nhà dân, homestay]
* Inner_toilet: (bool) Có vệ sinh khép kín riêng?
* Air_condition: (bool) Có sẵn điều hòa?
* Heater_shower: (bool) Có sẵn bình nóng lạnh?
* Furnish: (bool) Có sẵn any(tủ, giường, full đồ, tivi, đồ đạc đầy đủ, nội thất...)
* Parking_slot: (bool) Có chỗ để xe? 
* Num_buildings_nearby: (float) Số lượng tòa nhà, chung cư trong bán kính R
* Num_conv_nearby: (float) Số lượng tiện ích trong bán kính R (siêu thị, tạp hóa, TTTM, chợ, công viên, atm, quán cafe...)
* Dis_university: (float) Khoảng cách tới trường ĐH lớn gần nhất (hoặc có trường đại học trong phạm vi R)
* Dis_bus: (float) Khoảng cách tới trạm xe bus gần nhất
* Source: nguồn, ví dụ: 'thuephongtro'

Ghi chú: 1 có, 0 không có

## Sample Extracted Data:
https://drive.google.com/drive/folders/12_BPZofm-8Jeu9CQoHILuOXps_Bj-m8E?usp=sharing
