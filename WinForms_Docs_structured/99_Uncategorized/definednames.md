---
title: definednames.md
original_path: WinForms_Docs/99_Uncategorized/definednames.md
created_at: 2025-08-05
---








  









### Defined Names {#defined-names style="tab-stops: 0pt"}

 

**Named Ranges** is a powerful feature in Excel, which makes it possible to assign a name to a group of cells. XlsIO has APIs for inserting new named ranges into workbooks, and also to read existing named ranges. Named Ranges are mainly used in formulae.

 

It enables users with better readability, and at a glance we can predict what it is, and what we\'re adding up with the meaningful range names.

 

To create named ranges, open **Insert menu**, point to **Name** and select **Define**. Names are created at workbook-level, by default, but you can create a sheet-level name, by entering the sheet name followed by an exclamation mark (!), followed by the name of the range. For instance, to create a named range \"x\" on Sheet1, open **Insert menu**, point to **Name**, select **Define**, and enter the name as \'Sheet1!x\'.

 

{border="0"}

Figure 123: Inserting Defined Names using Insert Menu[]

[] 

***[]*** 

[] 

{border="0"}

Figure 124: Define Name Dialog Box[]

***[]*** 

You can create named ranges in spreadsheets through XlsIO with the **IName** interface. Range for the name is specified through **RefersToRange** property, from which you can access the Range text and other information. This can be specified for workbooks and worksheets.

 

Following code example illustrates how to create named ranges and use it in formulas.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                  |
|                                                                                                                                                                   |
| **[]**                                                                                                                        |
|                                                                                                                                                                   |
| [// The first worksheet object in the worksheets collection is accessed.]                                       |
|                                                                                                                                                                   |
| [IWorksheet][ sheet = workbook.Worksheets\[0\];]                          |
|                                                                                                                                                                   |
| []                                                                                                                            |
|                                                                                                                                                                   |
| [// Defining the Range and using it in the Formula.]                                                            |
|                                                                                                                                                                   |
| [IName][ lname1 = workbook.Names.Add([\"One\"]);] |
|                                                                                                                                                                   |
| [lname1.RefersToRange = sheet.Range\[[\"C3\"]\];]                                                     |
|                                                                                                                                                                   |
| []                                                                                                                            |
|                                                                                                                                                                   |
| [IName][ lname2 = workbook.Names.Add([\"Two\"]);] |
|                                                                                                                                                                   |
| [lname2.RefersToRange = sheet.Range\[[\"D3\"]\];]                                                     |
|                                                                                                                                                                   |
| []                                                                                                                            |
|                                                                                                                                                                   |
| [// Formula using Defined Names.]                                                                               |
|                                                                                                                                                                   |
| [sheet.Range\[[\"E3\"]\].Formula = [\"=SUM(One,Two)\"];]                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                       |
|                                                                                                                                                                                            |
| **[]**                                                                                                                                                 |
|                                                                                                                                                                                            |
| [\' The first worksheet object in the worksheets collection is accessed.]                                                                |
|                                                                                                                                                                                            |
| [Dim][ sheet [As] IWorksheet = workbook.Worksheets(0)]                           |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [\' Defining the Range and using it in the Formula.]                                                                                     |
|                                                                                                                                                                                            |
| [Dim][ lname1 [As] IName = workbook.Names.Add([\"One\"])] |
|                                                                                                                                                                                            |
| [lname1.RefersToRange = sheet.Range([\"C3\"])]                                                                                  |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [Dim][ lname2 [As] IName = workbook.Names.Add([\"Two\"])] |
|                                                                                                                                                                                            |
| [lname2.RefersToRange = sheet.Range([\"D3\"])]                                                                                  |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [\' Formula using Defined Names.]                                                                                                        |
|                                                                                                                                                                                            |
| [sheet.Range([\"E3\"]).Formula = [\"=SUM(One,Two)\"]]                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 125: XlsIO with Named Ranges[]

 

Following code example illustrates how to get/set sheet-level named ranges.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                   |
|                                                                                                                                                                    |
| **[]**                                                                                                                         |
|                                                                                                                                                                    |
| [IWorksheet sheet = workbook.Worksheets\[0\];]                                                                                 |
|                                                                                                                                                                    |
| []                                                                                                                             |
|                                                                                                                                                                    |
| [// Add a name.]                                                                                                 |
|                                                                                                                                                                    |
| [IName][ lname1 = sheet.Names.Add([\"CellName\"]);] |
|                                                                                                                                                                    |
| [lname1.RefersToRange = sheet.Range([\"C3\"]);]                                                         |
|                                                                                                                                                                    |
| []                                                                                                                             |
|                                                                                                                                                                    |
| [// Get name.]                                                                                                   |
|                                                                                                                                                                    |
| [Console.Writeline(sheet.Names\[[\"CellName\"]\].Value);]                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                         |
|                                                                                                                                                                                              |
| **[]**                                                                                                                                                   |
|                                                                                                                                                                                              |
| [Dim sheet As IWorksheet =  workbook.Worksheets(0) ]                                                                                                     |
|                                                                                                                                                                                              |
| []                                                                                                                                          |
|                                                                                                                                                                                              |
| [\' Add a name.]                                                                                                                           |
|                                                                                                                                                                                              |
| [Dim][ lname1 [As] IName = sheet.Names.Add([\"CellName\"])] |
|                                                                                                                                                                                              |
| [lname1.RefersToRange = sheet.Range([\"C3\"])]                                                                                    |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [\' Get name.]                                                                                                                             |
|                                                                                                                                                                                              |
| [Console.Writeline(sheet.Names(\"CellName\").Value)]                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

You can get/read all the names from a worksheet or workbook just by enumerating the INames collection as follows.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                 |
|                                                                                                                                                                  |
| **[]**                                                                                                                       |
|                                                                                                                                                                  |
| [for][ ([int] i = 0; i \<= workbook.Names.Count; i++)] |
|                                                                                                                                                                  |
| [{]                                                                                                                          |
|                                                                                                                                                                  |
| [    [Console].WriteLine(workbook.Names\[i\].Name.ToString());]                                         |
|                                                                                                                                                                  |
| [    [Console].WriteLine(workbook.Names\[i\].RefersToRange.Address.ToString());]                        |
|                                                                                                                                                                  |
| [    [Console].WriteLine(workbook.Names\[i\].Name.Value.ToString());]                                   |
|                                                                                                                                                                  |
| [}]                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                   |
|                                                                                                                                                                                        |
| **[]**                                                                                                                                             |
|                                                                                                                                                                                        |
| [Dim][ i [As] [Integer]]                                |
|                                                                                                                                                                                        |
| [For][  i = 0 [To]  workbook.Names.Count [Step]  i + 1] |
|                                                                                                                                                                                        |
| [     Console.WriteLine(workbook.Names(i).Name.ToString())]                                                                                        |
|                                                                                                                                                                                        |
| [     Console.WriteLine(workbook.Names(i).RefersToRange.Address.ToString())]                                                                       |
|                                                                                                                                                                                        |
| [     Console.WriteLine(workbook.Names(i).Name.Value.ToString())]                                                                                  |
|                                                                                                                                                                                        |
| [Next]                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

You can also delete a name in the workbook/worksheet by using the **Delete** method of IName. Note that deleting the cell, does not delete the name from the **Name** collection.

 

Following table lists the properties of **IName**.

 


  Property        Description
  --------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Index           Returns the index number of the Name object within the collection. This is a Read-Only property.
  IsLocal         Indicates whether name is local.
  Name            Returns or sets the name of the object. Read/Write String.
  NameLocal       Returns or sets the name of the object, in the language of the user. Read/Write String for Name.
  RefersToRange   Gets/sets the Range associated with the Name object.
  Value           For the Name object, a string containing the formula that the name is defined to is referred. The string is in A1-style notation in the language of the macro, without an equal sign.
  ValueR1C1       Gets named range Value in R1C1 style. This is a Read-Only property.
  Visible         Determines whether the object is visible. Read/Write Boolean.
  Scope           Returns the scope of the name range.


 

**Scope of Named Range**

 

The scope of the named range can be accessed as follows.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                              |
|                                                                                                                                                               |
| **[]**                                                                                                                    |
|                                                                                                                                                               |
| [IName][ name = workbook.Names.Add([\"Name1\"]);] |
|                                                                                                                                                               |
| [name.RefersToRange = sheet.Range\[[\"A1\"]\];]                                                    |
|                                                                                                                                                               |
| [Console][.WriteLine(name.Scope);]                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                     |
|                                                                                                                                                                          |
| []                                                                                                                                   |
|                                                                                                                                                                          |
| [Dim name As IName][  = workbook.Names.Add([\"Name1\"])] |
|                                                                                                                                                                          |
| [name.RefersToRange = sheet.Range([\"A1\"])]                                                                 |
|                                                                                                                                                                          |
| [Console][.WriteLine(name.Scope)]                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

