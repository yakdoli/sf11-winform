---
title: lookandfeelsettings10.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\lookandfeelsettings10.md
created_at: 2025-07-03
---






##### Look and Feel Settings {#look-and-feel-settings style="tab-stops: 0pt"}

 

The look and feel of the groupbar can be controlled by defining custom **ItemLook** instances in **ItemLooks** collection or by editing default ItemLook settings in the **DefaultItemLook** and **DefaultDisabledItemLook** properties.

[] 

The topics discussed are given below.

 

###### 5.6.1.2.8.1 AutoFormat Style Options {#autoformat-style-options style="tab-stops: 0pt"}

[] 

The GroupBar control provides pre-defined set of styles that can be applied to your control just on a click of the button. You can set the desired look and feel for the control that includes some popular styles too.

 

The Autoformat window can be opened by right clicking the control and selecting the **Auto Format\...** option opens the following **Auto Format** dialog box.

[] 

{border="0"}

Figure 335

[] 

The left pane lists the various pre-defined style scheme that are available. The right pane shows the preview of the currently selected scheme. Select the required style, and click **OK** to apply the selected scheme to the control.

[] 

Example of an pre-defined look and feel

[] 

The following image shows the GroupBar with **Silver Solid** style setting.

[] 

{border="0"}

 

 []{#p449}Figure 336

###### []{#_Item_Looks_1}5.6.1.2.8.2 Item Looks {#item-looks style="tab-stops: 0pt"}

 

The ItemLooks Collection Editor contains **Default** properties that allows to set default look and feel to the control and its disabled state, and **Custom** properties that allows you to customize the look and feel accordingly.

While defining the custom looks the name of the style sheet, where the styles are defined, must be set to the **CustomCss** property.

[] 


  ------------------- --------------------------------------------------------------
  GroupBar Property   Description
  CustomCss           Specifies the styles for the control delimited by semicolon.
  ------------------- --------------------------------------------------------------


[] 

The ItemLooks properties are as follows.

[] 


+-------------------+-------------------------------------------------------------------------------------------------------------+
| ItemLook Property | Description                                                                                                 |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| Enabled           | Gets/sets the boolean value that specifies the enabled state of the control. Default value is true.         |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| ID                | Specifies id of the item.                                                                                   |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| ImageHeight       | Specifies the height of the image.                                                                          |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| ImageWidth        | Specifies the width of the image.                                                                           |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| LeftImageHeight   | Specifies height of the left image.                                                                         |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| LeftImageWidth    | Specifies width of the left image.                                                                          |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| RightImageHeight  | Specifies height of the right image.                                                                        |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| RightImagewidth   | Specifies width of the right image.                                                                         |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| TextPaddingBottom | Specifies text padding around the node text, in pixel units.                                                |
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


[] 

**ID** specifies the id of the look. The text padding and the image height and width can be set for the groupbar item images. Image height and width specifies the dimensions of the expand / collapse image. Also the dimensions of the left and right images can be set using the corresponding properties.

 

The **StateDefault**, **StateActive**, **StatePushed** and **StateHover** categories contains the following css class properties that defines styles for groupbar items.

[] 


  ----------------------------- ------------------------------------------------------------
  ItemLook Property             Description
  ImageContainerCSSClass        Specifies styles for the image container.
  ImageCSSClass                 Specifies styles for the image.
  ItemCSSClass                  Specifies styles for an item.
  LeftImageCellCSSClass         Specifies styles for the left image.
  LeftImageContainerCSSClass    Specifies styles for the left image container.
  LeftImageCSSClass             Specifies styles for the left image.
  LeftImageURL                  Specifies path of the left image to be used for the item.
  RightImageCellCSSClass        Specifies styles for the cell holding the arrow image.
  RightImageContainerCSSClass   Specifies styles for the right image container.
  RightImageCSSClass            Specifies styles for the right image.
  RightImageURL                 Specifies path of the right image to be used for the item.
  TextCellCSSClass              Specifies text padding from bottom, in pixel units.
  TextContainerCSSClass         Specifies text padding from left, in pixel units.
  ----------------------------- ------------------------------------------------------------


[] 

The styles can be applied to individual nodes by setting the id of the look to the **Look** and **LookDisabled** property of the required groupbar items in the Designer dialog. This way the styles will be applied only to those nodes.

[] 


  ------------------------ ---------------------------------------------------------------
  GroupBar Item Property   Description
  Look                     Specifies styles to be applied for groupbar items.
  LookDisabled             Specifies styles to be applied for disabled state of an item.
  ------------------------ ---------------------------------------------------------------


[]{#_Default_Looks_2}5.6.1.2.8.2.1      Default Looks

[] 

The default looks used by the control is defined in the following properties that can also be edited in **ItemLooks Collection Editor** dialog.

[] 

[·      ]DefaultItemLook

[·      ]DefaultDisabledItemLook

[] 

{border="0"}

Figure 337

[] 

Changes made to these properties are saved in aspx as follows.

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][DefaultItemLookDisabled][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [\<][StateDataDefault] [LeftImageCSSClass ][= \"groupBarImgLeftCSS\"] [ItemCSSClass ][= \"groupBarItemDisabled\"] [ImageCSSClass ][= \"groupBarImgCSS\" ][ImageContainerCSSClass ][= \"groupBarImgCont\"] [RightImageCellCSSClass ][= \"groupBarImgRightCell\"] [TextCellCSSClass ][= \"groupBarTextCell\" ][LeftImageCellCSSClass ][= \"groupBarImgLeftCell\"] [LeftImageContainerCSSClass ][= \"groupBarImgLeftCont\"] [RightImageCSSClass ][= \"groupBarImgRightCSS\" ][TextContainerCSSClass ][= \"groupBarItemDisabled\"] [RightImageContainerCSSClass ][= \"groupBarImgRightCont\"\>\</][StateDataDefault][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [\<][StateDataHover] [LeftImageCSSClass ][= \"groupBarImgLeftCSS\"] [ItemCSSClass ][= \"groupBarItemDisabled\"] [ImageCSSClass ][= \"groupBarImgCSS\" ][ImageContainerCSSClass ][= \"groupBarImgCont\"] [RightImageCellCSSClass ][= \"groupBarImgRightCell\"] [TextCellCSSClass ][= \"groupBarTextCell\" ][LeftImageCellCSSClass ][= \"groupBarImgLeftCell\"] [LeftImageContainerCSSClass ][= \"groupBarImgLeftCont\" ][RightImageCSSClass ][= \"groupBarImgRightCSS\"] [TextContainerCSSClass ][= \"groupBarItemDisabled\"] [RightImageContainerCSSClass ][= \"groupBarImgRightCont\"\>\</][StateDataHover][\>]]     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\</][DefaultItemLookDisabled][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][DefaultItemLook][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [   [\<][StateDataDefault] [LeftImageCSSClass ][= \"groupBarImgLeftCSS\"] [ItemCSSClass ][= \"groupBarItemDef\"] [ImageCSSClass ][= \"groupBarImgCSS\" ][ImageContainerCSSClass ][= \"groupBarImgCont\"] [RightImageCellCSSClass ][= \"groupBarImgRightCell\"] [TextCellCSSClass ][= \"groupBarTextCell\" ][LeftImageCellCSSClass ][= \"groupBarImgLeftCell\"] [LeftImageContainerCSSClass ][= \"groupBarImgLeftCont\"] [RightImageCSSClass ][= \"groupBarImgRightCSS\" ][TextContainerCSSClass ][= \"groupBarTextContDef\"] [RightImageContainerCSSClass ][= \"groupBarImgRightCont\"\>\</][StateDataDefault][\>]]        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [   [\<][StateDataHover] [LeftImageCSSClass ][= \"groupBarImgLeftCSS\"] [ItemCSSClass ][= \"groupBarItemHover\"] [ImageCSSClass ][= \"groupBarImgCSS\" ][ImageContainerCSSClass ][= \"groupBarImgCont\"] [RightImageCellCSSClass ][= \"groupBarImgRightCell\"] [TextCellCSSClass ][= \"groupBarTextCell\" ][LeftImageCellCSSClass ][= \"groupBarImgLeftCell\"] [LeftImageContainerCSSClass ][= \"groupBarImgLeftCont\" ][RightImageCSSClass ][= \"groupBarImgRightCSS\"] [TextContainerCSSClass ][= \"groupBarTextContHover\"] [RightImageContainerCSSClass ][= \"groupBarImgRightCont\"\>\</][StateDataHover][\>]]        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [   [\<][StateDataExpanded] [LeftImageCSSClass ][= \"groupBarImgLeftCSS\"] [ItemCSSClass ][= \"groupBarItemExp\"] [ImageCSSClass ][= \"groupBarImgCSS\" ][ImageContainerCSSClass ][= \"groupBarImgCont\"] [RightImageCellCSSClass ][= \"groupBarImgRightCell\"] [TextCellCSSClass ][= \"groupBarTextCell\" ][LeftImageCellCSSClass ][= \"groupBarImgLeftCell\"] [LeftImageContainerCSSClass ][= \"groupBarImgLeftCont\"] [RightImageCSSClass ][= \"groupBarImgRightCSS\" ][TextContainerCSSClass ][= \"groupBarTextContExp\"] [RightImageContainerCSSClass ][= \"groupBarImgRightCont\"\>\</][StateDataExpanded][\>]]      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [     [\<][StateDataPushed] [LeftImageCSSClass ][= \"groupBarImgLeftCSS\"] [ItemCSSClass ][= \"groupBarItemPushed\"] [ImageCSSClass ][= \"groupBarImgCSS\" ][ImageContainerCSSClass ][= \"groupBarImgCont\"] [RightImageCellCSSClass ][= \"groupBarImgRightCell\"] [TextCellCSSClass ][= \"groupBarTextCell\" ][LeftImageCellCSSClass ][= \"groupBarImgLeftCell\"] [LeftImageContainerCSSClass ][= \"groupBarImgLeftCont\" ][RightImageCSSClass ][= \"groupBarImgRightCSS\"] [TextContainerCSSClass ][= \"groupBarTextContPushed\"] [RightImageContainerCSSClass ][= \"groupBarImgRightCont\"\>\</][StateDataPushed][\>]]  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\</][DefaultItemLook][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Note that the default css style sheet used by the GroupBar control is available at the following location: \'/Syncfusion/Resources/Toolsweb/CSS/GroupBar_Default.css\'. This css file defines the following css styles. The **ItemCSS**, **ItemHoverCSS** and **ItemExpandedCSS** properties are set to refer to these styles by default.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [.groupBarRootCSSClass]                                                                                                                                                      |
|                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [        [background-color]:[#EEEEEE];]                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [        [border]:[1px];]                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [        [border-color]:[black];]                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| [        [border-top-color]:[gray];]                                                                                                               |
|                                                                                                                                                                                                                                                 |
| [        [border-left-color]:[gray];]                                                                                                              |
|                                                                                                                                                                                                                                                 |
| [        [border-style]:[solid];]                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [.groupBarRootCSSClass][ [.groupBarItemDef] ]                                                     |
|                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [        [background-color]:[#3F3F3F];]                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [        [border]:[1px];]                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [        [border-color]:[#000000];]                                                                                                                |
|                                                                                                                                                                                                                                                 |
| [        [border-top-color]:[#808080];]                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [        [border-left-color]:[#808080];]                                                                                                           |
|                                                                                                                                                                                                                                                 |
| [        [border-style]:[solid];]                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| [        [cursor]:[pointer];]                                                                                                                      |
|                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [.groupBarRootCSSClass][ [.groupBarItemExp]]                                                      |
|                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [    [background-color]:[#3F3F3F];]                                                                                                                |
|                                                                                                                                                                                                                                                 |
| [        [border]:[1px];]                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [        [border-color]:[#000000];]                                                                                                                |
|                                                                                                                                                                                                                                                 |
| [        [border-top-color]:[#808080];]                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [        [border-left-color]:[#808080];]                                                                                                           |
|                                                                                                                                                                                                                                                 |
| [        [border-style]:[solid];]                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| [        [cursor]:[pointer];]                                                                                                                      |
|                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [.groupBarRootCSSClass][ [.groupBarItemHover] ]                                                   |
|                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [        [background-color]:[#8D8F95];]                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [        [border]:[1px];]                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [        [border-top-color]:[#B8B8B9];]                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [        [border-left-color]:[#B8B8B9];]                                                                                                           |
|                                                                                                                                                                                                                                                 |
| [        [border-right-color]:[black];]                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [        [border-bottom-color]:[black];]                                                                                                           |
|                                                                                                                                                                                                                                                 |
| [        [border-style]:[solid];]                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| [        [cursor]:[pointer];]                                                                                                                      |
|                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [/\*Text container\*/]                                                                                                                                                        |
|                                                                                                                                                                                                                                                 |
| [.groupBarRootCSSClass][ [.groupBarTextCont]]                                                     |
|                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [        [color]: [White];]                                                                                                                        |
|                                                                                                                                                                                                                                                 |
| [        [font-family]:[verdana];]                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [        [font-size]:[12px];]                                                                                                                      |
|                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [.groupBarRootCSSClass][ [.ControlSubPanelCSSClass] [.groupBarItemDef] ]   |
|                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [        [background-color]:[#EEEEEE];]                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [        [border]:[solid] [1px] [#EEEEEE];]                                                              |
|                                                                                                                                                                                                                                                 |
| [        [border-style]:[solid];]                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| [        [cursor]:[pointer];]                                                                                                                      |
|                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [.groupBarRootCSSClass][ [.ControlSubPanelCSSClass] [.groupBarItemHover] ] |
|                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [        [background-color]:[#CCCCCC];]                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [        [border]:[1px];]                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [        [border-color]:[#AAAAAA];]                                                                                                                |
|                                                                                                                                                                                                                                                 |
| [        [border-top-color]:[#FFFFFF];]                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [        [border-left-color]:[#FFFFFF];]                                                                                                           |
|                                                                                                                                                                                                                                                 |
| [        [border-style]:[solid];]                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| [        [cursor]:[pointer];]                                                                                                                      |
|                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [.groupBarRootCSSClass][ [.ControlSubPanelCSSClass] [.groupBarItemPushed]] |
|                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [        [background-color]:[#FFFFFF];]                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [        [border]:[1px];]                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [        [border-color]:[#FFFFFF];]                                                                                                                |
|                                                                                                                                                                                                                                                 |
| [        [border-top-color]:[#AAAAAA];]                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [        [border-left-color]:[#AAAAAA];]                                                                                                           |
|                                                                                                                                                                                                                                                 |
| [        [border-style]:[solid];]                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| [        [cursor]:[pointer];]                                                                                                                      |
|                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [.groupBarRootCSSClass][ [.ControlSubPanelCSSClass] [.groupBarTextCont]]   |
|                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [        [color]: [Black];]                                                                                                                        |
|                                                                                                                                                                                                                                                 |
| [        [font-family]:[verdana];]                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [        [font-size]:[11px];]                                                                                                                      |
|                                                                                                                                                                                                                                                 |
| [}       ]                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 338: GroupBar in Design View with default settings

[] 

See Also

[] 

[[ItemLook Properties]{.UGHyperlink}]()[, ]{.UGHyperlink}[CSS applicable segments in GroupBar]{.UGHyperlink}[, ]{.UGHyperlink}[Custom Looks]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#_Custom_Looks_2}5.6.1.2.8.2.2      Custom Looks

[] 

The **Custom Looks** tab in **ItemLooks Collection Editor** in the designer lets you add custom ItemLook instances to the collection.

[] 

{border="0"}

Figure 339:

[] 

The property window on the right lets you set the property values for this newly created ItemLook instance. The css related properties values should point to a custom css style defined in .css file attached to the application. This newly created ItemLook will get added to the aspx code as follows.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][cc1][:][groupbar][ [id ][= \"Groupbar1\"] [runat ][= \"server\"] [controlrootcssclass ][= \"RootCSS\"] [controlrootpanelcssclass ][= \"\" ][customcss ][= \"css/group.css\" ][width ][= \"140px\"] [height][=\"176px\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [  \<][Items][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [    \<][cc1][:][GroupBarItem][ [Look ][= \"RootLook\"] [Text ][= \"Extended Trading\"\>\</][cc1][:][GroupBarItem][\>]]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [    ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [    \<][cc1][:][GroupBarItem][ [Look ][= \"RootLook\"] [Text ][= \"Market Activity\"] [Expanded ][= \"True\"\>]]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [      \<][cc1][:][GroupBarItem][ [Look ][= \"ChildLook\"] [Text ][= \"Market Indices\"\>\</][cc1][:][GroupBarItem][\>]]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [      \<][cc1][:][GroupBarItem][ [Look ][= \"ChildLook\"] [Text ][= \"Sector Indicies\"\>\</][cc1][:][GroupBarItem][\>]]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [      \<][cc1][:][GroupBarItem][ [Look ][= \"ChildLook\"] [Text ][= \"Total Returns\"\>\</][cc1][:][GroupBarItem][\>]]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [    \</][cc1][:][GroupBarItem][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [  \</][Items][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [  ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [  \<][ItemLooks][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [    \<][cc1][:][GroupBarItemLook][ [ID][=\"ChildLook\"\>]]                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [      \<][StateDataPushed][ [TextCellCSSClass ][= \"Child_TextCellCSS\"\>\</][StateDataPushed][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [      \<][StateDataHover][ [ItemCSSClass ][= \"HovChild_ItemCSS\"] [TextCellCSSClass ][= \"Child_TextCellCSS\"\>\</][StateDataHover][\>]]                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [      \<][StateDataDefault][ [TextCellCSSClass ][= \"Child_TextCellCSS\"\>\</][StateDataDefault][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [    \</][cc1][:][GroupBarItemLook][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [    ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [    \<][cc1][:][GroupBarItemLook][ [ID ][= \"RootLook\"\>]]                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [      \<][StateDataPushed][ [ItemCSSClass ][= \"DefRoot_ItemCSS\"] [TextCellCSSClass ][= \"Root_TextCellCSS\"\>\</][StateDataPushed][\>]]                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [      \<][StateDataExpanded][ [ItemCSSClass ][= \"DefRoot_ItemCSS\"] [TextCellCSSClass ][= \"Root_TextCellCSS\"\>\</][StateDataExpanded][\>]]                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [      \<][StateDataHover][ [ItemCSSClass ][= \"HovRoot_ItemCSS\"] [TextCellCSSClass ][= \"Root_TextCellCSS\"\>\</][StateDataHover][\>]]                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [      \<][StateDataDefault][ [ItemCSSClass ][= \"DefRoot_ItemCSS\"] [TextCellCSSClass ][= \"Root_TextCellCSS\"\>\</][StateDataDefault][\>]]                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [    \</][cc1][:][GroupBarItemLook][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [  \</][ItemLooks][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\</][cc1][:][groupbar][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The css style settings is shown below.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [.RootCSS]                                                                                                     |
|                                                                                                                                                                                   |
| [{]                                                                                                                           |
|                                                                                                                                                                                   |
| [        [background-color]:[#C0CACC]; ]                                             |
|                                                                                                                                                                                   |
| [        [border] :[1px] [solid] [black];] |
|                                                                                                                                                                                   |
| [}]                                                                                                                           |
|                                                                                                                                                                                   |
| []                                                                                                                            |
|                                                                                                                                                                                   |
| [.DefRoot_ItemCSS]                                                                                             |
|                                                                                                                                                                                   |
| [{]                                                                                                                           |
|                                                                                                                                                                                   |
| [        [background-color]: [#7A8187];]                                             |
|                                                                                                                                                                                   |
| [        [border]:[1px] [solid] [black];]  |
|                                                                                                                                                                                   |
| [        [padding-bottom]:[3px];]                                                    |
|                                                                                                                                                                                   |
| [        [padding-top]:[3px];  ]                                                     |
|                                                                                                                                                                                   |
| [}]                                                                                                                           |
|                                                                                                                                                                                   |
| [.HovRoot_ItemCSS]                                                                                             |
|                                                                                                                                                                                   |
| [{]                                                                                                                           |
|                                                                                                                                                                                   |
| [        [background-color]: [#7A8187];]                                             |
|                                                                                                                                                                                   |
| [        [border]:[1px] [solid] [black];]  |
|                                                                                                                                                                                   |
| [        [padding-bottom]:[3px];]                                                    |
|                                                                                                                                                                                   |
| [        [padding-top]:[3px];  ]                                                     |
|                                                                                                                                                                                   |
| [        [cursor]:[hand]; ]                                                          |
|                                                                                                                                                                                   |
| [}]                                                                                                                           |
|                                                                                                                                                                                   |
| [.Root_TextCellCSS]                                                                                            |
|                                                                                                                                                                                   |
| [{]                                                                                                                           |
|                                                                                                                                                                                   |
| [        [color]:[White] ; ]                                                         |
|                                                                                                                                                                                   |
| [        [padding-left]:[5px]; ]                                                     |
|                                                                                                                                                                                   |
| [        [font-family]:[Verdana];]                                                   |
|                                                                                                                                                                                   |
| [        [font-family]:[12px];  ]                                                    |
|                                                                                                                                                                                   |
| [}]                                                                                                                           |
|                                                                                                                                                                                   |
| [.Child_TextCellCSS]                                                                                           |
|                                                                                                                                                                                   |
| [{]                                                                                                                           |
|                                                                                                                                                                                   |
| [        [padding-left]:[8px]; ]                                                     |
|                                                                                                                                                                                   |
| [        [font-family]:[Verdana];]                                                   |
|                                                                                                                                                                                   |
| [        [font-family]:[10px];          ]                                            |
|                                                                                                                                                                                   |
| [}]                                                                                                                           |
|                                                                                                                                                                                   |
| [.HovChild_ItemCSS]                                                                                            |
|                                                                                                                                                                                   |
| [{]                                                                                                                           |
|                                                                                                                                                                                   |
| [        [cursor]:[hand];]                                                           |
|                                                                                                                                                                                   |
| [        [background-color]:[#f6f9ff];  ]                                            |
|                                                                                                                                                                                   |
| [}]                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 340: GroupBar with Custom settings

[] 

See Also

[] 

[[ItemLook Properties]{.UGHyperlink}]()[, ]{.UGHyperlink}[CSS applicable segments in GroupBar]{.UGHyperlink}[, ]{.UGHyperlink}[[Default Looks]{.UGHyperlink}]()[]{.UGHyperlink}

 

###### []{#_CSS_Styles_3}5.6.1.2.8.3 CSS Styles {#css-styles style="tab-stops: 0pt"}

[] 

The GroupBar control comprises of distinct segments for which css style definitions can be set. The default styles of the layered groupbar structure can be replaced with custom style settings by applying the css class names to the corresponding style properties.

[] 

Structure of GroupBar control

[] 

The groupbar structure consists of 2 root level and 1 sub panel segments as shown below.

[] 

{border="0"}

**[]** 

Figure 341: Structure of GroupBar control

[] 

The below table lists the various segments and their corresponding CSS properties, whose settings affect their styles.

[] 


  -------------- -------------------------- --------------------------------
  Element        Property                   Default Value (CSS Class Name)
  Root element   ControlRootCssClass        groupBarRootCSSClass
  Root panel     ControlRootPanelCssClass   ControlRootPanelCSSClass
  Sub panel      ControlSubPanelCSSClass    ControlSubPanelCSS
  -------------- -------------------------- --------------------------------


[] 

Customizing GroupBar Root-level and Sub-panel segments

[] 

To customize the look and feel of one of the above segments, simply create a custom css style and associate it with the CSS property corresponding to the segment.

[] 

{border="0"}

**[]** 

Figure 342: GroupBar with css settings for the root elements

[] 

The style properties set to the custom css values and the style definitions are shown below.

[] 


  -------------------------- -------------------------------
  Property                   Value (Custom CSS Class Name)
  ControlRootCssClass        RootCSS
  ControlRootPanelCssClass   RootPanelCSS
  ControlSubPanelCSSClass    SubPanelCSS
  -------------------------- -------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------+
| **[\[Css Styles\]]**                                                |
|                                                                                                                       |
| []                                                                 |
|                                                                                                                       |
| [.RootCSS]                                                         |
|                                                                                                                       |
| [{]                                                                               |
|                                                                                                                       |
| [        [background-color]:[#7a87a1] ;] |
|                                                                                                                       |
| [        [padding]:[10px];  ]            |
|                                                                                                                       |
| [}]                                                                               |
|                                                                                                                       |
| [.RootPanelCSS]                                                    |
|                                                                                                                       |
| [{]                                                                               |
|                                                                                                                       |
| [        [background-color]:[#95a1b2];]  |
|                                                                                                                       |
| [        [padding]:[10px];  ]            |
|                                                                                                                       |
| [}]                                                                               |
|                                                                                                                       |
| [.SubPanelCSS]                                                     |
|                                                                                                                       |
| [{]                                                                               |
|                                                                                                                       |
| [        [background-color]:[#aebace] ;] |
|                                                                                                                       |
| [        [padding]:[5px];      ]         |
|                                                                                                                       |
| [}]                                                                               |
+-----------------------------------------------------------------------------------------------------------------------+

[] 

Structure of the groupbar Item

[] 

A single groupbar item is segregated into different image and text sections, the look for all of which can be controlled through css-property settings. An item allows setting the left and right images and the item text.

[] 

{border="0"}

**[]** 

Figure 343: Structure of a groupbar Item

**[]** 

The below table lists the item-level segments and their corresponding CSS properties whose settings affect their styles.

[] 


  ----------------------- ----------------------------- ----------------------
  Element                 Property                      Default CSS Value
  Left image cell         LeftImageCellCSSClass         groupBarImgLeftCell
  Left image container    LeftImageContainerCSSClass    groupBarImgLeftCont
  Left image              LeftImageCSSClass             groupBarImgLeftCSS
  Text cell               TextCellCssClass              groupBarTextCell
  Text container          TextContainerCssClass         groupBarTextCont
  Right image cell        RightImageCellCSSClass        groupBarImgRightCell
  Right image container   RightImageContainerCSSClass   groupBarImgRightCont
  Right image             RightImageCSSClass            groupBarImgRightCSS
  ----------------------- ----------------------------- ----------------------


[] 

Customizing GroupBar Item-level segments

[] 

The following section shows some custom styles applied on the different item-level segments and a screenshot of the resulting look.

[] 


+---------------------------------------------------------------------+-----------------------------+------------------+----------------------------------------------------------------------------------------------------------------------+
| Image                                                               | Property                    | Custom CSS Style | CSS Definition                                                                                                       |
+---------------------------------------------------------------------+-----------------------------+------------------+----------------------------------------------------------------------------------------------------------------------+
| {border="0"}                          | ItemCSSClass                | Def_ItemCSS      | .Def_ItemCSS                                                                                                         |
|                                                                     |                             |                  |                                                                                                                      |
| []  |                             |                  | {                                                                                                                    |
|                                                                     |                             |                  |                                                                                                                      |
| GroupBar with style settings for left image                         |                             |                  |   [background-color]:[#95a1b2];                                             |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  |   [padding]:[5px];                                                          |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  | }                                                                                                                    |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  | .LeftImgCellCSS                                                                                                      |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  | {                                                                                                                    |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  |   [border]:[1px] [solid] [black]; |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  | }                                                                                                                    |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  | .LeftImgContCSS                                                                                                      |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  | {                                                                                                                    |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  |   [background-color]:[#ffbb66];                                             |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  |   [padding-left]:[2px];                                                     |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  |   [padding-top]:[2px];                                                      |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  |   [padding-right]:[2px];                                                    |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  | }                                                                                                                    |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  | .LeftImgCSS                                                                                                          |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  | {                                                                                                                    |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  |   [width]:[16px];                                                           |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  |   [height]:[15px];                                                          |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  | }                                                                                                                    |
|                                                                     +-----------------------------+------------------+                                                                                                                      |
|                                                                     | LeftImageCellCSSClass       | LeftImgCellCSS   |                                                                                                                      |
|                                                                     +-----------------------------+------------------+                                                                                                                      |
|                                                                     | LeftImageContainerCSSClass  | LeftImgContCSS   |                                                                                                                      |
|                                                                     +-----------------------------+------------------+                                                                                                                      |
|                                                                     | LeftImageCSSClass           | LeftImgCSS       |                                                                                                                      |
+---------------------------------------------------------------------+-----------------------------+------------------+----------------------------------------------------------------------------------------------------------------------+
| {border="0"}                          | RightImageCellCSSClass      | RightImgCellCSS  | .RightImgCellCSS                                                                                                     |
|                                                                     |                             |                  |                                                                                                                      |
| []  |                             |                  | {                                                                                                                    |
|                                                                     |                             |                  |                                                                                                                      |
| GroupBar with style settings for right image                        |                             |                  |   [border]:[1px] [solid] [black]; |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  | }                                                                                                                    |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  | .RightImgContCSS                                                                                                     |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  | {                                                                                                                    |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  |   [background-color]:[#ffbb66];                                             |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  |   [padding-left]:[2px];                                                     |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  |   [padding-top]:[2px];                                                      |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  |   [padding-right]:[2px];                                                    |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  | }                                                                                                                    |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  | .RightImgCSS                                                                                                         |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  | {                                                                                                                    |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  |   [width]:[16px];                                                           |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  |   [height]:[15px];                                                          |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  | }                                                                                                                    |
|                                                                     +-----------------------------+------------------+                                                                                                                      |
|                                                                     | RightImageContainerCSSClass | RightImgContCSS  |                                                                                                                      |
|                                                                     +-----------------------------+------------------+                                                                                                                      |
|                                                                     | RightImageCSSClass          | RightImgCSS      |                                                                                                                      |
+---------------------------------------------------------------------+-----------------------------+------------------+----------------------------------------------------------------------------------------------------------------------+
| {border="0"}                          | TextCellCssClass            | Def_TextCellCSS  | .Def_TextCellCSS                                                                                                     |
|                                                                     |                             |                  |                                                                                                                      |
| []  |                             |                  | {                                                                                                                    |
|                                                                     |                             |                  |                                                                                                                      |
| GroupBar with style settings for text                               |                             |                  |   [color] :[White] ;                                                        |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  |   [padding-left]:[8px];                                                     |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  |   [padding-right]:[8px];                                                    |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  | }                                                                                                                    |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  | .Def_TextContCSS                                                                                                     |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  | {                                                                                                                    |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  |   [background-color]: [#aebace];                                            |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  |   [padding]:[15px];                                                         |
|                                                                     |                             |                  |                                                                                                                      |
|                                                                     |                             |                  | }                                                                                                                    |
|                                                                     +-----------------------------+------------------+                                                                                                                      |
|                                                                     | TextContainerCssClass       | Def_TextContCSS  |                                                                                                                      |
+---------------------------------------------------------------------+-----------------------------+------------------+----------------------------------------------------------------------------------------------------------------------+


[] 

See Also

[] 

[[ItemLook Properties]{.UGHyperlink}]()[, ]{.UGHyperlink}[[Default Looks]{.UGHyperlink}]()[, ]{.UGHyperlink}[[Custom Looks]{.UGHyperlink}]()[]{.UGHyperlink}

 

 

[]{#related-topics}

