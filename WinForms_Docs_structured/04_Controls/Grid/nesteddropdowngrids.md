---
title: nesteddropdowngrids.md
original_path: WinForms_Docs/04_Controls/Grid/nesteddropdowngrids.md
created_at: 2025-08-05
---






##### Nested Drop-down Grids {#nested-drop-down-grids style="tab-stops: 0pt"}

[] 

Nested Drop-down grids are used to represent multi-level data in a grid. For example, if a bank wants to load all the accounts of an enrolled user in a grid control for a financial project, and some of the accounts have subaccounts with options to be selected under each subaccount, which need to be loaded/ shown as a subelement to that account, Nested Drop-down grids can be used to represent the data. The data can be distributed in parent (primary) grid, child grid, and so on. Grid Data Bound Grid control can display hierarchical data using Nested Drop-down grids.

 

**Example:**

 

In the code example below, the parent (primary) grid is the \'Customers\' table from the NorthWind database. On clicking a row of this table, the \'Orders\' table will be displayed in a new grid providing details on orders placed by the customers. On clicking any of the rows in Orders table, another grid named \'Order_Details\' table is displayed providing details on the order details of the selected row in the Orders table. 

 

This example has a derived GridDataBoundGrid class called the **GridHierDataBoundGrid** used for all the grids to be displayed. In the constructor for this class, the tables for parent and child are to be passed.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                               |
| [// Parent table to Child table.]                                                                                                                                                           |
|                                                                                                                                                                                                                                               |
| [// Create the outermost grid for the customers table-uses GridHierDataBoundGrid class.]                                                                                                    |
|                                                                                                                                                                                                                                               |
| [this][.customerGrid1 = [new] GridHierDataBoundGrid([this], [this].dataSet11.Customers,]  |
|                                                                                                                                                                                                                                               |
| [this][.dataSet11.Orders, [this].orderGrid2, [new] QueryFilterStringEventHandler(ProvideOrdersFilterStrings),] |
|                                                                                                                                                                                                                                               |
| [new][ QueryFormatGridEventHandler(ProvideOrderFormat), [true]);]                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\' Parent table to Child table.]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\' Create the outermost grid for the customers table-uses GridHierDataBoundGrid class.]                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Me][.customerGrid1 = [New] GridHierDataBoundGrid([Me], [Me].dataSet11.Customers, [Me].dataSet11.Orders, [Me].orderGrid2, [New] QueryFilterStringEventHandler([AddressOf] ProvideOrdersFilterStrings), [New] QueryFormatGridEventHandler([AddressOf] ProvideOrderFormat), [True])] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Finally, to specify a relationship between a parent table and a child table, an event handler must be passed for the **QueryFilterString** event. The event should specify the FilterString that defines the relationship between the parent table and the child table.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                               |
| [// Parent table to Child table.]                                                                                                                                           |
|                                                                                                                                                                                                                               |
| [private][ [void] ProvideOrdersFilterStrings([object] sender, QueryFilterStringEventArgs e)]   |
|                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                       |
|                                                                                                                                                                                                                               |
| [if][ ([this].customerGrid1.Model\[e.Row, e.Column + 1\].Text != [\"\"])]                   |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                               |
| [// Add 1 to get to Customer ID.]                                                                                                                                           |
|                                                                                                                                                                                                                               |
| [e.FilterString = [string].Format([\"CustomerID = \'{0}\'\"], [this].customerGrid1.Model\[e.Row, e.Column + 1\].Text);] |
|                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                          |
| [\' Parent table to Child table.]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                          |
| [Private][ [Sub] ProvideOrdersFilterStrings([ByVal] sender [As] [Object], [ByVal] e [As] QueryFilterStringEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                          |
| [If][ [Me].customerGrid1.Model(e.Row, e.Column + 1).Text \<\> [\"\"] [Then]]                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                          |
| [\' Add 1 to get to Customer ID.]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                          |
| [e.FilterString = [String].Format([\"CustomerID = \'{0}\'\"], [Me].customerGrid1.Model(e.Row, e.Column + 1).Text)]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                          |
| [End][ [If]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                          |
| [End][ [Sub]]                                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][215][: Nested Drop-down Grids]*

[] 

A sample demonstrating this feature is available under the following sample installation path.

[] 

***\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Windows\\Samples\\2.0\\Data Bound\\GDBG Drop Grid Demo***

 

[]{#p379} 

 

[]{#related-topics}

