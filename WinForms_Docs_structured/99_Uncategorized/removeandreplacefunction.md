---
title: removeandreplacefunction.md
original_path: WinForms_Docs/99_Uncategorized/removeandreplacefunction.md
created_at: 2025-08-05
---








  









### Remove and Replace Function {#remove-and-replace-function style="tab-stops: 0pt"}

 

This section discusses the Remove and Replace Function available for the CalcEngine.

[] 

Remove Function

[] 

Removing unused functions from the Function Library, reduces the memory usage and speeds up parsing as well. Also, if you are only using a selected few Library functions, you may want to remove the unused ones. This can be done using the methods given below.

[] 

[·      ]To remove all functions, you can clear the hash table that holds them by using the **engine.LibraryFunctions.Clear** method.

[] 

+-----------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                |
|                                                                                               |
| []                                          |
|                                                                                               |
| [// Remove all functions from the Library.] |
|                                                                                               |
| [engine.LibraryFunctions.Clear();]          |
+-----------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                |
|                                                                                                               |
| []                                          |
|                                                                                                               |
| [// Remove all functions from the Library.] |
|                                                                                                               |
| [engine.LibraryFunctions.Clear()]           |
+---------------------------------------------------------------------------------------------------------------+

[] 

After clearing all functions, you can add few functions that will be used often. To know how to add functions, see .

[] 

[·      ]To remove a single function from the Function Library, use the **CalcEngine.RemoveFunction** method, passing a \"function name\" as the string that references this function, from a formula.

[] 

+----------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                     |
|                                                                                                    |
| []                                             |
|                                                                                                    |
| [// Remove formula name MyMin from the Library.] |
|                                                                                                    |
| [engine.RemoveFunction([\"MyMin\"]);]   |
+----------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                     |
|                                                                                                    |
| []                                             |
|                                                                                                    |
| [\' Remove formula name MyMin from the Library.] |
|                                                                                                    |
| [engine.RemoveFunction([\"MyMin\"])]    |
+----------------------------------------------------------------------------------------------------+

[] 

Replace Function

 

To replace a function with another implementation, you must remove the original name, and add the same name again with a different delegate method.

 

[]{#related-topics}

