---
title: expressions1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\expressions1.md
created_at: 2025-07-03
---








  









### Expressions {#expressions style="tab-stops: 0pt"}

 

You can add new properties to your data object that are algebraic expressions involving other properties of the object.

 

To add an expression, you need to create an **ExpressionFieldDescriptor** and add it to the **Engine.TableDescriptor.Expression.Fields** collection. Here we illustrate this process by adding an expression that computes 2.1 times the value of property B plus 3.2.

[] 

1    In the Console Application, comment out all the code that is in the **Main** method and add this code to create a data object and set it into the **GroupingEngine**.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                            |
| [// Create an arraylist of random MyObjects.]                                                                                                                                            |
|                                                                                                                                                                                                                                            |
| [ArrayList list = ][new][ ArrayList();]                                               |
|                                                                                                                                                                                                                                            |
| [Random r = ][new][ Random();]                                                        |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [for][(][int][ i = 0; i \< 10; i++)] |
|                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                            |
| [     list.Add(][new][ MyObject(r.Next(5)));]                                         |
|                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [// Create a Grouping.Engine object.]                                                                                                                                                    |
|                                                                                                                                                                                                                                            |
| [Engine groupingEngine = ][new][ Engine();]                                           |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [// Set its datasource.]                                                                                                                                                                 |
|                                                                                                                                                                                                                                            |
| [groupingEngine.SetSourceList(list);]                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                  |
| [\' Create an arraylist of random MyObjects.]                                                                                                                                                  |
|                                                                                                                                                                                                                                                  |
| [Dim][ list ][As New][ ArrayList()]        |
|                                                                                                                                                                                                                                                  |
| [Dim][ r ][As New][ Random()]              |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                  |
| [Dim][ i ][As Integer]                                                                       |
|                                                                                                                                                                                                                                                  |
| [For][ i = 0 ][To][ 10]                    |
|                                                                                                                                                                                                                                                  |
| [    list.Add(][New][ MyObject(r.Next(5)))]                                                 |
|                                                                                                                                                                                                                                                  |
| [Next]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                  |
| [\' Create a Grouping.Engine object.]                                                                                                                                                          |
|                                                                                                                                                                                                                                                  |
| [Dim][ groupingEngine][ As New][ Engine()] |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                  |
| [\' Set its datasource.]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                  |
| [groupingEngine.SetSourceList(list)]                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2    Now you must add code to list the data, add an expression property and then display the value of the expression. To retrieve the value, you must use the **Record.GetValue** method by passing it as the name of the expression that you had assigned when it was created.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                           |
| [// Display the data before filtering.]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                           |
| [foreach][(Record rec ][in][ groupingEngine.Table.FilteredRecords)]                 |
|                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                           |
| [        MyObject obj = rec.GetData() ][as][ MyObject;]                                                                              |
|                                                                                                                                                                                                                                                                                           |
| [        ][if][(obj != ][null][)] |
|                                                                                                                                                                                                                                                                                           |
| [        {]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                           |
| [            Console.WriteLine(obj);]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                           |
| [        }]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                           |
| [// Pause]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                           |
| [Console.ReadLine(); ]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                           |
| [       ][ // Add an expression property.]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                           |
| [ExpressionFieldDescriptor efd = ][new][ ExpressionFieldDescriptor(\"MultipleOfB\", \"2.1 \* \[B\] + 3.2\");]                        |
|                                                                                                                                                                                                                                                                                           |
| [        groupingEngine.TableDescriptor.ExpressionFields.Add(efd);]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                           |
| [// Display the data after adding the field.]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                           |
| [foreach][(Record rec ][in][ groupingEngine.Table.FilteredRecords)]                 |
|                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                           |
| [        Console.WriteLine(rec.GetValue(\"MultipleOfB\"));]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                           |
| [// Pause]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                           |
| [Console.ReadLine(); ]                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\' Display the data before filtering.]                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Dim][ rec ][As ][Record]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [For Each][ rec ][In][ groupingEngine.Table.FilteredRecords]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    ][Dim][ obj ][As][ MyObject = ][CType][(rec.GetData(), MyObject)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [   ][ If Not][ (obj ][Is Nothing][) ][Then]                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [       Console.WriteLine(obj)]                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [   ][ End If]                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Next][ rec]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\' Pause]                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Console.ReadLine() ]                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\                                                                                                                                                                                                                                                                                                                                                                                                                                |
| \' Add an expression property.]                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Dim][ efd][ As New][ ExpressionFieldDescriptor(\"MultipleOfB\", \"2.1 \* \[B\] + 3.2\")]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [groupingEngine.TableDescriptor.ExpressionFields.Add(efd)]                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\' Display the data after adding the field.]                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [For][ ][Each][ rec ][In][ groupingEngine.Table.FilteredRecords]                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    Console.WriteLine(rec.GetValue(\"MultipleOfB\"))]                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Next][ rec]                                                                                                                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 19: Screen Showing the Initial Data Followed by Values Computed Using the Expression 2.1 \* \[B\] + 3.2

[]{#related-topics}

