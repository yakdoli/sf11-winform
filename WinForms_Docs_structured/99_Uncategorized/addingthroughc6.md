---
title: addingthroughc6.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingthroughc6.md
created_at: 2025-07-03
---






#### Adding through C# {#adding-through-c style="tab-stops: 0pt"}

Following are the steps to add the PropertyGrid control by using VisualStudio in C#:

[] 

1.   Open Visual Studio. On the **File** menu, select **New -\> Project**. This opens the New Project Dialog box.

[] 

{border="0"}

Figure 815: VisualStudio Opening Project

[] 

 

2.   On the Project Dialog window, select **WPF Application**, in the Name field, type the name of the project, and then click **OK**.

 

3.   Add the following reference with the sample project:

 

**Syncfusion.PropertyGrid.Wpf.dll**

**Syncfusion.Shared.Wpf.dll**

**Syncfusion.Tools.Wpf.dll**

 

4.   Click the C# file and add the PropertyGrid control to your application as follows.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                              |
| [           ]                                                                                                                                                 |
|                                                                                                                                                                                              |
| []                                                                                                                                                            |
|                                                                                                                                                                                              |
| [Syncfusion.Windows.PropertyGrid.[PropertyGrid] propertyGrid = [new] Syncfusion.Windows.PropertyGrid.[PropertyGrid]();\ |
| propertyGrid.Height = 250;\                                                                                                                                                                  |
| propertyGrid.Width = 250;\                                                                                                                                                                   |
| propertyGrid.BorderBrush = [new] [SolidColorBrush]([Colors].Gray);\                                                     |
| propertyGrid.BorderThickness = [new] [Thickness](2);\                                                                                           |
| propertyGrid.SelectedObject = [new] [Button]();\                                                                                                |
| LayoutRoot.Children.Add(propertyGrid);]                                                                                                                  |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 816: PropertyGrid

 

[]{#related-topics}

