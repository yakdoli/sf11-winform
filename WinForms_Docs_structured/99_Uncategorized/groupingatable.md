---
title: groupingatable.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\groupingatable.md
created_at: 2025-07-03
---








  









### Grouping a Table {#grouping-a-table style="tab-stops: 0pt"}

 

In this lesson, you will start working with the **Grouping.Engine** object to see how to apply a grouping to the data as well as summarize the data. In the  section, you used the **grouping.Engine.Table.Records** collection to access the data in the Grouping.Engine object. The **grouping.Engine.Table** property is the property of the Grouping.Engine that holds the actual data needed by Essential Grouping.

[] 

[You will now look at the property that holds the schema information that is associated with the data, i.e., the **grouping.Engine.TableDescriptor** property. For example, the **TableDescriptor.Columns** property holds a collection of ColumnDescriptor objects that define the schema information on the columns in the data. ]

[] 


Note: Here, the columns correspond to the public properties in our sample MyObject class, A, B, C, and D.


[] 

We will now continue using the same sample created in the  section and add the corresponding code at the bottom of the Main method.

[] 

1.   To group the \'MyObject\' ArrayList by a particular property, say property C, you have to add only the property name (\"C\") to the **grouping.Engine.TableDescriptor.GroupedColumns** collections. Add the following code snippet to the bottom of the **Main** method.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                          |
| [// Group on property C.]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                          |
| [groupingEngine.TableDescriptor.GroupedColumns.Add(\"C\");]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                          |
| [        ]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                          |
| [// Display the records in the engine after grouping.]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                          |
| [foreach][(Record rec ][in][ groupingEngine.Table.Records)]                        |
|                                                                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                          |
| [       MyObject obj = rec.GetData() ][as][ MyObject;]                                                                              |
|                                                                                                                                                                                                                                                                                          |
| [       ][if][(obj != ][null][)] |
|                                                                                                                                                                                                                                                                                          |
| [       {]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                          |
| [         Console.WriteLine(obj);]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                          |
| [       }]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\' Group on property C.]                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [groupingEngine.TableDescriptor.GroupedColumns.Add(\"C\")]                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\' Display the records in the engine after grouping.]                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [For Each][ rec ][In][ groupingEngine.Table.Records]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    ][Dim][ obj ][As][ MyObject = ][CType][(rec.GetData(), MyObject)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    ][If Not][ (obj ][Is Nothing][) ][Then]                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [           Console.WriteLine(obj)]                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [   ][ End If]                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Next][ rec]                                                                                                                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   After running the code from step 1, a screen similar to the one below will be displayed. Note that the bottom list displayed is now sorted by **column C**. This is a one side effect of grouping by column C.

[] 

[] 

{border="0"}

Figure 14: Display After Grouping by Property C

More:





