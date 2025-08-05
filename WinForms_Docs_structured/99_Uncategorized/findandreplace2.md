---
title: findandreplace2.md
original_path: WinForms_Docs/99_Uncategorized/findandreplace2.md
created_at: 2025-08-05
---






#### Find and Replace {#find-and-replace style="tab-stops: 0pt"}

[] 

Find and Replace feature in Excel enables to navigate between large spreadsheets. It carries out a simultaneous search in Microsoft Excel values, formulas and also comments.

 

XlsIO also has support for finding and replacing contents in a worksheet. It has various options to find the first matching entry, find all the matching entries, and replace the found content with various data and data sources.

 

{border="0"}

Figure 57: Find and Replace Dialog Box[]

 

XlsIO has the following common find and replace methods and properties, and their usage. This section describes all the methods listed below.

 

[·      ]FindFirst

[·      ]FindAll

[·      ]FindStringStartswith

[·      ]FindStringEndswith

[·      ]Replace

[] 

Following are the possible types of params of the **ExcelFindType** enumerator in the FindFirst and FindAll methods.

 


  -------------------- -------------------------------------------------
  Member Name          Description
  Text                 Represents the Text Finding type.
  Formula              Represents the Formula Finding type.
  FormulaStringValue   Represents the FormulaStringValue Finding type.
  Error                Represents the Error Finding type.
  Number               Represents the Number Finding type.
  FormulaValue         Represents the FormulaValue Finding type.
  -------------------- -------------------------------------------------


**** 

Following are the possible types of params of the **ExcelFindOptions** enumerator in the FindFirst and FindAll methods.

**** 

  ----------------- ----------------------------------------------------------------
  Member Name       Description
  Match Case        Matches case while finding the value.
  MatchEntireCell   Matches the whole word being searched while finding the value.
  ----------------- ----------------------------------------------------------------

 

Find First

 

This method has overloads for searching the first cell with the specified typed value. **The ExcelFindType** enumerator provides options to set the data type of the string (i.e. value and formula value) to be searched, and the **ExcelFindOptions** enumerator provides the options to match the strings associated with the find value.

 


  Methods                                               Description
  ----------------------------------------------------- ------------------------------------------------------------------------------------------------
  FindFirst(Boolean)                                    This method searches for the cell with specified bool value.
  FindFirst (DateTime)                                  This method searches for the cell with specified DateTime value.
  FindFirst (TimeSpan)                                  This method searches for the cell with specified TimeSpan value.
  FindFirst (Double, ExcelFindType)                     This method searches for the cell with specified double value.
  FindFirst (String, ExcelFindType, ExcelFindOptions)   This method searches for the cell with specified string value, again based on the Find options


**** 

**** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                          |
| [//FindFirst with Number]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                          |
| [IRange][ result = sheet.FindFirst(1000000.00075, [ExcelFindType].Number);]                                                                                              |
|                                                                                                                                                                                                                                                                                          |
| [                                ]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                          |
| [// Gets the cell display text]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                          |
| [txtDisplay.Text = result.DisplayText.ToString();]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                          |
| [                ]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                          |
| [//Find First with Match case]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                          |
| [IRange][ result = sheet.FindFirst([\"Simple text\"], [ExcelFindType].Text, [ExcelFindOptions].MatchCase);]              |
|                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                          |
| [// Gets the cell display text.]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                          |
| [txtDisplay.Text = result.DisplayText.ToString();]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                          |
| [//Find First with MatchEntireCellContent]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                          |
| [IRange][ result = sheet.FindFirst([\"Simple text\"], [ExcelFindType].Text, [ExcelFindOptions].MatchEntireCellContent);] |
|                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                          |
| [// Gets the cell display text]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                          |
| [txtDisplay.Text = result.DisplayText.ToString();]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                          |
| [\'FindFirst with Number][]                                                                                                        |
|                                                                                                                                                                                                                                          |
| [Dim result As Range = sheet.FindFirst(1000000.00075, [ExcelFindType].Number)]                                                                                               |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [\'Gets the cell display text]                                                                                                                                                         |
|                                                                                                                                                                                                                                          |
| [txtDisplay.Text = result.DisplayText.ToString()]                                                                                                                                                    |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [\'Find First with Match case]                                                                                                                                                         |
|                                                                                                                                                                                                                                          |
| [Dim result As IRange = sheet.FindFirst([\"Simple text\"], [ExcelFindType].Text, [ExcelFindOptions].MatchCase)]              |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [\'Gets the cell display text.]                                                                                                                                                        |
|                                                                                                                                                                                                                                          |
| [txtDisplay.Text = result.DisplayText.ToString()]                                                                                                                                                    |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [\'Find First with MatchEntireCellContent]                                                                                                                                             |
|                                                                                                                                                                                                                                          |
| [Dim result As IRange = sheet.FindFirst([\"Simple text\"], [ExcelFindType].Text, [ExcelFindOptions].MatchEntireCellContent)] |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [\'Gets the cell display text.]                                                                                                                                                        |
|                                                                                                                                                                                                                                          |
| [txtDisplay.Text = result.DisplayText.ToString()]                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

**FindAll**

This method searches all the cells, and returns all the entries in the sheet that matches the specified data.

 


  --------------------------------------------------- -----------------------------------------------------------------------------------------------------
  Methods                                             Description
  FindAll(Boolean)                                    This method searches for all the cells with specified bool value.
  FindAll(DateTime)                                   This method searches for all the cells with specified DateTime value.
  FindAll(TimeSpan)                                   This method searches for all the cells with specified TimeSpan value.
  FindAll(Double, ExcelFindType)                      This method searches for all the cells with specified double value.
  FindAll (String, ExcelFindType, ExcelFindOptions)   This method searches for all the cells with specified string value, again based on the Find options
  --------------------------------------------------- -----------------------------------------------------------------------------------------------------


 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                            |
| [//Find All with Text]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                            |
| [IRange][\[\] result =sheet .FindAll ([\"Simple Text\"],[ExcelFindType].Text );]                                                                   |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [//Find All with Simple text and Match Case]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                            |
| [IRange][\[\] result = sheet.FindAll([\"Simple text\"], [ExcelFindType].Text, [ExcelFindOptions].MatchCase);]              |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [//Find All with Simple Text and MatchEntireCellContent]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                            |
| [IRange][\[\] result = sheet.FindAll([\"Simple text\"], [ExcelFindType].Text, [ExcelFindOptions].MatchEntireCellContent);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| **[ \[VB\]]**                                                                                                                                                                                        |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [\'Find All with Text]                                                                                                                                                                 |
|                                                                                                                                                                                                                                          |
| [Dim result() As IRange =sheet.FindAll ([\"Simple Text\"],[ExcelFindType].Text)]                                                                     |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [\'Find All with Simple text and Match Case]                                                                                                                                           |
|                                                                                                                                                                                                                                          |
| [Dim result() As IRange = sheet.FindAll([\"Simple text\"], [ExcelFindType].Text, [ExcelFindOptions].MatchCase)]              |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [\'Find All with Simple Text and MatchEntireCellContent]                                                                                                                               |
|                                                                                                                                                                                                                                          |
| [Dim result() As IRange = sheet.FindAll([\"Simple text\"], [ExcelFindType].Text, [ExcelFindOptions].MatchEntireCellContent)] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

FindStringStartswith

 

This method has overloads to search for the first cell that starts with the specified value. The **ExcelFindType** enumerator provides options to set the data type of the string (i.e. value and formula value) to be searched.\
\

+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Methods                                           | Description                                                                                                           |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| FindStringStartsWith( String , ExcelFindType)     | These methods search for cells that start with the specified string value for the given find type.                    |
|                                                   |                                                                                                                       |
|                                                   |                                                                                                                       |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| FindStringStartsWith( String, ExcelFindType,bool) | These methods searchfor cells which start with the specified string value, for the given find type and boolean value. |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+

**** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                       |
| [//Starts with Simple Text]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [IRange][ result = result = sheet.FindStringStartsWith([\"Sim\"], [ExcelFindType].Text);]                     |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [//StartsWith the Number with Text format]                                                                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [IRange][ result = sheet.FindStringStartsWith([\"\$8\"], [ExcelFindType].Text);]                              |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [//Startswith the Text with MatchCase]                                                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [IRange][ result = sheet.FindStringStartsWith([\"Si\"], [ExcelFindType].Text, [false]);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

\
\

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [\'Starts with Simple Text][]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                 |
| [Dim][ result [As] IRange = result = sheet.FindStringStartsWith([\"Sim\"], [ExcelFindType].Text)]                     |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [\'StartsWith the Number with Text format][]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| [Dim][ result [As] IRange = sheet.FindStringStartsWith([\"\$8\"], [ExcelFindType].Text)]                              |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [\'Startswith the Text with MatchCase][]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| [Dim][ result [As] IRange = sheet.FindStringStartsWith([\"Si\"], [ExcelFindType].Text, [False])] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

\
FindStringEndswith

\
This method has overloads to search for cells that have the first cell ending with the specified typed value. **ExcelFindType** enumerator provides options to set the data type of the value and formula value/string to be searched.\
\

  ---------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  Methods                                              Description
  FindStringEndsWith ( String, ExcelFindType)          These methods search for the cell which ends with the specified string value, for the given find type.
  FindStringStartsWith ( String, ExcelFindType,bool)   These methods search for the cell which ends with the specified string value, for the given find type and bool value.
  ---------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                      |
| [//Ends with Text]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                      |
| [IRange][ result = result = sheet.FindStringEndsWith([\"Text\"], [ExcelFindType].Text);]                     |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                      |
| [//EndsWith the Number with Text format]                                                                                                                                                           |
|                                                                                                                                                                                                                                                      |
| [IRange][ result = sheet.FindStringEndsWith([\"00\"], [ExcelFindType].Text);]                                |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                      |
| [//Endswith the Text with MatchCase]                                                                                                                                                               |
|                                                                                                                                                                                                                                                      |
| [IRange][ result = sheet.FindStringEndsWith([\"Case\"],[ExcelFindType].Text, [false]);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

\
\

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                 |
| [\'Starts with Simple Text][]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                 |
| [Dim][ result [As] IRange = result = sheet.FindStringEndsWith([\"][Text][ \"], [ExcelFindType].Text)] |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                 |
| [\'StartsWith the Number with Text format][]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                 |
| [Dim][ result [As] IRange = sheet.FindStringEndsWith([\"00\"], [ExcelFindType].Text)]                                                                 |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                 |
| [\'Startswith the Text with MatchCase][]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                 |
| [Dim][ result [As] IRange = sheet.FindStringEndsWith([\"Case\"], [ExcelFindType].Text, [False])]                                 |
|                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Replace

 

This method enables to replace a string, with the data of various data types and data sources, such as data table, data column and array. Following are the overloads for the **Replace** method.

[] 


  -------------------------------------- --------------------------------------------------
  Methods                                Description
  Replace(String, DateTime)              Replaces specified string by specified value.
  Replace(String, Double)                Replaces specified string by specified value.
  Replace(String, String)                Replaces specified string by specified value.
  Replace(String, DataColumn, Boolean)   Replaces specified string by data column values.
  Replace(String, DataTable, Boolean)    Replaces specified string by data table values.
  Replace(String, Double\[\], Boolean)   Replaces specified string by data from array.
  Replace(String, Int32\[\], Boolean)    Replaces specified string by data from array.
  Replace(String, String\[\], Boolean)   Replaces specified string by data from array.
  -------------------------------------- --------------------------------------------------


 

Following code example illustrates how to replace strings with various data.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                               |
| [// Replacing the Text.]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                               |
| [sheet.Replace([\"Find and Replace\"], [\"New Find and Replace\"]);]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                               |
| [// Replacing a date value by using datetime.]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                               |
| [sheet.Replace([\"Datevalue\"], [DateTime].Now);]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                               |
| [// Replace using array value.]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                               |
| [sheet.Replace([\"Arrayvalue\"], [new] [string]\[\] { [\"ArrayValue1\"], [\"ArrayValue2\"], [\"ArrayValue3\"] }, [true]);] |
|                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                               |
| [// Replacing a data table by calling a function SampleDataTable().]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                               |
| [DataTable][ table = SampleDataTable();]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                               |
| [sheet.Replace([\"DataTable\"], table, [true]); ]                                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                      |
| [\' Replacing the Text.]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                      |
| [sheet.Replace([\"Find and Replace\"], [\"New Find and Replace\"])]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                      |
| [\' Replacing a date value by using datetime.]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                      |
| [sheet.Replace([\"Datevalue\"], DateTime.Now)]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                      |
| [\' Replace using array value.]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                      |
| [sheet.Replace([\"Arrayvalue\"], [New] [String]() {[\"ArrayValue1\"], [\"ArrayValue2\"], [\"ArrayValue3\"]}, [True])] |
|                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                      |
| [\' Replacing a data table by calling a function SampleDataTable().]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                      |
| [Dim][ table [As] DataTable = SampleDataTable()]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                      |
| [sheet.Replace([\"DataTable\"], table, [True])]                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#related-topics}

