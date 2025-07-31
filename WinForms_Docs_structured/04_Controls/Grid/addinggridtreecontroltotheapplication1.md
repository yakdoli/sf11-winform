---
title: addinggridtreecontroltotheapplication1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\addinggridtreecontroltotheapplication1.md
created_at: 2025-07-03
---








  









## Adding GridTree Control to the Application {#adding-gridtree-control-to-the-application style="tab-stops: 0pt"}

[]{#p12}[] 

Now that we have  and we have seen the basic steps to be followed before adding our Grid controls.

 

In this section, we will see how to add a GridTree control to the WPF application and load data from the database. This grid requires the RequestTreeItems event to be handled in order to populate the data, where in the ParentItem property must be set to provide children.

**[]** 

RequestTreeItems Event

This event is handled to populate the GridTree control with child items for the corresponding parent items. This event will return a list of objects belonging to a particular node.

**[]** 

Step-by-step Procedure to Create a GridTree Control and Load it with Sample Data

The following steps will add a GridData control and load it with Northwind Customers table.

 

1.   Setup a data source. Here the data source is a Northwind Table:

**[]** 

{border="0"}

Figure 9:  Northwind Customers table

The preceding screen shot shows a sample data from the Northwind Customers table.


 

{border="0"}Note:  This table is available in your sample installation path:


[] 

\...\\My Documents\\Syncfusion\\EssentialStudio\\\<Installed Version\>\\Common\\Data

[] 

2.   Connect to the data source using the below code.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                           |
| [string][ connectionString = [string].Format([@\"Data Source = {0}\"], [LayoutControl].FindFile([\"Northwind.sdf\"]));] |
|                                                                                                                                                                                                                                                                                                           |
| [Northwind][ nw = [new] [Northwind](connectionString);]                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Create a GridTree control and map the RequestTreeItems event as follows:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][syncfusion][:][GridTreeControl][ Name][=\"treeGrid\"][ RequestTreeItems][=\"treeGrid_RequestTreeItems\"][ EnableNodeSelection][=\"False\"][  ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                                    [ PercentSizingBehavior][=\"SizeUntouchedColumns\" \>][    ]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][syncfusion][:][GridTreeControl.Columns][\>]                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][syncfusion][:][GridTreeColumn][ MappingName][=\"Title\"][ [ Width][=\"180\"/\>]]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][syncfusion][:][GridTreeColumn][ MappingName][=\"FirstName\"][ PercentWidth][=\"1\"/\>]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][syncfusion][:][GridTreeColumn][ MappingName][=\"LastName\"][ PercentWidth][=\"1\"/\>]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][syncfusion][:][GridTreeColumn][ MappingName][=\"ReportsTo\" /\>]                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][syncfusion][:][GridTreeColumn][ MappingName][=\"EmployeeID\" /\>]                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\</][syncfusion][:][GridTreeControl.Columns][\>][ ]                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\</][syncfusion][:][GridTreeControl][\>]                                                                                                                                                                                                                                                                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Handle RequestTreeItems event to populate the grid.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                |
| [private][ [void] treeGrid_RequestTreeItems([object] sender, [GridTreeRequestTreeItemsEventArgs] args)] |
|                                                                                                                                                                                                                                                                |
| [        {]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| [            [//When ParentItem is null, you need to set args.ChildList to be the root items\...]]                                                                                                   |
|                                                                                                                                                                                                                                                                |
| [            [if] (args.ParentItem == [null])]                                                                                                                                   |
|                                                                                                                                                                                                                                                                |
| [            {]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                |
| [                [//get the root list - get all employees who have no boss ]]                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [                args.ChildList = nw.Employees.Where(employee =\> (!employee.ReportsTo.HasValue)); [//get all employees who has no boss)]]                                                           |
|                                                                                                                                                                                                                                                                |
| [               ]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                |
| [            }]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                |
| [            [else] [//if ParentItem not null, then set args.ChildList to the child items for the given ParentItem.]]                                                           |
|                                                                                                                                                                                                                                                                |
| [            {   [//get the children of the parent object]]                                                                                                                                          |
|                                                                                                                                                                                                                                                                |
| [                [Employees] emp = args.ParentItem [as] [Employees];]                                                                                 |
|                                                                                                                                                                                                                                                                |
| [                [if] (emp != [null])]                                                                                                                                           |
|                                                                                                                                                                                                                                                                |
| [                {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [                    [//get all employees that report to the parent employee]]                                                                                                                       |
|                                                                                                                                                                                                                                                                |
| [                    args.ChildList = nw.Employees.Where(employee =\> employee.ReportsTo == emp.EmployeeID);]                                                                                                              |
|                                                                                                                                                                                                                                                                |
| [                }]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [            }]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Run the application.

 

{border="0"}

Figure 10: Output---Simple GridTree Control

[] 

The preceding screen shot shows a basic GridTree control loaded with Northwind Customer table data by handing RequestTreeItems event.

[]{#related-topics}

