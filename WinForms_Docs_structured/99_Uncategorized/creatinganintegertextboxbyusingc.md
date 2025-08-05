---
title: creatinganintegertextboxbyusingc.md
original_path: WinForms_Docs/99_Uncategorized/creatinganintegertextboxbyusingc.md
created_at: 2025-08-05
---






##### Creating an IntegerTextBox by using C# {#creating-an-integertextbox-by-using-c style="tab-stops: 0pt"}

The steps to create an IntegerTextBox by using Visual Studio in C# are as follows:

1.  Open Visual Studio.

    2.  On the File menu, select **New -\> Project**. This opens the New Project Dialog box.

 

{border="0"}

Figure 604: Open New Project

3.   On the Project Dialog window, select **WPF Application**, in the name field, type the name of the project, and then click **OK**.

 

{border="0"}

 

Figure 605: New Project Dialog

 

4.   Add the following reference with the sample project:

[·      ]Syncfusion.Shared.WPF.dll

[] 

{border="0"}

 

Figure 606: Solution Explorer

 

5.   Click the **C#** file, to open the C# file and add the **IntegerTextBox** to the application.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[C#][]**                                                                                                                              |
|                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                         |
|                                                                                                                                                                                                                              |
| **[namespace][ WpfApp]**                                                                                      |
|                                                                                                                                                                                                                              |
| **[{]**                                                                                                                                                                     |
|                                                                                                                                                                                                                              |
| **[    [public] [partial] [class] [MainWindow] : [Window]]** |
|                                                                                                                                                                                                                              |
| **[    {]**                                                                                                                                                                 |
|                                                                                                                                                                                                                              |
| **[        [public] MainWindow()]**                                                                                                                    |
|                                                                                                                                                                                                                              |
| **[        {]**                                                                                                                                                             |
|                                                                                                                                                                                                                              |
| **[            InitializeComponent();]**                                                                                                                                    |
|                                                                                                                                                                                                                              |
| **[            [//Adding IntegerTextBox to Application]]**                                                                                            |
|                                                                                                                                                                                                                              |
| **[            Syncfusion.Windows.Shared.[IntegerTextBox] integerTextBox = [new]]**                                            |
|                                                                                                                                                                                                                              |
| **[                                    Syncfusion.Windows.Shared.[IntegerTextBox]();]**                                                             |
|                                                                                                                                                                                                                              |
| **[            integerTextBox.Height = 25;]**                                                                                                                               |
|                                                                                                                                                                                                                              |
| **[            integerTextBox.Width = 100;]**                                                                                                                               |
|                                                                                                                                                                                                                              |
| **[            [this].LayoutRoot.Children.Add(integerTextBox);]**                                                                                      |
|                                                                                                                                                                                                                              |
| **[        }]**                                                                                                                                                             |
|                                                                                                                                                                                                                              |
| **[    }]**                                                                                                                                                                 |
|                                                                                                                                                                                                                              |
| **[}]**[]                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

{border="0"}

 

Figure 607: IntegerTextBox

 

See Also

[]{.UGHyperlink}

[]{.UGHyperlink}

[[]]{.underline} 

[]{#related-topics}

