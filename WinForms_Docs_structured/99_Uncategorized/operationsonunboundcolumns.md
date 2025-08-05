---
title: operationsonunboundcolumns.md
original_path: WinForms_Docs/99_Uncategorized/operationsonunboundcolumns.md
created_at: 2025-08-05
---






#### Operations on Unbound Columns {#operations-on-unbound-columns style="tab-stops: 0pt"}

[] 

Unbound columns allow association of related values that is bound from an **Expression** in the unbound column or through handling the **QueryUnboundColumnValue** event. Operations like **Sorting,** **Filtering**, **Grouping**, **Summaries** and **ConditionalFormatting** can now be applied on these dynamic values bound to the underlying source. It uses **LINQ Functional Expressions** to be dynamically evaluated at runtime, and thus only Strongly-Typed source can be used with this feature.

[] 

{border="0"}

Figure 109: Operations on Unbound Columns

**[]** 

**[]** 

Sorting on Unbound Columns

**[]** 

Sorting can be done interactively either click on the header, or by declare in **XAML,** by using the following code.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**[  ]                                                                                                                                                     |
|                                                                                                                                                                                                                                                |
| [      ]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                |
| [\<syncfusion:GridDataControl.SortColumns\>]                                                                                                                                                               |
|                                                                                                                                                                                                                                                |
| [            \<syncfusion:GridDataSortColumn ColumnName=\"Multiply\" SortDirection=\"Descending\" /\>]                                                                                                     |
|                                                                                                                                                                                                                                                |
| [        \</syncfusion:GridDataControl.SortColumns\>]                                                                                                                                                      |
|                                                                                                                                                                                                                                                |
| [        \<syncfusion:GridDataControl.VisibleColumns\>]                                                                                                                                                    |
|                                                                                                                                                                                                                                                |
| [            \<syncfusion:GridDataVisibleColumn MappingName=\"CustomerID\" HeaderText=\"Customer ID\" /\>]                                                                                                 |
|                                                                                                                                                                                                                                                |
| [            \<syncfusion:GridDataVisibleColumn MappingName=\"OrderDate\" HeaderText=\"Order Date\" /\>]                                                                                                   |
|                                                                                                                                                                                                                                                |
| [            \<syncfusion:GridDataVisibleColumn MappingName=\"Freight\" HeaderText=\"Freight\" AllowFilter=\"True\"\>]                                                                                     |
|                                                                                                                                                                                                                                                |
| [                \<syncfusion:GridDataVisibleColumn.FilterPane\>]                                                                                                                                          |
|                                                                                                                                                                                                                                                |
| [                    \<syncfusion:GridDataTextFilteringPane IsThemed=\"False\" Foreground=\"Black\" PredicateType=\"And\" /\>]                                                                             |
|                                                                                                                                                                                                                                                |
| [                \</syncfusion:GridDataVisibleColumn.FilterPane\>]                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [            \</syncfusion:GridDataVisibleColumn\>]                                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| [            \<syncfusion:GridDataUnboundVisibleColumn MappingName=\"Multiply\" HeaderText=\"Freight \* 100\" Expression=\"Freight \* 100\" AllowFilter=\"True\" AllowDrag=\"True\" AllowGroup=\"True\"\>] |
|                                                                                                                                                                                                                                                |
| [            \</syncfusion:GridDataUnboundVisibleColumn\>]                                                                                                                                                 |
|                                                                                                                                                                                                                                                |
| [            \<syncfusion:GridDataUnboundVisibleColumn MappingName=\"FreightSqr\" HeaderText=\"Freight Square\" Expression=\"Freight \^ 2\" AllowFilter=\"True\"\>]                                        |
|                                                                                                                                                                                                                                                |
| [            \</syncfusion:GridDataUnboundVisibleColumn\>]                                                                                                                                                 |
|                                                                                                                                                                                                                                                |
| [        \</syncfusion:GridDataControl.VisibleColumns\>]                                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

Figure 110: Sorting

***[]*** 

**[]** 

Filtering on Unbound Columns

**[]** 

Unbound columns support two modes of filtering in the WPF **GridDataControl:**

**[]** 

[·      ]Excel-like Filtering

[·      ]Advanced Filtering

**[]** 

**[]** 

Excel-like Filtering mode

**[]** 

Set **AllowFilter** property to **true** to enable **Excel-like Filtering** in Unbound Column.

The following code illustrates this.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                              |
| [ \<syncfusion:GridDataUnboundVisibleColumn MappingName=\"Multiply\" HeaderText=\"Freight \* 100\" Expression=\"Freight \* 100\" AllowFilter=\"True\" AllowDrag=\"True\" AllowGroup=\"True\"\>] |
|                                                                                                                                                                                                                                              |
| [            \</syncfusion:GridDataUnboundVisibleColumn\>]                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

Figure 111: Excel Filtering

***[]*** 

***[]*** 

**[]** 

Advanced Filtering Mode

**[]** 

Add Advanced Filtering in Unbound Column, by using the following code.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                        |
| [    \<syncfusion:GridDataUnboundVisibleColumn MappingName=\"Multiply\" HeaderText=\"Freight \* 100\" Expression=\"Freight \* 100\" AllowFilter=\"True\" AllowDrag=\"True\" AllowGroup=\"True\"\>] |
|                                                                                                                                                                                                                                        |
| [                \<syncfusion:GridDataVisibleColumn.FilterPane\>]                                                                                                                                  |
|                                                                                                                                                                                                                                        |
| [                    \<syncfusion:GridDataTextFilteringPane IsThemed=\"False\" Foreground=\"Black\" PredicateType=\"And\" /\>]                                                                     |
|                                                                                                                                                                                                                                        |
| [                \</syncfusion:GridDataVisibleColumn.FilterPane\>]                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [            \</syncfusion:GridDataUnboundVisibleColumn\>]                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

{border="0"}

Figure 112: Advanced Filtering

***[]*** 

***[]*** 

**[]** 

Grouping on Unbound Columns

**[]** 

Grouping can be done interactively / declaratively through **XAML** over the Unbound Columns.

[] 

+----------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                             |
|                                                                                                                |
| **[]**                                                                     |
|                                                                                                                |
| [    \<syncfusion:GridDataControl.GroupedColumns\>]                        |
|                                                                                                                |
| [            \<syncfusion:GridDataGroupColumn ColumnName=\"Multiply\" /\>] |
|                                                                                                                |
| [        \</syncfusion:GridDataControl.GroupedColumns\>]                   |
+----------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

Figure 113: Grouping

**[]** 

Summaries on Unbound Columns

**[]** 

The Default summaries work the same way as with bound columns.

Below is the list of different types of Summary declaration in **XAML**.

[] 

Table Summaries

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                              |
|                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                      |
|                                                                                                                                                                                                                 |
| [ \<syncfusion:GridDataControl.TableSummaryRows\>]                                                                                                                          |
|                                                                                                                                                                                                                 |
| [            \<syncfusion:GridDataSummaryRow ShowSummaryInRow=\"False\" Title=\"Total : {FreightMultiplySummary}\" TitleColumnCount=\"3\"\>]                                |
|                                                                                                                                                                                                                 |
| [                \<syncfusion:GridDataSummaryRow.SummaryColumns\>]                                                                                                          |
|                                                                                                                                                                                                                 |
| [                    \<syncfusion:GridDataSummaryColumn Name=\"FreightMultiplySummary\" MappingName=\"Multiply\" SummaryType=\"Int32Aggregate\" Format=\"\'{Max:d}\'\" /\>] |
|                                                                                                                                                                                                                 |
| [                \</syncfusion:GridDataSummaryRow.SummaryColumns\>]                                                                                                         |
|                                                                                                                                                                                                                 |
| [            \</syncfusion:GridDataSummaryRow\>]                                                                                                                            |
|                                                                                                                                                                                                                 |
| [        \</syncfusion:GridDataControl.TableSummaryRows\>]                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**[]** 

Caption Summary

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ \<syncfusion:GridDataControl.CaptionSummaryRow\>]                                                                                                                             |
|                                                                                                                                                                                                                              |
| [            \<syncfusion:GridDataSummaryRow ShowSummaryInRow=\"False\" Title=\"\'{CountSummary}\'\" TitleColumnCount=\"4\"\>]                                                  |
|                                                                                                                                                                                                                              |
| [                \<syncfusion:GridDataSummaryRow.SummaryColumns\>]                                                                                                              |
|                                                                                                                                                                                                                              |
| [                    \<syncfusion:GridDataSummaryColumn Name=\"CountSummary\"  MappingName=\"Multiply\" SummaryType=\"DoubleAggregate\" Format=\"Total - \'{Sum:###.00}\'\" \>] |
|                                                                                                                                                                                                                              |
| [                    \</syncfusion:GridDataSummaryColumn\>]                                                                                                                     |
|                                                                                                                                                                                                                              |
| [                \</syncfusion:GridDataSummaryRow.SummaryColumns\>]                                                                                                             |
|                                                                                                                                                                                                                              |
| [            \</syncfusion:GridDataSummaryRow\>]                                                                                                                                |
|                                                                                                                                                                                                                              |
| [        \</syncfusion:GridDataControl.CaptionSummaryRow\>]                                                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

Group Summary

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [  \<syncfusion:GridDataControl.CaptionSummaryRow\>]                                                                                                                            |
|                                                                                                                                                                                                                     |
| [            \<syncfusion:GridDataSummaryRow ShowSummaryInRow=\"False\" Title=\"\'{CountSummary}\'\" TitleColumnCount=\"4\"\>]                                                  |
|                                                                                                                                                                                                                     |
| [                \<syncfusion:GridDataSummaryRow.SummaryColumns\>]                                                                                                              |
|                                                                                                                                                                                                                     |
| [                    \<syncfusion:GridDataSummaryColumn Name=\"CountSummary\"  MappingName=\"Multiply\" SummaryType=\"DoubleAggregate\" Format=\"Total - \'{Sum:###.00}\'\" \>] |
|                                                                                                                                                                                                                     |
| [                    \</syncfusion:GridDataSummaryColumn\>]                                                                                                                     |
|                                                                                                                                                                                                                     |
| [                \</syncfusion:GridDataSummaryRow.SummaryColumns\>]                                                                                                             |
|                                                                                                                                                                                                                     |
| [            \</syncfusion:GridDataSummaryRow\>]                                                                                                                                |
|                                                                                                                                                                                                                     |
| [        \</syncfusion:GridDataControl.CaptionSummaryRow\>]                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**[]** 

[] 

{border="0"}

Figure 114: Summaries

**[]** 

**[]** 

Custom Summaries on Unbound Columns

**[]** 

Custom Summary calculation differs for Unbound Columns. It has additional parameter to supply a **dynamic lambda** delegate for invoking the unbound values at runtime.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [   public interface ISummaryExpressionAggregate : ISummaryAggregate]                                                                         |
|                                                                                                                                                                                   |
| [    {]                                                                                                                                       |
|                                                                                                                                                                                   |
| [        Action\<IEnumerable, string, Expression\<Func\<string, object, object\>\>, PropertyDescriptor\> CalculateAggregateExpressionFunc();] |
|                                                                                                                                                                                   |
| [    }]                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

All the default Summary Aggregate now implements **ISummaryExpressionAggregate** interface. This typically informs the **ICollectionViewAdv** to expect an Expression to evaluate at runtime.

**[]** 

**[]** 

Expression Trees evaluation for Aggregate methods

**[]** 

A return value is required for any **LINQ Aggregate** method to be implemented.  In order to make the unbound column get invoked through the **lambda delegate**, we have an **internal wrapper lambda** that is generic.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ private static Expression GetInvokeExpressionAggregateFunc\<TResult\>(ParameterExpression paramExp, string propertyName, Expression\<Func\<string, object, object\>\> expressionFunc)] |
|                                                                                                                                                                                                                              |
| [        {]                                                                                                                                                                              |
|                                                                                                                                                                                                                              |
| [            // constructing a wrapper Func that would return a generic value]                                                                                                           |
|                                                                                                                                                                                                                              |
| [            Func\<Expression\<Func\<string, object, object\>\>, string, object, TResult\> fun = (func, prop, rec) =\>]                                                                  |
|                                                                                                                                                                                                                              |
| [            {]                                                                                                                                                                          |
|                                                                                                                                                                                                                              |
| [                var lambda = func.Compile();]                                                                                                                                           |
|                                                                                                                                                                                                                              |
| [                TResult val = (TResult)lambda.DynamicInvoke(new object\[\] { prop, rec });]                                                                                             |
|                                                                                                                                                                                                                              |
| [                return val;]                                                                                                                                                            |
|                                                                                                                                                                                                                              |
| [            };]                                                                                                                                                                         |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                              |
| [            Expression\<Func\<Expression\<Func\<string, object, object\>\>, string, object, TResult\>\> eIFunc = (func, prop, rec) =\> fun(func, prop, rec);]                           |
|                                                                                                                                                                                                                              |
| [            var invokeExp = Expression.Invoke(Expression.Constant(fun), new Expression\[\] { Expression.Constant(expressionFunc), Expression.Constant(propertyName), paramExp });]      |
|                                                                                                                                                                                                                              |
| [            return invokeExp;]                                                                                                                                                          |
|                                                                                                                                                                                                                              |
| [        }]                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The above method simply wraps the Unbound Column's **lambda** expression into an Expression that would return typed value, thus enabling direct calls **to Sum\<TResult\>(Expression\<Func\<T,TResult\>\>** where **TResult** can be any numeric data type.

[]{#p238} 

[]{#related-topics}

