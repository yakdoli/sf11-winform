---
title: customizingtemplateswithexpressionblend.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\customizingtemplateswithexpressionblend.md
created_at: 2025-07-03
---






#### [Customizing templates with Expression Blend]{#_Ref262127604} {#customizing-templates-with-expression-blend style="tab-stops: 0pt"}

The steps to customize templates by using Expression Blend are as follows:

1.   Create a new application in Expression Blend. Refer .

The following are the default resources, which are used for HierarchyNavigator control that can be changed in Expression Blend.

{border="0"}

 

Figure 591: Default Resources for Hierarchy Navigator

**[]** 

2.   Right-click the **HierarchyNavigator** control and select **Edit**, then select **Style**, and type a name.

[] 

{border="0"}

 

Figure 592: HierarchyNavigator in Expression Blend

 

3.   Right-click the **HierarchyNavigatorItemsControl** and select **Edit**, then select **Template**, and then select **Edit a Copy**, to edit the Refresh button, the History button, or the overall content. Additional styles (templates) can be used to edit a template available in the **HierarchyNavigatorItemsControl** class.

{border="0"}

 

Figure 593: HierarchyNavigatorItemsControl in Expression Blend

[] 

4.   Right-click the **Part_HierarchyNavigatorItemsControl** and select **Edit**, and then select **Additional Templates**. A list of additional styles to edit will be displayed. Figure 40 displays the style names.

 

{border="0"}

 

Figure 594: Edit Additional Templates

[{border="0"} ]{#_Ref261964963}

 

Figure 595: Additional styles illustrated

**[]** 

5.   Storyboards used in the VisualStateManager of every control are easy to customize and manage.

6.   For example, the HierarchyNavigatorItem control has two states: Normal and MouseOver. This is available on the States window, which can be accessed by clicking the **Window** menu and selecting **States**.

 

 

{border="0"}

 

Figure 596: States window

**[]** 

7.   Click the Visual State name, to edit the storyboard.

{border="0"}

 

Figure 597: Editing the storyboard

**[]** 

More:







