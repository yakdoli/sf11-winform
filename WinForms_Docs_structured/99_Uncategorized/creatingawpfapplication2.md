---
title: creatingawpfapplication2.md
original_path: WinForms_Docs/99_Uncategorized/creatingawpfapplication2.md
created_at: 2025-08-05
---








  









## Creating a WPF Application[]{#p8}[]{#p9} {#creating-a-wpf-application style="tab-stops: 0pt"}

To create a new WPF application in Visual Studio 2008, follow the below steps:**[]**

1.   Open Visual Studio 2008. Go to File menu and click New Project.

[] 

{border="0"}

Figure 4:  File menu

 

2.   In the New Project dialog, Select WPF Application and give the project name as WPF Application.

 

{border="0"}

Figure 5:  New Project dialog - WPF Application

 

3.   A new WPF application is now created.

 

Adding Grid Controls

The first step before adding a Grid control to the WPF application, is to add a Scroll Viewer control, which presents a scrollable area that can host any visible control. Essential Grid can be easily hosted inside this control. The visibility of the horizontal and vertical scrollbars of the Scroll Viewer can be set using HorizontalScrollBarVisibility and VerticalScrollBarVisibility properties respectively. The Grid integrates with the Scroll Viewer supporting both the CanContentScroll modes.

**[]** 

CanContentScroll Property

This property of the Scroll Viewer indicates whether or not the contents hosted inside the control are allowed to scroll. This can be set to true or false.

**[]** 

[·      ]If CanContentScroll is set to *True*, the grid will be nested inside the Scroll Viewer and its MeasureOverride method (http://msdn.microsoft.com/en-us/library/system.windows.frameworkelement.measureoverride.aspx) will have no effect. The grid will be responsible for scrolling the rows and columns in the given viewable area and will synchronize as required with the scrollbars of the Scroll Viewer. The Grid will be in a virtual mode and the data will be loaded on demand.

[·      ]If CanContentScroll is set to *False*, the grid will return the total height of all rows and total width of all columns in its MeasureOverride method. The parent control will handle the scrolling. Rows and column cells will not be virtualized as they will be fixed.

**[]** 


 

{border="0"}Note: When If CanContentScroll is set to False, freezing rows or columns is not possible.


**[]** 

A WPF application with basic preparations is ready now. Next step is to add the Grid controls to the application. The following sections elaborates on adding different Grid controls and loading them with data, programmatically.

[] 

[]{.UGHyperlink}

[]{.UGHyperlink}

[]{.UGHyperlink}

 

[]{#related-topics}

