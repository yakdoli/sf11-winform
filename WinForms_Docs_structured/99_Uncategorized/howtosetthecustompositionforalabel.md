---
title: howtosetthecustompositionforalabel.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtosetthecustompositionforalabel.md
created_at: 2025-07-03
---








  









## How To Set the Custom Position For a Label {#how-to-set-the-custom-position-for-a-label style="tab-stops: 0pt"}

[] 

We can adjust the label position by setting the **Position** property as \'Custom\'. Then, we have to set the Offset values for the X and Y coordinates to specify the label position.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                           |
|                                                                                                                                                          |
| []                                                                                                      |
|                                                                                                                                                          |
| [// Setting custom position for a label ]                                                              |
|                                                                                                                                                          |
| [outerRect.Labels.Add([new] Syncfusion.Windows.Forms.Diagram.[Label]()); ] |
|                                                                                                                                                          |
| [outerRect.Labels\[0\].Text = [\"Rectangle\"]; ]                                              |
|                                                                                                                                                          |
| [outerRect.Labels\[0\].Position = [Position].Custom; ]                                          |
|                                                                                                                                                          |
| [outerRect.Labels\[0\].OffsetX = 50; ]                                                                               |
|                                                                                                                                                          |
| [outerRect.Labels\[0\].OffsetY= 65; ]                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                               |
|                                                                                                                                  |
| []                                                                              |
|                                                                                                                                  |
| [\' Setting custom position for a label ]                                      |
|                                                                                                                                  |
| [outerRect.Labels.Add([New] Syncfusion.Windows.Forms.Diagram.Label()) ] |
|                                                                                                                                  |
| [outerRect.Labels(0).Text = [\"Rectangle\"] ]                         |
|                                                                                                                                  |
| [outerRect.Labels(0).Position = Position.Custom ]                                            |
|                                                                                                                                  |
| [outerRect.Labels(0).OffsetX = 50 ]                                                          |
|                                                                                                                                  |
| [outerRect.Labels(0).OffsetY= 65 ]                                                           |
+----------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p96} 

 

[]{#related-topics}

