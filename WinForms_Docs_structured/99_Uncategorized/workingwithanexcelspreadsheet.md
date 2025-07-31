---
title: workingwithanexcelspreadsheet.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\workingwithanexcelspreadsheet.md
created_at: 2025-07-03
---








  









## Working with an Excel Spreadsheet[]{#p44} {#working-with-an-excel-spreadsheet style="tab-stops: 0pt"}

 

You can use the Microsoft Excel to design spreadsheets that can be used on systems where MS Excel is not installed. This can be done by using a combination of Essential XlsIO and Essential Calculate, where the former can be used to read and write the spreadsheet and later to actually do the computation as values in the spreadsheet are modified.

 

Example

 

To illustrate this process, consider a sample project, Essential Studio\\x.x.x.x\\Windows\\Calculation.Windows\\Samples\\2.0\\XlsFileUsingExcelRW.

 


{border="0"} Note: This requires you to have Essential XlsIO installed in addition to Essential Calculate. MS Excel is not required.


 

The spreadsheet you are using is a car insurance calculator. It uses Names to manage variable values and has the following four sheets.

 

[·      ]**Inputs**-Contains the input values for the car insurance calculations like the state, age, and so on.

[·      ]**LookUps**-Contains data that determine insurance rates[. ]For example, each state has a weight assigned to it; each age has a weight assigned to it, and so on.

[·      ]**Calculate**-Does the actual calculations[. ]Based on the input values from the input sheet, formulas in this sheet, look up appropriate weights from the LookUps sheet, and compute the car insurance cost depending upon these weights.

[·      ]**Outputs**-Contains the computed results obtained from the Calculate sheet.

 

{border="0"}

Figure 37: Worksheet that Receives Inputs

 

{border="0"}

Figure 38: Worksheet that Holds LookUp Tables

 

{border="0"}

Figure 39: Worksheet that Performs Calculations

 

{border="0"}

Figure 40: Dialog Box Showing Named Variables

***[]*** 

This layout represents a general calculation design process which you can use for batch processing of information. The idea is that you change the inputs (all on a single sheet) and then return the outputs (all from a single sheet). There may be a web service or a server application that will allow clients to upload inputs and then download outputs. Or it could just be a batch processing calculation engine. Using this technique, you can use Excel to design complex calculations and then have a simple application that runs on systems without Excel, to input new values and retrieve computed results.

 

For example, consider the below form which accepts input values from the user. Once the values are set, the user clicks a button on the form that puts these values into the inputs sheet and then retrieves the insurance costs from the Outputs sheet and displays it on the form.

 

{border="0"}

Figure 41: Form interface for our Excel Workbook

 

Before learning about the actual code used in this sample to access XLS files, you need to know about a couple of classes in Essential Calculate as well as the role that Essential XlsIO will play.

More:









