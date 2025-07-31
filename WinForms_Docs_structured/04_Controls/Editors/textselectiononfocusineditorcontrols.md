---
title: textselectiononfocusineditorcontrols.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Editors\textselectiononfocusineditorcontrols.md
created_at: 2025-07-03
---








  









## Text Selection On Focus in Editor Controls {#text-selection-on-focus-in-editor-controls style="tab-stops: 0pt"}

The Editor controls can behave as standard text box when selected. With TextSelectionOnFocus property, the cursor can be placed at the position of the mouse pointer, when Editors are clicked initially.

[] 

[·      ]The Editor controls when clicked initially ensure selection of the entire text and on subsequent

[·      ]Click the cursor would be placed at the position of mouse pointer.

[·      ]When the property TextSelectionOnFocus is set to false, the entire text is not selected initially but the cursor would be placed at the position of mouse pointer.

[] 

The following code snippets illustrate this:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][syncfusion][:][DoubleTextBox ][TextSelectionOnFocus][=\"true\"\>\< /][syncfusion][:][DoubleTextBox][\>]  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][syncfusion][:][DoubleTextBox ][TextSelectionOnFocus][=\"false\"\>\< /][syncfusion][:][DoubleTextBox][\>] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [DoubleTextBox][ doubleTextBox = [new] [DoubleTextBox]();] |
|                                                                                                                                                                                                                                 |
| [doubleTextBox.TextSelectionOnFocus = [true];]                                                                                                         |
|                                                                                                                                                                                                                                 |
| [doubleTextBox.TextSelectionOnFocus = [false];]                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[]*** 

{border="0"}

***[]*** 

Figure 1055: DoubleTextBox with TextSelectionOnFocus set to true

***[]*** 

{border="0"}

***[]*** 

Figure 1056: DoubleTextBox with TextSelectionOnFocus set to false

 

[]{#related-topics}

