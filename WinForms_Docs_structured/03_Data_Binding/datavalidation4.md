---
title: datavalidation4.md
original_path: WinForms_Docs/03_Data_Binding/datavalidation4.md
created_at: 2025-08-05
---








  









### Data Validation {#data-validation style="tab-stops: 0pt"}

 

The Data Validation feature available in MS Excel dynamically validates the data that is entered into a cell. The validation rules are specified in the Data Validation **Settings** tab. Data Validation in MS Excel is achieved by selecting the \"Validation\" item in the **Data** menu. Excel has various validation types for each **data type**, and options to show the error box for invalid data through the **Data Validation** dialog box, which is shown in the following screen shot.

 

[] 

{border="0"}

Figure 130: Data Validation Settings[]

[] 

Data Validation in Essential XlsIO

[] 

Essential XlsIO, equivalent to the MS Excel, is built with APIs to read and write data validation in a worksheet by using the **IDataValidation** class. Following are some validation types that XlsIO supports.

[] 

[·      ]Text Length Validation

[·      ]Time Validation

[·      ]List Validation

[·      ]Number Validation

[·      ]Date Validation

[·      ]Custom Validation

[] 

[ An article which describes data validation is available in the following path: ][[http://www.syncfusion.com:91/products/xlsio/backoffice/Articles/data_validation.aspx]{.UGHyperlink}](http://www.syncfusion.com:91/products/xlsio/backoffice/Articles/data_validation.aspx)[.]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                             |
| [// Data validation to list the values in the first cell.]                                                                                                                                                |
|                                                                                                                                                                                                                                                             |
| [IDataValidation][ validation = sheet.Range\[[\"A1\"]\].DataValidation;]                                                                    |
|                                                                                                                                                                                                                                                             |
| [sheet.Range\[[\"A1\"]\].Text = [\"Data validation list\"];]                                                                                                            |
|                                                                                                                                                                                                                                                             |
| [validation.ListOfValues = [new] [string]\[\] { [\"ListItem1\"], [\"ListItem2\"], [\"ListItem3\"] };] |
|                                                                                                                                                                                                                                                             |
| [validation.PromptBoxText = [\"Data Validation list\"];]                                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [validation.IsPromptBoxVisible = [true];]                                                                                                                                                          |
|                                                                                                                                                                                                                                                             |
| [validation.ShowPromptBox = [true];]                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                   |
| [\' Data validation to list the values in the first cell.]                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [Dim][ validation [As] IDataValidation = sheet.Range([\"A1\"]).DataValidation]                                   |
|                                                                                                                                                                                                                                                   |
| [sheet.Range([\"A1\"]).Text = [\"Data validation list\"]]                                                                                                       |
|                                                                                                                                                                                                                                                   |
| [validation.ListOfValues = [New] [String]() {[\"ListItem1\"],[\"ListItem2\"],[\"ListItem3\"]}] |
|                                                                                                                                                                                                                                                   |
| [validation.PromptBoxText = [\"Data Validation list\"]]                                                                                                                                |
|                                                                                                                                                                                                                                                   |
| [validation.IsPromptBoxVisible = [True]]                                                                                                                                                 |
|                                                                                                                                                                                                                                                   |
| [validation.ShowPromptBox = [True]]                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following screen shots illustrates the error alert settings through the **Data Validation** dialog box in MS Excel.

 

[] 

{border="0"}

Figure 131: Error Alert Options in MS Excel[]

***[]*** 

***[]*** 

{border="0"}

Figure 132: Error box**[]**

XlsIO has numerous validation rules and features which are demonstrated in the following code example. **AllowType** property sets the type of validation, **CompareOperator** sets the validation criteria, and **ShowErrorBox** shows the error box with an error message.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                          |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [// Data Validation for Numbers.]                                                                                                       |
|                                                                                                                                                                                           |
| [IDataValidation][ validation1 = sheet.Range\[[\"A3\"]\].DataValidation;] |
|                                                                                                                                                                                           |
| [sheet.Range\[[\"A3\"]\].Text = [\"Enter a Number\"];]                                                |
|                                                                                                                                                                                           |
| [validation1.AllowType = [ExcelDataType].Integer;]                                                                            |
|                                                                                                                                                                                           |
| [validation1.CompareOperator = [ExcelDataValidationComparisonOperator].Between;]                                              |
|                                                                                                                                                                                           |
| [validation1.FirstFormula = [\"0\"];]                                                                                         |
|                                                                                                                                                                                           |
| [validation1.SecondFormula = [\"10\"];]                                                                                       |
|                                                                                                                                                                                           |
| [validation1.ShowErrorBox = [true];]                                                                                             |
|                                                                                                                                                                                           |
| [validation1.ErrorBoxText = [\"Enter Value between 0 to 10\"];]                                                               |
|                                                                                                                                                                                           |
| [validation1.ErrorBoxTitle = [\"ERROR\"];]                                                                                    |
|                                                                                                                                                                                           |
| [validation1.PromptBoxText = [\"Data Validation using Condition for Numbers\"];]                                              |
|                                                                                                                                                                                           |
| [validation1.ShowPromptBox = [true];]                                                                                            |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [// Data Validation for Date.]                                                                                                          |
|                                                                                                                                                                                           |
| [IDataValidation][ validation2 = sheet.Range\[[\"A5\"]\].DataValidation;] |
|                                                                                                                                                                                           |
| [sheet.Range\[[\"A5\"]\].Text = [\"Enter the Date\"];]                                                |
|                                                                                                                                                                                           |
| [validation2.AllowType = [ExcelDataType].Date;]                                                                               |
|                                                                                                                                                                                           |
| [validation2.CompareOperator = [ExcelDataValidationComparisonOperator].Between;]                                              |
|                                                                                                                                                                                           |
| [validation2.FirstDateTime = [new] [DateTime](2003, 5, 10);]                                             |
|                                                                                                                                                                                           |
| [validation2.SecondDateTime = [new] [DateTime](2004, 5, 10);]                                            |
|                                                                                                                                                                                           |
| [validation2.ShowErrorBox = [true];]                                                                                             |
|                                                                                                                                                                                           |
| [validation2.ErrorBoxText = [\"Enter Value between 10/5/2003 to 10/5/2004\"];]                                                |
|                                                                                                                                                                                           |
| [validation2.ErrorBoxTitle = [\"ERROR\"];]                                                                                    |
|                                                                                                                                                                                           |
| [validation2.PromptBoxText = [\"Data Validation using Condition for Date\"];]                                                 |
|                                                                                                                                                                                           |
| [validation2.ShowPromptBox = [true]; ]                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                  |
| [\' Data Validation for Numbers.]                                                                                                                              |
|                                                                                                                                                                                                                  |
| [Dim][ validation1 [As] IDataValidation = sheet.Range([\"A3\"]).DataValidation] |
|                                                                                                                                                                                                                  |
| [sheet.Range([\"A3\"]).Text = [\"Enter a Number\"]]                                                                            |
|                                                                                                                                                                                                                  |
| [validation1.AllowType = ExcelDataType.Integer]                                                                                                                              |
|                                                                                                                                                                                                                  |
| [validation1.CompareOperator = ExcelDataValidationComparisonOperator.Between]                                                                                                |
|                                                                                                                                                                                                                  |
| [validation1.FirstFormula = [\"0\"]]                                                                                                                  |
|                                                                                                                                                                                                                  |
| [validation1.SecondFormula = [\"10\"]]                                                                                                                |
|                                                                                                                                                                                                                  |
| [validation1.ShowErrorBox = [True]]                                                                                                                     |
|                                                                                                                                                                                                                  |
| [validation1.ErrorBoxText = [\"Enter Value between 0 to 10\"]]                                                                                        |
|                                                                                                                                                                                                                  |
| [validation1.ErrorBoxTitle = [\"ERROR\"]]                                                                                                             |
|                                                                                                                                                                                                                  |
| [validation1.PromptBoxText = [\"Data Validation using Condition for Numbers\"]]                                                                       |
|                                                                                                                                                                                                                  |
| [validation1.ShowPromptBox = [True]]                                                                                                                    |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                  |
| [\' Data Validation for Date.]                                                                                                                                 |
|                                                                                                                                                                                                                  |
| [Dim][ validation2 [As] IDataValidation = sheet.Range([\"A5\"]).DataValidation] |
|                                                                                                                                                                                                                  |
| [sheet.Range([\"A5\"]).Text = [\"Enter the Date\"]]                                                                            |
|                                                                                                                                                                                                                  |
| [validation2.AllowType = ExcelDataType.Date]                                                                                                                                 |
|                                                                                                                                                                                                                  |
| [validation2.CompareOperator = ExcelDataValidationComparisonOperator.Between]                                                                                                |
|                                                                                                                                                                                                                  |
| [validation2.FirstDateTime = [New] DateTime(2003,5,10)]                                                                                                 |
|                                                                                                                                                                                                                  |
| [validation2.SecondDateTime = [New] DateTime(2004,5,10)]                                                                                                |
|                                                                                                                                                                                                                  |
| [validation2.ShowErrorBox = [True]]                                                                                                                     |
|                                                                                                                                                                                                                  |
| [validation2.ErrorBoxText = [\"Enter Value between 10/5/2003 to 10/5/2004\"]]                                                                         |
|                                                                                                                                                                                                                  |
| [validation2.ErrorBoxTitle = [\"ERROR\"]]                                                                                                             |
|                                                                                                                                                                                                                  |
| [validation2.PromptBoxText = [\"Data Validation using Condition for Date\"]]                                                                          |
|                                                                                                                                                                                                                  |
| [validation2.ShowPromptBox = [True]]                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Reading the Existing Data Validation Settings

 

You can also read the Data Validation settings in an existing workbook. The following code example illustrates this.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                            |
|                                                                                                                                                                                             |
| **[]**                                                                                                                                                  |
|                                                                                                                                                                                             |
| [// Reading the Data Validation list.]                                                                                                    |
|                                                                                                                                                                                             |
| [this][.comboBox1.Items.AddRange(sheet.Range\[ \"A1\" \].DataValidation.ListOfValues); ] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                |
|                                                                                                                                                                                     |
| **[]**                                                                                                                                          |
|                                                                                                                                                                                     |
| [\' Reading the Data Validation list.]                                                                                            |
|                                                                                                                                                                                     |
| [Me][.comboBox1.Items.AddRange(sheet.Range(\"A1\").DataValidation.ListOfValues)] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

See Also

 

[]

 

[]{#related-topics}

