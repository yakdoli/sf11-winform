---
title: creatingamaskedtextboxbyusingc.md
original_path: WinForms_Docs/99_Uncategorized/creatingamaskedtextboxbyusingc.md
created_at: 2025-08-05
---






##### Creating a MaskedTextBox by using C# {#creating-a-maskedtextbox-by-using-c style="tab-stops: 0pt"}

The steps to create a MaskedTextBox by using Visual Studio in C# are as follows:

1.   Open Visual Studio.

2.   On the File menu, select **New -\> Project**. This opens the New Project Dialog box.

 

{border="0"}

Figure 666: Open New Project[]

[] 

3.   On the Project Dialog window, select **WPF Application**, in the name field, type the name of the project, and then click **OK**.

 

{border="0"}

 

Figure 667: New Project Dialog

[] 

4.   Add the following reference with the sample project:

[·      ]Syncfusion.Shared.WPF.dll

[] 

{border="0"}

 

Figure 668: Solution Explorer

[] 

5.   Click the **C#** file, to open the C# file and add the **MaskedTextBox** to the application.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **C#[    ]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [public][ [partial] [class] [MainWindow] : [Window]] |
|                                                                                                                                                                                                                                                               |
| [    {]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                               |
| [        [public] MainWindow()]                                                                                                                                                         |
|                                                                                                                                                                                                                                                               |
| [        {]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                               |
| [            InitializeComponent();]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                               |
| [            Syncfusion.Windows.Shared.[MaskedTextBox] maskedTextBox = [new] Syncfusion.Windows.Shared.[MaskedTextBox]();]              |
|                                                                                                                                                                                                                                                               |
| [            maskedTextBox.Height = 25;]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                               |
| [            maskedTextBox.Width = 150;]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                               |
| [            maskedTextBox.Mask = [\"00/00/0000\"];]                                                                                                                                 |
|                                                                                                                                                                                                                                                               |
| [            [this].LayoutRoot.Children.Add(maskedTextBox);]                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| [        }]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                               |
| [    }]                                                                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

Figure 669:  MaskedTextBox

See Also

[]{.UGHyperlink}

[]{.UGHyperlink}

 

[]{#related-topics}

