---
title: hostingchildcontrols.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\hostingchildcontrols.md
created_at: 2025-07-03
---






#### Hosting Child Controls[]{#p24} {#hosting-child-controls style="tab-stops: 0pt"}

[] 

Child controls can be easily hosted by the CommandBar through designer as well as through code. This can be done by selecting the client controls from the toolbox and dropping it onto the particular CommandBar. The control will be resized to fit the CommandBar\'s client bounds.

 

A CommandBar can host a single control / multiple controls. This can be done as follows.

 

Single Control

[] 

You can drag-and-drop the single client control onto the CommandBar.

**[]** 

Multiple Controls

[] 

To accommodate multiple controls, place the controls within a Panel control and set it to be the CommandBar\'s client.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                              |
|                                                                                                                                                             |
| []                                                                                                        |
|                                                                                                                                                             |
| [this][.commandBar1.Controls.Add([this].panel1);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                     |
|                                                                                                                                                        |
| []                                                                                                   |
|                                                                                                                                                        |
| [Me][.commandBar1.Controls.Add([Me].panel1)] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 26: CommandBar Hosting Multiple Controls (Label and ComboBox)

[] 

The method associated with the above property is given below.

[] 


  ------------------------ -------------------------------------------------------------------------------------------
  Method                   Description
  CalcChildControlBounds   Calculates the client control bounds for the specified CommandBar size and dock position.
  ------------------------ -------------------------------------------------------------------------------------------


[]{#related-topics}

