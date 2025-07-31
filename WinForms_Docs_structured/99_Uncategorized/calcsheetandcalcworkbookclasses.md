---
title: calcsheetandcalcworkbookclasses.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\calcsheetandcalcworkbookclasses.md
created_at: 2025-07-03
---








  









### CalcSheet and CalcWorkbook Classes {#calcsheet-and-calcworkbook-classes style="tab-stops: 0pt"}

 

In the Adding Calculation Support section, you would have learnt how to support referencing multiple ICalcData objects in a workbook fashion. The technique used there relies on registering each ICalcData object directly with a single instance of the CalcEngine. Different ICalcData objects are managed by tying together in a Tab Control as the Tab Pages. To support a general workbook structure where there are no support objects like Tab Pages and Tab Controls to provide the links, the Essential Calculate library includes two classes: **CalcSheet** and **CalcWorkbook**.

[] 

[·      ]The **CalcSheet** class is an ICalcData derived object that plays the role of a single worksheet.

[·      ]It does have the optional facility to hold row/column type data objects that can be set through indexing an instance of the class.

[·      ]This class will allocate storage to hold such data.

[·      ]The CalcWorkbook class is a collection of CalcSheets.

[·      ]You can use these classes to manage the support for working with Excel spreadsheets.

[] 

{border="0"} For more detailed information on these classes, check out the class reference.

 

[]{#related-topics}

