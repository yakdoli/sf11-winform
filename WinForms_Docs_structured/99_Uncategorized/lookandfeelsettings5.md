---
title: lookandfeelsettings5.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\lookandfeelsettings5.md
created_at: 2025-07-03
---






##### Look and Feel Settings {#look-and-feel-settings style="tab-stops: 0pt"}

 

The look and feel of the treeview can be controlled using AutoFormat options and also by defining custom ItemLook instances in ItemLooks collection or by editing default ItemLook settings in DefaultItemLook and DefaultDisabledItemLook properties.

 

The topics discussed are given below.

[]{#p290} 

###### 5.3.1.2.13.1        AutoFormat Styles {#autoformat-styles style="tab-stops: 0pt"}

[] 

The TreeView control provides pre-defined set of styles that can be applied to your control just on a click of the button. You can set the desired look and feel for the control that includes some popular styles too.

 

The Autoformat window can be opened by right clicking the control and selecting the \'Auto Format\...\' option opens the following Auto Format dialog box.

[] 

{border="0"}

Figure 193

[] 

The left pane lists the various pre-defined style scheme that are available. The right pane shows the preview of the currently selected scheme. Select the required style and click OK to apply the selected scheme to the control.

[] 

Example of a popular look and feel

[] 

The following image shows the TreeView with **MSDN** style setting.

[] 

{border="0"}

Figure 194

[] 

The new built-in format skins added for TreeView are as follows.

[] 

[·      ]Outlook

[] 

{border="0"}

Figure 195

[] 

[·      ]Vista

[] 

{border="0"}

Figure 196

 

[] 

[·      ]Blue

[] 

{border="0"}

Figure 197

 

[] 

[·      ]Black

[] 

{border="0"}

Figure 198

 

[] 

[·      ]Brown

[] 

{border="0"}

Figure 199

[] 

[·      ]Green

[] 

{border="0"}

Figure 200

 

###### []{#_ItemLook_Settings}5.3.1.2.13.2        ItemLook Settings {#itemlook-settings style="tab-stops: 0pt"}

 

 

The ItemLooks Collection Editor contains Default property settings that includes the default look and disabled looks, and Custom properties that allows you to customize the look and feel accordingly.

 

The ItemLooks properties are given below.

 


+-------------------+-------------------------------------------------------------------------------------------------------------+
| Property          | Description                                                                                                 |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| ID                | Specifies the id of the item looks settings.                                                                |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| LeftImageHeight   | Specifies the height of the left image.                                                                     |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| LeftImageWidth    | Specifies the width of the right image.                                                                     |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| RightImageHeight  | Specifies the height of the right image.                                                                    |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| RightImageWidth   | Specifies the width of the right image.                                                                     |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| TextPaddingBottom | Specifies the space in pixels around the node text.                                                         |
+-------------------+                                                                                                             |
| TextPaddingLeft   |                                                                                                             |
+-------------------+                                                                                                             |
| TextPaddingRight  |                                                                                                             |
+-------------------+                                                                                                             |
| TextPaddingTop    |                                                                                                             |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| StateDataActive   | Specifies the various look and feel options for different states such as default, active, hover and expand. |
+-------------------+                                                                                                             |
| StateDataDefault  |                                                                                                             |
+-------------------+                                                                                                             |
| StateDataExpanded |                                                                                                             |
+-------------------+                                                                                                             |
| StateDataHover    |                                                                                                             |
+-------------------+-------------------------------------------------------------------------------------------------------------+


 

The ID specifies the id of the look. The text padding and the image\'s height and width can be set for the tree nodes.

The StateDefault, StateActive, StatePushed and StateHover categories contain the following CSS class properties that define styles for treeview nodes.

 


  ----------------------------- ----------------------------------------------------------------
  Property                      Description
  CheckBoxCellCSSClass          Specifies styles for the cell containing the checkbox.
  CheckBoxCssClass              Specifies styles for the checkbox.
  ItemCSSClass                  Specifies styles for the items.
  LeftImageCellCSSClass         Specifies styles for the left image.
  LeftImageContainerCSSClass    Specifies styles for the left image container.
  LeftImageCSSClass             Specifies styles for the left image.
  LeftImageUrl                  Specifies the path of the left image to be used for the node.
  RightImageCellCSSClass        Specifies styles for the cell holding the arrow image.
  RightImageContainerCSSClass   Specifies styles for the right image container.
  RightImageCSSClass            Specifies styles for the right image.
  RightImageUrl                 Specifies the path of the right image to be used for the node.
  TextCellCssClass              Specifies the styles for the cell holding the text.
  TextContainerCssClass         Specifies the styles for the container for the text cell.
  ----------------------------- ----------------------------------------------------------------


 

Images to the left and right of the text can be set, by assigning the respective image name to the corresponding property of the look. Make sure to set the ImageBaseUrl property of the TreeView.

 

Note: The ImageBaseUrl property allows you to specify the path from where the images have to be obtained. By default it is set to \'images\' folder. You can either create a folder called \'images\' and add all the images to be set using the item looks, else use a custom folder and rename the ImageBaseUrl property.

 

The styles can be applied to individual nodes by setting the id of the look to the Look and LookDisabled (for disabled nodes with Disabled property set to True) properties of the required tree nodes in the Designer dialog box. This way the styles will be applied only to those nodes.

 


  --------------- ---------------------------------------------------
  Item Property   Description
  Look            Specifies the look for a node.
  LookDisabled    Specifies the look for an item in disabled state.
  --------------- ---------------------------------------------------


 

See Also

 

[CSS Styles]{.UGHyperlink}[, ]{.UGHyperlink}[Default Looks]{.UGHyperlink}[, ]{.UGHyperlink}[Custom Looks]{.UGHyperlink}[]{.UGHyperlink}

[]{#p292} 

[]{#_Default_Looks}5.3.1.2.13.2.1     Default Looks

[] 

Setting styles for Active and Disabled states

[] 

TreeView comes with some default look and feels that requires you to apply just by assigning the styles. It also enables to set looks for items in active and disabled states. Styles applied for these states can be default styles or for some actions like node expand and mouse hover.

[] 

{border="0"}

Figure 201

[] 

The below sample code snippets define the default styles for the items in active state on expanding the nodes, on mouse over and the default style settings for the treeview nodes, and the default disabled style.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[aspx\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][DefaultItemLookDisabled][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [  [\<][StateDataActive] [LeftImageCellCSSClass ][= \"tvImgCell\"] [ItemRowCSSClass ][= \"tvItemRow\"] [LeftImageCSSClass ][= \"tvImg\"] [ItemCSSClass ][= \"tvItemDisabled\"] [CheckBoxCellCSSClass ][= \"tvCheckCell\"] [RightImageCSSClass ][= \"tvArr\"] [TextCellCSSClass ][= \"tvTextCell\"] [CheckBoxCSSClass ][= \"tvCheck\"] [RightImageContainerCSSClass ][= \"tvArrCont\"] [RightImageCellCSSClass ][= \"tvArrCell\"] [LeftImageContainerCSSClass ][= \"tvImgCont\"] [TextContainerCSSClass ][= \"tvTextCont\"\>\</][StateDataActive][\>]]                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [  ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [  \<][StateDataHover][ [LeftImageCellCSSClass ][= \"tvImgCell\"] [ItemRowCSSClass ][= \"tvItemRow\"] [LeftImageCSSClass ][= \"tvImg\"] [ItemCSSClass ][= \"tvItemDisabled\"] [CheckBoxCellCSSClass ][= \"tvCheckCell\"] [RightImageCSSClass ][= \"tvArr\"] [TextCellCSSClass ][= \"tvTextCell\"] [CheckBoxCSSClass ][= \"tvCheck\"] [RightImageContainerCSSClass ][= \"tvArrCont\"] [RightImageCellCSSClass ][= \"tvArrCell\"] [LeftImageContainerCSSClass ][= \"tvImgCont\"] [TextContainerCSSClass ][= \"tvTextCont\"\>\</][StateDataHover][\>]]     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [  ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [  \<][StateDataDefault][ [LeftImageCellCSSClass ][= \"tvImgCell\"] [ItemRowCSSClass ][= \"tvItemRow\"] [LeftImageCSSClass ][= \"tvImg\"] [ItemCSSClass ][= \"tvItemDisabled\"] [CheckBoxCellCSSClass ][= \"tvCheckCell\"] [RightImageCSSClass ][= \"tvArr\"] [TextCellCSSClass ][= \"tvTextCell\"] [CheckBoxCSSClass ][= \"tvCheck\"] [RightImageContainerCSSClass ][= \"tvArrCont\"] [RightImageCellCSSClass ][= \"tvArrCell\"] [LeftImageContainerCSSClass ][= \"tvImgCont\"] [TextContainerCSSClass ][= \"tvTextCont\"\>\</][StateDataDefault][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\</][DefaultItemLookDisabled][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]Note that the default CSS style sheet used by the treeview control is available at the following location:**/Syncfusion/Resources/Toolsweb/CSS/treeview_default.css**.[ ]This CSS file defines the following CSS styles.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[StyleSheet\]]**                                                                                                                                       |
|                                                                                                                                                                                                                |
| []                                                                                                                                            |
|                                                                                                                                                                                                                |
| [.tvView]                                                                                                                                   |
|                                                                                                                                                                                                                |
| [{]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [        [border]: [1px] [solid] [gray];]                               |
|                                                                                                                                                                                                                |
| [        [padding-top] : [4px];]                                                                                  |
|                                                                                                                                                                                                                |
| [}]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [.tvView][ [.tvTextCont]]                                        |
|                                                                                                                                                                                                                |
| [{]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [        [font-family]: [tahoma]; ]                                                                               |
|                                                                                                                                                                                                                |
| [        [font-size]: [11px];]                                                                                    |
|                                                                                                                                                                                                                |
| [        [padding]: [2px];]                                                                                       |
|                                                                                                                                                                                                                |
| [        [cursor]: [default];]                                                                                    |
|                                                                                                                                                                                                                |
| [}]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [.tvView][ [.tvItemHover] [.tvTextCont]]  |
|                                                                                                                                                                                                                |
| [{]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [        [text-decoration]:[underline];]                                                                          |
|                                                                                                                                                                                                                |
| [}]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [.tvView][ [.tvItemActive] [.tvTextCont]] |
|                                                                                                                                                                                                                |
| [{]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [        [color]: [white];]                                                                                       |
|                                                                                                                                                                                                                |
| [}]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [.tvView][ [.tvItemActive] [.tvTextCell]] |
|                                                                                                                                                                                                                |
| [{]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [        [background-color]: [gray];]                                                                             |
|                                                                                                                                                                                                                |
| [}]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [.tvView][ [.tvImgCell]]                                         |
|                                                                                                                                                                                                                |
| [{]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [        [padding-right]:[3px];]                                                                                  |
|                                                                                                                                                                                                                |
| [}]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [.tvView][ [.tvNodeEdit]]                                        |
|                                                                                                                                                                                                                |
| [{]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [        [border]:[1px] [gray] [solid];]                                |
|                                                                                                                                                                                                                |
| [        [font-family]: [tahoma]; ]                                                                               |
|                                                                                                                                                                                                                |
| [        [font-size]: [11px];]                                                                                    |
|                                                                                                                                                                                                                |
| [}]                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#_Custom_Looks}5.3.1.2.13.2.2     Custom Looks

[] 

We can easily customize the default look of the treeview nodes. **Custom Looks** properties in **ItemLooks Collection Editor** allows you to apply custom looks to your treeview.

[] 

Using Designer

[] 

ItemLooks Editor lets you easily create the item looks for the items. If you create your own ItemLooks then this will override the default look.

[] 

{border="0"}

Figure 202

 

[] 

1.   Give the CSS class names in the appropriate CSS styles.

50.  Once you given the styles in the item look editor, in HTML view you can see the below code like this.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][cc1][:][treeview][ [id][=\"TreeView2\"] [runat][=\"server\"] [CssClass][=\"TreeView\"\>]]                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [  [\<][itemlooks][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [    [\<][cc1][:][TreeViewItemLook] [ID][=\"Look1\"\>]]                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][StateDataActive][ [ItemRowCSSClass ][= \"Act_ItemRowCss\"] [RightImageCSSClass ][= \"Act_RightImageCss\"] [LeftImageURL ][= \"folder.gif\"]  [TextContainerCSSClass ][= \"Act_TextCont\"\>  \</][StateDataActive][\>]]        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][StateDataDefault][ [ItemRowCSSClass ][= \"Def_ItemRowCss\"] [RightImageCSSClass ][= \"Def_RightImageCss\"] [LeftImageURL ][= \"folder.gif\"] [TextContainerCSSClass ][= \"Def_TextCont\"\> \</][StateDataDefault][\>]]        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][StateDataExpanded][ [ItemRowCSSClass ][= \"Def_ItemRowCss\"] [RightImageCSSClass ][= \"Def_RightImageCss\"] [LeftImageURL ][= \"folder_open.gif\"] [TextContainerCSSClass ][= \"Def_TextCont\"\> \</][StateDataExpanded][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][StateDataHover][ [ItemRowCSSClass ][= \"Hov_ItemRowCss\"] [RightImageCSSClass ][= \"Hov_RightImageCss\"] [LeftImageURL ][= \"folder.gif\"] [TextContainerCSSClass ][= \"Hov_TextCont\"\> \</][StateDataHover][\>]]            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [    [\</][cc1][:][TreeViewItemLook][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [  [\</][itemlooks][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\</][cc1][:][treeview][\>]                                                                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

51.  Set the Look ID to **Look** property for the tree nodes to which the specified styles should be applied. To apply styles for the disabled nodes, set the look ID to the **LookDisabled** property.

[] 

{border="0"}

[] 

Figure 203: Designer image

[] 

Using Code

[] 

ItemLooks can be created and added to the treeview. Here we can see how the ItemLooks instance can be created and added programmatically. And these ItemLooks can be applied to the treeview items like below.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                      |
|                                                                                                                                       |
| []                                                                                                |
|                                                                                                                                       |
| [TreeViewItemLook look=[new] TreeViewItemLook();]            |
|                                                                                                                                       |
| [look.ID=[\"RootNodeLook\"];]                              |
|                                                                                                                                       |
| [look.StateDataDefault.ItemCSSClass=[\"Def_ItemCss\"];]    |
|                                                                                                                                       |
| [look.StateDataExpanded.ItemCSSClass = [\"Exp_ItemCss\"];] |
|                                                                                                                                       |
| [look.StateDataHover.ItemCSSClass = [\"Hov_ItemCss\"];]    |
|                                                                                                                                       |
| [TreeView1.ItemLooks.Add(RootItemsLook);]                                         |
|                                                                                                                                       |
| [TreeViewNode node= [new] TreeViewNode();]                   |
|                                                                                                                                       |
| [node.Text = [\"Essential Chart\"];]                       |
|                                                                                                                                       |
| [node.Look=[\"RootNodeLook\"];]                            |
+---------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [Private][ look [As] TreeViewItemLook = [New] TreeViewItemLook()] |
|                                                                                                                                                                                                                                  |
| [Private][ look.ID=[\"RootNodeLook\"]]                                               |
|                                                                                                                                                                                                                                  |
| [Private][ look.StateDataDefault.ItemCSSClass=[\"Def_ItemCss\"]]                     |
|                                                                                                                                                                                                                                  |
| [Private][ look.StateDataExpanded.ItemCSSClass = [\"Exp_ItemCss\"]]                  |
|                                                                                                                                                                                                                                  |
| [Private][ look.StateDataHover.ItemCSSClass = [\"Hov_ItemCss\"]]                     |
|                                                                                                                                                                                                                                  |
| [TreeView1.ItemLooks.Add(RootItemsLook)]                                                                                                                                     |
|                                                                                                                                                                                                                                  |
| [Private][ node [As] TreeViewNode = [New] TreeViewNode()]         |
|                                                                                                                                                                                                                                  |
| [Private][ node.Text = [\"Essential Chart\"]]                                        |
|                                                                                                                                                                                                                                  |
| [Private][ node.Look=[\"RootNodeLook\"]]                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### []{#_CSS_Styles_1}5.3.1.2.13.3        CSS Styles {#css-styles style="tab-stops: 0pt"}

[] 

The TreeView control comprises of distinct segments for which css style definitions can be set. The default styles of the layered treeview structure can be replaced with custom style settings by applying the css class names to the corresponding style properties.

[] 

Structure of TreeView control

[] 

The treeview structure consists of a single level of outer root segment and 2 item-level segments as shown below. Every item added to the treeview contains the item row segment for which styles can be applied using the appropriate properties.

[] 

{border="0"}

[] 

Figure 204: Structure of TreeView control

[] 

The below table lists the item-level segments and their corresponding **CSS** properties whose settings affect their styles.

[] 


  -------------------- ----------------- --------------------------------
  Element              Property          Default Value (CSS Class Name)
  Root element         CSSClass          tvView
  Root panel element   ItemRowCSSClass   tvItemRow
  -------------------- ----------------- --------------------------------


[] 

Customizing TreeView Root-level segments

[] 

To customize the look and feel of one of the above segments, simply create a custom css style and associate it with the CSS property corresponding to that segment.

[] 

{border="0"}

[] 

Figure 205: TreeView with css settings for the root elements

**[]** 

The CSS properties set to the custom CSS values and the style definitions are shown below.

[] 


  ----------------- -------------------------------
  Property          Value (Custom CSS Class Name)
  CSSClass          Def_CSSClass
  ItemRowCSSClass   Def_ItemRowCSS
  ----------------- -------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Css Styles\]]**                                                                                          |
|                                                                                                                                                                                 |
| []                                                                                                           |
|                                                                                                                                                                                 |
| [Def_CSSClass]                                                                                               |
|                                                                                                                                                                                 |
| [{]                                                                                                                         |
|                                                                                                                                                                                 |
| [  [border]: [#333365] [2px] [solid];  ] |
|                                                                                                                                                                                 |
| [  [cursor]: [default];]                                                           |
|                                                                                                                                                                                 |
| [  [background-color]:[#DBE2F2];]                                                  |
|                                                                                                                                                                                 |
| [}]                                                                                                                         |
|                                                                                                                                                                                 |
| [.Def_ItemRowCSS]                                                                                            |
|                                                                                                                                                                                 |
| [{]                                                                                                                         |
|                                                                                                                                                                                 |
| [  [padding-top]:[2px];]                                                           |
|                                                                                                                                                                                 |
| [}]                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Structure of the treeview Item

**[]** 

A single tree item is segregated into different image and text sections, the look for all of which can again be controlled through their corresponding CSS property settings. An item consists of showline, check box, text, left and right image as shown below.

[] 

{border="0"}

[] 

Figure 206: Structure of a treeview Item

[] 

The below table lists the item-level segments and their corresponding CSS properties whose settings affect their styles.

[] 


  -------------------------- ----------------------------- --------------------------------
  Element                    Property                      Default Value (CSS Class Name)
  ControlRootTableCSSClass   ItemCSSClass                  tvItem
  Checkbox cell              CheckBocCellCssClass          tvCheckCell
  Checkbox                   CheckBoxCssClass              tvCheck
  Left image cell            LeftImageCellCSSClass         tvImgCell
  Left image container       LeftImageContainerCSSClass    tvImgCont
  Left image                 LeftImageCSSClass             tvImg
  Text cell                  TextCellCssClass              tvTextCell
  Text container             TextContainerCssClass         tvTextCont
  Right image cell           RightImageCellCSSClass        tvArrCell
  Right image container      RightImageContainerCSSClass   tvArrCont
  Right image                RightImageCSSClass            tvArr
  -------------------------- ----------------------------- --------------------------------


[] 

Customizing TreeView Item-level segments

[] 

The following section shows some custom styles applied on the different item-level segments and a screenshot of the resulting look.

[] 


+---------------------------------------------------------------------------------------+-----------------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Image                                                                                 | Property                    | Custom CSS Style    | CSS Definition                                                                                                                                              |
+---------------------------------------------------------------------------------------+-----------------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                    | ItemCSSClass                | Def_ItemCSS         | [.Def_ItemCSS]                                                                                           |
|                                                                                       |                             |                     |                                                                                                                                                             |
| {border="0"}                                            |                             |                     | [{]                                                                                                                     |
|                                                                                       |                             |                     |                                                                                                                                                             |
| []  |                             |                     | [  [padding-top]:[3px];]                                                       |
|                                                                                       |                             |                     |                                                                                                                                                             |
| TreeView with style settings for checkbox                                             |                             |                     | [  [padding-left]:[9px];]                                                      |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [  [padding-right]:[5px];]                                                     |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [  [padding-bottom]:[3px]; ]                                                   |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [}]                                                                                                                     |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [.CheckBoxCssClass]                                                                                      |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [{  ]                                                                                                                   |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [  [background-color]:[#ffbb6f]; ]                                             |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [  [border]:[1px] [solid] [black]; ] |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [}]                                                                                                                     |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [.CheckBoxCellCssClass]                                                                                  |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [{]                                                                                                                     |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [   [padding]:[5px];         ]                                                 |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [}]                                                                                                                     |
|                                                                                       +-----------------------------+---------------------+                                                                                                                                                             |
|                                                                                       | CheckBoxCellCssClass        | Def_CheckBoxCellCSS |                                                                                                                                                             |
|                                                                                       +-----------------------------+---------------------+                                                                                                                                                             |
|                                                                                       | CheckBoxCssClas             | Def_CheckBoxCSS     |                                                                                                                                                             |
+---------------------------------------------------------------------------------------+-----------------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []  | LeftImageCellCSSClass       | LeftImgCellCSS      | [.LeftImgCellCSS]                                                                                        |
|                                                                                       |                             |                     |                                                                                                                                                             |
| {border="0"}                                            |                             |                     | [{]                                                                                                                     |
|                                                                                       |                             |                     |                                                                                                                                                             |
| []  |                             |                     | [  [border]:[1px] [solid] [black]; ] |
|                                                                                       |                             |                     |                                                                                                                                                             |
| TreeView with style settings for left image                                           |                             |                     | [}]                                                                                                                     |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [.LeftImgContCSS]                                                                                        |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [{]                                                                                                                     |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [  [background-color]:[#ffbb6f]; ]                                             |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [  [padding]:[6px];          ]                                                 |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [}]                                                                                                                     |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [.LeftImgCSS]                                                                                            |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [{]                                                                                                                     |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [  [height]:[17px];]                                                           |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [  [width]:[16px];]                                                            |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [}]                                                                                                                     |
|                                                                                       +-----------------------------+---------------------+                                                                                                                                                             |
|                                                                                       | LeftImageContainerCSSClass  | LeftImgContCSS      |                                                                                                                                                             |
|                                                                                       +-----------------------------+---------------------+                                                                                                                                                             |
|                                                                                       | LeftImageCSSClass           | LeftImgCSS          |                                                                                                                                                             |
+---------------------------------------------------------------------------------------+-----------------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []  | RightImageCellCSSClass      | RightImgCellCSS     | [.RightImgCellCSS]                                                                                       |
|                                                                                       |                             |                     |                                                                                                                                                             |
| {border="0"}                                            |                             |                     | [{]                                                                                                                     |
|                                                                                       |                             |                     |                                                                                                                                                             |
| []  |                             |                     | [  [border]:[1px] [solid] [black]; ] |
|                                                                                       |                             |                     |                                                                                                                                                             |
| TreeView with style settings for right image                                          |                             |                     | [}]                                                                                                                     |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [.RightImgContCSS]                                                                                       |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [{]                                                                                                                     |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [  [background-color]:[#ffbb6f]; ]                                             |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [  [padding]:[6px];          ]                                                 |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [}]                                                                                                                     |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [.RightImgCSS]                                                                                           |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [{]                                                                                                                     |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [  [height]:[17px];]                                                           |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [  [width]:[16px];]                                                            |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [}]                                                                                                                     |
|                                                                                       +-----------------------------+---------------------+                                                                                                                                                             |
|                                                                                       | RightImageContainerCSSClass | RightImgContCSS     |                                                                                                                                                             |
|                                                                                       +-----------------------------+---------------------+                                                                                                                                                             |
|                                                                                       | RightImageCSSClass          | RightImgCSS         |                                                                                                                                                             |
+---------------------------------------------------------------------------------------+-----------------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []  | TextCellCssClass            | Def_TextCellCSS     | [.Def_TextCellCSS]                                                                                       |
|                                                                                       |                             |                     |                                                                                                                                                             |
| {border="0"}                                            |                             |                     | [{]                                                                                                                     |
|                                                                                       |                             |                     |                                                                                                                                                             |
| []  |                             |                     | [  [padding]:[10px];]                                                          |
|                                                                                       |                             |                     |                                                                                                                                                             |
| TreeView with style settings for text                                                 |                             |                     | [  [background-color]:[#c0c9db]; ]                                             |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [}]                                                                                                                     |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [.Def_TextContCSS]                                                                                       |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [{]                                                                                                                     |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [  [font-family]:[Verdana];]                                                   |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [  [font-size]:[11px];]                                                        |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [  [color]:[black] ;  ]                                                        |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [  [font-weight]:[bold];]                                                      |
|                                                                                       |                             |                     |                                                                                                                                                             |
|                                                                                       |                             |                     | [}]                                                                                                                     |
|                                                                                       +-----------------------------+---------------------+                                                                                                                                                             |
|                                                                                       | TextContainerCssClass       | Def_TextContCSS     |                                                                                                                                                             |
+---------------------------------------------------------------------------------------+-----------------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

See Also

[] 

[[ItemLook Settings]{.UGHyperlink}]()[, ]{.UGHyperlink}[[Default Looks]{.UGHyperlink}]()[, ]{.UGHyperlink}[[Custom Looks]{.UGHyperlink}]()[]{.UGHyperlink}

 

 

[]{#related-topics}

