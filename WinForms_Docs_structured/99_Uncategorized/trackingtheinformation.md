---
title: trackingtheinformation.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\trackingtheinformation.md
created_at: 2025-07-03
---








  









### Tracking the Information {#tracking-the-information style="tab-stops: 0pt"}

 

To track information used during calculations, **CalcEngine** manages several hash tables. Here is a table of the public hash tables in CalcEngine and a description of their keys and values:

[] 

Table 12: Hash Table


  ----------------------- ------------------------ -------------------------- -----------------------------------------------------------------------
  Hash Table              Key                      Value                      Description
  FormulaInfoTable        Cell reference           FormulaInfo object         Tracks formula/value information for this cell[.]
  DependentCells          Cell reference           Hashtable object           Tracks cells that depend on this cell.
  DependentFormulaCells   Formula cell reference   Hashtable object           Tracks cells that the formula cell depends upon.
  NamedRanges             Name string              Value string               Associates the named range with its value.
  LibraryFunctions        Function name            LibraryFunction delegate   Associates the function name with its method.
  ----------------------- ------------------------ -------------------------- -----------------------------------------------------------------------


[] 

Within CalcEngine, all data is assumed to be part of a rectangular array reference through cell coordinates like A1, C18, and so on. Even **CalcQuickBase** does not require or use such cell-type notation internally on the user side. When it communicates with CalcEngine, it converts its \[name\]-type notation into cell references that CalcEngine can understand. It is these cell references that are used as keys for the first three listed hash tables.

 

[]{#related-topics}

