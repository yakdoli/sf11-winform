---
title: addingcontrolstothescrollbar1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingcontrolstothescrollbar1.md
created_at: 2025-07-03
---






##### Adding Controls to the ScrollBar {#adding-controls-to-the-scrollbar style="tab-stops: 0pt"}

[] 

There are two collection properties available for the ScrollersFrame which lets you add controls before or after the scrollbars. They are **ControlsAfter** and **ControlsBefore** properties.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                      |
|                                                                                                                                                                                                     |
| []                                                                                                                                                 |
|                                                                                                                                                                                                     |
| [//Adding controls to the scrolls through ControlsAfter or ControlsBefore]                                                                        |
|                                                                                                                                                                                                     |
| [this][.scrollersFrame2.HorizontalScroller.ControlsBefore.Add(buttonAdv3);]                                    |
|                                                                                                                                                                                                     |
| [this][.scrollersFrame2.VerticalScroller.ControlsAfter.Add(buttonAdv1);]                                       |
|                                                                                                                                                                                                     |
| [this][.scrollersFrame2.VerticalScroller.ControlsAfter.Add(buttonAdv2);][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                            |
|                                                                                                                                                               |
| []                                                                                                          |
|                                                                                                                                                               |
| [\'Adding controls to the scrolls through ControlsAfter or ControlsBefore ]                                 |
|                                                                                                                                                               |
| [Me][.scrollersFrame2.HorizontalScroller.ControlsBefore.Add(buttonAdv3)] |
|                                                                                                                                                               |
| [Me][.scrollersFrame2.VerticalScroller.ControlsAfter.Add(buttonAdv1)]    |
|                                                                                                                                                               |
| [Me][.scrollersFrame2.VerticalScroller.ControlsAfter.Add(buttonAdv2)]    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

The below images illustrates the controls that are added, before and after the scrolls.

[] 

{border="0"}

[] 

Figure 1413: Controls added before and after the ScrollBars

**[]** 

See Also

[] 

[[Visual Styles]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Visual_Styles_1)[]

 

 

[]{#related-topics}

