---
title: restrictdockingoftoolbaradvforaspecificposition1.md
original_path: WinForms_Docs/99_Uncategorized/restrictdockingoftoolbaradvforaspecificposition1.md
created_at: 2025-08-05
---






#### Restrict Docking of ToolBarAdv for a specific position {#restrict-docking-of-toolbaradv-for-a-specific-position style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; tab-stops: 0pt"}

You can restrict docking of ToolBarAdv by setting the following properties. Each will restrict docking at corresponding positions in ToolBarManager.

 

[·      ]**CanDockAtLeft---**restricts docking at the left.

[·      ]**CanDockAtTop---**restricts docking at the left.

[·      ]**CanDockAtRight---**restricts docking at the left.

[·      ]**CanDockAtBottom---**restricts docking at the left.

 

Following code restricts docking at the top:

[[]]{.Heading3Char} 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][shared][:][ToolBarManager][ x][:][Name][=\"toolBarManager\"][ CanDockAtTop][=\"False\"][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                              [ \>\</][shared][:][ToolBarManager][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[[]]{.Heading3Char} 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                       |
|                                                                                                                                                                                                    |
| [ToolBarManager][ toolBarManager = [new] [ToolBarManager]();] |
|                                                                                                                                                                                                    |
| [            toolBarManager.CanDockAtTop = [false];]                                                                                      |
|                                                                                                                                                                                                    |
| []                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[[    ]]{.Heading3Char}

 

[]{#related-topics}

