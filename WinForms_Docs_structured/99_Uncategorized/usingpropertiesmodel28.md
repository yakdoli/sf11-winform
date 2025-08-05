---
title: usingpropertiesmodel28.md
original_path: WinForms_Docs/99_Uncategorized/usingpropertiesmodel28.md
created_at: 2025-08-05
---






#### Using Properties Model {#using-properties-model style="PAGE-BREAK-AFTER: auto; tab-stops: 0pt"}

1.   In the **controller**, create an object for the **DiagramPropertiesModel** class and set the **HorizontalGridLineStyle** and **VerticalGridLineStyle** properties and pass this model class to **view data**.

 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                           |
| [DiagramPropertiesModel][ model = [new] [DiagramPropertiesModel]()]                                                                |
|                                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                           |
| [    ShowHorizontalGridLine = [true],]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                           |
| [    ShowVerticalGridLine = [true],]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                           |
| [    HorizontalGridLineStyle = [new] [GridLineStyle]() { GridLineColor = [\"#ccddff\"], GridLineThickness = 3.0 },]                                                             |
|                                                                                                                                                                                                                                                                                                           |
| [    VerticalGridLineStyle = [new] [GridLineStyle]() { GridLineColor = [\"#cceeff\"], GridLineThickness = 3.0 },]                                                               |
|                                                                                                                                                                                                                                                                                                           |
| [    DiagramMode = ][DiagramMode][.SVG][] |
|                                                                                                                                                                                                                                                                                                           |
| [};]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                           |
| [ViewData\[[\"GridLines\"]\] = model;][]                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**Note:** If you want to create the diagram in the Canvas mode, change the **DiagramMode** to **Canvas**. By default the diagram is rendered in the SVG mode.

**[]** 

2.   Create a **view**. In the **view**, invoke the **Diagram** helper with the control ID which is the same as the **view data** name.


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View][]**                                                                  |
|                                                                                                                                                                        |
| [  [\<%]{]                                                                            |
|                                                                                                                                                                        |
| [              Html.Syncfusion().Diagram([\"GridLines\"])]                                |
|                                                                                                                                                                        |
| [                  .Render();]                                                                                    |
|                                                                                                                                                                        |
| [    }]                                                                                                           |
|                                                                                                                                                                        |
| [  [%\>]][ ] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

3.   Build and run the application.

 

 

{border="0"}

Figure 142: Custom Gridline Style

 

Tables for Properties, Methods, and Events

Properties

The properties of gridlines are tabulated as follows:

  ------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------- -----------------------------------------------
  **[Property]**                                                                         **[Description]**                                                                                                                                                               **[Type]**      **[Data Type]**
  [ShowVerticalGridLine][]   [Gets or sets a value indicating whether the vertical gridlines will be displayed. The default value is False.][]   [Server side]   [Binary, true or false]
  [ShowHorizontalGridLine]                                                               [Gets or sets a value indicating whether the horizontal gridlines will be displayed. The default value is False.]                                                               [Server side]   [Binary, true or false]
  [GridHorizontalOffset]                                                                 [Gets or sets the horizontal offset value for the grid.]                                                                                                                        [Server side]   [Double]
  [GridVerticalOffset]                                                                   [Gets or sets the vertical offset value for the grid.]                                                                                                                          [Server side]   [Double]
  [HorizontalGridLineStyle]                                                              [Gets or sets the style for the horizontal gridlines.]                                                                                                                          [Server side]   [GridLineStyle]
  [VerticalGridLineStyle]                                                                [Gets or sets the style for the vertical gridlines.]                                                                                                                            [Server side]   [GridLineStyle]
  ------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------- -----------------------------------------------

[] 

Methods

  Method                           Description                                                                                                                     Parameters                                      Type                                  Return Type
  -------------------------------- ------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------- ------------------------------------- ------------------------------
  showHorizontalGridLine           [Sets a value indicating whether the horizontal gridlines will be displayed.][]   Binary, true or false[]   [Client side]   [Void]
  showVerticalGridLine             [Sets a value indicating whether the vertical gridlines will be displayed.]                               Binary, true or false[]   [Client side]   [Void]
  setGridLineHorizontalOffset      [Sets the horizontal offset value.]                                                                       Float offsetValue[]       [Client side]   [Void]
  setGridLineVerticalOffset        [Sets the vertical offset value.]                                                                         Float offsetValue[]       [Client side]   [Void]
  setHorizontalGridLineThickness   [Sets the horizontal gridline thickness.]                                                                 Float thickness[]         [Client side]   [Void]
  setVerticalGridLineThickness     [Sets the vertical gridline thickness.]                                                                   Float thickness[]         [Client side]   [Void]
  setHorizontalGridLineColor       [Sets the horizontal gridline color.]                                                                     String color[]            [Client side]   [Void]
  setVerticalGridLineColor         [Sets the vertical gridline color.]                                                                       String color[]            [Client side]   [Void]

 

Sample Link

To view samples:

1.   Open the **Diagram** sample browser from the dashboard (Refer to the [Samples and Location](http://help.syncfusion.com/ug_92/User%20Interface/ASP.NET%20MVC/Diagram/default.htm?turl=Documents%2F22samplesandlocation.htm) chapter).

2.  Navigate to **Diagram.Mvc** \> **Getting Started** \> **Grid Lines demo**.

[]{#related-topics}

