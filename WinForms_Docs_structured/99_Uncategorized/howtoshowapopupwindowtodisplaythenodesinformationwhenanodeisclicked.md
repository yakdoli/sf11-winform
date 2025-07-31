---
title: howtoshowapopupwindowtodisplaythenodesinformationwhenanodeisclicked.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoshowapopupwindowtodisplaythenodesinformationwhenanodeisclicked.md
created_at: 2025-07-03
---








  









## How to show a popup window to display the node\'s information when a node is clicked?[] {#how-to-show-a-popup-window-to-display-the-nodes-information-when-a-node-is-clicked style="tab-stops: 0pt"}

[] 

When a node is clicked, the **OnClientNodeClick** public event is handled. Using this event we can display a popup window.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<script language=[\"javascript\"] type=[\"text/javascript\"]\>]      |
|                                                                                                                                                          |
| []                                                                                                                   |
|                                                                                                                                                          |
| [Function][ OnDiagramMouseDown([ByVal] oData)] |
|                                                                                                                                                          |
| [{]                                                                                                                  |
|                                                                                                                                                          |
| [      alert(oData.El.InModelName); // shows alert window [with] node name]                     |
|                                                                                                                                                          |
| [}]                                                                                                                  |
|                                                                                                                                                          |
| []                                                                                                                   |
|                                                                                                                                                          |
| [\</script\>]                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 76


{border="0"}[Note:] Using the OnDiagramMouseDown function, users can write their own code to show the popup window or do some other things. Data.El is an HTML \<IMG\> element.


[]{#related-topics}

