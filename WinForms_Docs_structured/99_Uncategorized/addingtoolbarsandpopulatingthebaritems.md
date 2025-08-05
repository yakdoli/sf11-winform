---
title: addingtoolbarsandpopulatingthebaritems.md
original_path: WinForms_Docs/99_Uncategorized/addingtoolbarsandpopulatingthebaritems.md
created_at: 2025-08-05
---






##### Adding Toolbars and Populating the Bar Items {#adding-toolbars-and-populating-the-bar-items style="tab-stops: 0pt"}

[] 

To add a toolbar and populate it with the bar items follow the below steps.

[] 

[·      ]To create a new toolbar, go to the Toolbars tab in the Customize dialog, select New and specify a name (Ex: MainMenu) for the toolbar.

[] 

{border="0"}

**[]** 

Figure 720: Adding a New Toolbar

[] 

[·      ]This will create a new bar component in the designer as shown in the image below. Name this component as \'MainMenu\'. This will also make a corresponding entry in the Toolbars list.

[] 

{border="0"}

**[]** 

Figure 721: MainMenu bar created in the Form Designer

**[]** 

[·      ]Set the toolbar as a main menu, by selecting the **IsMainMenu** option in the BarStyle property of the mainMenuBar component.

[] 

{border="0"}

[] 

Figure 722: Setting BarStyle with IsMainMenu Checked

**[]** 

[·      ]Fill your toolbars with items by simply dragging-and-dropping the items from the Command tab into the toolbars and submenus. To fill the sub menu of the parent bar items, again drag the required bar items inside it.

[] 

{border="0"}

[] 

Figure 723: Filling Toolbars with BarItems

[] 

[·      ]You can drag and dock the toolbars on all four sides of the designer by dragging through the gripper on the left of the toolbar and moving them to any desired position. The toolbars can also be floated. See Toolbar Properties for more details.

[] 


{border="0"} Note: If a toolbar from the mainFrameBarManager and one (or more) from the child forms gets merged (the rules for merging are discussed in the[ ]MDI Merging topic), the BarItems in the toolbar will be ordered based on their MergeOrder property.


[] 

If this is a **ChildFrameBarManager**, all the toolbars (including the main menu) will be floating at design-time. This is because the child toolbars will be docked to the main form rather than to your child form during run-time, and hence, floating avoids polluting your child forms during design-time.

[] 

{border="0"}

[] 

Figure 724: Floating ChildForm Toolbars

**[]** 

See Also

[[]]{.UGHyperlink} 

[Concepts and Features]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

