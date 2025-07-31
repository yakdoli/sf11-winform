---
title: howtoshowhidetheexpandersinanolapchart.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\howtoshowhidetheexpandersinanolapchart.md
created_at: 2025-07-03
---






##### How to show/hide the expanders in an OlapChart? {#how-to-showhide-the-expanders-in-an-olapchart style="tab-stops: 0pt"}

[] 

The visibility of the expanders in the OlapChart can be toggled by using the ShowExpanders property available in the OlapReport.

The following code snippet describes this in detail:

 

+--------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                         |
|                                                                                                                    |
|                                                                                                                    |
|                                                                                                                    |
| [this].olapchart1.OlapDataManager.CurrentReport.ShowExpanders = [false]; |
|                                                                                                                    |
|                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                       |
|                                                                                                                  |
|                                                                                                                  |
|                                                                                                                  |
| [ Me].olapchart1.OlapDataManager.CurrentReport.ShowExpanders = [False] |
|                                                                                                                  |
|                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------+

[] 

The following image shows an OlapChart with expanders disabled:

 

{border="0"}

Figure 63: Expanders Disabled in an OlapChart[]

[] 


{border="0"}Note: Since this property interacts with the OlapDataManager you need to assign this property before the call to DataBind() or DataBind() method in the OlapChart and should be invoked after changing this property to see this in effect.


[] 

[]{#related-topics}

