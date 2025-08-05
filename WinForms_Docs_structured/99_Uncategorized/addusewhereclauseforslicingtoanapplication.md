---
title: addusewhereclauseforslicingtoanapplication.md
original_path: WinForms_Docs/99_Uncategorized/addusewhereclauseforslicingtoanapplication.md
created_at: 2025-08-05
---








  









## Add UseWhereClauseForSlicing to an Application {#add-usewhereclauseforslicing-to-an-application style="tab-stops: 0pt"}

The user can add the UseWhereClauseForSlicing property to an application by setting the property to a Boolean value.  To perform the slicing operation using the 'Where' clause, set the property to *true*. To perform the slicing operation using the 'Select' clause, set the property to *false*.  By default, the value of the UseWhereClauseForSlicing property is *true*.

 

**To perform slicing operation using 'Where' clause:**

+---------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                              |
|                                                                                                               |
| [OlapDataManager.UseWhereClauseForSlicing = [true];] |
+---------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                 |
|                                                                                                                                                                  |
| [OlapDataManager.UseWhereClauseForSlicing = [True]][ ] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**[To ]perform slicing operation using 'Select' clause:**

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                        |
|                                                                                                                                                                                         |
| [this][.olapGridControl1.OlapDataManager.UseWhereClauseForSlicing = [false];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                     |
|                                                                                                                                                                                      |
| [Me][.olapGridControl1.OlapDataManager.UseWhereClauseForSlicing = [False]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

