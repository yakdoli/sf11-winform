---
title: formulaauditing.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\formulaauditing.md
created_at: 2025-07-03
---








  









### Formula Auditing {#formula-auditing style="tab-stops: 0pt"}

 

Excel has an option to find the quickest way to identify any cell that contains an error on the active worksheet, and ignore the error that is showed with green indicator, through the Error Checking dialog box. This dialog box provides various options to get information on the error, how a formula is evaluated, its trace, and an option to ignore the error by changing its data type.

 

{border="0"}

Figure 126: : Error Checking[]

 

Excel has the following set of rules that can be enabled or disabled, to show/hide warnings with green indicators.

 

[·      ]**Evaluates to Error Value**-This rule treats cells containing formulas that result in an error, and displays a warning.

[·      ]**Text Date**-This rule treats formulas that contain text formatted cells with years represented as 2-digits, as an error, and displays a warning while checking for errors.

[·      ]**Number stored as Text**-This rule treats numbers formatted as text or preceded by an apostrophe, as an error, and displays a warning.

[·      ]**Inconsistent Formula in Region**-This rule treats a formula in a region of your worksheet that differs from the other formulas in the same region, as an error, and displays a warning.

[·      ]**Formula omits Cells in Region**-This rule treats formulas that omit certain cells in a region, as an error, and displays a warning.

[·      ]**Unlocked Cells containing Formulas**-This rule treats an unlocked cell containing a formula, as an error, and displays a warning when checking for errors.

[·      ]**Formulas referring to Empty Cells**-This rule treats formulas that refer to empty cells, as an error, and displays a warning.

[] 

{border="0"}

Figure 127: Options Dialog Box - Error Checking[]

 

XlsIO provides all the above options to ignore errors, and remove the green indicators. This can be done through the **IgnoreErrorOptions** property of the IRange interface.

 

Following are the values that can be set for the IgnoreError option, through the **ExcelIgnoreError** enumerator.

 


  ---------------------- -----------------------------------------------------------------------
  Member name            Description
  None                   Represents None flag of excel ignore error indicator.
  EvaluateToError        Represents EvaluateToError flag of excel ignore error indicator.
  EmptyCellReferences    Represents EmptyCellReferences flag of excel ignore error indicator.
  NumberAsText           Represents NumberAsText flag of excel ignore error indicator.
  OmittedCells           Represents OmittedCells flag of excel ignore error indicator.
  InconsistentFormula    Represents InconsistentFormula flag of excel ignore error indicator.
  TextDate               Represents TextDate flag of excel ignore error indicator.
  UnlockedFormulaCells   Represents UnlockedFormulaCells flag of excel ignore error indicator.
  All                    Represents All flag of excel ignore error indicator.
  ---------------------- -----------------------------------------------------------------------


 

Following code example illustrates how to ignore or set an error indicator.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                       |
|                                                                                                                                                                        |
| **[]**                                                                                                                             |
|                                                                                                                                                                        |
| [// Sets warning if number is entered as text.]                                                                      |
|                                                                                                                                                                        |
| [sheet.Range\[[\"A2:D2\"]\].IgnoreErrorOptions = [ExcelIgnoreError].NumberAsText;] |
|                                                                                                                                                                        |
| []                                                                                                                                 |
|                                                                                                                                                                        |
| [// Ignores all the error warnings.]                                                                                 |
|                                                                                                                                                                        |
| [sheet.Range\[[\"A3\"]\].IgnoreErrorOptions = [ExcelIgnoreError].None;]            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                       |
|                                                                                                                                            |
| **[]**                                                                                                 |
|                                                                                                                                            |
| [\' Sets warning if number is entered as text.]                                          |
|                                                                                                                                            |
| [sheet.Range\[[\"A2:D2\"]\].IgnoreErrorOptions = ExcelIgnoreError.NumberAsText] |
|                                                                                                                                            |
| []                                                                                                     |
|                                                                                                                                            |
| [\' Ignores all the error warnings.]                                                     |
|                                                                                                                                            |
| [sheet.Range\[[\"A3\"]\].IgnoreErrorOptions = ExcelIgnoreError.None]            |
+--------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

