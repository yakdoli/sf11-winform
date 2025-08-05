---
title: deletecollectionofrecordsingridgroupingcontrol.md
original_path: WinForms_Docs/04_Controls/Grid/deletecollectionofrecordsingridgroupingcontrol.md
created_at: 2025-08-05
---






#### Delete Collection of Records in GridGroupingControl {#delete-collection-of-records-in-gridgroupingcontrol style="tab-stops: 0pt"}

[] 

Essential **GridGroupingControl** now supports deletion of collection of Records from the **GridGroupingControl** instead of deleting records one by one.

**GridGroupingControl** supports three methods of deleting records.

 

[·      ]**DeleteAll -** Deletes all the records

[·      ]**Delete All\[Selected\] -** Delect selected records

[·      ]**Delete Selected Records -** Deletes Specified records

 

**[]** 

For these methods **DeleteAll** have been implemented to support delete all the records,**Delete All\[Selected\]** deletes selected records, and **Delete Selected Records** delete specified records from the **GridGroupingControl**.

 

 

**Deleting All**

 

The following code illustrates deleting all the records.

[] 

+-----------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                              |
|                                                                                               |
| **[]**                                                    |
|                                                                                               |
| [//This will delete all the records from the grid table.] |
|                                                                                               |
| [this.gridGroupingControl1.Table.Records.DeleteAll();]    |
+-----------------------------------------------------------------------------------------------+

[] 

When the code runs, Deleting all records is bound to **Delete All** button.

 

**Deleting Selected Records**

The following code illustrates deleting records manually selected. 

[] 

+----------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                   |
|                                                                                                    |
| **[]**                                                         |
|                                                                                                    |
| [// this will delete selected records from the grid table. ]   |
|                                                                                                    |
| [this.gridGroupingControl1.Table.SelectedRecords.DeleteAll();] |
+----------------------------------------------------------------------------------------------------+

 

When the code runs,  Deleting manually selected record is bound to **Delete All\[Selected\]** button 

 

**Deleting Specified Records**

The following code illustrates deleting Specified records.

{border="0"}***Note***: Parameter -- Specify the collection of records need to be deleted.

[] 

+----------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                   |
|                                                                                                    |
| **[]**                                                         |
|                                                                                                    |
| [//Delete the specified records from the table ]               |
|                                                                                                    |
| [ this.gridGroupingControl1.Table.Records.DeleteRecords(rec);] |
+----------------------------------------------------------------------------------------------------+

[] 

When the code runs,  Deleting specified records are bound to **Delete Selected Records** button.

[] 

{border="0"}

 

*[Figure ][416][: Delete Collection of Records in GridGroupingControl]*

***[]*** 

[] 

 

[]{#p515} 

 

[]{#related-topics}

