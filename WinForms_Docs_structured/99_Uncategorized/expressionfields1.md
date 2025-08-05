---
title: expressionfields1.md
original_path: WinForms_Docs/99_Uncategorized/expressionfields1.md
created_at: 2025-08-05
---






#### Expression Fields {#expression-fields style="tab-stops: 0pt"}

Expression Fields enable you to add a column that holds calculated values based on other fields in the same record. These expression columns are created in the same way as any unbound column, by using the GridDataUnboundVisibleColumn class. This contains the Expression property which needs to be set with a non-null value for an expression column. Expressions can include arithmetic, logical, relational, and few string operators, which will finally get translated into LINQ expressions for evaluation.

 

The following table lists the supported operators and examples for each.

 


  -------------------------- ------------ ---------------------------------------------------------------------------------------- -----------------------------------------
  Expression                 Syntax       Description                                                                              Example Usage
  Mod                        \%           Divides first argument by second argument and returns remainder.                         \[UnitPrice\] % 10
  Multiplication, Division   \*,/         Multiplies/Divides first argument by second argument.                                    \[QunatityPerUnit\] \* \[UnitsInStock\]
  Addition, Subtraction      +,-          Adds first argument with second argument/Subtracts second argument from the first one.   \[UnitsInStock\]+\[Quantity\]
  Or                         OR           Returns 1 if either the first argument or the second one returns true.                   \[Val\]=50 OR \[Val\]=100
  And                        AND          Returns 1 if both parameters return true.                                                \[Val\]\< 50 AND \[Val\]\>100
  Less than                  \<** **      Returns true if first parameter is less than the second one.                             \[OrderID\] \< 2000
  Greater than               \>** **      Returns true if first parameter is greater than the second one.                          \[OrderID\] \> 2500
  Less than Or Equal to      \<=          Returns true if first parameter is less than or equal to the second one.                 \[OrderID\] \<= 2050
  Greater than Or Equal to   \>=          Returns true if first parameter is greater than or equal to the second one.              \[OrderID\] \>= 2056
  Equal                      =            Returns true if both arguments have same value.                                          \[CustomerID\] = 90
  Not Equal to               \<\>** **    Returns true if both arguments does not have same value.                                 \[CustomerID\] \<\> 95
  StartsWith                 StartsWith   Returns true if the value starts with the given string.                                  ProductName StartsWith Chai
  EndsWith                   EndsWith     Returns true if the value ends with the specified string.                                PruductName EndsWith i
  Contains                   Contains     Returns true if the value contains the specified string.                                 ProductName Contains hai
  -------------------------- ------------ ---------------------------------------------------------------------------------------- -----------------------------------------


 

Example

 

1.   Instantiate a GridDataControl and bind it to a data source.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][syncfusion][:][GridDataControl][ x][:][Name][=\"dataGrid\"][ [ShowAddNewRow][=\"False\" ][ShowFilters][=\"False\" ][AutoPopulateColumns][=\"False\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [AutoPopulateRelations][=\"False\" ][ItemsSource][=\"{][StaticResource][ productsSource][}\" ][ShowGroupDropArea][=\"True\"\>]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][syncfusion][:][GridDataControl][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Add an unbound visible column and set its Expression property to the desired formula expression. The unbound visible column also contains the CaseSensitive property, which makes the column names specified in the expression, case sensitive, when set to true. If necessary, you can also customize the expression like any other visible column.

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][syncfusion][:][GridDataControl.VisibleColumns][\>]                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    ][\<][syncfusion][:][GridDataUnboundVisibleColumn][ MappingName][=\"100UnitPrice\"][ HeaderText][=\"Price of 100 units\"][ Expression][=\"UnitPrice \* 100\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        ][\<][syncfusion][:][GridDataUnboundVisibleColumn.ColumnStyle][\>]                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            ][\<][syncfusion][:][GridDataColumnStyle][ Background][=\"PeachPuff\"/\>]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        ][\</][syncfusion][:][GridDataUnboundVisibleColumn.ColumnStyle][\>]                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    ][\</][syncfusion][:][GridDataUnboundVisibleColumn][\>]                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][syncfusion][:][GridDataControl.VisibleColumns][\>]                                                                                                                                                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 192: Grid with Expression Fields

***[]*** 

Accessing Expression Values

 

You can use the GetUnboundValue method of Grid Table to access the computed expression value of a particular unbound cell. This is an overloaded method with the following prototypes:

 

[·      ]GetUnboundValue(RecordIndex, GridDataUnboundVisibleColumn)

[·      ]GetUnboundValue(RowIndex, ColumnIndex)

 

The following code example illustrates how to use this method.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                      |
|                                                                                                                                                                                 |
| []                                                                                                                                          |
|                                                                                                                                                                                 |
| [// Retrieve the expression value by using row and column indices.]                                                           |
|                                                                                                                                                                                 |
| [object][ value = [this].dataGrid.Model.Table.GetUnboundValue(5, 5);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

