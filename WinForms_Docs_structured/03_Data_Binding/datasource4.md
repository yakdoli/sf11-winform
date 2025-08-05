---
title: datasource4.md
original_path: WinForms_Docs/03_Data_Binding/datasource4.md
created_at: 2025-08-05
---








  









## Data source {#data-source style="tab-stops: 0pt"}

OLAP Grid control use ADOMD, which is Microsoft\'s data access technology of choice, for retrieving data from OLAP servers. While ADOMD was built primarily to retrieve OLAP data from SQL Server Analysis Services (Microsoft\'s OLAP Server), ADOMD\'s adherence to industry standards like XML/A, now allows you to access any OLAP server (SAP, SAS, Hyperion, etc.) through ADOMD. Therefore, it provides you the ability to visualize by using the Syncfusion OLAP control, OLAP data from many of the data sources including Microsoft\'s SSAS.

 

OLAP Data can be bound to the OLAP Grid with the help of the OlapDataManager. The OlapDataManager requires the OlapReport, which contains the Dimension and the Measure Elements.

[] 

More:





