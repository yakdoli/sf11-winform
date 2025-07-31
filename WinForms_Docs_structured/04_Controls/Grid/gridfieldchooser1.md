---
title: gridfieldchooser1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\gridfieldchooser1.md
created_at: 2025-07-03
---








  









### Grid Field Chooser {#grid-field-chooser style="tab-stops: 0pt"}

[] 

You can customize the column appearance of a Grid Grouping control by using a plug-in utility called the **Field Chooser**. The **FieldChooser** class can be associated with the Grid Grouping control to add/remove columns from the grid. The following code example illustrates this.

[] 

1.   Using C#

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                                          |
| [FieldChooser][ fchooser = [new] [FieldChooser]([this].gridGroupingControl1);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                      |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                         |
| [Dim][ fchooser [As] [New] FieldChooser([Me].gridGroupingControl1)] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Following screen shot shows Grid Grouping control with the Field dialog box.

[] 

{border="0"}

[] 

*[Figure ][467][: Grid Grouping control with Field Dialog Box]*

[] 

To add/remove columns by using the Field Chooser, right-click on a column header, and select the **Field Chooser** menu item to view the **Field** dialog box. This dialog box lists all the column names with check boxes. You can select/clear the check boxes to add/remove the respective columns from the Grid Grouping control.

 

A sample demonstration of the Grid Field Chooser feature is available in the following sample installation path.

[] 

***\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Grouping Grid Layout\\Grid Field Chooser Demo***

 

[]{#p536} 

 

[]{#related-topics}

