---
title: throughxpmenusframework.md
original_path: WinForms_Docs/99_Uncategorized/throughxpmenusframework.md
created_at: 2025-08-05
---






#### Through XP Menus Framework {#through-xp-menus-framework style="tab-stops: 0pt"}

[] 

The XP Menus framework provides the flexibility to add detached toolbars that can host any .NET control. These toolbars are detached from the framework, i.e., they cannot participate in user customization. Otherwise, they are seamless in look and feel.

[] 

1.   Right click on the **MainFrameBarManager** component and choose the **Add Detached CommandBar** option to add a detached toolbar.

 

2.   Add that control by dragging and dropping to any .NET control. If you need to host multiple controls, you will need to first add a panel to the CommandBar and then add the controls to this panel.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| [// Declare the controls.]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                 |
| [private][ Syncfusion.Windows.Forms.Tools.XPMenus.[MainFrameBarManager] mainFrameBarManager2;]                                                        |
|                                                                                                                                                                                                                                                                 |
| [private][ Syncfusion.Windows.Forms.Tools.[CommandBar] commandBar2;]                                                                                  |
|                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                 |
| [// Initialize the controls.]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                 |
| [this][.mainFrameBarManager2 = [new] Syncfusion.Windows.Forms.Tools.XPMenus.[MainFrameBarManager]([this]);] |
|                                                                                                                                                                                                                                                                 |
| [this][.commandBar2 = [new] Syncfusion.Windows.Forms.Tools.[CommandBar]();]                                                      |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [// Set the properties.]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                 |
| [this][.mainFrameBarManager2.DetachedCommandBars.Add([this].commandBar2);]                                                                            |
|                                                                                                                                                                                                                                                                 |
| [this][.mainFrameBarManager2.Form = [this];]                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [this][.commandBar1.Text = [\"commandBar1\"];]                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                                     |
| [\' Declare the controls.]                                                                                                                                                        |
|                                                                                                                                                                                                                                     |
| [Private][ mainFrameBarManager2 [As] Syncfusion.Windows.Forms.Tools.XPMenus.MainFrameBarManager]                          |
|                                                                                                                                                                                                                                     |
| [Private][ commandBar2 [As] Syncfusion.Windows.Forms.Tools.CommandBar]                                                    |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                                     |
| [\' Initialize the controls.]                                                                                                                                                     |
|                                                                                                                                                                                                                                     |
| [Me][.mainFrameBarManager2 = [New] Syncfusion.Windows.Forms.Tools.XPMenus.MainFrameBarManager([Me])] |
|                                                                                                                                                                                                                                     |
| [Me][.commandBar2 = [New] Syncfusion.Windows.Forms.Tools.CommandBar()]                                                    |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [\' Set the properties.]                                                                                                                                                          |
|                                                                                                                                                                                                                                     |
| [Me][.mainFrameBarManager2.DetachedCommandBars.Add([Me].commandBar2)]                                                     |
|                                                                                                                                                                                                                                     |
| [Me][.mainFrameBarManager2.Form = [Me]]                                                                                   |
|                                                                                                                                                                                                                                     |
| [Me][.commandBar1.Text = [\"commandBar1\"]]                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}?

[] 

Figure 10: Adding Detached CommandBar Through Design Time Verb

[] 

{border="0"}

[] 

Figure 11: Detached CommandBar created Through MainFrameBarManager

[] 

See Also

[] 

[Through Designer]{.UGHyperlink}[, ]{.UGHyperlink}[Through Code]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

