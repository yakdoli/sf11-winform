---
title: creatingadatetimeeditcontrolinc1.md
original_path: WinForms_Docs/99_Uncategorized/creatingadatetimeeditcontrolinc1.md
created_at: 2025-08-05
---






##### Creating a DateTimeEdit control in C# {#creating-a-datetimeedit-control-in-c style="tab-stops: 0pt"}

The steps to create a DateTimeEdit control by using Visual Studio in C# are as follows:

 

1.   Open Visual Studio.

2.   On the File menu, select **New -\> Project**. This opens the New Project Dialog box.

 

{border="0"}

Figure 266: Open New Project[]

[] 

3.   On the Project Dialog window, select **WPF Application**, in the name field, type the name of the project, and then click **OK**.

 

{border="0"}

Figure 267: New Project Dialog[]

4.   Add the following reference with the sample project:

 

[·      ]Syncfusion.Shared.WPF.dll

[] 

{border="0"}

Figure 268: Solution Explorer

[] 

5.   Click the **C#** file, to open the C# file and add the **DateTimeEdit** control to the application.

Here is the code to create the DateTimeEdit control in C#:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [C#]                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [namespace][ WpfApp]                                                                                      |
|                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                     |
|                                                                                                                                                                                                                          |
| [    [public] [partial] [class] [MainWindow] : [Window]] |
|                                                                                                                                                                                                                          |
| [    {]                                                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [        [public] MainWindow()]                                                                                                                    |
|                                                                                                                                                                                                                          |
| [        {]                                                                                                                                                             |
|                                                                                                                                                                                                                          |
| [            InitializeComponent();]                                                                                                                                    |
|                                                                                                                                                                                                                          |
| [            [//Adding DateTimeEdit control to application from Syncfusion.Windows.Shared]]                                                       |
|                                                                                                                                                                                                                          |
| [            Syncfusion.Windows.Shared.[DateTimeEdit] dateTimeEdit = [new]]                                                |
|                                                                                                                                                                                                                          |
| [                               Syncfusion.Windows.Shared.[DateTimeEdit]();]                                                                    |
|                                                                                                                                                                                                                          |
| [            dateTimeEdit.Width = 200;]                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [            dateTimeEdit.Height = 25;]                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [            [this].LayoutRoot.Children.Add(dateTimeEdit);]                                                                                        |
|                                                                                                                                                                                                                          |
| [        }]                                                                                                                                                             |
|                                                                                                                                                                                                                          |
| [    }]                                                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 269: DateTimeEdit

**[]** 

See Also

[]{.UGHyperlink}

[[]]{.underline}

 

[]{#related-topics}

