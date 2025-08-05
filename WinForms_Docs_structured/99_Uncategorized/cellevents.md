---
title: cellevents.md
original_path: WinForms_Docs/99_Uncategorized/cellevents.md
created_at: 2025-08-05
---






##### Cell Events {#cell-events style="tab-stops: 0pt"}

[] 

The Cell events are as follows:

 

**CellButtonClicked**-Occurs when the user has clicked on a child button element inside a cell renderer.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                    |
| [this][.groupingEngine.TableControl.CellButtonClicked+=[new] Syncfusion.Windows.Forms.Grid.[GridCellButtonClickedEventHandler](TableControl_CellButtonClicked);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                |
|                                                                                                                                                                                                                    |
| [AddHandler][ groupingEngine.TableControl.CellButtonClicked, [AddressOf] TableControl_CellButtonClicked] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The event handler receives an argument of type GridCellButtonClickedEventArgs containing data related to this event.

 

The following GridCellButtonClickedEventArgs properties provide information specific to this event.

[   ]

[·      ]**RowIndex**-Gets the row index.

[·      ]**ColIndex**-Gets the column index.

[·      ]**ButtonIndex**-The index of the clicked cell button element.

[] 

**CellClick**-Occurs when the user clicks inside a cell.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [this][.groupingEngine.TableControl.CellClick+=[new] Syncfusion.Windows.Forms.Grid.[GridCellClickEventHandler](TableControl_CellClick);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                 |
|                                                                                                                                                                                                    |
| []                                                                                                                                                |
|                                                                                                                                                                                                    |
| [AddHandler][ groupingEngine.TableControl.CellClick, [AddressOf] TableControl_CellClick] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The event handler receives an argument of type GridCellClickEventArgs containing data related to this event.

 

The following GridCellClickEventArgs properties provide information specific to this event.

[] 

[·      ]**RowIndex**-Gets the row index.       

[·      ]**ColIndex**-Gets the column index.

[·      ]**MouseEventArgs**-The System.Windows.Forms.MouseEventArgs originating this event.

[·      ]**IsOverImage**-Indicates if the mouse was over a image in static cell when the mouse was released.

[] 

**CellDoubleClick**-Occurs when the user double-clicks inside a cell.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                        |
| [this][.groupingEngine.TableControl.CellDoubleClick+=[new] Syncfusion.Windows.Forms.Grid.[GridCellClickEventHandler](TableControl_CellDoubleClick);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                             |
|                                                                                                                                                                                                                |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                |
| [AddHandler][ groupingEngine.TableControl.CellDoubleClick, [AddressOf] TableControl_CellDoubleClick] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The event handler receives an argument of type GridCellClickEventArgs containing data related to this event.

 

The following GridCellClickEventArgs properties provide information specific to this event.

[] 

[·      ]**RowIndex**-Gets the row index.       

[·      ]**ColIndex**-Gets the column index.

[·      ]**MouseEventArgs**-The System.Windows.Forms.MouseEventArgs originating this event.

[·      ]**IsOverImage**-Indicates if the mouse was over a image in static cell when the mouse was released.

 

**CellDrawn**-Occurs for every cell after the grid has drawn the specified cell.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| [this][.groupingEngine.TableControl.CellDrawn+=[new] Syncfusion.Windows.Forms.Grid.[GridDrawCellEventHandler](TableControl_CellDrawn);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                 |
|                                                                                                                                                                                                    |
| []                                                                                                                                                |
|                                                                                                                                                                                                    |
| [AddHandler][ groupingEngine.TableControl.CellDrawn, [AddressOf] TableControl_CellDrawn] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The event handler receives an argument of type GridDrawCellEventArgs containing data related to this event.

 

The following GridDrawCellEventArgs properties provide information specific to this event.

[] 

[·      ]**Graphics**-Gets the  Graphics context.

[·      ]**Renderer**-Gets the cell renderer.

[·      ]**Bounds**-Gets the Cell boundaries.

[·      ]**RowIndex**-Gets the row index.

[·      ]**ColIndex**-The column index.

[·      ]**Style**-The Syncfusion.Windows.Forms.Grid.GridStyleInfo object that holds cell information.

[·      ]**IsBackgroundErased**-True if the cell background has already been drawn with the interior as specified in the style object.

 

[]{#p501} 

[] 

In this section, you will learn about the following events.

[] 

 

[]{#p502} 

 

###### 4.3.4.13.2.1        CellButtonClicked Event {#cellbuttonclicked-event style="tab-stops: 0pt"}

[] 

It occurs when a user has clicked on a child button element inside the cell renderer. The event handler receives an argument of type **GridCellButtonClickedEventArgs** containing data related to this event. This event can be invoked as follows.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [this][.gridGroupingControl1.TableControlCellButtonClicked+=[new] [GridCellButtonClickedEventHandler](TableControl_CellButtonClicked);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [AddHandler Me][.gridGroupingControl1.TableControlCellButtonClicked, [AddressOf] TableControl_CellButtonClicked] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following **GridCellButtonClickedEventArgs** properties provide information specific to this event.

[] 


  ------------- -----------------------------------------------------------
   Properties   Description
  Button        A reference to the GridCellButton for the clicked button.
  ButtonIndex   The index of the cell button clicked.
  ColIndex      Specifies the column index of the cell.
  RowIndex      Specifies the row index of the cell.
  ------------- -----------------------------------------------------------


**[]** 

Example

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [private][ [void] TableControl_CellButtonClicked([object] sender, [GridCellButtonClickedEventArgs] e)] |
|                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| [Console.Writeline([\"CellButtonClicked\"]);]                                                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ [Sub] TableControl_CellButtonClicked([ByVal] sender [As] [Object], [ByVal] e [As] GridCellButtonClickedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                  |
| [Console.Writeline([\"CellButtonClicked\"])]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Sub]]                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p503} 

 

###### 4.3.4.13.2.2        CellClick Event {#cellclick-event style="tab-stops: 0pt"}

[] 

It occurs when the user clicks inside a cell. The event handler receives an argument of type **GridCellClickEventArgs** containing data related to this event. This event can be invoked as follows.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [this][.gridGroupingControl1.TableControlCellClick+=[new] Syncfusion.Windows.Forms.Grid.GridCellClickEventHandler(TableControl_CellClick);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                         |
|                                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                                            |
| [AddHandler Me][.gridGroupingControl1.TableControlCellClick, [AddressOf] TableControl_CellClick] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

The following **GridCellClickEventArgs** properties provide information specific to this event.

[] 


  ---------------- -----------------------------------------------------------------------------------------
   Properties      Description
  IsOverImage      Indicates if the mouse was over the image in a static cell when the mouse was released.
  MouseEventArgs   The MouseEventArgs originating this event.
  ColIndex         Specifies the column index of the cell.
  RowIndex         Specifies the row index of the cell.
  Cancel           Specifies a value to indicate if this event should be canceled.
  ---------------- -----------------------------------------------------------------------------------------


[] 

Example

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [private][ [void] TableControl_CellClick([object] sender, [GridCellClickEventArgs] e)] |
|                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                            |
| [Console.Writeline([\"CellClicked\"]);]                                                                                                                                         |
|                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                  |
| [Private][ [Sub] TableControl_CellClick([ByVal] sender [As] [Object], [ByVal] e [As] GridCellClickEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                  |
| [Console.Writeline([\"CellClicked\"])]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Sub]]                                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p504} 

 

###### 4.3.4.13.2.3        CellDrawn Event {#celldrawn-event style="tab-stops: 0pt"}

[] 

It occurs for every cell after the grid has drawn the specified cell. The event handler receives an argument of type **GridDrawCellEventArgs** containing data related to this event. This event can be invoked as follows.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [this][.gridGroupingControl1.TableControlCellDrawn+=[new] Syncfusion.Windows.Forms.Grid.GridDrawCellEventHandler(TableControl_CellDrawn);     ] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                         |
|                                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                                            |
| [AddHandler Me][.gridGroupingControl1.TableControlCellDrawn, [AddressOf] TableControl_CellDrawn] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

The following GridTableControlCellDrawnEventArgs properties provide information specific to this event.

[] 


  -------------------- -------------------------------------------------------------------------------------------------------------
   Properties          Description
  Bounds               Cell boundaries including borders and margins.
  Renderer             The GridCellRendererBase associated with the cell.
  Graphics             The Graphics context.
  IsBackgroundErased   Specifies if the cell background has already been drawn with the interior as specified in the style object.
  ColIndex             Specifies the column index of the cell.
  RowIndex             Specifies the row index of the cell.
  Cancel               Specifies a value to indicate if this event should be canceled.
  -------------------- -------------------------------------------------------------------------------------------------------------


**[]** 

You can handle the TableControlCellDrawn to draw the error icon in an invalid cell as follows.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                                           |
| [private][ [void] TableControl_CellDrawn([object] sender, [GridDrawCellEventArgs] e)] |
|                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                           |
| [Console.Writeline([\"Cell Drawn\"]);]                                                                                                                                         |
|                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                 |
| [Private][ [Sub] TableControl_CellDrawn([ByVal] sender [As] [Object], [ByVal] e [As] GridDrawCellEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                 |
| [Console.Writeline([\"Cell Drawn\"])]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p505} 

 

###### 4.3.4.13.2.4        CellDoubleClick Event {#celldoubleclick-event style="tab-stops: 0pt"}

[] 

It occurs when the user double-clicks inside a cell. The event handler receives an argument of type **GridCellClickEventArgs** containing data related to this event. This event can be invoked as follows.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [this][.gridGroupingControl1.TableControlCellDoubleClick+=[new] Syncfusion.Windows.Forms.Grid.GridCellClickEventHandler(TableControl_CellDoubleClick);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                     |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [AddHandler Me][.gridGroupingControl1.TableControlCellDoubleClick, [AddressOf] TableControl_CellDoubleClick] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following **GridCellClickEventArgs** properties provide information specific to this event.

[] 


  ---------------- -----------------------------------------------------------------------------------------
   Properties      Description
  IsOverImage      Indicates if the mouse was over the image in a static cell when the mouse was released.
  MouseEventArgs   The MouseEventArgs originating this event.
  ColIndex         Specifies the column index of the cell.
  RowIndex         Specifies the row index of the cell.
  Cancel           Specifies a value to indicate if this event should be canceled.
  ---------------- -----------------------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                  |
| [private][ [void] TableControl_CellDoubleClick([object] sender, [GridCellClickEventArgs] e)] |
|                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                  |
| [Console.Writeline([\"Cell DoubleClicked\"]);]                                                                                                                                        |
|                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] TableControl_CellDoubleClick([ByVal] sender [As] [Object], [ByVal] e [As] GridCellClickEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                        |
| [Console.Writeline([\"Cell DoubleClicked\"])]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p506} 

 

[]{#related-topics}

