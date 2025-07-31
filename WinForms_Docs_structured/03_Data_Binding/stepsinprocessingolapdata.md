---
title: stepsinprocessingolapdata.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\stepsinprocessingolapdata.md
created_at: 2025-07-03
---








  









### Steps in processing OLAP Data {#steps-in-processing-olap-data style="tab-stops: 0pt"}

To process the OLAP data:

1.   Get the input to establish a connection to the specified data source. The connection information can be given as a connection string that contains information about the data source.

Example connection string: "DataSource = localhost; Initial Catalog = Adventure Works DW";

2.   Connect to a server or an off-line cube as a data source.

3.   Once the connection is established, provide input for data processing. You can give two types of inputs to process the OLAP data. They are:

[·      ]MDX Query - You can write a MDX Query for the database and give that query as an input.

[·      ]OlapReport - You can create an OLAP report and give that report as an input to the OlapDataManager.

4.   The output will not differ, based on the input type. The processing method will differ in OLAP base, based on the input type.

5.   If MDX query as given as an input then the query will be executed on the connected data base.

6.   If **OlapReport** is given as an input:

a.   MDX query specification will be created based on the **OlapReport**.

b.   From the MDX query specification, the MDX query will be generated with the help of **OlapQueryBuilderEngine**.

c.   The generated query will be executed on the connection database.

7.   Once the query is executed either from the MDX query input or from the **OlapReport** input, the result is obtained.

8.   This result set will be formatted to provide input for the controls. The formatted input should be passed to the controls.

9.   The output will be displayed in the controls.

 

In Silverlight:

 

1.   The OlapDataManager requires a OlapReport and a Virtual Channel in the form of *OlapDataManager*.

2.   The *OlapDataManager* is a set to control and in the *DataBind* method, the control will make an asynchronous call with the help of a virtual channel provided in *OlapDataManager.*

3.   Now with the help of WCF Service, the control communicates with Olap base to retrieve *CellSet*.

4.   Now the Control passes the obtained *CellSet* to the *OlapDataManager* and in turn the *OlapDataManager* returns the *PivotEngine* to the control.

5.   The output will reflect in the controls.

 

[]{#related-topics}

