---
title: customcursor.md
original_path: WinForms_Docs/99_Uncategorized/customcursor.md
created_at: 2025-08-05
---






##### Custom Cursor {#custom-cursor style="tab-stops: 0pt"}

 

This section discusses the cursor settings of the Edit Control.

 

Presently, Edit Control supports all the cursors contained in the **Windows Forms Cursors** enumerator. You can set any desired cursor to the Edit Control by using its **Cursor** property as shown below.

 


+-----------------------------------+--------------------------------------------------------------------------------------------------------+
| Edit Control Property             | Description                                                                                            |
+-----------------------------------+--------------------------------------------------------------------------------------------------------+
| Cursor                            | Sets the cursor that is displayed when the mouse pointer is over the control. The options provided are |
|                                   |                                                                                                        |
|                                   |                                                                                                        |
|                                   |                                                                                                        |
|                                   | [·      ]AppStarting                                                      |
|                                   |                                                                                                        |
|                                   | [·      ]Arrow                                                            |
|                                   |                                                                                                        |
|                                   | [·      ]Cross                                                            |
|                                   |                                                                                                        |
|                                   | [·      ]Default                                                          |
|                                   |                                                                                                        |
|                                   | [·      ]Hand                                                             |
|                                   |                                                                                                        |
|                                   | [·      ]Help                                                             |
|                                   |                                                                                                        |
|                                   | [·      ]HSplit                                                           |
|                                   |                                                                                                        |
|                                   | [·      ]IBeam                                                            |
|                                   |                                                                                                        |
|                                   | [·      ]No                                                               |
|                                   |                                                                                                        |
|                                   | [·      ]NoMove2D                                                         |
|                                   |                                                                                                        |
|                                   | [·      ]NoMoveHoriz                                                      |
|                                   |                                                                                                        |
|                                   | [·      ]NoMoveVert                                                       |
|                                   |                                                                                                        |
|                                   | [·      ]PanEast                                                          |
|                                   |                                                                                                        |
|                                   | [·      ]PanNE                                                            |
|                                   |                                                                                                        |
|                                   | [·      ]PanNorth                                                         |
|                                   |                                                                                                        |
|                                   | [·      ]PanNW                                                            |
|                                   |                                                                                                        |
|                                   | [·      ]PanSE                                                            |
|                                   |                                                                                                        |
|                                   | [·      ]PanSouth                                                         |
|                                   |                                                                                                        |
|                                   | [·      ]PanSW                                                            |
|                                   |                                                                                                        |
|                                   | [·      ]PanWest                                                          |
|                                   |                                                                                                        |
|                                   | [·      ]SizeAll                                                          |
|                                   |                                                                                                        |
|                                   | [·      ]SizeNESW                                                         |
|                                   |                                                                                                        |
|                                   | [·      ]SizeNS                                                           |
|                                   |                                                                                                        |
|                                   | [·      ]SizeNWSE                                                         |
|                                   |                                                                                                        |
|                                   | [·      ]SizeWE                                                           |
|                                   |                                                                                                        |
|                                   | [·      ]UpArrow                                                          |
|                                   |                                                                                                        |
|                                   | [·      ]VSplit                                                           |
|                                   |                                                                                                        |
|                                   | [·      ]WaitCursor                                                       |
+-----------------------------------+--------------------------------------------------------------------------------------------------------+


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                |
|                                                                                                                                                                               |
| []                                                                                                                          |
|                                                                                                                                                                               |
| [// Set any desired cursor to the Edit Control.]                                                                            |
|                                                                                                                                                                               |
| [this][.editControl1.Cursor = System.Windows.Forms.[Cursors].Hand;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                  |
|                                                                                                                                                     |
| []                                                                                                |
|                                                                                                                                                     |
| [\' Set any desired cursor to the Edit Control.]                                                  |
|                                                                                                                                                     |
| [Me][.editControl1.Cursor = System.Windows.Forms.Cursors.Hand] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Showing / Hiding Cursor Caret**

 

The **ShowCaret** and **HideCaret** methods are used to either show / hide the cursor caret.

 

+------------------------------------------------------------------------------------+
| **[\[C#\]]**                     |
|                                                                                    |
| []                               |
|                                                                                    |
| [// Shows the cursor caret.]     |
|                                                                                    |
| [this.editControl1.ShowCaret();] |
|                                                                                    |
| []                               |
|                                                                                    |
| [// Hides the cursor caret.]     |
|                                                                                    |
| [this.editControl1.HideCaret();] |
+------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                   |
|                                                                                                                      |
| []                                                                               |
|                                                                                                                      |
| [\' Shows the cursor caret.]                                       |
|                                                                                                                      |
| [Me][.editControl1.ShowCaret()] |
|                                                                                                                      |
| []                                                                               |
|                                                                                                                      |
| [\' Hides the cursor caret.]                                       |
|                                                                                                                      |
| [Me][.editControl1.HideCaret()] |
+----------------------------------------------------------------------------------------------------------------------+

 

A sample demonstrating the Custom Cursor feature is available in the below sample installation path.

 

***..\\My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Edit.Windows\\Samples\\2.0\\Advanced Editor Functions\\CustomCursorDemo***

[]{#p80} 

[]{#related-topics}

