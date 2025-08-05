---
title: iteratingthroughthedata.md
original_path: WinForms_Docs/03_Data_Binding/iteratingthroughthedata.md
created_at: 2025-08-05
---








  









### Iterating Through the Data {#iterating-through-the-data style="tab-stops: 0pt"}

 

Now, we have set a datasource in the Grouping Engine. Lets see how to iterate through the data.

 

This section will show you how to access the data through the **Grouping.Engine** object by using the **Engine.Table.Records** collection.

 

Add the following code to the main function. This code will iterate through the **Records** collection and will display the output in the Console.

 

{border="0"} Console is a text-only user interface that allows the user to interact with the operating system or text-based application by entering the text through the keyboard and reading the text output from the computer screen.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                            |
| [// Access the data directly from the Engine.]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                            |
| [foreach][(Record rec ][in][ groupingEngine.Table.Records)]                          |
|                                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                            |
| [         MyObject obj = rec.GetData() ][as][ MyObject;]                                                                              |
|                                                                                                                                                                                                                                                                                            |
| [         ][if][(obj != ][null][)] |
|                                                                                                                                                                                                                                                                                            |
| [         {]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                            |
| [            Console.WriteLine(obj);]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| [         }]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                            |
| [// Pause]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                            |
| [Console.ReadLine(); ]                                                                                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\' Access the data directly from the Engine.]                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Dim][ rec ][As][ Record]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [For][ ][Each][ rec ][In][ groupingEngine.Table.Records]                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [       ][Dim][ obj ][As][ MyObject = ][CType][(rec.GetData(), MyObject)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [      ][ If Not][ (obj ][Is Nothing][) ][Then]                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [             Console.WriteLine(obj)]                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [      ][ End If]                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Next][ rec]                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\' Pause]                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Console.ReadLine() ]                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 13: Console Showing Two Sets of Output (Directly from the List and from the Engine)

[]{#related-topics}

