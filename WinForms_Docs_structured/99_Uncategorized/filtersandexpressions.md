---
title: filtersandexpressions.md
original_path: WinForms_Docs/99_Uncategorized/filtersandexpressions.md
created_at: 2025-08-05
---






##### Filters and Expressions {#filters-and-expressions style="tab-stops: 0pt"}

[] 

Grouping Grid supports record filters and expression fields. Record Filters let you display a subset of records that meets a given filter criteria. Expression Fields are unbound fields added to the grouping grid that can be used to display any calculation results based on other fields in the same record.

 

Further topics in this section discuss these concepts in detail with suitable examples.

[] 

 

[]{#p430} 

 

###### 4.3.4.3.4.1 Expression Fields {#expression-fields style="tab-stops: 0pt"}

[] 

**Expression Fields** will allow you to add a column that holds calculated values based on other fields in the same record. These expression columns can be visible or invisible, can be used in grouping and sorting and may be employed as summary fields for summary rows. As with adding Summary Rows and Summary Columns, you can use collection editors to add Expression Fields.

**[]** 

**Expression Fields Collection**

 

The Expression Fields collection of a TableDescriptor defines expression fields. This collection is managed by ExpressionFieldDescriptor collection in which each entry termed as ExpressionFieldDescriptor defines one expression field. The data for expression fields are calculated at runtime based on the ExpressionFieldDescriptor.Expression text formula and can depend on other fields in the same record. 

 

Adding Expression Fields Through Designer

 

In the property window of the grouping grid, if you open the TableDescriptor section, you will notice the ExpressionFields collection property. Clicking this will open the ExpressionFieldDescriptor Collection Editor. The editor displays the properties, necessary to setup expression fields. The table given below gives a brief description about some important properties.

[] 


+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property Name                     | Description                                                                                                                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                              | Specifies the name of the expression field.                                                                                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Expression                        | Specifies the formula expression.                                                                                                                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ResultType                        | Lets you specify the result type to which the expression should be converted to.                                                                                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ForceImmediateSaveValue           | Indicates whether the changes to the field in a record should trigger the SaveValue event; Make it to False to avoid triggering ListChanged events when the expression field is modified. |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ReferencedFields                  | Saves a list of referenced field names used in the expression. Use semicolon as a delimiter to specify multiple fields.                                                                   |
|                                   |                                                                                                                                                                                           |
|                                   | This list will be used by the engine to determine which cells to update when ListChanged event is triggered.                                                                              |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

You can add any number of expression fields to the table. The following image depicts this.

[] 

{border="0"}

[] 

*[Figure ][296][: ExpressionFieldDescriptor Collection Editor]*

**[]** 

[] 

Programmatically

[] 

Expression Fields can also be set through code. The following code example adds two expression fields to the Statistics table.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [// Define expression fields.]                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [ExpressionFieldDescriptor][ exp1 = [new] [ExpressionFieldDescriptor]([\"Winning %\"], [\"(\[wins\] \*100)/(\[wins\]+\[ties\]+\[losses\])\"], [\"System.Double\"]);]   |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [ExpressionFieldDescriptor][ exp1 = [new] [ExpressionFieldDescriptor]([\"Loosing %\"], [\"(\[losses\] \*100)/(\[wins\]+\[ties\]+\[losses\])\"], [\"System.Double\"]);] |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [// Add the expression fields to the grid table.]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [this][.gridGroupingControl1.TableDescriptor.ExpressionFields.AddRange([new] Syncfusion.Grouping.[ExpressionFieldDescriptor]\[\] { exp1, exp2 });]                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\' Define expression fields.]                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Dim][ exp1 [As] ExpressionFieldDescriptor = [New] ExpressionFieldDescriptor([\"Winning %\"], [\"(\[wins\] \*100)/(\[wins\]+\[ties\]+\[losses\])\"], [\"System.Double\"])]   |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Dim][ exp2 [As] ExpressionFieldDescriptor = [New] ExpressionFieldDescriptor([\"Loosing %\"], [\"(\[losses\] \*100)/(\[wins\]+\[ties\]+\[losses\])\"], [\"System.Double\"])] |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\' Add the expression fields to the grid table.]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [this.gridGroupingControl1.TableDescriptor.ExpressionFields.AddRange([New] Syncfusion.Grouping.ExpressionFieldDescriptor() {exp1, exp2})]                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The screen shot given below highlights these expression fields.

[] 

{border="0"}

***[]*** 

*[Figure ][297][: Setting Expression Fields Through Code]*

[] 


{border="0"}Note: For more details, refer the following browser sample:

 

\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Filters and Expressions\\Expression Field Demo


 

[]{#p431}[] 

See Also

 

 

4.3.4.3.4.1.1      Nested Expression Fields

[] 

Expression fields can be **nested**, means that the formula expression of an expression fields can have reference to other fields. Given below are examples for nested expression fields.

[] 

[·      ]ExpressionField1.Expression = \" \[Col1\] \* 100 \"

[·      ]ExpressionField2.Expression = \" \[ExpressionField1\] + 0.5 \"

[·      ]ExpressionField3.Expression = \" \[ExpressionField1\] + \[ExpressionField2\] \"

[] 

Sample Code

[] 

The following code examples are used to create nested expression fields.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [// Define expression fields that are nested.]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [ExpressionFieldDescriptor][ expField1 = [new] [ExpressionFieldDescriptor]([\"ExpCol1\"], [\"\[wins\]+\[ties\]+\[losses\]\"], [typeof](System.[Double]));] |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [ExpressionFieldDescriptor][ expField2 = [new] [ExpressionFieldDescriptor]([\"ExpCol2\"], [\"\[ExpCol1\]\*100\"], [typeof](System.[Double]));]             |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [// Add these expression fields to the grid table.        ]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [this][.gridGroupingControl1.TableDescriptor.ExpressionFields.AddRange([new] [ExpressionFieldDescriptor]\[\] { expField1, expField2 });]                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [// Appearance Settings.]                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [this][.gridGroupingControl1.TableDescriptor.Columns\[[\"ExpCol1\"]\].Appearance.AnyRecordFieldCell.BackColor = [Color].Cornsilk;]                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [this][.gridGroupingControl1.TableDescriptor.Columns\[[\"ExpCol2\"]\].Appearance.AnyRecordFieldCell.BackColor = [Color].Cornsilk;]                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [\' Define expression fields that are nested.]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [Dim][ expField1 [As] ExpressionFieldDescriptor = [New] ExpressionFieldDescriptor([\"ExpCol1\"], [\"\[wins\]+\[ties\]+\[losses\]\"], [GetType](System.Double)))] |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [Dim][ expField1 [As] ExpressionFieldDescriptor = [New] ExpressionFieldDescriptor([\"ExpCol2\"], [\"\[ExpCol1\]\*100\"], [GetType](System.Double))]              |
|                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [\' Add these expression fields to the grid table.]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [Me][.gridGroupingControl1.TableDescriptor.ExpressionFields.AddRange([New] ExpressionFieldDescriptor() {expField1, expField2})]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [\' Appearance Settings.]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [Me][.gridGroupingControl1.TableDescriptor.Columns([\"ExpCol1\"]).Appearance.AnyRecordFieldCell.BackColor = Color.Cornsilk]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [Me][.gridGroupingControl1.TableDescriptor.Columns([\"ExpCol2\"]).Appearance.AnyRecordFieldCell.BackColor = Color.Cornsilk]                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Here is a sample screen shot showing two expression fields **ExpCol1** and **ExpCol2** where **ExpCol2** is referencing **ExpCol1**.

[] 

{border="0"}

[] 

*[Figure ][298][: Nested Expression Fields]*

 

[]{#p432} 

 

4.3.4.3.4.1.2      List of Expressions

[] 

A note on Valid Expression Syntax

 

Expressions may be any well-formed algebraic combination of column mapping names enclosed with brackets (\[\]), numerical constants and literals, and the algebraic and logical operators are listed below.

 

The computations are performed as listed, with level one operations done first. Alpha constants used with match and like should be enclosed in apostrophes (\').

[] 

[·      ]\*, / : multiplication, division.

[·      ]+, - : addition, subtraction.

[·      ]\<, \>, =, \<=, \>=: less than, greater than, equal, less than or equal.

[·      ]match, like, in, between.

[·      ]or, and.

[] 

Below is the list of operators used and their descriptions.

[] 


  -------------------------- ------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------
  Expression                 Syntax        Description                                                                                                                                                                                                                                                                                                                                                                                                                         Example Usage
  Multiplication, Division   \*,/          Multiplies/Divides first argument by second arguMultiplies/Divides first argument by second argument.                                                                                                                                                                                                                                                                                                                               \[Wins\] \* \[Losses\] / 100
  Addition, Subtraction      +,-           Adds first argument with second argument/ Subtracts second argument from the first one.                                                                                                                                                                                                                                                                                                                                             \[Wins\]+\[Losses\]
  Or                         OR            Returns 1 if either the first argument or the second one returns true.                                                                                                                                                                                                                                                                                                                                                              \[Val\]=50 OR \[Val\]=100
  And                        AND           Returns 1 if both parameters return true.                                                                                                                                                                                                                                                                                                                                                                                           \[Val\]\< 50 AND \[Val\]\>100
  Less than                  \<            Returns true if first parameter is less than the second one.                                                                                                                                                                                                                                                                                                                                                                        \[OrderID\] \< 2000
  Greater than               \>            Returns true if first parameter is greater than the second one.                                                                                                                                                                                                                                                                                                                                                                     \[OrderID\] \> 2500
  Less than Or Equal to      \<=           Returns true if first parameter is less than or equal to the second one.                                                                                                                                                                                                                                                                                                                                                            \[OrderID\] \<= 2050
  Greater than Or Equal to   \>=           Returns true if first parameter is greater than or equal to the second one.                                                                                                                                                                                                                                                                                                                                                         \[OrderID\] \>= 2056
  Equal                      =             Returns true if both arguments have same value.                                                                                                                                                                                                                                                                                                                                                                                     \[CustomerID\] = 90
  Not Equal to               \<\>          Returns true if both arguments does not have same value.                                                                                                                                                                                                                                                                                                                                                                            \[CustomerID\] \<\> 95
  Match                      match         Returns 1 if there is any occurrence of the right-hand argument in the left-hand argument. For example, \[CompanyName\] match \'RTR\' returns 0 for any record whose CompanyName field does not contain RTR anywhere in the string.                                                                                                                                                                                                 \[Company\] match \'Syncfusion\'
  Like                       Like          Checks if the field starts exactly as specified in the right-hand argument. For example, \[CompanyName\] like \'RTR\' returns 1 for any record whose CompanyName field is exactly RTR. You can use an asterisk as a wildcard. \[CompanyName\] like \'RTR\*\' returns 1 for any record whose CompanyName field starts with RTR. \[CompanyName\] like \'\*RTR\' returns 1 for any record whose CompanyName field ends with RTR.       \[Sport\] like \'Basket\*\'
  In                         in            Checks if the field value is any of the values listed in the right-hand operand. The collection of items used as the right-hand should be separated by commas and enclosed with brackets({}). For example, \[code\] in {1,10,21} returns 1 for any record whose code field contains 1, 10 or 21. \[CompanyName\] in {RTR,MAS} returns 1 for any record whose CompanyName field is RTR or MAS.                                       \[Country\] in {\"USA\", \"UK\"}
  Between                    between       Checks if a date field value between the two values is listed in the right-hand operand. For example, \[date\] between {2/25/2004, 3/2/2004} returns 1 for any record whose date field is greater or equal 2/25/2004 and less than 3/2/2004. To represent the current date, use the token TODAY. To represent DateTime.MinValue, leave the first argument empty. To represent DateTime.MaxValue, leave the second argument empty.   \[OrderDate\] between {2/25/2007, TODAY}
  Between time               betweentime   Checks if a time in the date field value between the two values is listed in the right-hand operand. For example, \[time\] between {04:00:00 PM, 05:00:00 PM} returns 1 for any record whose date field is greater than or equal  to 04:00 and less than 05:00. The time will be calculated along with the date for betweentime.                                                                                                    \[OrderDate\] between {"04/17/2008 9:00:00 PM", "04/21/2008 07:00:00 AM"}
  -------------------------- ------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------


 

[]{#p433} 

 

###### []{#_RecordFilters}4.3.4.3.4.2 RecordFilters {#recordfilters style="tab-stops: 0pt"}

[] 

**RecordFilters** otherwise called as **RowFilters** will allow you to restrict displayed records to those that will satisfy the logical condition that you specify with a FilterRowDescriptor. You have the option of typing an expression (similar to an Expression Field) or entering a condition using an editor dialog.

[] 

RecordFilters Collection

 

The RecordFilters collection defines filter criteria for showing or hiding records. Each filter in this collection is internally maintained by a **RecordFilterDescriptor**. All the RecordFilterDescriptors for a given filter are managed by the **RecordFilterDescriptorCollection** which is returned by the RecordFilters property of the TableDescriptor. Filters can be specified through text formulas similar to expression fields or through the entries of **FilterConditionCollection**. FilterConditionCollection is a set of conditions each with a **CompareOperator** and a **CompareValue** to compare with the value retrieved from the record. A condition can also have a custom **ICustomFilter** object if you want to provide your own logic for evaluating filter criteria.

 

Adding Filters Through Designer

**[]** 

Record Filters can easily be added through the designer. Opening the TableDescriptor.RecordFilters property in the property window will display the RecordFilterDescriptor Collection Editor that allows you to define record filters. The designer settings shown in the below image will setup a record filter for the field **\'wins\',** to display only the records with **wins \> 20**.

[] 

{border="0"}

[] 

*[Figure ][299][: RecordFilterDescriptor Collection Editor]*

[] 

Here is the description for some important properties used to set a row filter.

[] 


  ----------------- ----------------------------------------------------------------------------
  Property          Description
  Name              Specifies the name of the field with which the filter is compared.
  Conditions        A collection of conditions each with a CompareOperator and a CompareValue.
  Expression        A formula expression similar to expression fields.
  LogicalOperator   Indicates the logical operator used if multiple conditions are given.
  ----------------- ----------------------------------------------------------------------------


**[]** 

Programmatically

 

To add a record filter, you must create a RecordFilterDescriptor by specifying the field name with which the filter should be compared and a filter condition that contains a CompareOperator and a CompareValue. The possible options for a CompareOperator are Equals, NotEquals, LessThan, LessThanOrEqualTo, GreaterThan, GreaterThanOrEqualTo, Like, Match and Custom ( for Custom Filter). A filter criteria can also be specified as an expression text similar to the one used in expression fields. A LogicalOperator will be used when you specify more than one condition for a given filter. Finally add the record filter descriptor to the RecordFilters collection of the Table Descriptor.

 

Following code example illustrates how to add a record filter for the column \"wins\" to display only the records with wins \> 20.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                           |
| [FilterCondition][ cond = [new] [FilterCondition]([FilterCompareOperator].GreaterThan, 20);] |
|                                                                                                                                                                                                                                                                                           |
| [RecordFilterDescriptor][ filter = [new] [RecordFilterDescriptor]([\"wins\"], cond);]        |
|                                                                                                                                                                                                                                                                                           |
| [this][.gridGroupingControl1.TableDescriptor.RecordFilters.Add(filter);]                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                    |
| [Dim][ cond [As] FilterCondition = [New] FilterCondition(FilterCompareOperator.GreaterThan, 20)]                    |
|                                                                                                                                                                                                                                                                                    |
| [Dim][ filter [As] RecordFilterDescriptor = [New] RecordFilterDescriptor([\"wins\"], cond)] |
|                                                                                                                                                                                                                                                                                    |
| [Me][.gridGroupingControl1.TableDescriptor.RecordFilters.Add(filter)]                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Given below is a sample screen shot showing the grid filtered with **wins \> 20**.

[] 

{border="0"}

***[]*** 

*[Figure ][300][: Adding Record Filters Through Code]*

[] 


 

{border="0"}Note: Filter Expressions share the same format as in expression fields. For a list of valid expressions, refer [List of Filter Expressions.]{.UGHyperlink}[]{.UGHyperlink}


**[]** 

Nested Tables

 

Record Filters can also be set to the nested tables by accessing the RecordFilters collection of the ChildTableDescriptor.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [FilterCondition][ cond = [new] [FilterCondition]([FilterCompareOperator].GreaterThan, 20);] |
|                                                                                                                                                                                                                                                           |
| [RecordFilterDescriptor][ filter = [new] [RecordFilterDescriptor]([\"OrderID\"], cond);]     |
|                                                                                                                                                                                                                                                           |
| [this][.gridGroupingControl1.GetTableDescriptor([\"Orders\"]).RecordFilters.Add(filter);]                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| [Dim][ ][cond [As] FilterCondition = [New] FilterCondition(FilterCompareOperator.GreaterThan, 20)] |
|                                                                                                                                                                                                                                                                                    |
| [Dim][ filter [As] RecordFilterDescriptor = [New] RecordFilterDescriptor([\"OrderID\"], cond)]                              |
|                                                                                                                                                                                                                                                                                    |
| [Me][.gridGroupingControl1.GetTableDescriptor(\"Orders\").RecordFilters.Add(filter)]                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Special Characters in Filter Values

 

To match the special characters like left bracket (\[), question mark (?), number sign (#) and asterisk (\*), enclose them in square brackets (like \[#\] for \# and  \[\*\] for \* etc.,). The right bracket (\]) can\'t be used within a group to match itself, but it can be used outside a group as an individual character.

 

This is illustrated in the below example with our Grid Grouping control.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                    |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [void][ Form1_Load([object] sender, [EventArgs] e)]                             |
|                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [ArrayList][ rank = [new] [ArrayList]();]                                    |
|                                                                                                                                                                                                                   |
| [RankData][ rankData = [new] [RankData]([\"aaa\"]);] |
|                                                                                                                                                                                                                   |
| [rank.Add(rankData);]                                                                                                                                                         |
|                                                                                                                                                                                                                   |
| [rankData = [new] [RankData]([\"bbb#\"]);]                                                               |
|                                                                                                                                                                                                                   |
| [rank.Add(rankData);]                                                                                                                                                         |
|                                                                                                                                                                                                                   |
| [gridGroupingControl1.DataSource = rank;]                                                                                                                                     |
|                                                                                                                                                                                                                   |
| [string][ filter = [\"\"];]                                                                          |
|                                                                                                                                                                                                                   |
| [RecordFilterDescriptor][ rfd = [null];]                                                             |
|                                                                                                                                                                                                                   |
| [Record][ r = [null];]                                                                               |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [foreach][ ([RankData] a [in] rank)]                                            |
|                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [filter = [\"\[WellName\] like \'\"] + ReplaceSpcChar(a.WellName) + [\"\'\"]; ]                                               |
|                                                                                                                                                                                                                   |
| [rfd = [new] [RecordFilterDescriptor](filter);]                                                                                  |
|                                                                                                                                                                                                                   |
| [gridGroupingControl1.TableDescriptor.RecordFilters.Add(rfd);]                                                                                                                |
|                                                                                                                                                                                                                   |
| [int][ cont = gridGroupingControl1.Table.FilteredRecords.Count;]                                                             |
|                                                                                                                                                                                                                   |
| [r = [new] [Record](gridGroupingControl1.Table);]                                                                                |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                   |
| [// Exception will be thrown here if special characters are not enclosed in square brackets.]                                                                   |
|                                                                                                                                                                                                                   |
| [r = gridGroupingControl1.Table.FilteredRecords\[0\]; ]                                                                                                                       |
|                                                                                                                                                                                                                   |
| [rankData = r.GetData() [as] [RankData];]                                                                                        |
|                                                                                                                                                                                                                   |
| [gridGroupingControl1.TableDescriptor.RecordFilters.Clear();]                                                                                                                 |
|                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                   |
| [private][ [string] ReplaceSpcChar([string] pattern)]                              |
|                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [// Take caution while replacing the pattern and ensure that only the intended pattern is modified.]                                                            |
|                                                                                                                                                                                                                   |
| [pattern = pattern.Replace([\"\[\"], [\"\[\[\]\"]);]                                                                          |
|                                                                                                                                                                                                                   |
| [pattern = pattern.Replace([\"#\"], [\"\[#\]\"]);]                                                                            |
|                                                                                                                                                                                                                   |
| [pattern = pattern.Replace([\"\*\"], [\"\[\*\]\"]);]                                                                          |
|                                                                                                                                                                                                                   |
| [pattern = pattern.Replace([\"?\"], [\"\[?\]\"]);]                                                                            |
|                                                                                                                                                                                                                   |
| [return][ pattern;]                                                                                                          |
|                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] Form1_Load([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                         |
| [Dim][ rank [As] [New] ArrayList()]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                         |
| [Dim][ rankData [As] [New] RankData([\"aaa\"])]                                                                                                  |
|                                                                                                                                                                                                                                                                                                         |
| [rank.Add(rankData)]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                         |
| [rankData = [New] RankData([\"bbb#\"])]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                         |
| [rank.Add(rankData)]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                         |
| [gridGroupingControl1.DataSource = rank]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                         |
| [Dim][ filter [As] [String] = [\"\"]]                                                                                                            |
|                                                                                                                                                                                                                                                                                                         |
| [Dim][ rfd [As] RecordFilterDescriptor = [Nothing]]                                                                                                                      |
|                                                                                                                                                                                                                                                                                                         |
| [Dim][ r [As] Record = [Nothing]]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| [For][ [Each] a [As] RankData [In] rank]                                                                                                            |
|                                                                                                                                                                                                                                                                                                         |
| [filter = [\"\[WellName\] like \'\"] & ReplaceSpcChar(a.WellName) & [\"\'\"]]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                         |
| [rfd = [New] RecordFilterDescriptor(filter)]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                         |
| [gridGroupingControl1.TableDescriptor.RecordFilters.Add(rfd)]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                         |
| [Dim][ cont [As] [Integer] = gridGroupingControl1.Table.FilteredRecords.Count]                                                                                           |
|                                                                                                                                                                                                                                                                                                         |
| [r = [New] Record(gridGroupingControl1.Table)]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                         |
| [\' Exception will be thrown here if special characters are not enclosed in square brackets.]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                         |
| [r = gridGroupingControl1.Table.FilteredRecords(0)]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| [rankData = [TryCast](r.GetData(), RankData)]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                         |
| [gridGroupingControl1.TableDescriptor.RecordFilters.Clear()]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                         |
| [Next][ a]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| [Private][ [Function] ReplaceSpcChar([ByVal] pattern [As] [String]) [As] [String]]   |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [\' Take caution while replacing the pattern and ensure that only the intended pattern is modified.]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                         |
| [pattern = pattern.Replace([\"\[\"], [\"\[\[\]\"])]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| [pattern = pattern.Replace([\"#\"], [\"\[#\]\"])]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                         |
| [pattern = pattern.Replace([\"\*\"], [\"\[\*\]\"])]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| [pattern = pattern.Replace([\"?\"], [\"\[?\]\"])]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                         |
| [Return][ pattern]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| [End][ [Function]]                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


[{border="0"}]Note: The \'Like\' operator here is implemented similar to the 'Like' operator in VB.NET, where "#" character is considered as a character in patterns. Refer http://msdn.microsoft.com/en-us/library/swf8kaxw.aspx for detailed information.


[] 

Clearing Filters

[] 

Row Filters that are added for a table can be cleared by calling the Clear() method of the RecordFilters property.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| []                                                                                                      |
|                                                                                                                                                                                           |
| [this][.gridGroupingControl1.TableDescriptor.RecordFilters.Clear();] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                     |
|                                                                                                                                                                                        |
| []                                                                                                                                               |
|                                                                                                                                                                                        |
| [Me][.gridGroupingControl1.TableDescriptor.RecordFilters.Clear()] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


[{border="0"}]Note: For more details, refer the following browser sample:

 

\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Filters and Expressions\\Filtering Tutorial


 

[]{#p434} 

 

4.3.4.3.4.2.1      Filter Bar

[] 

Grouping Grid provides in-built support for displaying a **Filter Bar** across the columns. It can be used to filter and unfilter the records at run time. It is very user interactive and more advantageous than using the RecordFilters collection. The main reason for its wide usage is that it could display various filter options for the columns. You can be able to add your own filter criteria too.

 

When filter bar is applied, a new row (Filter Row) will be added at the top of the table displaying the filter options for the columns in a drop down. Each cell in the filter bar row is a simple ComboBox cell whose items are the filter options. The filter options for a given column includes one entry for each value in that column.

[] 

**Setting up a Filter Bar**

 

The Filter Bar can be enabled by setting the ShowFilterBar and AllowFilter properties to true. The AllowFilter property can be set for the columns that require filter options.

 

Given below is the code to set the filter for all the columns in the main table.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                    |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                   |
| [// Show Filter Bar for the main table.]                                                                                                                        |
|                                                                                                                                                                                                                   |
| [this][.gridGroupingControl1.TopLevelGroupOptions.ShowFilterBar = [true];]                              |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [// Change the appearance of the Filter Row.]                                                                                                                   |
|                                                                                                                                                                                                                   |
| [this][.gridGroupingControl1.TableDescriptor.Appearance.FilterBarCell.BackColor = [Color].CornSilk;] |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [// Enable filter for all columns.]                                                                                                                             |
|                                                                                                                                                                                                                   |
| [for][ ([int] i = 0; i \< gridGroupingControl1.TableDescriptor.Columns.Count; i++)]                     |
|                                                                                                                                                                                                                   |
| [gridGroupingControl1.TableDescriptor.Columns\[i\].AllowFilter = [true];]                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                |
|                                                                                                                                                                                   |
| []                                                                                                                              |
|                                                                                                                                                                                   |
| [\' Show Filter Bar for the main table.]                                                                                        |
|                                                                                                                                                                                   |
| [Me][.gridGroupingControl1.TopLevelGroupOptions.ShowFilterBar = [True]] |
|                                                                                                                                                                                   |
| []                                                                                                                               |
|                                                                                                                                                                                   |
| [\' Change the appearance of the Filter Row .           ]                                                                       |
|                                                                                                                                                                                   |
| [ [Me].gridGroupingControl1.TableDescriptor.Appearance.FilterBarCell.BackColor = Color.AliceBlue]                        |
|                                                                                                                                                                                   |
| [                ]                                                                                                                            |
|                                                                                                                                                                                   |
| [\' Enable the filter for all columns.]                                                                                         |
|                                                                                                                                                                                   |
| [Dim][ i [As] [Integer] = 0]                       |
|                                                                                                                                                                                   |
| [Do][ [While] i \< gridGroupingControl1.TableDescriptor.Columns.Count]  |
|                                                                                                                                                                                   |
| [gridGroupingControl1.TableDescriptor.Columns(i).AllowFilter = [True]]                                                   |
|                                                                                                                                                                                   |
| [i += 1]                                                                                                                                      |
|                                                                                                                                                                                   |
| [Loop]                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Through Designer

[] 

A filter bar can also be added at design time by setting the above properties through the property window of the grouping grid. The designer settings shown below adds the filter for the columns CompanyName and ContactTitle.

[] 

{border="0"}

[] 

*[Figure ][301][: Setting ShowFilterBar Property]*

[] 

{border="0"}

[] 

*[Figure ][302][: AllowFilter property enabled by using the GridColumnDescriptor Collection Editor]*

**[]** 

Setting AllowFilter property for the column CompanyName

[] 

Here is a sample screen shot that shows the filter bar with filters enabled for the columns CompanyName and ContactTitle. The records are filtered against the filter condition ContactTitle = \'Sales Representative\'. The image also shows the filter options for the column CompanyName.

**[]** 

{border="0"}

***[]*** 

*[Figure ][303][: FilterBars added for \"CompanyName\" and \"ContactTitle\" Columns]*

[] 

While enabling the FilterBar, it automatically adds up an option for showing **All** records and a **Custom** option. Clicking the Custom option will open the RecordFilterDescriptor collection editor wherein you can edit the filter conditions or add any more filters you want. The following screen shot illustrates this process.

[] 

{border="0"}

[] 

*[Figure ][304][: Editing Filter Conditions by using the RecordFilterDescriptor Collection Editor]*

[] 

NestedTables and NestedGroups

[] 

AutoFilterRow can also be added to the nested tables and groups. To turn on the Filter Bar for the Nested Tables, set the property ShowFilterBar under NestedTableGroupOptions. For all the groups, ShowFilterBar under ChildGroupOptions need to be set to true.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                       |
| [// Show Filter Bar for the child tables.]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                       |
| [this][.gridGroupingControl1.NestedTableGroupOptions.ShowFilterBar = ][true][;] |
|                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                       |
| [// Show Filter Bar for the groups.]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                       |
| [this][.gridGroupingControl1.ChildGroupOptions.ShowFilterBar = ][true][;]       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                           |
|                                                                                                                                                                                                              |
| []                                                                                                                                                         |
|                                                                                                                                                                                                              |
| [\' Show Filter Bar for the child tables.]                                                                                                                 |
|                                                                                                                                                                                                              |
| [Me][.gridGroupingControl1.[NestedTableGroupOptions].ShowFilterBar = [True]] |
|                                                                                                                                                                                                              |
| []                                                                                                                                                          |
|                                                                                                                                                                                                              |
| [\' Show Filter Bar for the groups.]                                                                                                                       |
|                                                                                                                                                                                                              |
| [Me][.gridGroupingControl1.[ChildGroupOptions].ShowFilterBar = [True]]       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: For more details, refer the following browser sample:

 

\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Filters and Expressions\\Filter Bar Demo


 

[]{#p435} 

 

4.3.4.3.4.2.2      Dynamic Filter

[] 

Dynamic Filter serves as good replacement for the default Filter Bar, which provides advanced filtering capabilities. It is available as an add-on feature for Essential Grid, and is built on the foundation of the regular filter bar with added provisions to support dynamic filtering, user-friendliness, and so on.

 

The dynamic filter can be used with Nested Tables and Nested Groups too. To make it more interactive, it adds a Filter Button at the right-most corner of every Filter Bar Cell, on clicking, which drops down into a list showing the available comparative operators. On hovering any filter bar cell, a filter icon is displayed, indicating whether a filter is applied to that particular column or not. The key feature of the dynamic filtering mechanism is that it allows you to view the filter results as you type each and every character. It supports user-defined filter criteria as well.

 

**Set up Dynamic Filter**

 

The dynamic filter is defined in the GridDynamicFilter class, which exposes two public methods, **WireGrid** and **UnwireGrid**, in order to hook up and unhook the dynamic filter with the desired grid.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                              |
|                                                                                                                                                                                             |
| []                                                                                                                                        |
|                                                                                                                                                                                             |
| [GridDynamicFilter][ f = [new] [GridDynamicFilter]();] |
|                                                                                                                                                                                             |
| [if][ (showDynamicFilter)]                                                                             |
|                                                                                                                                                                                             |
| [{]                                                                                                                                                     |
|                                                                                                                                                                                             |
| [f.WireGrid(gridGroupingControl1);]                                                                                                                     |
|                                                                                                                                                                                             |
| [}]                                                                                                                                                     |
|                                                                                                                                                                                             |
| [else]                                                                                                                                     |
|                                                                                                                                                                                             |
| [f.UnWireGrid(gridGroupingControl1);]                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                          |
|                                                                                                                                                                                             |
| []                                                                                                                                        |
|                                                                                                                                                                                             |
| [Dim][ f [As] GridDynamicFilter = [New] GridDynamicFilter()] |
|                                                                                                                                                                                             |
| [If][ showDynamicFilter [Then]]                                                   |
|                                                                                                                                                                                             |
| [f.WireGrid(gridGroupingControl1)]                                                                                                                      |
|                                                                                                                                                                                             |
| [Else]                                                                                                                                     |
|                                                                                                                                                                                             |
| [f.UnWireGrid(gridGroupingControl1)]                                                                                                                    |
|                                                                                                                                                                                             |
| [End][ [If]]                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Sample Output

 

Below image illustrates a sample output.

[] 

{border="0"}

[] 

*[Figure ][305][: Dynamic Filter]*

[] 


{border="0"}Note: For more details, refer the following browser sample:

 

\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Filters and Expressions\\Dynamic Filter Demo


 

[]{#p436}4.3.4.3.4.2.2.1    Localization Support for CompareOperatorListBox

 

The dynamic filter in the GridGrouping control provides support to customize the display content of the static element. Using this you can localize the static elements in the compare operator list box.

 

Use Case Scenarios

With this feature, you can localize the options in the compare operator list box to display the language specific to your locale.

 

Sample Link

A demo of this feature is available in the following location:

 

***{Installed Path}\\Syncfusion\\EssentialStudio\\x.x.x.x\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Filters and Expressions\\Dynamic Filter Demo***

**** 

Adding Localization Support for CompareOperatorListBox

To localize the content, create a class file and add an interface as *ILocalizationProvider*. Assign the required content to be displayed to the *DynamicFilterResourceIdentifiers* of the *GetLocalizedString* method as illustrated in the following code:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                          |
| [public][ [string] GetLocalizedString(System.Globalization.[CultureInfo] culture, [string] name)] |
|                                                                                                                                                                                                                                                          |
| [        {]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                          |
| [            [if] (str == [\"True\"])]                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [            {]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                          |
| [                [switch] (name)]                                                                                                                                                               |
|                                                                                                                                                                                                                                                          |
| [                {]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [                    #region][ Menu Package]                                                                                                                        |
|                                                                                                                                                                                                                                                          |
| [                    [case] DynamicFilterResourceIdentifiers.StartsWith:]                                                                                                                       |
|                                                                                                                                                                                                                                                          |
| [                        [return] [\"empieza con\"];]                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [                    [case] DynamicFilterResourceIdentifiers.EndsWith:]                                                                                                                         |
|                                                                                                                                                                                                                                                          |
| [                        [return] [\"termina con\"];]                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [                    [case] DynamicFilterResourceIdentifiers.Equals:]                                                                                                                           |
|                                                                                                                                                                                                                                                          |
| [                        [return] [\"es igual a\"];]                                                                                                                    |
|                                                                                                                                                                                                                                                          |
| [                    [case] DynamicFilterResourceIdentifiers.GreaterThan:]                                                                                                                      |
|                                                                                                                                                                                                                                                          |
| [                        [return] [\"mayor que\"];]                                                                                                                     |
|                                                                                                                                                                                                                                                          |
| [                    [case] DynamicFilterResourceIdentifiers.GreaterThanOrEqualTo:]                                                                                                             |
|                                                                                                                                                                                                                                                          |
| [                        [return] [\"Mayor o igual a\"];]                                                                                                               |
|                                                                                                                                                                                                                                                          |
| [                    [case] DynamicFilterResourceIdentifiers.LessThan:]                                                                                                                         |
|                                                                                                                                                                                                                                                          |
| [                        [return] [\"menos que\"];]                                                                                                                     |
|                                                                                                                                                                                                                                                          |
| [                    [case] DynamicFilterResourceIdentifiers.LessThanOrEqualTo:]                                                                                                                |
|                                                                                                                                                                                                                                                          |
| [                        [return] [\"Menor o igual a\"];]                                                                                                               |
|                                                                                                                                                                                                                                                          |
| [                    [case] DynamicFilterResourceIdentifiers.Like:]                                                                                                                             |
|                                                                                                                                                                                                                                                          |
| [                        [return] [\"como\"];]                                                                                                                          |
|                                                                                                                                                                                                                                                          |
| [                    [case] DynamicFilterResourceIdentifiers.Match:]                                                                                                                            |
|                                                                                                                                                                                                                                                          |
| [                        [return] [\"partido\"];]                                                                                                                       |
|                                                                                                                                                                                                                                                          |
| [                    [case] DynamicFilterResourceIdentifiers.NotEquals:]                                                                                                                        |
|                                                                                                                                                                                                                                                          |
| [                        [return] [\"no es igual\"];]                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [                    [case] DynamicFilterResourceIdentifiers.ExpressionMATCH:]                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [                        [return] [\"expresión de coincidencia\"];]                                                                                                     |
|                                                                                                                                                                                                                                                          |
| [                    #endregion][]                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [                    [default]:]                                                                                                                                                                |
|                                                                                                                                                                                                                                                          |
| [                        [return] [string].Empty;]                                                                                                                         |
|                                                                                                                                                                                                                                                          |
| [                }]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [            }]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                          |
| [            [else] ]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                          |
| [            {]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                          |
| [                [switch] (name)]                                                                                                                                                               |
|                                                                                                                                                                                                                                                          |
| [                {]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [                    #region][ Menu Package]                                                                                                                        |
|                                                                                                                                                                                                                                                          |
| [                    [case] DynamicFilterResourceIdentifiers.StartsWith:]                                                                                                                       |
|                                                                                                                                                                                                                                                          |
| [                        [return] [\"StartsWith\"];]                                                                                                                    |
|                                                                                                                                                                                                                                                          |
| [                    [case] DynamicFilterResourceIdentifiers.EndsWith:]                                                                                                                         |
|                                                                                                                                                                                                                                                          |
| [                        [return] [\"EndsWith\"];]                                                                                                                      |
|                                                                                                                                                                                                                                                          |
| [                    [case] DynamicFilterResourceIdentifiers.Equals:]                                                                                                                           |
|                                                                                                                                                                                                                                                          |
| [                        [return] [\"Equals\"];]                                                                                                                        |
|                                                                                                                                                                                                                                                          |
| [                    [case] DynamicFilterResourceIdentifiers.GreaterThan:]                                                                                                                      |
|                                                                                                                                                                                                                                                          |
| [                        [return] [\"GreaterThan\"];]                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [                    [case] DynamicFilterResourceIdentifiers.GreaterThanOrEqualTo:]                                                                                                             |
|                                                                                                                                                                                                                                                          |
| [                        [return] [\"GreaterThanOrEqualTo\"];]                                                                                                          |
|                                                                                                                                                                                                                                                          |
| [                    [case] DynamicFilterResourceIdentifiers.LessThan:]                                                                                                                         |
|                                                                                                                                                                                                                                                          |
| [                        [return] [\"LessThan\"];]                                                                                                                      |
|                                                                                                                                                                                                                                                          |
| [                    [case] DynamicFilterResourceIdentifiers.LessThanOrEqualTo:]                                                                                                                |
|                                                                                                                                                                                                                                                          |
| [                        [return] [\"LessThanOrEqualTo\"];]                                                                                                             |
|                                                                                                                                                                                                                                                          |
| [                    [case] DynamicFilterResourceIdentifiers.Like:]                                                                                                                             |
|                                                                                                                                                                                                                                                          |
| [                        [return] [\"Like\"];]                                                                                                                          |
|                                                                                                                                                                                                                                                          |
| [                    [case] DynamicFilterResourceIdentifiers.Match:]                                                                                                                            |
|                                                                                                                                                                                                                                                          |
| [                        [return] [\"Match\"];]                                                                                                                         |
|                                                                                                                                                                                                                                                          |
| [                    [case] DynamicFilterResourceIdentifiers.NotEquals:]                                                                                                                        |
|                                                                                                                                                                                                                                                          |
| [                        [return] [\"NotEquals\"];]                                                                                                                     |
|                                                                                                                                                                                                                                                          |
| [                    [case] DynamicFilterResourceIdentifiers.ExpressionMATCH:]                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [                        [return] [\"ExpressionMATCH\"];]                                                                                                               |
|                                                                                                                                                                                                                                                          |
| [                    #endregion][]                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [                    [default]:]                                                                                                                                                                |
|                                                                                                                                                                                                                                                          |
| [                        [return] [string].Empty;]                                                                                                                         |
|                                                                                                                                                                                                                                                          |
| [                }]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [            }]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                          |
| [        }]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Public][ [Function] GetLocalizedString([ByVal] culture [As] System.Globalization.CultureInfo, [ByVal] name [As] [String]) [As] [String]] |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                  [If] str = [\"True\"] [Then]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                        [Select] [Case] name]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\'                             #Region \"Menu Package\"][]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] DynamicFilterResourceIdentifiers.StartsWith]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [\"empieza con\"]]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] DynamicFilterResourceIdentifiers.EndsWith]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [\"termina con\"]]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] DynamicFilterResourceIdentifiers.Equals]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [\"es igual a\"]]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] DynamicFilterResourceIdentifiers.GreaterThan]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [\"mayor que\"]]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] DynamicFilterResourceIdentifiers.GreaterThanOrEqualTo]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [\"Mayor o igual a\"]]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] DynamicFilterResourceIdentifiers.LessThan]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [\"menos que\"]]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] DynamicFilterResourceIdentifiers.LessThanOrEqualTo]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [\"Menor o igual a\"]]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] DynamicFilterResourceIdentifiers.Like]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [\"como\"]]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] DynamicFilterResourceIdentifiers.Match]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [\"partido\"]]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] DynamicFilterResourceIdentifiers.NotEquals]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [\"no es igual\"]]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] DynamicFilterResourceIdentifiers.ExpressionMATCH]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [\"expresión de coincidencia\"]]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\'                             #End Region][]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] [Else]]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [String].Empty]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                        [End] [Select]]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                  [Else]]                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                        [Select] [Case] name]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\'                             #Region \"Menu Package\"][]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] DynamicFilterResourceIdentifiers.StartsWith]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [\"StartsWith\"]]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] DynamicFilterResourceIdentifiers.EndsWith]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [\"EndsWith\"]]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] DynamicFilterResourceIdentifiers.Equals]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [\"Equals\"]]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] DynamicFilterResourceIdentifiers.GreaterThan]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [\"GreaterThan\"]]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] DynamicFilterResourceIdentifiers.GreaterThanOrEqualTo]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [\"GreaterThanOrEqualTo\"]]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] DynamicFilterResourceIdentifiers.LessThan]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [\"LessThan\"]]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] DynamicFilterResourceIdentifiers.LessThanOrEqualTo]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [\"LessThanOrEqualTo\"]]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] DynamicFilterResourceIdentifiers.Like]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [\"Like\"]]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] DynamicFilterResourceIdentifiers.Match]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [\"Match\"]]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] DynamicFilterResourceIdentifiers.NotEquals]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [\"NotEquals\"]]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] DynamicFilterResourceIdentifiers.ExpressionMATCH]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [\"ExpressionMATCH\"]]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\'                             #End Region][]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                              [Case] [Else]]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                                    [Return] [String].Empty]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                        [End] [Select]]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                  [End] [If]]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [Function]]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{#_x0000_i1259 border="0" width="246" height="200"}

Figure 306: Localized CompareOperatorListBox

[] 

 

 

4.3.4.3.4.2.3      Working with Filters

[] 

This section deals with different options to process the filter rows.

 

**Accessing FilteredRecords**

 

If you want to work with the subset of the records being filtered from a grid table, then you can use FilteredRecords collection for that table. This is a read only collection that manages the subset of records that has been filtered against a filter criteria.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                                     |
| []                                                                                                                |
|                                                                                                                                                                     |
| [GridTable][ table = [this].grid.Table;]               |
|                                                                                                                                                                     |
| [foreach][ (Record frec [in] table.FilteredRecords)]      |
|                                                                                                                                                                     |
| [{]                                                                                                                             |
|                                                                                                                                                                     |
| [Console][.WriteLine([\"Record Info : \"] + frec);] |
|                                                                                                                                                                     |
| [}]                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                             |
|                                                                                                                                                                                                                |
| []                                                                                                                                                           |
|                                                                                                                                                                                                                |
| [Private][ table [As] GridTable = [Me].grid.Table]                              |
|                                                                                                                                                                                                                |
| [For][ [Each] frec [As] Record [In] table.FilteredRecords] |
|                                                                                                                                                                                                                |
| [Console.WriteLine([\"Record Info : \"] & frec)]                                                                                                   |
|                                                                                                                                                                                                                |
| [Next][ frec]                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Accessing the FilterBarString

[] 

To get access to the FilteredString, you can use the GetFilterBarText of the FilterBarCellRenderer. Following code example illustrates how to print the filter bar string for a given column.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                     |
| [private][ [void] GetFilterBarString()]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    [int] row = 0, col=0;]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    [string] colName = [null]; ]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    [GridTableCellStyleInfo] style;]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    [// Ensure the filter bar is visible and RecordFilters collection is not empty,]]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    [// and get the filter bar row index and index of the field, by using the value with which]]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    [// the grid records are filtered.]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    [if](gridGroupingControl1.TableDescriptor.RecordFilters.Count \> 0)]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    colName = gridGroupingControl1.TableDescriptor.RecordFilters\[0\].MappingName;]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    [foreach] (Element el [in] [this].gridGroupingControl1.Table.DisplayElements)]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    {]                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                     |
| [        [if] (el.IsFilterBar() && colName != [null])]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                     |
| [            style = gridGroupingControl1.Table.GetTableCellStyle(el, colName);]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                     |
| [            row = style.TableCellIdentity.RowIndex;]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                     |
| [            col = style.TableCellIdentity.ColIndex;]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    }]                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    [// By using the calculated row and column indices, get the filter bar string of the record filter.]]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    [GridTableFilterBarCellRenderer] cr = [this].gridGroupingControl1.TableControl.CellRenderers\[[\"FilterBarCell\"]\] [as] [                             GridTableFilterBarCellRenderer];] |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    [if] (cr != [null] && row != 0)]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    {]                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                     |
| [         [Console].WriteLine(cr.GetFilterBarText([this].gridGroupingControl1.TableModel\[row, col\]));]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    }]                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] GetFilterBarString()]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                            |
| [Dim][ row [As] [Integer] = 0, col [As] [Integer] = 0]                                                                                            |
|                                                                                                                                                                                                                                                                                                                            |
| [Dim][ colName [As] [String] = [Nothing]]                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                            |
| [Dim][ style [As] GridTableCellStyleInfo]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                            |
| [\' Ensure the filter bar is visible and RecordFilters collection is not empty,]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                            |
| [\' and get the filter bar row index and index of the field, by using the value with which]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                            |
| [\' the grid records are filtered.]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                            |
| [If][ gridGroupingControl1.TableDescriptor.RecordFilters.Count \> 0 [Then]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                            |
| [colName = gridGroupingControl1.TableDescriptor.RecordFilters(0).MappingName]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                            |
| [End][ [If]]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                            |
| [For][ [Each] el [As] Element [In] [Me].gridGroupingControl1.Table.DisplayElements]                                                               |
|                                                                                                                                                                                                                                                                                                                            |
| [If][ el.IsFilterBar() [AndAlso] [Not] colName [Is] [Nothing] [Then]]                                                        |
|                                                                                                                                                                                                                                                                                                                            |
| [style = gridGroupingControl1.Table.GetTableCellStyle(el, colName)]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                            |
| [row = style.TableCellIdentity.RowIndex]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                            |
| [col = style.TableCellIdentity.ColIndex]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                            |
| [End][ [If]]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                            |
| [Next][ el]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                            |
| [  \' By using the calculated row and column indices, get the filter bar string of the record filter.]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                            |
| [Dim][ cr [As] GridTableFilterBarCellRenderer = TryCast([Me].gridGroupingControl1.TableControl.CellRenderers([\"FilterBarCell\"]), GridTableFilterBarCellRenderer)] |
|                                                                                                                                                                                                                                                                                                                            |
| [If][ [Not] cr [Is] [Nothing] [AndAlso] row \<\> 0 [Then]]                                                                   |
|                                                                                                                                                                                                                                                                                                                            |
| [Console.WriteLine(cr.GetFilterBarText([Me].gridGroupingControl1.TableModel(row, col)))]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                            |
| [End][ [If]]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p437} 

 

4.3.4.3.4.2.4      Filter By DisplayMember

[] 

Grid Grouping control filters the data records by the value member of the columns by default. This behavior can be customized to get the filters work with display member of the columns. This is accomplished in the Filter By DisplayMember feature.

 

**Implementation**

 

The implementation includes the following classes.

[] 

[·      ]**GroupingGridFilterBarExt** - It derives a custom filter bar cell type named FilterByDisplayMemberCell and use this cell type in the place of default filter bar cell.

[·      ]**GridFilterByDisplayMemberCellModel** - This is the cell model class that loads the filter drop down with the display strings of the respective filter bar column and creates cell renderer.

[·      ]**GridFilterByDisplayMemberCellRenderer** - This is the cell renderer class that sets up the actual filter string by replacing the display string with the value string.

[] 

Following code example illustrates how to enable/disable this custom filter.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                    |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [// Enable filter.]                                                                                                                                             |
|                                                                                                                                                                                                                   |
| [GroupingGridFilterBarExt][ gGCFilter = [new] [GroupingGridFilterBarExt]();] |
|                                                                                                                                                                                                                   |
| [gGCFilter.WireGrid(gridGroupingControl1);]                                                                                                                                   |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [// Disable filter.]                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [gGCFilter.UnwireGrid(gridGroupingControl1);]                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [\' Enable filter.]                                                                                                                                             |
|                                                                                                                                                                                                                   |
| [Dim][ gGCFilter [As] GroupingGridFilterBarExt = [New] GroupingGridFilterBarExt()] |
|                                                                                                                                                                                                                   |
| [gGCFilter.WireGrid(gridGroupingControl1)]                                                                                                                                    |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [\' Disable filter.]                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [gGCFilter.UnwireGrid(gridGroupingControl1)]                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][307][: Filtering By Display Member]*

[] 


 

{border="0"}Note: For more details, refer the following browser sample:

 

\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Filters and Expressions\\Filter By DisplayMember Demo


 

[]{#p438} 

 

[]{#_List_of_Filter}4.3.4.3.4.2.5      List of Filter Expressions

[] 

Filter expressions can be set and added to RecordFilters collection through a textual string. The string should abide by the syntax to be followed and should be valid.

 

The following table lists tokens used, (Expression Filters) and their descriptions.

[] 

[] 


+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Syntax                | Expression                                             | Description                                                                                                                            |
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| \*                    | \[columnname\] \* \'anynumber\'                        | Filters grid based on the multiplied value computed.                                                                                   |
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| /                     | \[columnname\] / \'anynumber\'                         | Filters grid based on the divided value computed.                                                                                      |
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| \+                    | \[columnname\] + \'anynumber\'                         | Filters grid based on the result computed.                                                                                             |
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| \-                    | \[columnname\] -- \'anynumber\'                        | Filters grid based on computed value.                                                                                                  |
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| \<                    | \[columnname\] \< \'anynumber\'                        | Filters grid displaying records whose specified column holds value lesser than the mentioned value.                                    |
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| \>                    | \[columnname\] \> \'anynumber\'                        | Filters grid displaying records whose specified column holds value greater than the mentioned value.                                   |
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| =                     | \[columnname\] = \'value\'                             | Filters grid displaying records whose specified column holds value equal to the mentioned value.                                       |
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| \<=                   | \[columnname\] \<= \'anynumber\'                       | Filters grid displaying records whose specified column holds value lesser than or equal to the mentioned value.                        |
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| \>=                   | \[columnname\] \>= \'anynumber\'                       | Filters grid displaying records whose specified column holds value greater than or equal to the mentioned value.                       |
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| \<\>                  | 
|                       |   -------------------------------                      |                                                                                                                                        |
|                       |   \[columnname\] \<\> \'value\'                        |                                                                                                                                        |
|                       |   -------------------------------                      |                                                                                                                                        |
|                       | 
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| AND                   | \[expression1\] AND \[expression2\] AND\[expression\]  | Filters grid displaying records that meet criteria of all the expressions.                                                             |
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| OR                    | \[expression1\] OR \[expression2\] OR\[expression\]    | Filters grid displaying records that meet criteria of either or all the expressions.                                                   |
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| XOR                   | \[expression1\] XOR \[expression2\] XOR \[expression\] | Filters grid displaying records that doesn\'t meet criteria of either or all the expressions.                                          |
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| LIKE                  | \[columnname\] LIKE \'value\'                          | Filters grid displaying records whose specified column holds value equal to the mentioned value(irrespective of character casing).     |
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| MATCH                 | \[columnname\] MATCH \'value\'                         | Filters grid displaying records whose specified column holds whole or a part of the mentioned value(irrespective of character casing). |
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| BETWEEN               | \[columnname\] BETWEEN {date1,date2}                   | Filters grid displaying records whose date lies between the two dates irrespective of the time.                                        |
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| BETWEENTIME           | \[columnname\] BETWEENTIME  {datetime1,datetime2}      | Filters grid displaying records whose datetimevalue lies between the two dates and respective times.                                   |
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| IN                    | \[columnname\] IN \'val1,val2,..,valn\'                | Filters grid displaying records whose specified column hold the values mentioned.                                                      |
+-----------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+


[] 

 

[]{#p439} 

[]{#related-topics}

