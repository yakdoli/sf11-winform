---
title: comboboxcells.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\comboboxcells.md
created_at: 2025-07-03
---






##### Combo Box Cells {#combo-box-cells style="tab-stops: 0pt"}

A combo box is a component with a drop-down arrow that users click to display an associated list of choices. The user displays the list by clicking or dragging the drop-down arrow.

 

This cell type allows you to choose the cell value from a drop-down list. You can customize this list in many ways by setting the appropriate GridStyleInfo property. Some interesting options are Autocomplete, associate a string collection, associate LINQ source etc. You can also use this drop-down like a foreign key-- for example, displaying one column in the drop-down while saving the cell value from another column in the data source.

**[]** 


 

{border="0"}Note: A foreign key is a field in a relational table that matches the primary key column of another table. The foreign key can be used to cross-reference tables.


**[]** 

The table below lists various properties that can affect combo box cells.

 

Table 6: GridStyleInfo Property[]


+-----------------------------------+----------------------------------------------------------------------------------------------------------+
| GridStyleInfo Property            | Description                                                                                              |
+-----------------------------------+----------------------------------------------------------------------------------------------------------+
| CellType                          | Set to "ComboBox" for a Combo box control                                                                |
+-----------------------------------+----------------------------------------------------------------------------------------------------------+
| ChoiceList                        | String collection for the drop-down                                                                      |
+-----------------------------------+----------------------------------------------------------------------------------------------------------+
| DropDownStyle                     | Determines the drop-down cell behavior.                                                                  |
|                                   |                                                                                                          |
|                                   | Editable                                                                                                 |
|                                   |                                                                                                          |
|                                   | Autocomplete                                                                                             |
|                                   |                                                                                                          |
|                                   | Exclusive                                                                                                |
+-----------------------------------+----------------------------------------------------------------------------------------------------------+
| ItemsSource                       | Specifies the binding source for the Combo box.                                                          |
+-----------------------------------+----------------------------------------------------------------------------------------------------------+
| Display Member                    | String that names the public property from the data source object to be displayed in the cell.           |
+-----------------------------------+----------------------------------------------------------------------------------------------------------+
| Value Member                      | String that names the public property from the data source object to be used as the value for this cell. |
+-----------------------------------+----------------------------------------------------------------------------------------------------------+


[] 

Before we proceed further the following note provides more information on the drop-down styles:

**[]** 


{border="0"}Note:



***[·    ]***Editable-Editable combo boxes combine an editable text field and provide users the additional option of typing an item that might or might not be on the list. The item to be typed in the text field need not be case-sensitive.

***[·    ]***Autocomplete-Autocomplete combo boxes predict a word or phrase that the user wants to type in the associated text box without the user actually typing it completely.

***[·    ]***Exclusive-This is a non-editable combo box where user is allowed to select only the options available from the drop-down list.


**[]** 

Combo-boxes can be added to the Grid in two different ways as follows:

**[]** 

1.   Using ChoiceList

2.   Using ItemsSource

**[]** 

Using ChoiceList

Let us see how to build different kinds of combo boxes using ChoiceList. This allows you to customize the options to be displayed in a drop-down.

 

Setting Up an Editable Combo Box

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                             |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
|                                                                                                                                                                                        |
| [StringCollection][ list = [new] [StringCollection]();] |
|                                                                                                                                                                                        |
| [list.Add([\"One\"]);]                                                                                                     |
|                                                                                                                                                                                        |
| [list.Add([\"Two\"]);]                                                                                                     |
|                                                                                                                                                                                        |
| [list.Add([\"Three\"]);]                                                                                                   |
|                                                                                                                                                                                        |
| [list.Add([\"Four\"]);]                                                                                                    |
|                                                                                                                                                                                        |
| [list.Add([\"Five\"]);]                                                                                                    |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
|                                                                                                                                                                                        |
| [//Editable Combo]                                                                                                                   |
|                                                                                                                                                                                        |
| [var combo1 = [this].grid.Model\[1, 2\];]                                                                                     |
|                                                                                                                                                                                        |
| [combo1.CellType = [\"ComboBox\"];]                                                                                        |
|                                                                                                                                                                                        |
| [combo1.ChoiceList = list;]                                                                                                                        |
|                                                                                                                                                                                        |
| [combo1.DropDownStyle = GridDropDownStyle.Editable;]                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Output

The following output is generated using the code above.

**[]** 

{border="0"}

Figure 16:  Editable Combo Box using ChoiceList

 

An Editable Combo Box in a Grid is created

Setting Up Autocomplete Combo Box

+----------------------------------------------------------------------------------------------------+
| [\[C#\]]                                         |
|                                                                                                    |
| []                                                             |
|                                                                                                    |
| [//Autocomplete combo]                           |
|                                                                                                    |
| [var combo2 = [this].grid.Model\[2, 2\];] |
|                                                                                                    |
| [combo2.CellType = [\"ComboBox\"];]    |
|                                                                                                    |
| [combo2.ChoiceList = list;]                                    |
|                                                                                                    |
| [combo2.DropDownStyle = GridDropDownStyle.AutoComplete;]       |
+----------------------------------------------------------------------------------------------------+

[] 

Output

The following output is generated using the code above.

[] 

{border="0"}

Figure 17:  Autocomplete Combo box using  ChoiceList

 

An Autocomplete Combo Box in a Grid is created

Setting Up Exclusive Combo Box

**[]** 

+----------------------------------------------------------------------------------------------------+
| [\[C#\]]                                         |
|                                                                                                    |
| []                                                             |
|                                                                                                    |
| [//Exclusive Combo]                              |
|                                                                                                    |
| [var combo3 = [this].grid.Model\[3, 2\];] |
|                                                                                                    |
| [combo3.CellType = [\"ComboBox\"];]    |
|                                                                                                    |
| [combo3.ChoiceList = list;]                                    |
|                                                                                                    |
| [combo3.DropDownStyle = GridDropDownStyle.Exclusive;]          |
+----------------------------------------------------------------------------------------------------+

 

Output

The following output is generated using the code above.

[] 

{border="0"}

Figure 18: Exclusive Combo box using ChoiceList

 

An Exclusive Combo Box in a Grid is created.

Using ItemsSource

The combo boxes created using ItemsSource class ensure that the options available in the drop-down list are populated from the data source the combo box is bound to. The user cannot customize the list unlike combo boxes created using ChoiceList class. The combo boxes in the following examples are bound to Northwind Employee table. The values of the FirstName column form the ItemsSource. The FirstName column is used as the display member of the combo box whose value member is EmployeeID.

**[]** 

Setting up editable combo box

+-----------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                        |
|                                                                                                                                   |
| **[]**                                                                          |
|                                                                                                                                   |
| [//Editable Combo bound to the "FirstName" column of Northwind Employee Table.] |
|                                                                                                                                   |
| [var combo1 = [this].grid.Model\[4, 2\];]                                |
|                                                                                                                                   |
| [combo1.CellType = [\"ComboBox\"];]                                   |
|                                                                                                                                   |
| [combo1.ItemsSource = northWind.Employees.Select(emp =\> emp.FirstName).ToList();]            |
|                                                                                                                                   |
| [combo1.DropDownStyle = GridDropDownStyle.Editable;]                                          |
+-----------------------------------------------------------------------------------------------------------------------------------+

[] 

Output

The following output is generated using the code above.

[] 

{border="0"}

Figure 19:  : Editable Combo box using ItemsSource

 

An editable Combo Box in a Grid is created.

 

Setting Up an Autocomplete Combo Box

+---------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                            |
|                                                                                                                                       |
| **[]**                                                                              |
|                                                                                                                                       |
| [//Autocomplete Combo bound to the "FirstName" column of Northwind Employee Table.] |
|                                                                                                                                       |
| [var combo2 = [this].grid.Model\[5, 2\];]                                    |
|                                                                                                                                       |
| [combo2.CellType = [\"ComboBox\"];]                                       |
|                                                                                                                                       |
| [combo2.ItemsSource = northWind.Employees.Select(emp =\> emp.FirstName).ToList();]                |
|                                                                                                                                       |
| [combo2.DropDownStyle = GridDropDownStyle.AutoComplete;]                                          |
|                                                                                                                                       |
| [combo2.DisplayMember = [\"FirstName\"];]                                 |
|                                                                                                                                       |
| [combo2.ValueMember = [\"EmployeeID\"];]                                  |
+---------------------------------------------------------------------------------------------------------------------------------------+

[] 

Output

The following output is generated using the code above.

[] 

{border="0"}

Figure 20:  Autocomplete Combo box using ItemsSource

 

An Autocomplete Combo Box in a Grid is created

Setting Up an Exclusive Combo Box

[] 

+------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                         |
|                                                                                                                                    |
| []                                                                                             |
|                                                                                                                                    |
| [//Exclusive Combo bound to the "FirstName" column of Northwind Employee Table.] |
|                                                                                                                                    |
| [var combo3 = [this].grid.Model\[6, 2\];]                                 |
|                                                                                                                                    |
| [combo3.CellType = [\"ComboBox\"];]                                    |
|                                                                                                                                    |
| [combo3.ItemsSource = northWind.Employees.Select(emp =\> emp.FirstName).ToList();]             |
|                                                                                                                                    |
| [combo3.DropDownStyle = GridDropDownStyle.Exclusive;]                                          |
+------------------------------------------------------------------------------------------------------------------------------------+

 

Output

The following output is generated using the code above.

[] 

{border="0"}

Figure 21:  Exclusive Combo box using ItemsSource

 

An Exclusive Combo Box in a Grid is created.


[{border="0"}]Note: For complete code, please refer to the following browser sample.


[] 

***\...\\My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Grid.WPF\\Samples\\3.5\\WindowsSamples\\Cell Types\\Combo Box Cell Demo***

**** 

[]{#related-topics}

