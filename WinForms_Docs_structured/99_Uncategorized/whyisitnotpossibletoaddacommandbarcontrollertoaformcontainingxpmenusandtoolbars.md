---
title: whyisitnotpossibletoaddacommandbarcontrollertoaformcontainingxpmenusandtoolbars.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\whyisitnotpossibletoaddacommandbarcontrollertoaformcontainingxpmenusandtoolbars.md
created_at: 2025-07-03
---






#### Why is it not possible to add a CommandBarController to a form containing XP Menus and ToolBars? {#why-is-it-not-possible-to-add-a-commandbarcontroller-to-a-form-containing-xp-menus-and-toolbars style="tab-stops: 0pt"}

[]{#p39}[] 

The CommandBars framework should be used only with the standard .NET Menus / ToolBars and not with the Essential Tools XP Menus. This is because the XP Menus designer infrastructure will freeze the .Net environment.

 

But it is possible to add a CommandBar to a form containing XP Menus through code as shown in the sample screen shot.

[] 

{border="0"}

[] 

Figure 36: CommandBar added to XP Menus and ToolBars

 

[]{#related-topics}

