---
title: howdoipaintthegroupbaritemimagewithoutscalingtheimage.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howdoipaintthegroupbaritemimagewithoutscalingtheimage.md
created_at: 2025-07-03
---






##### How do I paint the GroupBarItem image without scaling the image? {#how-do-i-paint-the-groupbaritem-image-without-scaling-the-image style="tab-stops: 0pt"}

 

You can draw the image of GroupBarItem (without scaling it), by overriding the DrawGroupBarImage method of the GroupBar. ****

+-------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                      |
|                                                                                                       |
| [// For this callback to occur LargeImageMode must be set to true.\                                   |
|  this.groupBarItem1.LargeImageMode = true;]                       |
|                                                                                                       |
| [protected override void DrawGroupBarImage(Graphics gph, int nindex, Rectangle rcbar)\                |
| {\                                                                                                    |
| Point location = new Point(rcbar.X + 20, rcbar.Y);\                                                   |
| gph.DrawImage(this.VisibleGroupBarItems\[nindex\].Image, new Rectangle(location, new Size(20, 20)));\ |
| }]                                                                |
+-------------------------------------------------------------------------------------------------------+

**** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                             |
| [\' For this callback to occur LargeImageMode must be set to true.][]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                             |
| [Me][.groupBarItem1.LargeImageMode = [True]]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                             |
| [Overrides ][Sub][ ][DrawGroupBarImage(Graphics gph, [Integer] n][index, Rectangle rcbar)] |
|                                                                                                                                                                                                                                                                                                                                             |
| [Dim][ location [As] [New] Point(rcbar.X + 20, rcbar.Y)]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                             |
| [gph.DrawImage([Me].VisibleGroupBarItems(nindex).Image, [New] Rectangle(location, [New] Size(20, 20)))]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                             |
| [End][ ][Sub]                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#_GroupView} 

 

[]{#related-topics}

