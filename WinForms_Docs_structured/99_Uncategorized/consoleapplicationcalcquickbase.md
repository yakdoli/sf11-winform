---
title: consoleapplicationcalcquickbase.md
original_path: WinForms_Docs/99_Uncategorized/consoleapplicationcalcquickbase.md
created_at: 2025-08-05
---






#### Console Application CalcQuickBase {#console-application-calcquickbase style="tab-stops: 0pt"}

 

The step-by-step procedure to create a simple console application is as follows:

 

1.   From Visual Studio, use File \| New \| Project to create a new Console Application named CalcQuickBaseTutorial. After creating the project, open the References node in the Solution Explorer and add a reference to Syncfusion.Calculate.Base. At this point, your Solution Explorer window should appear similar to this one.

[] 

{border="0"}

Figure 15: Essential Calculate Reference Added to the Project

[] 

2.   In the Main method, add the code to create a **CalcQuickBase** object. Also add the code to loop through the process of retrieving a string and using **CalcQuickBase.ParseAndCompute** to perform the calculation that is represented by the string. Given below is the code that handles these tasks.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                     |
| [using][ System;]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                     |
| [using][ Syncfusion.Calculate;]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                     |
| [namespace][ CalcQuickBaseTutorial]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                     |
| [      ][  /// \<summary\>]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                     |
| [        /// Summary description for Class1.]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                     |
| [        /// \</summary\>]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                     |
| [        ][class][ Class1]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                     |
| [              ][  /// \<summary\>]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                     |
| [                /// The main entry point for the application.]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                     |
| [                /// \</summary\>]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                     |
| [                \[STAThread\]]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                     |
| [               ][ static void][ Main(][string][\[\] args)] |
|                                                                                                                                                                                                                                                                                                                     |
| [                {]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                     |
| [                        CalcQuickBase cq = ][new][ CalcQuickBase();]                                                                                          |
|                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                     |
| [                        ][string][ s;]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                     |
| [                        ][while][( (s = Console.ReadLine()) != \"\" )]                                                                                        |
|                                                                                                                                                                                                                                                                                                                     |
| [                        {]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                     |
| [                                ][string][ val = cq.ParseAndCompute(s);]                                                                                      |
|                                                                                                                                                                                                                                                                                                                     |
| [                                Console.WriteLine(\"value= \" + val);]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                     |
| [                                // Blank line]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                     |
| [                                Console.WriteLine(\"\"); ]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                     |
| [                        }]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                     |
| [                }]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                             |
| [Imports][ System]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                             |
| [Imports][ Syncfusion.Calculate]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                             |
| [Namespace][ CalcQuickBaseTutorial]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                             |
| [    ][Class][ Class1]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                             |
| [       ][ Public Overloads Shared][ ][Sub][ Main()]                |
|                                                                                                                                                                                                                                                                                                                             |
| [            ][Dim][ cq ][As New][ CalcQuickBase]                   |
|                                                                                                                                                                                                                                                                                                                             |
| [            ][Dim][ s ][As String][ = Console.ReadLine()]          |
|                                                                                                                                                                                                                                                                                                                             |
| [           ][ Do While][ s \<\> \"\"]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                             |
| [                ][Dim][ val ][As String][ = cq.ParseAndCompute(s)] |
|                                                                                                                                                                                                                                                                                                                             |
| [                Console.WriteLine((\"value= \" + val))]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                             |
| [                Console.WriteLine(\"\") ]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                             |
| [                \' Blank line]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                             |
| [                s = Console.ReadLine()]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                             |
| [            ][Loop]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                             |
| [        ][\' Main][ ]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                             |
| [        ][End Sub][ ]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                             |
| [    ][\' Class1]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                             |
| [  ][  End Class][ ]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                             |
| [\' CalcQuickBaseTutorial]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                             |
| [End Namespace][ ]                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Once the code is entered, run the application by pressing F5. Then enter an expression such as 1+2 and press Enter. Enter additional algebraic combinations of constants and named functions from the Function Library like Sin, Cos, Sum and Pi. Press Enter without entering anything to terminate the program. Below is a typical display of this.

[] 

[{border="0"}]

**[Figure ][16][: Application Display]**[]

 

[]{#p21} 

[]{#related-topics}

