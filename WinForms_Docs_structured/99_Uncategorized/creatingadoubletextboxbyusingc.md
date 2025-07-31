---
title: creatingadoubletextboxbyusingc.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingadoubletextboxbyusingc.md
created_at: 2025-07-03
---






##### Creating a DoubleTextBox by using C# {#creating-a-doubletextbox-by-using-c style="tab-stops: 0pt"}

 

The steps to create a DoubleTextBox by using VisualStudio in C# are as follows:

 

1.   Open Visual Studio.

2.   On the File menu, select **New -\> Project**. This opens the New Project Dialog box.

 

{border="0"}

Figure 412: Open New Project[]

[] 

3.   In the Project Dialog window, select **WPF Application**, in the name field, type the name of the project, and then click **OK**.

[] 

{border="0"}

Figure 413: New Project Dialog[]

[] 

4.   Add the following reference with the sample project:

[·      ]Syncfusion.Shared.WPF.dll

[] 

{border="0"}

Figure 414: Solution Explorer[]

[] 

5.   Click the **C#** file, to open the C# file and add the **DoubleTextBox** to the application.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[C#[]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                                     |
| [public][ [partial] [class] [MainWindow] : [Window]] |
|                                                                                                                                                                                                                                     |
| [    {]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                     |
| [        [public] MainWindow()]                                                                                                                                            |
|                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                     |
| [            InitializeComponent();]                                                                                                                                                            |
|                                                                                                                                                                                                                                     |
| [            [//Adding DoubleTextBox to Application]]                                                                                                                     |
|                                                                                                                                                                                                                                     |
| [            Syncfusion.Windows.Shared.[DoubleTextBox] doubleTextBox = [new]]                                                                      |
|                                                                                                                                                                                                                                     |
| [                          Syncfusion.Windows.Shared.[DoubleTextBox]();]                                                                                                |
|                                                                                                                                                                                                                                     |
| [            doubleTextBox.Height = 25;]                                                                                                                                                        |
|                                                                                                                                                                                                                                     |
| [            doubleTextBox.Width = 100;]                                                                                                                                                        |
|                                                                                                                                                                                                                                     |
| [            [this].LayoutRoot.Children.Add(doubleTextBox);]                                                                                                               |
|                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                     |
| [            }]                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 415: DoubleTextBox

 


Note:

If you do not set any value to the DoubleTextbox then the default value will be as follows:

If the UseNullOption is set to true then,

Value of the NullValue property will be the default value.

Otherwise

Zero will be the default value (based on the MinValue and MaxValue the default value will change).


**[]** 

See Also

[]{.UGHyperlink}

[]{.UGHyperlink}

[[]]{.UGHyperlink} 

[]{#related-topics}

