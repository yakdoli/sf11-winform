---
title: accessdatasource.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\accessdatasource.md
created_at: 2025-07-03
---








  









### Access Data Source {#access-data-source style="tab-stops: 0pt"}

[] 

Binding using Access Data Source

[] 

Set up the DataSource control. In order to start data binding GGC, you need to set a DataSource control.

The example below demonstrates the resulting code for control setting.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][sfwg][:][GridGroupingControl][ [ID][=\"GridGroupingControl1\"] [runat][=\"server\"\> ]]                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\</][sfwg][:][GridGroupingControl][\>]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][asp][:][AccessDataSource][ [ID][=\"AccessDataSource1\"] [runat][=\"server\" ][SelectCommand][=\"SELECT \* FROM \[Customers\]\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\</][asp][:][AccessDataSource][\>]                                                                                                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                        |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                                       |
| [protected][ [void] Page_Load([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                               |
|                                                                                                                                                                                                                       |
| [AccessDataSource1.DataFile = Server.MapPath([@\"\~\\App_Data\\NWIND.MDB\"]);]                                                                            |
|                                                                                                                                                                                                                       |
| [GridGroupingControl1.DataSource = AccessDataSource1;]                                                                                                                            |
|                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                          |
| [Protected][ [Sub] Page_Load([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                          |
| [AccessDataSource1.DataFile = Server.MapPath([\"\~\\App_Data\\NWIND.MDB\"])]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                          |
| [GridGroupingControl1.DataSource = AccessDataSource1]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                          |
| [End][ [Sub]]                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

To Bind a MDB file with VS 2005

[] 

Through Designer

[] 

To Bind a MDB file with VS 2005, follow the steps given below.

[] 

1.   Create a new C# or VB.NET project using the ASP.NET Web application template.

2.   Select a project and right-click to add an MDB file as follows.

[] 

{border="0"}

Figure 30

[] 

[] 

3.   You can also add an existing MDB file from the following path:

***[]*** 

\[Install drive\]:\\Documents and Settings\\UserName\\My Documents\\Syncfusion\\ EssentialStudio\\VersionNumber\\Web\\Data\\NWIND.MDB.

[] 

The MDB file is now added to the project.

[] 

{border="0"}

Figure 31

[] 

4.   Drag-and-drop the GridGroupingControl from the toolbox and select **New Data Source** from the smart tag.

[] 

{border="0"}

Figure 32

[] 

or

[] 

You can also drag-and-drop the **AccessDataSource** component from the **Data** tab of the VS .NET toolbox and use its SmartTag option to bind the data source.

[] 

{border="0"}

Figure 33

[] 

5.   Select **Access Database** from the configuration wizard.

[] 

{border="0"}

Figure 34

[] 

6.   Select **NWIND.MDB** file as data source to the GridGroupingControl as follows.

[] 

{border="0"}

Figure 35

[] 

7.   Now, select the columns to be retrieved in the following wizard.

[] 

{border="0"}

[] 

8.   Select the query to be executed by using the **TestQuery** button, and finally press **Finish** button.

[] 

{border="0"}

Figure 36

[] 

9.   Now, make sure that the **DataSourceID** property of the grid is set to **AccessDataSource1**.

10.  Run the application. The output would be the following.

[] 

{border="0"}

Figure 37

[] 

To customize the appearance of the GridGroupingControl, refer Appearance section.

 

[]{#p23} 

 

[]{#related-topics}

