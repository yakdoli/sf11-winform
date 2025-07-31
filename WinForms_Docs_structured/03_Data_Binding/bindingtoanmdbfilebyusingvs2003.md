---
title: bindingtoanmdbfilebyusingvs2003.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\bindingtoanmdbfilebyusingvs2003.md
created_at: 2025-07-03
---






#### Binding to an MDB File By Using VS 2003 {#binding-to-an-mdb-file-by-using-vs-2003 style="tab-stops: 0pt"}

[] 

The steps in this lesson are for use with Visual Studio 2003.

[] 

1.   Open the **Data** section of your toolbox and drag an **OleDbDataAdapter** onto your form. This will open the **Data** **Adapter** **Configuration** **Wizard**.

[] 

{border="0"}

 

Figure 7: Data Adapter Configuration Wizard

[] 

[] 

2.   You can use this wizard to create a connection to the NWIND.mdb file. Click **Next** to continue.

[] 

{border="0"}

 

Figure 8:  Setting up the Data Connection

**[]** 

 

3.   Click New Connection. The Data Link Properties dialog box will be displayed. In the Provider tab, select Microsoft Jet 4.0 OLE DB Provider option as shown in the following screen shot.

[] 

{border="0"}

 

Figure 9: Choose the Access Data Provider, Jet 4.0[]

**[]** 

[] 

4.   Click **Next**. The **Connection** tab will be displayed as follows.

[] 

{border="0"}

Figure 10: Click the Browse button to select the File[]

**[]** 

**[]** 

5.   Click the **Browse** button to browse and locate an mdb file. For example, \'NWIND.mdb\' is selected. This file is found in the following path: ***C:\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Data*** (this path will vary according to your installation location). Then click **OK**.

[] 

{border="0"}

Figure 11: Locating the Access file, NWIND.MDB

**[]** 

[] 

6.   Click **Next**.

[] 

{border="0"}

Figure 12: Setting the MDB file as the Data Connection

**[]** 

**[]** 

7.   Select **Use SQL statements** as your query type, and then click **Next**.

[] 

{border="0"}

[] 

Figure 13: Select to Use SQL Statements

**[]** 

8.   To generate the SQL statement, click **Query Builder**.

[] 

{border="0"}

**[]** 

Figure 14: Select the Query Builder

**[]** 

9.   In the **Add Table** dialog box, select the \'Suppliers\' table, click **Add**, and then click **Close**.

[] 

{border="0"}

**[]** 

Figure 15: Select the Suppliers Table

[] 

10.  In this Query Builder window, select **All Columns**. Then click **OK**.

[] 

{border="0"}

[] 

Figure 16: Select the Fields for your Query

 

11.  Click Next to confirm the Query that you have selected.

[] 

{border="0"}

**[]** 

Figure 17: Confirm the Query

**[]** 

12.  Click **Finish**. Your design surface will look similar to this.

[] 

{border="0"}

**[]** 

Figure 18: Adapter and Connection

[] 

13.  Next you will need to generate a data set from the OleDbDataAdapter. Right-click the **oleDbDataAdapter1** under the design surface and select **Generate DataSet**. The **Generate Dataset** dialog box will be displayed.

[] 

{border="0"}

**[]** 

Figure 19: Generating a Dataset

**[]** 

14.  Click **OK** to add a DataSet11 object next to the oleDbConnection1 under the design surface.

 

15.  From the toolbox, drag the **Grid Grouping control** to your form. Size and position it. Also, set the **DataSource** property to *dataSet11.Suppliers* Data Table as shown in the following screen shot.

[] 

{border="0"}

**[]** 

Figure 20: Designer with Grid Grouping control and setting the DataSource Property

[] 

16.  Double-click the form on the design surface to add a Load event handler. In this handler, add the following code.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [this][.oleDbDataAdapter.Fill(][this][.dataSet11);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                      |
| [Me][.oleDbDataAdapter.Fill(][Me][.dataSet11)] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The preceding code is used to load the data from the Data Table. Without this code, you will see an empty Grid Grouping control at run time.

 

17.  Finally, set the **Anchor** property of the Grid Grouping control to *All*, so that the Grid Grouping control can be easily sized with the form. This is depicted in the following screen shot.

[] 

{border="0"}

**[]** 

Figure 21: Setting the Anchor Property

**[]** 

18.  To allow grouping at run time, the Grid Grouping control displays a drop panel onto which the user can drag columns to be grouped. To display this drop panel, you need to set the **ShowGroupDropArea** property to *true* as shown in the following screen shot.

[] 

{border="0"}

**[]** 

Figure 22: Adding the Group Drop Area

**[]** 

Run the project. You will see the basic Grid Grouping control with the data as follows.

[] 

{border="0"}

 

Figure 23: Application showing Grid Grouping control with Data

**[]** 

19.  To group by CompanyName, click on the CompanyName column header and drag it to the drop area as illustrated in the following screen shot.

[] 

{border="0"}

**[]** 

Figure 24: Grouping by the CompanyName Column

[] 


Note: Each set of grouped values has its own \"Caption\" row and its own \"AddNew\" row (\*). Each group has its own PlusMinus cell that will let you expand/collapse the group.


[] 

{border="0"}

[] 

Figure 25: Grouped Grid

 

[]{#p13} 

 

[]{#related-topics}

