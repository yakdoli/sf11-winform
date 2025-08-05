---
title: usingessentialxlsio.md
original_path: WinForms_Docs/99_Uncategorized/usingessentialxlsio.md
created_at: 2025-08-05
---








  









### Using Essential XlsIO {#using-essential-xlsio style="tab-stops: 0pt"}

 

Essential XIsIO will give you an Excel-like Automation-type support without having MS Excel installed on the host system. This means that you can use this library to read and write an XLS file and hold its contents in memory.

 

**Limitation**-You cannot perform actual computations on the contents of the XLS file. Essential Calculate adds this ability.

 

A sample which illustrates the usage of Essential XlsIO with Essential Calculate is available in the following sample installation location:

[] 

***\<Install Location\>\\Windows\\Calculate.Windows\\Samples\\2.0\\Xls File Using CalcEngine Demo\\cs***

***[]*** 

In this sample, the following two classes are used:

**[]** 

[·      ]**ExcelRWCalcSheet** which is derived from **CalcSheet** and implements Syncfusion.XlsIO.IWorksheet

[·      ]**ExcelRWWorkbook** which is derived from **CalcWorkbook** and implements Syncfusion.XlsIO.IWorkbook.

[] 

These classes uses XlsIO library through the supported interfaces to populate a CalcWorkbook object from an XLS file. In addition, the derived classes use overrides to get and set the data through the XlsIO objects that holds the XLS data, instead of relying on the internal data storage that is available in CalcSheet. This gives us the ability to change values in the CalcWorkbook object and view the newly computed results. So, when you want to use an XLS file in your business objects and modify the values or get new calculated results, you can add these two classes to your project and utilize the support immediately in the same manner as this sample.

 

[]{#related-topics}

