---
title: lookandfeelsettings8.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\lookandfeelsettings8.md
created_at: 2025-07-03
---






##### Look and Feel Settings {#look-and-feel-settings style="tab-stops: 0pt"}

 

The look and feel of tabstrip can be controlled by defining custom ItemLook instances in ItemLooks collection or by editing default ItemLook settings in DefaultItemLook and DefaultDisabledItemLook properties.

The topics discussed are given below.

[]{#p411} 

###### 5.5.1.2.8.1 AutoFormat Styles {#autoformat-styles style="tab-stops: 0pt"}

[] 

The TabStrip control provides pre-defined set of styles that can be applied to your control just on a click of the button. You can set the desired look and feel for the control that includes some popular styles too.

The Autoformat window can be opened by right clicking the control, and selecting the **Auto Format\...** option opens the following **Auto Format** dialog box.

[] 

{border="0"}

Figure 303

[] 

The left pane lists the various pre-defined style scheme that are available. The right pane shows the preview of the currently selected scheme. Select the required style and click **OK** to apply the selected scheme to the control.

[] 

Example of a popular look and feel

[] 

The following image shows the TabStrip with **Office 2007 Luna Blue** style setting.

[] 

{border="0"}

Figure 304

 

###### 5.5.1.2.8.2 Item Looks {#item-looks style="tab-stops: 0pt"}

 

 

The ItemLooks Collection Editor is used to customize the default look and the default disabled look using DefaultItem properties. The Custom properties allows you to customize the look and feel of the control accordingly.

The ItemLooks properties are as follows.

 


+-------------------+-------------------------------------------------------------------------------------------------------------+
| Property          | Description                                                                                                 |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| Enabled           | Specifies the enabled state of the control.                                                                 |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| ID                | Specifies id of the item look.                                                                              |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| ImageHeight       | Specifies the height of the image.                                                                          |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| ImageWidth        | Specifies the width of the image.                                                                           |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| LeftImageHeight   | Specifies the height of the left image.                                                                     |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| LeftImageWidth    | Specifies the width of the right image.                                                                     |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| RightImageHeight  | Specifies the height of the right image.                                                                    |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| RightImageWidth   | Specifies the width of the right image.                                                                     |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| TextPaddingBottom | Specifies the space in pixels around the tab item\'s text.                                                  |
+-------------------+                                                                                                             |
| TextPaddingLeft   |                                                                                                             |
+-------------------+                                                                                                             |
| TextPaddingRight  |                                                                                                             |
+-------------------+                                                                                                             |
| TextPaddingTop    |                                                                                                             |
+-------------------+-------------------------------------------------------------------------------------------------------------+
| StateDataActive   | Specifies the various look and feel options for different states such as active, default, hover and pushed. |
+-------------------+                                                                                                             |
| StateDataDefault  |                                                                                                             |
+-------------------+                                                                                                             |
| StateDataHover    |                                                                                                             |
+-------------------+                                                                                                             |
| StateDataPushed   |                                                                                                             |
+-------------------+-------------------------------------------------------------------------------------------------------------+


 

The StateDefault, StateActive, StatePushed and StateHover categories contains the following css class properties that defines styles for tab items.

 


  ----------------------------- ------------------------------------------------------------
  Property                      Description
  ImageCellCSSClass             Specifies styles for the image cell.
  ImageContainerCSSClass        Specifies styles for the image container.
  ImageCSSClass                 Specifies styles for the image.
  ImageUrl                      Specifies path of the image to be inserted for an item.
  ItemCSSClass                  Specifies styles for an item.
  LeftImageCellCSSClass         Specifies styles for the left image.
  LeftImageContainerCSSClass    Specifies styles for the left image container.
  LeftImageCSSClass             Specifies styles for the left image.
  LeftImageUrl                  Specifies path of the left image to be used for the item.
  RightImageCellCSSClass        Specifies styles for the cell holding the arrow image.
  RightImageContainerCSSClass   Specifies styles for the right image container.
  RightImageCSSClass            Specifies styles for the right image.
  RightImageUrl                 Specifies path of the right image to be used for the item.
  TextCellCssClass              Specifies styles for the cell holding the text.
  TextContainerCssClass         Specifies styles for the text cell container.
  ----------------------------- ------------------------------------------------------------


 


  -------------------------- --------------------------------------------------------------------------------------------
  Property                   Description
  CentreSeparatorCSS         Specifies styles for the center separator of an item.
  ControlRootCSSClass        Specifies the class name of the css definitions to apply for the root element.
  ControlRootPanelCSSClass   Specifies the class name of the css definitions to apply for the root panel element.
  ControlRootTableCSSClass   Specifies the class name of the css definitions to apply for the root panel table element.
  CustomCSS                  Specifies the custom styles for the control delimited by semicolon.
  FirstSeparatorCSS          Specifies styles for the first separator of an item.
  ImageBaseUrl               Specifies the relative path of the images used in the control.
  LastSeparatorCSS           Specifies the class name of the css definitions to apply to the last separator of an item.
  -------------------------- --------------------------------------------------------------------------------------------


 


  -------------------- ----------------------------------------------------------------------------------------------
  Property             Description
  CenterSeparatorCSS   Specifies the class name of the css definitions to apply for the center separator.
  FirstSeparatorCSS    Specifies the class name of the css definitions to apply for the first separator of an item.
  ImageHoverPath       Specifies path of the left image to be used for an item in hover state.
  ImagePath            Specifies path of the left image to be used for an item.
  LastSeparatorCSS     Specifies the class name of the css definitions to apply for the last separator.
  Look                 Specifies the styles to use for an item.
  LookDisabled         Specifies the styles to use for an item in disabled state.
  SubpanelCSSClass     Specifies the class name of the css definitions to apply for the sub panel.
  -------------------- ----------------------------------------------------------------------------------------------


[]{#p413} 

5.5.1.2.8.2.1      Default Looks

[] 

The Default Looks used by the control is defined in the following look collection that can also be edited in the ItemLooks Collection Editor dialog box.

[] 

[·      ]DefaultItemLook

[·      ]DefaultDisabledItemLook

[] 

{border="0"}

*[Figure ][305]*

[] 

Changes made to these properties are saved in aspx as follows.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][DisabledItemLook][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [  \<][StateDataDefault][ [LeftImageCSSClass ][= \"tabImgLeftCSS\"] [ItemCSSClass ][= \"tabItemDisabled\"] [ImageCSSClass ][= \"tabImgCSS\" ][ImageContainerCSSClass ][ = \"tabImgCont\"] [RightImageCellCSSClass ][= \"tabImgRightCell\"] [TextCellCSSClass ][= \"tabTextCell\" ][LeftImageCellCSSClass ][= \"tabImgLeftCell\"] [LeftImageContainerCSSClass ][= \"tabImgLeftCont\"] [RightImageCSSClass ][= \"tabImgRightCSS\" ][TextContainerCSSClass ][= \"tabItemDisabled\"] [RightImageContainerCSSClass ][= \"tabImgRightCont\"] [ImageCellCSSClass ][= \"tabImgCell\"\>\</][StateDataDefault][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [  \<][StateDataActive][ [LeftImageCSSClass ][= \"tabImgLeftCSS\"] [ItemCSSClass ][= \"tabItemDisabled\"] [ImageCSSClass ][= \"tabImgCSS\" ][ImageContainerCSSClass ][= \"tabImgCont\"] [RightImageCellCSSClass ][= \"tabImgRightCell\"] [TextCellCSSClass ][= \"tabTextCell\" ][LeftImageCellCSSClass ][= \"tabImgLeftCell\"] [LeftImageContainerCSSClass ][= \"tabImgLeftCont\"] [RightImageCSSClass ][= \"tabImgRightCSS\" ][TextContainerCSSClass ][= \"tabItemDisabled\"] [RightImageContainerCSSClass ][= \"tabImgRightCont\"] [ImageCellCSSClass ][= \"tabImgCell\"\>\</][StateDataActive][\>]]    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [  \<][StateDataHover][ [LeftImageCSSClass ][= \"tabImgLeftCSS\"] [ItemCSSClass ][= \"tabItemDisabled\"] [ImageCSSClass ][= \"tabImgCSS\"  ][ImageContainerCSSClass ][= \"tabImgCont\"] [RightImageCellCSSClass ][= \"tabImgRightCell\"] [TextCellCSSClass ][= \"tabTextCell\" ][LeftImageCellCSSClass ][= \"tabImgLeftCell\"] [LeftImageContainerCSSClass ][= \"tabImgLeftCont\"] [RightImageCSSClass ][= \"tabImgRightCSS\" ][TextContainerCSSClass ][= \"tabItemDisabled\"] [RightImageContainerCSSClass ][= \"tabImgRightCont\"] [ImageCellCSSClass ][= \"tabImgCell\"\>\</][StateDataHover][\>]]     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [  \<][StateDataPushed][ [LeftImageCSSClass ][= \"tabImgLeftCSS\"] [ItemCSSClass ][= \"tabItemDisabled\"] [ImageCSSClass ][= \"tabImgCSS\" ][ImageContainerCSSClass ][= \"tabImgCont\"] [RightImageCellCSSClass ][= \"tabImgRightCell\"] [TextCellCSSClass ][= \"tabTextCell\" ][LeftImageCellCSSClass ][= \"tabImgLeftCell\"] [LeftImageContainerCSSClass ][= \"tabImgLeftCont\"] [RightImageCSSClass ][= \"tabImgRightCSS\" ][TextContainerCSSClass ][= \"tabItemDisabled\"] [RightImageContainerCSSClass ][= \"tabImgRightCont\"] [ImageCellCSSClass ][= \"tabImgCell\"\>\</][StateDataPushed][\>]]    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\</][DisabledItemLook][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][DefaultItemLook][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [  \<][StateDataDefault][ [LeftImageCSSClass ][= \"tabImgLeftCSS\"] [ItemCSSClass ][= \"tabItemDef\"] [ImageCSSClass ][= \"tabImgCSS\" ][ImageContainerCSSClass ][= \"tabImgCont\"] [RightImageCellCSSClass ][= \"tabImgRightCell\"] [TextCellCSSClass ][= \"tabTextCell\" ][LeftImageCellCSSClass ][= \"tabImgLeftCell\"] [LeftImageContainerCSSClass ][= \"tabImgLeftCont\"] [RightImageCSSClass][=\"tabImgRightCSS\" ][TextContainerCSSClass ][= \"tabTextContDef\"] [RightImageContainerCSSClass ][= \"tabImgRightCont\"] [ImageCellCSSClass ][= \"tabImgCell\"\>\</][StateDataDefault][\>]]          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [  [\<][StateDataActive] [LeftImageCSSClass ][= \"tabImgLeftCSS\"] [ItemCSSClass ][= \"tabItemActive\"] [ImageCSSClass ][= \"tabImgCSS\" ][ImageContainerCSSClass ][= \"tabImgCont\"] [RightImageCellCSSClass ][= \"tabImgRightCell\"] [TextCellCSSClass ][= \"tabTextCell\" ][LeftImageCellCSSClass][= \"tabImgLeftCell\"] [LeftImageContainerCSSClass ][= \"tabImgLeftCont\"] [RightImageCSSClass ][= \"tabImgRightCSS ][TextContainerCSSClass ][= \"tabTextContActive\"] [RightImageContainerCSSClass ][= \"tabImgRightCont\"] [ImageCellCSSClass ][= \"tabImgCell\"\>\</][StateDataActive][\>]]                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [  [\<][StateDataHover] [LeftImageCSSClass  ][= \"tabImgLeftCSS\"] [ItemCSSClass ][= \"tabItemHover\"] [ImageCSSClass ][= \"tabImgCSS\" ][ImageContainerCSSClass ][= \"tabImgCont\"] [RightImageCellCSSClass ][= \"tabImgRightCell\"] [TextCellCSSClass ][= \"tabTextCell\" ][LeftImageCellCSSClass ][= \"tabImgLeftCell\"] [LeftImageContainerCSSClass ][= \"tabImgLeftCont\"] [RightImageCSSClass ][= \"tabImgRightCSS\" ][TextContainerCSSClass ][= \"tabTextContHover\"] [RightImageContainerCSSClass ][= \"tabImgRightCont\"] [ImageCellCSSClass ][= \"tabImgCell\"\>\</][StateDataHover][\>]]                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [  \<][StateDataPushed][ [LeftImageCSSClass ][= \"tabImgLeftCSS\"] [ItemCSSClass ][= \"tabItemPushed\"] [ImageCSSClass ][= \"tabImgCSS\" ][ImageContainerCSSClass ][= \"tabImgCont\"] [RightImageCellCSSClass ][= \"tabImgRightCell\"] [TextCellCSSClass ][= \"tabTextCell\" ][LeftImageCellCSSClass ][= \"tabImgLeftCell\"] [LeftImageContainerCSSClass ][= \"tabImgLeftCont\"] [RightImageCSSClass ][= \"tabImgRightCSS\" ][TextContainerCSSClass ][= \"tabTextContPushed\"] [RightImageContainerCSSClass ][= \"tabImgRightCont\"] [ImageCellCSSClass ][= \"tabImgCell\"\>\</][StateDataPushed][\>]]    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\</][DefaultItemLook][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Note that the default css style sheet used by the tabstrip control is available at the following location: \'/Syncfusion/Resources/Toolsweb/CSS/Tabstrip.css\'. This css file defines the following css styles. The **ItemCSSClass**, **ItemHoverCSSClass** and **ItemSelectedCSSClass** properties are set to refer to these styles by default.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [.tabRoot]                                                                                                    |
|                                                                                                                                                                                  |
| [{]                                                                                                                          |
|                                                                                                                                                                                  |
| [        [background-color]:[gray];]                                                |
|                                                                                                                                                                                  |
| [}]                                                                                                                          |
|                                                                                                                                                                                  |
| []                                                                                                                           |
|                                                                                                                                                                                  |
| [.tabRoot][ [.tabRootPanel]]       |
|                                                                                                                                                                                  |
| [{]                                                                                                                          |
|                                                                                                                                                                                  |
| [        [padding]:[1px];]                                                          |
|                                                                                                                                                                                  |
| [}]                                                                                                                          |
|                                                                                                                                                                                  |
| []                                                                                                                           |
|                                                                                                                                                                                  |
| [/\*Item\*/]                                                                                                   |
|                                                                                                                                                                                  |
| [.tabRoot][ [.tabItemDef]]         |
|                                                                                                                                                                                  |
| [{]                                                                                                                          |
|                                                                                                                                                                                  |
| [        [padding]: [1px];]                                                         |
|                                                                                                                                                                                  |
| [        [border]: [0px];]                                                          |
|                                                                                                                                                                                  |
| [}]                                                                                                                          |
|                                                                                                                                                                                  |
| []                                                                                                                           |
|                                                                                                                                                                                  |
| [.tabRoot][ [.tabItemHover]]       |
|                                                                                                                                                                                  |
| [{]                                                                                                                          |
|                                                                                                                                                                                  |
| [        [background-color]:[#D3D3D3];]                                             |
|                                                                                                                                                                                  |
| [        [border]:[1px] [solid] [black];] |
|                                                                                                                                                                                  |
| [        [cursor]:[hand];]                                                          |
|                                                                                                                                                                                  |
| [}]                                                                                                                          |
|                                                                                                                                                                                  |
| []                                                                                                                           |
|                                                                                                                                                                                  |
| [.tabRoot][ [.tabItemActive]]      |
|                                                                                                                                                                                  |
| [{]                                                                                                                          |
|                                                                                                                                                                                  |
| [        [background-color]:[#A9A9A9];]                                             |
|                                                                                                                                                                                  |
| [        [border]:[1px] [solid] [black];] |
|                                                                                                                                                                                  |
| [        [cursor]:[hand];]                                                          |
|                                                                                                                                                                                  |
| [}]                                                                                                                          |
|                                                                                                                                                                                  |
| []                                                                                                                           |
|                                                                                                                                                                                  |
| [.tabRoot][ [.tabItemPushed]]      |
|                                                                                                                                                                                  |
| [{]                                                                                                                          |
|                                                                                                                                                                                  |
| [        [background-color]:[#A9A9A9];]                                             |
|                                                                                                                                                                                  |
| [        [border]:[1px] [solid] [black];] |
|                                                                                                                                                                                  |
| [        [cursor]:[hand];]                                                          |
|                                                                                                                                                                                  |
| [}]                                                                                                                          |
|                                                                                                                                                                                  |
| []                                                                                                                           |
|                                                                                                                                                                                  |
| [.tabRoot][ [.tabImgCSS]]          |
|                                                                                                                                                                                  |
| [{]                                                                                                                          |
|                                                                                                                                                                                  |
| [    [width]: [8px];]                                                               |
|                                                                                                                                                                                  |
| [        [height]: [12px];]                                                         |
|                                                                                                                                                                                  |
| [}]                                                                                                                          |
|                                                                                                                                                                                  |
| []                                                                                                                           |
|                                                                                                                                                                                  |
| [/\*Left image\*/]                                                                                             |
|                                                                                                                                                                                  |
| [.tabRoot][ [.tabImgLeftCSS]]      |
|                                                                                                                                                                                  |
| [{]                                                                                                                          |
|                                                                                                                                                                                  |
| [    [width]: [8px];]                                                               |
|                                                                                                                                                                                  |
| [        [height]: [12px];]                                                         |
|                                                                                                                                                                                  |
| [}]                                                                                                                          |
|                                                                                                                                                                                  |
| []                                                                                                                           |
|                                                                                                                                                                                  |
| [/\*Right image\*/]                                                                                            |
|                                                                                                                                                                                  |
| [.tabRoot][ [.tabImgRightCSS]]     |
|                                                                                                                                                                                  |
| [{]                                                                                                                          |
|                                                                                                                                                                                  |
| [    [width]: [8px];]                                                               |
|                                                                                                                                                                                  |
| [        [height]: [12px];]                                                         |
|                                                                                                                                                                                  |
| [}]                                                                                                                          |
|                                                                                                                                                                                  |
| []                                                                                                                           |
|                                                                                                                                                                                  |
| [/\*Text\*/]                                                                                                   |
|                                                                                                                                                                                  |
| [.tabRoot][ [.tabTextCell]]        |
|                                                                                                                                                                                  |
| [{]                                                                                                                          |
|                                                                                                                                                                                  |
| [        [padding-bottom]:[1px];]                                                   |
|                                                                                                                                                                                  |
| [}]                                                                                                                          |
|                                                                                                                                                                                  |
| []                                                                                                                           |
|                                                                                                                                                                                  |
| [.tabRoot][ [.tabTextCont]]        |
|                                                                                                                                                                                  |
| [{]                                                                                                                          |
|                                                                                                                                                                                  |
| [        [color]: [white]; ]                                                        |
|                                                                                                                                                                                  |
| [        [font-family]: [Tahoma]; ]                                                 |
|                                                                                                                                                                                  |
| [        [font-size]: [12px]; ]                                                     |
|                                                                                                                                                                                  |
| [        [margin]: [2px];         ]                                                 |
|                                                                                                                                                                                  |
| [}]                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

In design view, the default tabstrip control appears as follows.

[] 

{border="0"}

**[]** 

Figure 306: TabStrip in the Design View

5.5.1.2.8.2.2      Custom Looks

[] 

The Custom Looks tab in the ItemLooks Collection Editor in the designer lets you add custom ItemLook instances to the collection.

[] 

{border="0"}

Figure 307

[] 

The property window on the right lets you set the property values for this newly created ItemLook instance. The css related properties values should point to a custom css style defined in .css file attached to the application. This newly created ItemLook will get added to the aspx code as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][cc1][:][tabstrip][ [id ][= \"TabStrip1\"] [runat ][= \"server\"] [ControlRootTableCSSClass ][= \"topgroup\"] [ControlRootPanelCSSClass ][= \" \" ][CustomCSS ][= \"css\\Tab.css\"] [ControlRootCSSClass ][= \"topgroup\"] [CssClass ][= \" \"] [ImageBaseURL ][= \"images\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [  \<][Looks][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    [\<][cc1][:][TabStripItemLook] [ID][=\"RootLook\"\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [      [\<][StateDataDefault] [ItemCSSClass ][= \"Root_ItemCSS\"] [LeftImageCSSClass ][= \"empty\"] [LeftImageURL ][= \"..\\images\\nrm_lft.gif\"] [RightImageCSSClass ][= \"empty\" ][TextContainerCSSClass ][= \"DefRoot_TextCell\"] [RightImageURL ][= \"..\\images\\nrm_rght.gif\"\>\</][StateDataDefault][\>]]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [      [\<][StateDataPushed] [ItemCSSClass ][= \"Root_ItemCSS\"] [LeftImageCSSClass ][= \"empty\"] [LeftImageURL ][= \"..\\images\\sel_left.gif\"] [RightImageCSSClass ][= \"empty\" ][TextContainerCSSClass ][= \"SelRoot_TextCell\"] [RightImageURL ][= \"..\\images\\sel_rght.gif\"\>\</][StateDataPushed][\>]]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [      [\<][StateDataHover] [ItemCSSClass ][= \"Root_ItemCSS\"\>\</][StateDataHover][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    [\</][cc1][:][TabStripItemLook][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    \<][cc1][:][TabStripItemLook][ [ID][=\"ChildLook\"\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [      [\<][StateDataDefault] [ItemCSSClass][=\"DefChild_ItemCSS\"] [TextContainerCSSClass][=\"Child_TextCont\"] [\>\</][StateDataDefault][\>]                          [\</][cc1][:][TabStripItemLook][\>]]                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [  [\</][Looks][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [ \...]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [ \...]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\</][cc1][:][tabstrip][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The default css file is shown below.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| [.DefRoot_TextCell]                                                                    |
|                                                                                                                                                           |
| [{]                                                                                                   |
|                                                                                                                                                           |
| [  [background-image]:[url(../images/nrm_bg.png)]; ]         |
|                                                                                                                                                           |
| [  [color] :[Black] ;]                                       |
|                                                                                                                                                           |
| [  [font-size]:[11px];]                                      |
|                                                                                                                                                           |
| [  [font-family]:[Verdana] ;  ]                              |
|                                                                                                                                                           |
| [  [height]:[22px];]                                         |
|                                                                                                                                                           |
| [  [padding-top]:[4px]; ]                                    |
|                                                                                                                                                           |
| [  [padding-left]:[3px];]                                    |
|                                                                                                                                                           |
| [  [padding-right]:[3px];   ]                                |
|                                                                                                                                                           |
| [}]                                                                                                   |
|                                                                                                                                                           |
| [.SelRoot_TextCell]                                                                    |
|                                                                                                                                                           |
| [{]                                                                                                   |
|                                                                                                                                                           |
| [  [background-image]:[url(../images/sel_bg.gif)];         ] |
|                                                                                                                                                           |
| [  [color] :[Black] ;]                                       |
|                                                                                                                                                           |
| [  [font-size]:[11px];]                                      |
|                                                                                                                                                           |
| [  [font-family]:[Verdana] ;  ]                              |
|                                                                                                                                                           |
| [  [padding-top]:[4px]; ]                                    |
|                                                                                                                                                           |
| [  [padding-left]:[3px];]                                    |
|                                                                                                                                                           |
| [  [padding-right]:[3px];  ]                                 |
|                                                                                                                                                           |
| [  [height]:[22px];]                                         |
|                                                                                                                                                           |
| [}]                                                                                                   |
|                                                                                                                                                           |
| [.empty]                                                                               |
|                                                                                                                                                           |
| [{]                                                                                                   |
|                                                                                                                                                           |
| [}]                                                                                                   |
|                                                                                                                                                           |
| [.DefChild_ItemCSS]                                                                    |
|                                                                                                                                                           |
| [{]                                                                                                   |
|                                                                                                                                                           |
| [  [padding-left]:[8px];]                                    |
|                                                                                                                                                           |
| [  [padding-top]:[2px];  ]                                   |
|                                                                                                                                                           |
| [  [padding-bottom]:[2px];]                                  |
|                                                                                                                                                           |
| [}]                                                                                                   |
|                                                                                                                                                           |
| [.Child_TextCont]                                                                      |
|                                                                                                                                                           |
| [{]                                                                                                   |
|                                                                                                                                                           |
| [  [padding-left]:[8px];]                                    |
|                                                                                                                                                           |
| [  [padding-top]:[2px];  ]                                   |
|                                                                                                                                                           |
| [  [padding-bottom]:[2px];]                                  |
|                                                                                                                                                           |
| [  [color] :[black];]                                        |
|                                                                                                                                                           |
| [  [font-size]:[11px];]                                      |
|                                                                                                                                                           |
| [  [font-family]:[Verdana] ;  ]                              |
|                                                                                                                                                           |
| [}]                                                                                                   |
|                                                                                                                                                           |
| [.Root_ItemCSS]                                                                        |
|                                                                                                                                                           |
| [{]                                                                                                   |
|                                                                                                                                                           |
| [  [border]:[0px]; ]                                         |
|                                                                                                                                                           |
| [}]                                                                                                   |
|                                                                                                                                                           |
| [.topgroup]                                                                            |
|                                                                                                                                                           |
| [{]                                                                                                   |
|                                                                                                                                                           |
| [  [width]:[1500px];]                                        |
|                                                                                                                                                           |
| [}]                                                                                                   |
|                                                                                                                                                           |
| [.Level2group]                                                                         |
|                                                                                                                                                           |
| [{]                                                                                                   |
|                                                                                                                                                           |
| [  [width]:[1500px]; ]                                       |
|                                                                                                                                                           |
| [  [background-image]:[url(../images/bglevel2.gif)]; ]       |
|                                                                                                                                                           |
| [  [background-repeat]:[repeat-x];  ]                        |
|                                                                                                                                                           |
| [}        ]                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 308: The custom settings output

 

###### 5.5.1.2.8.3 CSS Styles {#css-styles style="tab-stops: 0pt"}

[] 

The TabStrip control comprises of distinct segments for which css style definitions can be set. The default styles of the layered tabstrip structure can be replaced with custom style settings by applying the css class names to the corresponding style properties.

[] 

Structure of TabStrip control

[] 

The tabstrip structure consists of 3 root-level and 1 item-level segments as shown below.

[] 

{border="0"}

**[]** 

Figure 309: Structure of TabStrip control

[] 

The below table lists the root-level segments and their corresponding CSS properties whose settings affect their styles.

[] 


  -------------------- -------------------------- --------------------------------
  Element              Property                   Default Value (CSS Class Name)
  Root element         ControlRootCSSClass        tabRoot
  Root panel element   ControlRootPanelCSSClass   tabRootPanel
  Root table element   ControlRootTableCSSClass   tabRootTable
  -------------------- -------------------------- --------------------------------


[] 

Customizing TabStrip Root-level segments

[] 

To customize the look and feel of one of the above segments, simply create a custom css style and associate it with the CSS property corresponding to the segment.

[] 

{border="0"}

**[]** 

Figure 310: TabStrip with css settings for the root elements

[] 

The css properties set to the custom css values and the style definitions are shown below.

[] 


+-----------------------------------+-----------------------------------+
|                                   |                                   |
|                                   |                                   |
| Property                          | Value (Custom CSS Class Name)     |
+-----------------------------------+-----------------------------------+
| ControlRootCSSClass               | RootElementCSS                    |
+-----------------------------------+-----------------------------------+
| ControlRootPanelCSSClass          | RootPanelElementCSS               |
+-----------------------------------+-----------------------------------+
| ControlRootTableCSSClass          | RootTableElementCSS               |
+-----------------------------------+-----------------------------------+


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Css Styles\]]**                                                  |
|                                                                                                                                         |
| []                                                                   |
|                                                                                                                                         |
| [.RootElementCSS]                                                    |
|                                                                                                                                         |
| [{]                                                                                 |
|                                                                                                                                         |
| [  [padding]:[20px]; ]                     |
|                                                                                                                                         |
| [  [background-color]:[#333365];         ] |
|                                                                                                                                         |
| [}]                                                                                 |
|                                                                                                                                         |
| [.RootPanelElementCSS]                                               |
|                                                                                                                                         |
| [{]                                                                                 |
|                                                                                                                                         |
| [  [padding]:[20px]; ]                     |
|                                                                                                                                         |
| [  [background-color]:[#f6f9ff];         ] |
|                                                                                                                                         |
| [}]                                                                                 |
|                                                                                                                                         |
| [.RootTableElementCSS]                                               |
|                                                                                                                                         |
| [{]                                                                                 |
|                                                                                                                                         |
| [  [padding]:[20px]; ]                     |
|                                                                                                                                         |
| [  [background-color]:[#c0c9db];         ] |
|                                                                                                                                         |
| [}]                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------+

[] 

Structure of a TabStrip Item

[] 

A single tab item is segregated into different image and text sections, the look for all of which can again be controlled through their corresponding css property settings. An item consists of a text and optionally an image.

[] 

{border="0"}

**[]** 

Figure 311: Structure of a tabstrip Item

[] 

The below table lists the item-level segments and their corresponding CSS properties whose settings affect their styles.

[] 


  ----------------------- ----------------------------- --------------------------------
  Element                 Property                      Default Value (CSS Class Name)
  Left image cell         LeftImageCellCSSClass         tabImgLeftCell
  Left image container    LeftImageContainerCSSClass    tabImgLeftCont
  Left image              LeftImageCSSClass             tabImgLeftCSS
  Image cell              ImageCellCSSClass             tabImgCell
  Image container         ImageContainerCSSClass        tabImgCont
  Image                   ImageCSSClass                 tabImgCSS
  Text cell               TextCellCssClass              tabTextCell
  Text container          TextContainerCssClass         tabTextContDef
  Right image cell        RightImageCellCSSClass        tabImgRightCell
  Right image container   RightImageContainerCSSClass   tabImgRightCont
  Right image             RightImageCSSClass            tabImgRightCSS
  ----------------------- ----------------------------- --------------------------------


[] 

**[Customizing TabStrip Item-level segments]**

[] 

The following section shows some custom styles applied on the different item-level segments and a screenshot of the resulting look.

[] 


+---------------------------------------------------------------------+-----------------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------+
| Image                                                               | Property                    | Custom CSS Class Name | CSS Definition                                                                                                         |
+---------------------------------------------------------------------+-----------------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------+
| []  | ItemCSSClass                | Def_ItemCSS           | .Def_ItemCSS                                                                                                           |
|                                                                     |                             |                       |                                                                                                                        |
| {border="0"}                          |                             |                       | {                                                                                                                      |
|                                                                     |                             |                       |                                                                                                                        |
| []  |                             |                       |   [background-color]:[#ccd4e6]  ;                                             |
|                                                                     |                             |                       |                                                                                                                        |
| TabStrip with style settings for left image                         |                             |                       |   [padding]:[10px];                                                           |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       |   [border]:[1px] [solid] [#333365]; |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       | }                                                                                                                      |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       | .LeftImgCellCSS                                                                                                        |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       | {                                                                                                                      |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       |   [border]:[1px] [solid] [black];   |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       | }                                                                                                                      |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       | .LeftImgContCSS                                                                                                        |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       | {                                                                                                                      |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       |   [background-color]:[#ffbb6f];                                               |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       |   [padding]:[5px];                                                            |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       | }                                                                                                                      |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       | .LeftImgCSS                                                                                                            |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       | {                                                                                                                      |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       |   [height]:[15px];                                                            |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       |   [width]:[16px];                                                             |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       | }                                                                                                                      |
|                                                                     +-----------------------------+-----------------------+                                                                                                                        |
|                                                                     | LeftImageCellCSSClass       | LeftImgCellCSS        |                                                                                                                        |
|                                                                     +-----------------------------+-----------------------+                                                                                                                        |
|                                                                     | LeftImageContainerCSSClass  | LeftImgContCSS        |                                                                                                                        |
|                                                                     +-----------------------------+-----------------------+                                                                                                                        |
|                                                                     | LeftImageCSSClass           | LeftImgCSS            |                                                                                                                        |
+---------------------------------------------------------------------+-----------------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------+
| []  | RightImageCellCSSClass      | RightImgCellCSS       | .RightImgContCSS                                                                                                       |
|                                                                     |                             |                       |                                                                                                                        |
| {border="0"}                          |                             |                       | {                                                                                                                      |
|                                                                     |                             |                       |                                                                                                                        |
| []  |                             |                       |   [background-color]:[#ffbb6f];                                               |
|                                                                     |                             |                       |                                                                                                                        |
| TabStrip with style settings for right image                        |                             |                       |   [padding]:[5px];                                                            |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       | }                                                                                                                      |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       | .RightImgCellCSS                                                                                                       |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       | {                                                                                                                      |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       |   [border]:[1px] [solid] [black];   |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       | }                                                                                                                      |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       | .RightImgCSS                                                                                                           |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       | {                                                                                                                      |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       |   [height]:[15px];                                                            |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       |   [width]:[16px];                                                             |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       | }                                                                                                                      |
|                                                                     +-----------------------------+-----------------------+                                                                                                                        |
|                                                                     | RightImageContainerCSSClass | RightImgContCSS       |                                                                                                                        |
|                                                                     +-----------------------------+-----------------------+                                                                                                                        |
|                                                                     | RightImageCSSClass          | RightImgCSS           |                                                                                                                        |
+---------------------------------------------------------------------+-----------------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------+
| []  | TextCellCssClass            | Def_TextCellCSS       | .Def_TextCellCSS                                                                                                       |
|                                                                     |                             |                       |                                                                                                                        |
| {border="0"}                          |                             |                       | {                                                                                                                      |
|                                                                     |                             |                       |                                                                                                                        |
| []  |                             |                       |   [padding]:[10px];                                                           |
|                                                                     |                             |                       |                                                                                                                        |
| TabStrip with style settings for text                               |                             |                       |   [background-color]:[#c0c9db];                                               |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       | }                                                                                                                      |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       | .Def_TextContCSS                                                                                                       |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       | {                                                                                                                      |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       |   [font-family]:[Verdana];                                                    |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       |   [font-size]:[11px];                                                         |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       |   [color]:[black] ;                                                           |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       |   [font-weight]:[bold];                                                       |
|                                                                     |                             |                       |                                                                                                                        |
|                                                                     |                             |                       | }                                                                                                                      |
|                                                                     +-----------------------------+-----------------------+                                                                                                                        |
|                                                                     | TextContainerCssClass       | Def_TextContCSS       |                                                                                                                        |
+---------------------------------------------------------------------+-----------------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------+


[] 

The structure of the item will be altered according to the text and the image position. The image and the text position can be controlled by setting the **ImageAndTextPosition** property. The below table shows the image, on setting the various options of the ImageAndTextPosition property.

[] 


  --------------------- --------------------------------------------
  Text Position Value   Image
  ImageLeftTextRight    {border="0"}
  TextLeftImageRight    {border="0"}
  ImageOverText         {border="0"}
  TextOverImage         {border="0"}
  --------------------- --------------------------------------------


 

[]{#related-topics}

