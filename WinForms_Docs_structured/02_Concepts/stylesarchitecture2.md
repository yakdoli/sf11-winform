---
title: stylesarchitecture2.md
original_path: WinForms_Docs/02_Concepts/stylesarchitecture2.md
created_at: 2025-08-05
---






#### Styles Architecture {#styles-architecture style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The tree control employs an extensive Styles Architecture, that let users specify node styles globally, specifically for a class of nodes. This is possible by using a style information instance for each class of nodes, represented by a **TreeNodeAdvStyleInfo**. Users will notice that for some of these classes of nodes, the style needs to be declared with a name at the tree level and stored in the tree\'s BaseStyles hatch table.

 

As illustrated below, implicit style inheritance is enforced by the framework while explicit style inheritance can be setup by the programmer. For all styles, explicit inheritance precedes implicit inheritance.

[] 

{border="0"}

[] 

Figure 1153: Implicit and Explicit Style Inheritance

**[]** 

Implicit Style Inheritance

 

When a style is not set in a style info object, it inherits the style from the previous level and so on until it reaches the default global style on top of the hierarchy. This is called implicit style inheritance and is illustrated below.

 

The different levels in the above hierarchy are,

[] 

[·      ]**Node Specific Style**: At the bottom of the hierarchy is the node specific style which lets users specify a style directly on a TreeNodeAdv. Refer Node specific Style.[]

[·      ]**Node\'s Child Style**: Each node also exposes a **ChildStyle** property where you can specify the style for the immediate children of that node. Refer Child Style[ ]for setting style of children nodes[.]

[·      ]**Node Level Styles**: The framework also lets you specify a style for all nodes at a particular level in the tree hierarchy, the top-most level being 1. Refer Node Level Style[ ]for setting node level style settings.

[·      ]**Standard Style or Global Style**: A standard, global style is exposed by the TreeViewAdv control to be applied on all the nodes in the tree. Refer Standard Style[ ]for setting style in a Tree level.

[] 

Explicit Style Inheritance

 

Any StyleInfo instance can also inherit explicitly from a specific named StyleInfo object. This can be done using the BaseStyle property of the TreeNodeAdvStyleInfo type. As noted previously, such named styles should be available in the tree control\'s BaseStyles Collection Editor. You can also add custom styles using this editor.

[] 


  ------------------------ ----------------------------------------
  TreeViewAdv Properties   Description
  BaseStyle                Indicates the base style of the nodes.
  ------------------------ ----------------------------------------


[] 

StandardStyle is the default style for the nodes. It can be edited using **StandardStyle** property. It can also be edited through BaseStyles Collection Editor dialog.

[] 

{border="0"}

[] 

Figure 1154: BaseStyles Collection Editor

 

 

 

 

More:











