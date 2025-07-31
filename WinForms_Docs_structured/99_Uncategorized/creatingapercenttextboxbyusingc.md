---
title: creatingapercenttextboxbyusingc.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingapercenttextboxbyusingc.md
created_at: 2025-07-03
---






##### Creating a PercentTextBox by using C# {#creating-a-percenttextbox-by-using-c style="tab-stops: 0pt"}

 

The steps to create a PercentTextBox by using Visual Studio in C# are as follows[:]

1.            Open Visual Studio.

2.   On the File menu, select **New -\> Project**. This opens the New Project Dialog box.

 

 

{border="0"}

Figure 763: Open New Project

 

3.   On the Project Dialog window, select **WPF Application**, in the name field, type the name of the project, and then click **OK**.

[] 

{border="0"}

Figure 764: New Project Dialog

 

4.   Add the following reference with the sample project:

[·      ]**Syncfusion.Shared.WPF.dll**[]

[] 

{border="0"}

Figure 765: Solution Explorer

[] 

[·      ]Click the **C#** file, to open the C# file and add the **PercentTextBox** to the application.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[C#]**[]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
| **[public][ [partial] [class] [MainWindow] : [Window]]** |
|                                                                                                                                                                                                                                                                   |
| **[    {]**                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                   |
| **[        [public] MainWindow()]**                                                                                                                                                         |
|                                                                                                                                                                                                                                                                   |
| **[        {]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                   |
| **[            InitializeComponent();]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                   |
| **[            Syncfusion.Windows.Shared.[PercentTextBox] percentTextBox = [new] Syncfusion.Windows.Shared.[PercentTextBox]();]**           |
|                                                                                                                                                                                                                                                                   |
| **[            percentTextBox.Width = 150;]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                   |
| **[            percentTextBox.Height = 25;]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                   |
| **[            [this].LayoutRoot.Children.Add(percentTextBox);]**                                                                                                                           |
|                                                                                                                                                                                                                                                                   |
| **[        }]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                   |
| **[     }]**                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 766: Percent TextBox


Note:

If you do not set any PercentValue to the PercentTextBox then the default value will be as follows:

If the UseNullOption is set to true then,

Value of the NullValue property will be the default value.

Otherwise

 Zero will be the default value (based on the MinValue and MaxValue the default value will change).

 


See Also

[]{.UGHyperlink}

[]{.UGHyperlink}

 

[]{#related-topics}

