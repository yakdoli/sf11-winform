---
title: floatingcommandbar.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\floatingcommandbar.md
created_at: 2025-07-03
---






##### [        ]Floating CommandBar {#floating-commandbar style="tab-stops: 0pt"}

[] 

By default, CommandBars can be floated on the form by dragging the gripper on the CommandBar. The properties that enable floating of CommandBars and customization of their settings are discussed below.

[] 

Table 5: CommandBar


  --------------------- -------------------------------------------------------------
  CommandBar Property   Description
  DisableFloating       Indicates whether the CommandBar is allowed to float.
  FloatModeWrapping     Indicates whether the CommandBar should wrap when floating.
  FloatBounds           Gets / sets the bounds of a floating CommandBar.
  Floating              Returns the current dock / float state of the CommandBar.
  --------------------- -------------------------------------------------------------


[] 

The float state of the CommandBar can be disabled by setting the **DisableFloating** property to \'True\'.

 

Setting **FloatModeWrapping** property to \'True\', wraps a floating CommandBar when it is resized to less than it\'s maximum length. The DisableFloating property must be set to \'False\' for this.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                         |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                   |
|                                                                                                                                                                                                                        |
| [this][.commandBar1.DisableFloating = [false];]                                                              |
|                                                                                                                                                                                                                        |
| [this][.commandBar1.FloatModeWrapping = [true];]                                                             |
|                                                                                                                                                                                                                        |
| [this][.commandBar1.FloatBounds = [new] System.Drawing.[Rectangle](419, 303, 183, 47);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                           |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [Me][.commandBar1.DisableFloating = [False]]                                       |
|                                                                                                                                                                                              |
| [Me][.commandBar1.FloatModeWrapping = [True]]                                      |
|                                                                                                                                                                                              |
| [Me][.commandBar1.FloatBounds = [New] System.Drawing.Rectangle(419, 303, 183, 47)] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 12: CommandBar in Float State

**[]** 

A sample which demonstrates the Floating CommandBar is available in the below sample installation path.

 

..My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\CommandBars Package\\CommandBars

[] 

See Also

[] 

[Docking CommandBar]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

