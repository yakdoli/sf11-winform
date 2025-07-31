---
title: creatingacurrencytextboxbyusingc.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingacurrencytextboxbyusingc.md
created_at: 2025-07-03
---






##### Creating a CurrencyTextBox by using C# {#creating-a-currencytextbox-by-using-c style="tab-stops: 0pt"}

The steps to create a CurrencyTextBox by using Visual Studio in C# are as follows:

1.   Open Visual Studio.

2.   On the File menu, select **New -\> Project**. This opens the New Project Dialog box.

 

{border="0"}

Figure 220: Open New Project[]

[] 

3.   In the Project Dialog window, select **WPF Application**, in the name field, type the name of the project, and then click **OK**.

[] 

{border="0"}

Figure 221: New Project Dialog

[] 

4.   Add the following reference with the sample project:

[·      ]Syncfusion.Shared.WPF.dll

[] 

{border="0"}

Figure 222: Solution Explorer

[] 

5.   Click the **C#** file, to open the C# file and add the **CurrencyTextBox** to the application.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                               |
| [    ]                                                                                                                                                                                                       |
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
| [            Syncfusion.Windows.Shared.[CurrencyTextBox] currencyTextBox = [new]]                                                                               |
|                                                                                                                                                                                                                                                               |
| [                          Syncfusion.Windows.Shared.[CurrencyTextBox]();]                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [            currencyTextBox.Width = 100;]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                               |
| [            currencyTextBox.Height = 25;]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                               |
| [            [this].LayoutRoot.Children.Add(currencyTextBox);]                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [        }]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                               |
| [     }]                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 223: CurrencyTextBox


Note:

If you do not set any value to the CurrencyTextBox then the default value will be as follows:

If the UseNullOption is set to true, Value of the NullValue property will be the default value.

Otherwise Zero will be the default value (based on the MinValue and MaxValue the default value will change).


 

See Also

[]{.UGHyperlink}

[]{.UGHyperlink}

 

[]{#related-topics}

