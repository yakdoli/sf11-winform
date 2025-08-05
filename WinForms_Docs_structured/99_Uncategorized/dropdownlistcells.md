---
title: dropdownlistcells.md
original_path: WinForms_Docs/99_Uncategorized/dropdownlistcells.md
created_at: 2025-08-05
---






##### Drop-down List Cells {#drop-down-list-cells style="tab-stops: 0pt"}

This cell type serves the same purpose as combo box control. The difference is that it will associate a multicolumn drop-down to the owner cell. The other common features like DropDownStyle, ItemsSource, DisplayMember and ValueMember are applicable to this cell too.

 

The code snippets below allow the user to construct different List Control Cells and their output. To set up drop-down List cell, set its CellType to "DropDownList".

 

Creating Editable Drop-down List Bound to Linq Source with 'FirstName' as its Display Member

+----------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                               |
|                                                                                                          |
| []                                                                   |
|                                                                                                          |
| [var dropdown1 = [this].grid.Model\[7, 2\];]    |
|                                                                                                          |
| [dropdown1.CellType = [\"DropDownList\"];]   |
|                                                                                                          |
| [dropdown1.ItemsSource = northWind.Employees.Select(emp =\>]         |
|                                                                                                          |
| [        [new]]                                 |
|                                                                                                          |
| [        {]                                                          |
|                                                                                                          |
| [            EmployeeID = emp.EmployeeID,]                           |
|                                                                                                          |
| [            FirstName = emp.FirstName,]                             |
|                                                                                                          |
| [            LastName = emp.LastName,]                               |
|                                                                                                          |
| [            Phone = emp.HomePhone]                                  |
|                                                                                                          |
| [        }).ToList();]                                               |
|                                                                                                          |
| [dropdown1.DisplayMember = [\"FirstName\"];] |
|                                                                                                          |
| [dropdown1.DropDownStyle = GridDropDownStyle.Editable;]              |
+----------------------------------------------------------------------------------------------------------+

[] 

Output

The following output is generated using the code above.

 

{border="0"}

Figure 22:  Editable Drop-down List Control

 

An Editable drop-down list is created.

Autocomplete Drop-down List Bound to Linq source with 'FirstName' as its Display Member and 'EmployeeID' as its ValueMember

 

+----------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                               |
|                                                                                                          |
| **[]**                                                 |
|                                                                                                          |
| [var dropdown2 = [this].grid.Model\[8, 2\];]    |
|                                                                                                          |
| [dropdown2.CellType = [\"DropDownList\"];]   |
|                                                                                                          |
| [dropdown2.ItemsSource = northWind.Employees.Select(emp =\>]         |
|                                                                                                          |
| [        [new]]                                 |
|                                                                                                          |
| [        {]                                                          |
|                                                                                                          |
| [            EmployeeID = emp.EmployeeID,]                           |
|                                                                                                          |
| [            FirstName = emp.FirstName,]                             |
|                                                                                                          |
| [            LastName = emp.LastName,]                               |
|                                                                                                          |
| [            Phone = emp.HomePhone]                                  |
|                                                                                                          |
| [        }).ToList();]                                               |
|                                                                                                          |
| [dropdown2.DisplayMember = [\"FirstName\"];] |
|                                                                                                          |
| [dropdown2.ValueMember = [\"EmployeeID\"];]  |
|                                                                                                          |
| [dropdown2.DropDownStyle = GridDropDownStyle.AutoComplete;]          |
+----------------------------------------------------------------------------------------------------------+

[] 

Output

The following output is generated using the code above.

[] 

{border="0"}

Figure 23:  Autocomplete Drop-down List Control

 

Exclusive Drop-down List Bound to Linq Source with FirstName as its DisplayMember.

+----------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                               |
|                                                                                                          |
| **[]**                                                 |
|                                                                                                          |
| [var dropdown3 = [this].grid.Model\[9, 2\];]    |
|                                                                                                          |
| [dropdown3.CellType = [\"DropDownList\"];]   |
|                                                                                                          |
| [dropdown3.ItemsSource = northWind.Employees.Select(emp =\>]         |
|                                                                                                          |
| [    [new]]                                     |
|                                                                                                          |
| [    {]                                                              |
|                                                                                                          |
| [        EmployeeID = emp.EmployeeID,]                               |
|                                                                                                          |
| [        FirstName = emp.FirstName,]                                 |
|                                                                                                          |
| [        LastName = emp.LastName,]                                   |
|                                                                                                          |
| [        Phone = emp.HomePhone]                                      |
|                                                                                                          |
| [    }).ToList();]                                                   |
|                                                                                                          |
| [dropdown3.DisplayMember = [\"FirstName\"];] |
|                                                                                                          |
| [dropdown3.DropDownStyle = GridDropDownStyle.Exclusive;]             |
+----------------------------------------------------------------------------------------------------------+

[] 

Output

The following output is generated using the code above.

[] 

{border="0"}

Figure 24:  Exclusive Drop-down List Control


{border="0"}Note: For complete code, please refer to the following browser sample.


[] 

***\...\\My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Grid.WPF\\Samples\\3.5\\WindowsSamples\\Cell Types\\Combo Box Cell Demo***

[]{#related-topics}

