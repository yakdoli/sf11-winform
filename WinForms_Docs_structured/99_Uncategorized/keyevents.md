---
title: keyevents.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\keyevents.md
created_at: 2025-07-03
---






##### Key Events {#key-events style="tab-stops: 0pt"}

[] 

Following are the key events:

 

**KeyDown-**Occurs when a key is pressed when control has focus.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                                |
| [this][.groupingEngine.TableControl.KeyDown+=[new] [KeyEventHandler](TableControl_KeyDown);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                             |
|                                                                                                                                                                                                |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                |
| [AddHandler][ groupingEngine.TableControl.KeyDown, [AddressOf] TableControl_KeyDown] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The event handler receives an argument of type KeyEventArgs containing data related to this event.

The following KeyEventArgs properties provide information specific to this event.

 

**KeyData**-Gets the key data for a System.Windows.Forms.Control.KeyDown or System.Windows.Forms.Control.KeyUp event. 

[  ]

[·      ]**Alt**-Gets a value indicating whether the ALT key was pressed.

[·      ]**Control**-Gets a value indicating whether the CTRL key was pressed.

[·      ]**Handled**-Gets or sets a value indicating whether the event was handled.

[·      ]**KeyCode**-Gets the keyboard code for a System.Windows.Forms.Control.KeyDown or System.Windows.Forms.Control.KeyUp.

[·      ]**KeyValue**-Gets the keyboard value for a System.Windows.Forms.Control.KeyDown or System.Windows.Forms.Control.KeyUp event.

[·      ]**Modifiers**-Gets the modifier flags for a System.Windows.Forms.Control.KeyDown or System.Windows.Forms.Control.KeyUp.

[·      ]**Shift**-Gets a value indicating whether the SHIFT key was pressed.

[·      ]**SuppressKeyPress**-Gets or sets a value indicating whether the key event should be passed on to the underlying control.

[] 

**KeyPress-**Occurs when a key is pressed when control has focus.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                                       |
| [this][.groupingEngine.TableControl.KeyPress+=[new] [KeyPressEventHandler](TableControl_KeyPress);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                               |
|                                                                                                                                                                                                  |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                  |
| [AddHandler][ groupingEngine.TableControl.KeyPress, [AddressOf] TableControl_KeyPress] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The event handler receives an argument of type KeyPressEventArgs containing data related to this event. The following KeyPressEventArgs  properties provide information specific to this event.

[] 

[·      ]**KeyChar**-The ASCII character corresponding to the key the user pressed.

[·      ]**Handled**-Gets or sets a value indicating whether the System.Windows.Forms.Control.KeyPress

[  ]

**KeyUp**:Occurs when a key is released when control has focus.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| [this][.groupingEngine.TableControl.KeyUp+=[new] [KeyEventHandler](TableControl_KeyUp);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                         |
|                                                                                                                                                                                            |
| []                                                                                                                                                                   |
|                                                                                                                                                                                            |
| [AddHandler][ groupingEngine.TableControl.KeyUp, [AddressOf] TableControl_KeyUp] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The event handler receives an argument of type KeyEventArgs containing data related to this event. The following KeyEventArgs  properties provide information specific to this event.

[] 

[·      ]**KeyData-**Gets the key data for a System.Windows.Forms.Control.KeyDown or System.Windows.Forms.Control.KeyUp event. 

[·      ]**Alt**-Gets a value indicating whether the ALT key was pressed.

[·      ]**Control**-Gets a value indicating whether the CTRL key was pressed.

[·      ]**Handled**-Gets or sets a value indicating whether the event was handled.

[·      ]**KeyCode**-Gets the keyboard code for a System.Windows.Forms.Control.KeyDown or System.Windows.Forms.Control.KeyUp

[·      ]**KeyValue**-Gets the keyboard value for a System.Windows.Forms.Control.KeyDown or System.Windows.Forms.Control.KeyUp event.

[·      ]**Modifiers**-Gets the modifier flags for a System.Windows.Forms.Control.KeyDown or System.Windows.Forms.Control.KeyUp event.

[·      ]**Shift**-Gets a value indicating whether the SHIFT key was pressed.

[·      ]**SuppressKeyPress**-Gets or sets a value indicating whether the key event should be passed on to the underlying control.           

 

[]{#p514} 

 

[]{#related-topics}

