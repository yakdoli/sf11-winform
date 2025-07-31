---
title: settingmdilayout.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\settingmdilayout.md
created_at: 2025-07-03
---






#### Setting MDI Layout {#setting-mdi-layout style="tab-stops: 0pt"}

**SetMDILayout()**  method is used to set the MDILayout of the child. There are three types of layouts that are available: They are:

[·      ]Cascade

[·      ]Horizontal

[·      ]Vertical

[] 

Cascade:

Cascade layout just cascades the window one by one as shown below:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                |
|                                                                                                                                                                                                 |
| **[DockingManager]**[.SetMDILayout([MDILayout].Cascade);][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 376: Cascaded Layout

                   

 

Horizontal:

This layout arranges the MDI windows in a horizontal manner as shown below:

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                   |
|                                                                                                                                                                                                                                 |
| **[DockingManager]**[.SetMDILayout([MDILayout].Horizontal);][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 377: Horizontal Layout

**[]** 

Vertical Layout:

This layout arranges the MDI windows in a vertical manner as shown below:

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                               |
| **[DockingManager]**[.SetMDILayout([MDILayout].Vertical);][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 378: Vertical Layout

                                                           

 

 

[]{#related-topics}

