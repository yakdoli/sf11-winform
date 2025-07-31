---
title: creatinganexceldocument2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatinganexceldocument2.md
created_at: 2025-07-03
---








  









## Creating an Excel Document {#creating-an-excel-document style="tab-stops: 0pt"}

 

When you add the Spreadsheet control to the application, it will be loaded with a blank workbook. You can save this as an Excel document. You can also create new workbooks if required.

To create a new workbook, call the *New* method. New workbook will be created with three worksheets by default. The following code illustrates this:

 

+-------------------------------------------------------------------------+
| [\[C#\]]               |
|                                                                         |
| [spreadControl.New();] |
+-------------------------------------------------------------------------+

 

+------------------------------------------------------------------------+
| [ \[VB\]]             |
|                                                                        |
| [spreadControl.New()] |
+------------------------------------------------------------------------+

 

You can also specify the number of worksheet you want to add in workbook by passing the sheet count to the *New* method. The following code illustrates this:

 

+--------------------------------------------------------------------------+
| [\[C#\]]                |
|                                                                          |
| [spreadControl.New(3);] |
+--------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------+
| [ \[VB\]]              |
|                                                                         |
| [spreadControl.New(3)] |
+-------------------------------------------------------------------------+

[] 

Using Command

You can also use the *NewCommand* to create the Excel document. By default when you execute the NewCommand it will create the workbook with three worksheets and you can also specify the number of worksheet you want to add in workbook by passing the sheet count as Command parameter.

 

The following code illustrates how to bind the *NewCommand* to a button:

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][Button][ Command][=\"{][Binding][ Path][=NewCommand}\"/\>] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

