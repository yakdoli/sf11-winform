---
title: selectcollectionofrecordsinthegridgroupingcontrol.md
original_path: WinForms_Docs/04_Controls/Grid/selectcollectionofrecordsinthegridgroupingcontrol.md
created_at: 2025-08-05
---






#### Select Collection of Records In the GridGroupingControl {#select-collection-of-records-in-the-gridgroupingcontrol style="tab-stops: 0pt"}

[] 

Essential **GridGroupingControl** now supports two methods for selecting records in grid table.

[] 

[·      ]SelectAll

[·      ]Select Specified Record

**[]** 

Selecting All

 

The following code illustrates how to select all record in grid table.

[] 

+----------------------------------------------------------------------------------------------+
| [//This will select all the records from the grid table] |
|                                                                                              |
| [this.gridGroupingControl1.Table.Records.SelectAll();]   |
+----------------------------------------------------------------------------------------------+

[] 

When the code runs, selecting all record is bound to **Select All** button.

[] 

{border="0"}

 

*[Figure ][417][: SelectAll]*

***[]*** 

Selecting Specified Records

 

The following code illustrates how to select specified records.

[] 


{border="0"}Note: Method Name:  AddRange

         Parameter: Specify the Record collection to be selected


[] 

+------------------------------------------------------------------------------------------------------+
| [//this will select the specified records in the grid table]     |
|                                                                                                      |
| [this.gridGroupingControl1.Table.SelectedRecords.AddRange(rec);] |
+------------------------------------------------------------------------------------------------------+

[] 

When the code runs, selecting specified is bound to **Select Specified Records** button.

[] 

{border="0"}

 

*[Figure ][418][: Illustrating AddRange]*

[] 

[] 

[] 

 

[]{#related-topics}

