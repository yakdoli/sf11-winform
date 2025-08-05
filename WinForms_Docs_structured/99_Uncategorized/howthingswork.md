---
title: howthingswork.md
original_path: WinForms_Docs/99_Uncategorized/howthingswork.md
created_at: 2025-08-05
---








  









### How Things Work {#how-things-work style="tab-stops: 0pt"}

 

1.   What happens when you enter the formula = A1 + 5 into a cell in a CalcSheet object?

 

2.   Here lets assume that CalcSheet is using its own internal data storage to hold values, so that it makes it simple to understand what is going on within CalcEngine. If the data is being held in some other object (like a DataGrid with a DataTable datasource) things will look the same from within the CalcEngine.

 

3.   Here is a sketch of the major steps taken within the library code when you enter a formula into a cell assuming CalcEngine.UseDependencies is True. The actual processing is more involved; these steps should give you an outline of what happens:

 

4.   The string is tested to see whether it begins with an equal sign. If not, CalcSheet stores the entered string in its internal memory so that it will be available if needed. A check is made to see if this cell is a key in the DependentCells collection. If it is, then all cells depending upon this cell are recomputed. This recomputing is a recursive process as changing a cell, that depends upon the changed cell which triggers the recomputing needs of the newly changed cell and so on.

 

5.   If the entered string does begin with an equal sign, the CalcEngine sees this as an entered formula. At this point, the CalcEngine checks to see if the cell is a key in the FormulaInfoTable.

 

6.   If the cell is a key in the FormulaInfoTable, the corresponding FormulaInfo object is retrieved and updated. This amounts to the following:

 

[·      ]Parsing the string.

[·      ]Computing the string.

[·      ]Saving the original formula, the parsed formula and the computed value in the FormulaInfo object.

 

7.   If the cell is not a key in the FormulaInfoTable, a new FormulaInfo object is created. This new FormulaInfo object is populated from the entered string. This amounts to the following:

[] 

[·      ]Parsing the string.

[·      ]Computing the string.

[·      ]Saving the original formula, the parsed formula and the computed value in the FormulaInfo object.

 

There are several other scenarios that must be handled in the CalcEngine. They include things like the newly entered string changes from an existing formula cell to a non-formula cell. In this situation, the CalcEngine uses the DependFormulaCells collection to remove dependencies that are no longer needed.

 

All this dependent tracking is done conditionally depending upon CalcEngine.UseDependencies. Additionally, you can turn off formula calculations using **CalcEngine.CalculatingSuspended**.

 

[]{#p70} 

[]{#related-topics}

