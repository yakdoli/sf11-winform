---
title: baritems.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\baritems.md
created_at: 2025-07-03
---






##### Bar Items      {#bar-items style="tab-stops: 0pt"}

[] 

This section will discuss various types of bar items, their properties and customization using the properties.

**[]** 

###### []{#p858}[]{#_Customize_Dialog}3.5.4.1.2.1 Customize Dialog {#customize-dialog style="tab-stops: 0pt"}

Bar items can be added to a BarManager using Customize dialog through Designer. See [Adding Bar Items to a BarManager] to know how to add bar items.

**[]** 

Customize Dialog

[] 

The **Customize** Dialog can be accessed at design time and also at runtime. It lets the end users to add and customize menus, toolbars and layout items during design time. This can be invoked at design time, by right-clicking the mainFrameBarManager and selecting the Customize option in the designer.

[] 

{border="0"}

[]{#p859} 

Figure 732: Customize dialog at Design Time

 

At run time, Customize dialog can be accessed by right-clicking on the Bar and clicking the Customize option. This dialog lets you control the layout of items in a toolbar.

[] 

{border="0"}

[] 

Figure 733: Accessing Customize Dialog at runtime by right-clicking the Bar

[] 

{border="0"}

 

Figure 734: Accessing the Customization Dialog at Run Time by using Menu Arrow Button

(BarStyle=IsMainMenu Unchecked)

**[]** 


 Note: To avoid displaying the bar items in Customize dialog at run time, set BarManager.ShowItemsInCustomizationDialog property to false.


[] 

[] 

{border="0"}

Figure 735: BarItems not displayed at Run Time

**[]** 


 Note: If you want to disable Customizing option for the users at run time, set BarManager.EnableCustomizing property to false. This will not provide option to open the Customize dialog at run time.


[] 

See Also

[] 

[[Bar Styles]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sindhujamj/Desktop/Bar%20Styles.html)[,]{.UGHyperlink}[ ]{.UGHyperlink}[[Customize Dialog Appearance]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sindhujamj/Desktop/CustomizeDialogAppearance.html)[]{.UGHyperlink}

 

 

###### []{#_Types_of_Bar}[3.5.4.1.2.2      ]Types of Bar Items[] {#types-of-bar-items style="tab-stops: 0pt"}

[] 

The following Bar items are discussed in this section.

[] 

[]{#p860}[]{#_BarItem}3.5.4.1.2.2.1      BarItem

[] 

A BarItem is a simple child bar item which can be dragged and dropped to a ParentBarItem. By selecting the Type as BarItem and giving the name, in the Add New BarItem dialog, we can create a new BarItem.

[] 

{border="0"}

[] 

Figure 736: Adding BarItem in the designer using Customize Dialog Box

[] 

Behavior Properties

[] 

Some properties are as follows.

[] 


+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ParentBarItem Property            | Description                                                                                                                                             |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Checked                           | Draws the bar item with a checked appearance.                                                                                                           |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Enabled                           | Enables or disables the bar item. Default value is true.                                                                                                |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| IsRecentlyUsedItem                | Indicates whether this item will appear in its parent\'s partial menus list. Partial Menus is discussed in [ParentBarItem] topic. |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Visible                           | Sets the visibility of the bar item.                                                                                                                    |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| MergeOrder                        | Relative Position of the bar item when it is merged with another.                                                                                       |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| MergeType                         | Sets behavior of the bar item when its bar is merged with another. The options are,                                                                     |
|                                   |                                                                                                                                                         |
|                                   |                                                                                                                                                         |
|                                   |                                                                                                                                                         |
|                                   | Add - Adds to the existing menu items. (Default)                                                                                                        |
|                                   |                                                                                                                                                         |
|                                   | Replace - Replaces an existing menu items at the same position in a merged menu.                                                                        |
|                                   |                                                                                                                                                         |
|                                   | MergeItems - Merged with an existing menu items at the same position in a merged menu.                                                                  |
|                                   |                                                                                                                                                         |
|                                   | Remove - Menu item will not be included in the merged menu. See ParentBarItem for merging the bar items.                                                |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Customizable                      | Specifies whether the bar item is involved in the customization.                                                                                        |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Padding                           | Gets or sets padding for items.                                                                                                                         |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| PaddingForThemesX                 | Specifies padding for theme control X.                                                                                                                  |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| PaddingForThemesY                 | Specifies padding for theme control Y.                                                                                                                  |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ShowMnemonicUnderlinesAlways      | It indicates whether to show underlines with mnemonic always.                                                                                           |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+


**[]** 

**[]** 

**[]** 

Other Common properties

**[]** 

[For setting images see ]Image Settings[; ][]

[For Editing the text and setting text alignments, See ]BarItem Text[; ][]

[For setting shortcuts for the bar items, see ]Keyboard shortcuts[ and ]

[For changing the Paint Style, ][see ]PaintStyle[ topic. ]

[Appearance of the Text can be customized. See ]Foreground Settings[ for details.]

[] 

{border="0"}

[] 

Figure 737: Illustrates BarItem in a ParentBarItem dropdown with Image and Keyboard shortcut and PaintStyle Settings

 

See Also

[] 

Customization Options[,][ UpdateUIOnAppIdle property in ]UI Command Update Patterns[ topic]

[]{#p861}[]{#_ParentBarItem}3.5.4.1.2.2.2      ParentBarItem

[] 

A **ParentBarItem** represents a submenu (drop-down menu) which can display one or more child BarItems on drop-down. A ParentBarItem can be placed inside a toolbar and it can contain another ParentBarItem as its child bar item. ParentBarItem comes with properties to control its appearance and behavior.

[] 

{border="0"}

[] 

Figure 738: Adding ParentBarItem by selecting Type as ParentBarItem through Designer using Customize Dialog Box

[] 

Behavior Settings

[] 

The following propertieslet you control the behavior of the ParentBarItem.

[] 


+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ParentBarItem Property            | Description                                                                                                            |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
| Checked                           | Draws the bar item with a checked appearance.                                                                          |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
| Enabled                           | Enables or disables the bar item. Default value is true.                                                               |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
| IsRecentlyUsedItem                | Indicates whether this item will appear in its parent\'s partial menus list.                                           |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
| Visible                           | Sets the visibility of the bar item.                                                                                   |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
| MergeOrder                        | Relative Position of the bar item when it is merged with another.                                                      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
| MergeType                         | Sets behavior of the bar item when its bar is merged with another. The options are,                                    |
|                                   |                                                                                                                        |
|                                   |                                                                                                                        |
|                                   |                                                                                                                        |
|                                   | Add - Adds to the existing menu items. (Default)                                                                       |
|                                   |                                                                                                                        |
|                                   | Replace - Replaces an existing menu items at the same position in a merged menu.                                       |
|                                   |                                                                                                                        |
|                                   | MergeItems - Merged with an existing menu items at the same position in a merged menu.                                 |
|                                   |                                                                                                                        |
|                                   | Remove - Menu item will not be included in the merged menu.                                                            |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
| Customizable                      | Specifies whether the bar item is involved in the customization.                                                       |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ParentStyle                       | Specifies the ParentStyle on which the menu will be drawn. The options are,                                            |
|                                   |                                                                                                                        |
|                                   |                                                                                                                        |
|                                   |                                                                                                                        |
|                                   | Default (Default),                                                                                                     |
|                                   |                                                                                                                        |
|                                   | DropDown.                                                                                                              |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
| Padding                           | Gets or sets padding for items.                                                                                        |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ScrollingSpeed                    | Specifies the scrollingspeed for the displayed child menu items.                                                       |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ScrollOnMouseMove                 | Specifies scroll items in menu when mouse moves over scroll buttons.                                                   |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
| UsePartialMenus                   | Specifies whether ParentBarItem will first show a list of  recently used items and an Expand button when dropped down. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ShowMnemonicUnderlinesAlways      | It indicates whether to show underlines with mnemonic always.                                                          |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+


**[]** 

Merging

**[]** 

XPMenus FrameWork lets you merge menu items of different ParentBarItems using **MergeItems** method.

**[]** 


+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ParentBarItem Method              | Description                                                                                                                                                                                                                                                                                                   |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MergeItems                        | Merges BarItems of one ParentBarItem with another ParentBarItem. Two ParentBarItems can be merged into one, based on the [MergeOrder] and[ ][MergeType][ ]properties of its children (/ menu item). Parameter is, |
|                                   |                                                                                                                                                                                                                                                                                                               |
|                                   |                                                                                                                                                                                                                                                                                                               |
|                                   |                                                                                                                                                                                                                                                                                                               |
|                                   | parentItemSrc - The ParentBarItem which is merged with this ParentBarItem.                                                                                                                                                                                                                                    |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**[]** 

{border="0"}

**[]** 

Figure 739: ParentBarItems displaying Child Bar Items / Menu Items before Merging

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                  |
|                                                                                                                                                                 |
| []                                                                                                            |
|                                                                                                                                                                 |
| [//Setting merge order and merge type of bar item5 (List) of ParentBarItem2]                                  |
|                                                                                                                                                                 |
| [this][.barItem5.MergeOrder = 0;]                                          |
|                                                                                                                                                                 |
| [this][.barItem5.MergeType = [MenuMerge].MergeItems;] |
|                                                                                                                                                                 |
| [//Merging parentbaritem2 menu items to parentbaritem1]                                                       |
|                                                                                                                                                                 |
| [this][.parentBarItem1.MergeItems(parentBarItem3);]                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                           |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [\'Setting merge order and merge type of bar item5 (List) of ParentBarItem2]                               |
|                                                                                                                                                              |
| [Me][.barItem5.MergeOrder = 0]                                          |
|                                                                                                                                                              |
| [Me][.barItem5.MergeType = [MenuMerge].MergeItems] |
|                                                                                                                                                              |
| [\'Merging parentbaritem2 menu items to parentbaritem1]                                                    |
|                                                                                                                                                              |
| [Me][.parentBarItem1.MergeItems(parentBarItem3)]                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[{border="0"}][]**

**[]** 

Figure 740: MenuItems of ParentBarItem2 merged to ParentBarItem1; MergeOrder of BarItem5(List)=0

**[]** 

Parent Style

[] 

The following figures display the parent styles.

**[]** 

{border="0"}

**[]** 

Figure 741: Default and Dropdown ParentStyle with IsMainMenu Unchecked

**[]** 

Partial Menus

**[]** 

The ParentBarItem can hide some of its menu items and display them on clicking an expand button at the bottom of the menu list, by using the **UsePartialMenus** and **IsRecentlyUsedItem** properties. With this feature we can display only the recently used items and can hide the rest. We can do this in **ParentBarItem.BeforePopup** event.

[] 


  ------------------------------ --------------------------------------------------------------------------------------
  BarManager Property            Description
  ExpandPartialMenusAfterDelay   Enables automatic expansion of the partial menus into full menus after a delay.
  UsePartialMenus                Enables or disables partial menus mode in submenus.
  PartialMenusResetDelay         Specifies the delay in days after an item\'s recently used setting will be replaced.
  ------------------------------ --------------------------------------------------------------------------------------


[] 


{border="0"} Note:[ ]To know all the properties of BarManager, click [here].


[] 

{border="0"}

[] 

Figure 742: ParentBarItem with Menu List

**[]** 

Applying Partial Menus

**[]** 


+-----------------------------------+-------------------------------------------------------+
| ParentBarItem Event               | Description                                           |
+-----------------------------------+-------------------------------------------------------+
| BeforePopUp                       | Handled before the popup menu is shown. Parameter is, |
|                                   |                                                       |
|                                   |                                                       |
|                                   |                                                       |
|                                   | cancel - lets you cancel the menu display.            |
+-----------------------------------+-------------------------------------------------------+


**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [this][.parentBarItem1.UsePartialMenus = [true];]                                                                                                   |
|                                                                                                                                                                                                                                                               |
| [private][ [void] parentBarItem1_BeforePopup([object] sender, System.ComponentModel.[CancelEventArgs] e)] |
|                                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                               |
| [    [// Hide New and Close BarItems in the partial menu]]                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [    [this].barItem1.IsRecentlyUsedItem = [false];]                                                                                                                             |
|                                                                                                                                                                                                                                                               |
| [    [this].barItem3.IsRecentlyUsedItem = [false];]                                                                                                                             |
|                                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                     |
| [Me][.parentBarItem1.UsePartialMenus = [True]]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                     |
| [Private][ [Sub] parentBarItem1_BeforePopup([ByVal] sender [As] [Object], [ByVal] e [As] System.ComponentModel.CancelEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    [\' Hide Open and Close BarItems in the partial menu ]]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    [Me].barItem1.IsRecentlyUsedItem = [False]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    [Me].barItem3.IsRecentlyUsedItem = [False]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                     |
| [End][ [Sub]]                                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 743: Expand Button Displayed; BarItem1 (New) and BarItem3 (Close) are Hidden

**[]** 

Other Common properties

**[]** 

[For setting images see ]Image Settings[ ][]

[For Editing the text and setting text alignments, ][see ]BarItem Text[ ][]

[For setting shortcuts for the bar items, see ]Keyboard shortcuts[ and ]

[For changing the Paint Style, ][see ]PaintStyle[ topic. ]

[Appearance of the Text can be customized. See ]Foreground Settings[ for details.]

**[]** 

See Also

**[]** 

[UI Command Update Patterns]{.UGHyperlink}[,]{.UGHyperlink}

[MainFrameBarManager Properties,]{.UGHyperlink}[]{.UGHyperlink}

[[Customize Dialog]{.UGHyperlink}]()[]{.UGHyperlink}

[[]]{.UGHyperlink} 

[]{#p862}3.5.4.1.2.2.3      DropDownBarItem

[] 

A DropDownBarItem is a BarItem that gets drawn with an arrow button to its right, which when clicked, will pop-up a window (note: not a menu) represented by a PopupControlContainer. This is identical to the Undo menu item in VS .NET code editor.

[] 

{border="0"}

***[]*** 

Figure 744: DropDownBarItem

 

The type should be selected as DropDownBarItem in the Add New BarItem dialog.

[] 

{border="0"}

[] 

Figure 745: Adding DropDownBarItem in the designer by using Customize Dialog Box

**[]** 

Displaying the Popup Menu

**[]** 

We need to associate a PopupControlContainer for showing the popup. Drag-and-drop a PopupControlContainer component and associate it with the DropDownBarItem using **PopupControlContainer** property of DropDownBarItem.

[] 

{border="0"}

[] 

Figure 746: Associating PopupControlContainer component with DropDownBarItem

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                             |
|                                                                                                                                                                                            |
| []                                                                                                                                       |
|                                                                                                                                                                                            |
| [this][.dropDownBarItem1.PopupControlContainer = [this].popupControlContainer1;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                    |
|                                                                                                                                                                                       |
| []                                                                                                                                  |
|                                                                                                                                                                                       |
| [Me][.dropDownBarItem1.PopupControlContainer = [Me].popupControlContainer1] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

We can add controls like ColorPickerUI control to this container and customize the popup for the DropDownBarItem.

[] 

{border="0"}

[] 

Figure 747: DropDownBarItem displaying ColorPickerUI in its Popup

**[]** 

**[]** 

**[]** 

Behavior Settings

**[]** 

DropDownBarItem supports all the behavior properties of the BarItem.

**[]** 

Other Common properties

**[]** 

For setting images see[ ]Image Settings[; ][]

For Editing the text and setting text alignments, See BarItem Text;

For setting shortcuts for the bar items, see[ ]Keyboard shortcuts[ and ]

For changing the Paint Style, see[ ]PaintStyle[ topic. ]

Appearance of the Text can be customized. See[ ]Foreground Settings[ for details.]

**[]** 

See Also

[] 

UpdateUIOnAppIdle property in UI Command Update Patterns topic,

[Customize Dialog]()[]

[]{#p863}3.5.4.1.2.2.4      ComboBoxBarItem

 

A[ ]**ComboBoxBarItem**[ ]is a BarItem that provides combobox-like behavior with an optional editable mode. This is identical to the **VS.NET Find combo box**[ ]in the code editor.

[] 

{border="0"}

**[]** 

Figure 748: Adding ComboBoxBarItem in the designer using Customize Dialog Box

    

Adding Items for ComboBoxBarItem dropdown

**[]** 

A list of items can be specified in **ComboBoxBarItem.ChoiceList** property. ComboBoxBarItem can also be associated with another control like FontListControl using the **ListBox** property. You can also specify the width for this BarItem.

 

The following properties deal with settings contents for the ComboBoxBarItem.

**[]** 


  -------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------
  ComboBoxBarItem Property   Description
  AutoAppend                 Specifies whether to automatically append the items entered by the user in the TextBox into the dropdown list.
  MaxDropDownItems           Specifies the maximum number of items to be shown in the drop down portion of ComboBoxBarItem.
  MinDropDownWidth           Sets the width of the drop down.
  MinWidth                   Sets the minimum width when this ComboBoxBarItem is placed in a menu or toolbar.
  TextBoxValue               Sets the value in the TextBox.
  PersistTextBoxValue        Specifies whether the TextBox value should be persisted after the application is shutdown.
  Listbox                    Specifies custom listbox in the dropdown. You can drag and drop a FontListControl for ex, and associate it to the ComboBoxBarItem using this property.
  ChoiceList                 Specifies the list for the bar item.
  -------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                     |
|                                                                                                                                                                    |
| []                                                                                                               |
|                                                                                                                                                                    |
| [this][.comboBoxBarItem1.AutoAppend=[true];]             |
|                                                                                                                                                                    |
| [this][.comboBoxBarItem1.MaxDropDownItems=3;]                                 |
|                                                                                                                                                                    |
| [this][.comboBoxBarItem1.MinDropDownWidth=1;]                                 |
|                                                                                                                                                                    |
| [this][.comboBoxBarItem1.MinWidth=100;]                                       |
|                                                                                                                                                                    |
| [this][.comboBoxBarItem1.TextBoxValue=\"Debug\";]                             |
|                                                                                                                                                                    |
| [this][.comboBoxBarItem1.PersistTextBoxValue=[true];]    |
|                                                                                                                                                                    |
| [this][.comboBoxBarItem1.ListBox = [this].fontListBox1;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                            |
|                                                                                                                                                               |
| []                                                                                                          |
|                                                                                                                                                               |
| [Me][.comboBoxBarItem1.AutoAppend=[True]]           |
|                                                                                                                                                               |
| [Me][.comboBoxBarItem1.MaxDropDownItems=3]                               |
|                                                                                                                                                               |
| [Me][.comboBoxBarItem1.MinDropDownWidth=1]                               |
|                                                                                                                                                               |
| [Me][.comboBoxBarItem1.MinWidth=100]                                     |
|                                                                                                                                                               |
| [Me][.comboBoxBarItem1.TextBoxValue=[\"Debug\"]]  |
|                                                                                                                                                               |
| [Me][.comboBoxBarItem1.PersistTextBoxValue=[True]]  |
|                                                                                                                                                               |
| [Me][.comboBoxBarItem1.ListBox = [Me].fontListBox1] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 749: Associating FontListControl with the ComboBoxBarItem

[] 

{border="0"}

[] 

Figure 750: ComboBoxBarItem with FontListBox

**[]** 


{border="0"} Note: Editable property should be set to true for displaying the FontListControl in this case and PaintStyle should be ImageAndText for displaying the ComboBoxBarItem text.


[] 

Behavior Settings

[] 

ComboBoxBarItem supports all the behavior properties of [BarItem]().

**[]** 

Other Common properties

**[]** 

[For setting images see ]Image Settings[; ][]

[For Editing the text and setting text alignments, See ]BarItem Text[; ][]

[For setting shortcuts for the bar items, see ]Keyboard shortcuts[ and ]

[Appearance of the Text can be customized. See ]Foreground Settings[ for details.]

[We can set banner text for the ComboBoxBarItem. Refer ][BannerTextProvider Component](../../../../../../../../Documents%20and%20Settings/sindhujamj/Desktop/D2H/ui/windows/tools/Documents/Tools%20-%20Part%202.docx#BannerTextProviderComponent)[ topic for more details.]

[] 

{border="0"}

Figure 751: Banner Text set for ComboBoxBarItem

***[]*** 

PersistAutoAppendList inclusion.

**[]** 

PersistAutoAppendList property is added to ComboBoxBarItem. 

When this property is set to false and AutoAppend is set to true, the item added to the ComboBoxBarItem will be added to the dropdown but it will not be saved.

[] 

{border="0"}

Figure 752: ComboBoxBarItem Dropdown

[] 

The following code illustrates how to include **PersistAutoAppendList**.


          {border="0"}Note: This can be used when the AutoAppend is set to true.


[] 

+----------------------------------------------------------------------------------------------------------+
| **[\[C# .Net\]]**                                           |
|                                                                                                          |
| [API:  this.comboBoxBarItem1.PersistAutoAppendList =false;] |
+----------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------+
| **[\[VB .Net\]]**                                    |
|                                                                                                   |
| [ Me.comboBoxBarItem1.PersistAutoAppendList = false] |
+---------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[   UpdateUIOnAppIdle property in ]{.UGHyperlink}[UI Command Update Patterns]{.UGHyperlink}[ topic ]{.UGHyperlink}

[How to handle KeyDown event in ComboBoxBarItem?]{.UGHyperlink}[ ]{.UGHyperlink}

[How to prevent the ComboBoxBarItem\'s dropdown from being closed after clicking a ChoiceList Item?]{.UGHyperlink}[]{.UGHyperlink}

[[Customize Dialog]{.UGHyperlink}]()[]{.UGHyperlink}

[] 

[]{#p864}[]{#_ListBarItem}3.5.4.1.2.2.5      ListBarItem

[] 

A[ ]**ListBarItem**[ ]is a BarItem which, when added to a ParentBarItem will expand itself into an ordered list of BarItems represented by the string list in its[ ]**ChildCaptions** property.

[] 

{border="0"}

**[]** 

Figure 753: Adding ListBarItem in the designer using Customize Dialog Box

**[]** 

Adding Items for the ListBarItems

**[]** 

A list of items can be specified in **ListBarItem.ChildCaptions** property and this ListBarItem should be added to a ParentBarItem. The list can be numbered by enabling **UseNumberedList** property.

[] 


  ---------------------- ------------------------------------------------------------------
  ListBarItem Property                        Description
  ChildCaptions          Specifies the list of items to be displayed in the ListBarItem.
  UseNumberedList        It specifies whether or not to use numbers in the expanded list.
  Customizable           Specifies whether the bar item is involved in the customization.
  ---------------------- ------------------------------------------------------------------


[] 


{border="0"} Note: The BarItem should not be in User Customization mode / Customizable property should be set to false, to effect these settings.


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                           |
| [this][.listBarItem1.Customizable = [false];]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                           |
| [this][.listBarItem1.ChildCaptions.AddRange([new] [string]\[\] {[\"Document1\"], [\"Document2\"], [\"Document3\"]});] |
|                                                                                                                                                                                                                                                                                                                           |
| [this][.listBarItem1.UseNumberedList = [true];]                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                       |
| [Me][.listBarItem1.Customizable = [False] ]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                       |
| [Me][.listBarItem1.ChildCaptions.AddRange([New] [String]() {[\"Document1\"], [\"Document2\"], [\"Document3\"]}) ] |
|                                                                                                                                                                                                                                                                                                                       |
| [Me][.listBarItem1.UseNumberedList = [True] ]                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 754: Numbered List

**[]** 

Behavior Settings

**[]** 

ListBarItem supports all the behavior properties of BarItem.

[] 

Other Common properties

[] 

[For setting images see ]Image Settings[; ][]

[For Editing the text and setting text alignments, ][see ]BarItem Text[; ][]

[For setting shortcuts for the bar items, see ]Keyboard shortcuts[ and ]

[For changing the Paint Style, ][see ]PaintStyle[ topic. ]

[Appearance of the Text can be customized. See ]Foreground Settings[ for details.]

[] 

See Also

[] 

UpdateUIOnAppIdle property in UI Command Update Patterns topic,

[Customize Dialog]()[]

[]{#_MDIListBarItem}3.5.4.1.2.2.6      MDIListBarItem

[]{#p865}[] 

An **MDIListBarItem** is a ListBarItem that will expand itself to show a list of MDIChild windows in the form, when placed in a ParentBarItem.

[] 

{border="0"}

 

Figure 755: Adding MDIListBarItem in the designer using Customize Dialog Box

**[]** 

Specify the MDI List Size in **MDIListSize** property.

**[]** 


  ---------------------- ------------------------------------------------------------------
  ListBarItem Property   Description
  MDIListSize            Specifies number of child links to be specified.
  UseNumberedList        It specifies whether or not to use numbers in the expanded list.
  ---------------------- ------------------------------------------------------------------


[] 

{border="0"}

**[]** 

Figure 756: MDIListBar item displaying the MDI Children in the Form

**[]** 

A sample demonstrating this feature is available in the below sample installation location.

 

..My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Menus Package\\XPMenusMDI

**[]** 

Behavior Settings

**[]** 

DropDownBarItem supports all the behavior properties of BarItem.

[] 

Other Common properties

 

[For setting images see ]Image Settings[; ][]

[For Editing the text and setting text alignments, See ]BarItem Text[; ][]

[For setting shortcuts for the bar items, see ]Keyboard shortcuts[ and ]

[For changing the Paint Style, ][see ]PaintStyle[ topic. ]

[Appearance of the Text can be customized. See ]Foreground Settings[ for details.]

[] 

See Also

[] 

UpdateUIOnAppIdle property in UI Command Update Patterns topic,

[[Customize Dialog]{.UGHyperlink}]()[]{.UGHyperlink}

[] 

[]{#p866}3.5.4.1.2.2.7      StaticBarItem

[] 

A **StaticBarItem** is a BarItem that provides users a label-like behavior to show plain text in the toolbars and menus.

 

The user cannot click or interact with this type of BarItem. It is typically used in the status bar-type toolbar.

[] 

{border="0"}

[] 

Figure 757: Adding StaticBarItem Through designer using Customize Dialog Box

[] 

The text displayed in the status bar can be changed based on the bar items selected. Insert the following code snippet in the \'Selected\' event handler of any bar items whose status is to be known.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                              |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| [private][ [void] Item_Selected([object] sender, System.[EventArgs] e)] |
|                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [BarItem][ item = sender [as] [BarItem];]                                                    |
|                                                                                                                                                                                                                             |
| [this][.staticBarItem1.Text = item.Text;]                                                                                              |
|                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                   |
| [Private][ [Sub] Item_Selected([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                   |
| [    [Dim] item [As] BarItem = [CType](IIf([TypeOf] sender [Is] BarItem, sender, [Nothing]), BarItem)]                                          |
|                                                                                                                                                                                                                                                                                                                   |
| [    [Me].staticBarItem1.Text = item.Text]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                   |
| [End][ [Sub]]                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 758: StatusBar displaying the bar item that is Selected

[] 

Behavior Settings

[] 


+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ParentBarItem Property            | Description                                                                                                                                             |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| FlatBorderColor                   | Sets border color for the StaticBarItem.                                                                                                                |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| IsRecentlyUsedItem                | Indicates whether this item will appear in its parent\'s partial menus list. Partial Menus is discussed in [ParentBarItem] topic. |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Visible                           | Sets the visibility of the bar item.                                                                                                                    |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| MergeOrder                        | Relative Position of the bar item when it is merged with another.                                                                                       |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| MergeType                         | Sets behavior of the bar item when its bar is merged with another. The options are,                                                                     |
|                                   |                                                                                                                                                         |
|                                   |                                                                                                                                                         |
|                                   |                                                                                                                                                         |
|                                   | *Add* - Adds to the existing menu items. (Default)                                                                                                      |
|                                   |                                                                                                                                                         |
|                                   | *Replace* - Replaces an existing menu items at the same position in a merged menu.                                                                      |
|                                   |                                                                                                                                                         |
|                                   | *MergeItems* - Merged with an existing menu items at the same position in a merged menu.                                                                |
|                                   |                                                                                                                                                         |
|                                   | *Remove* - Menu item will not be included in the merged menu.                                                                                           |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Customizable                      | Specifies whether the bar item is involved in the customization.                                                                                        |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Padding                           | Gets or sets padding for items.                                                                                                                         |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ShowMnemonicUnderlinesAlways      | It indicates whether to show underlines with mnemonic always.                                                                                           |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

Other Common properties

**[]** 

[For setting images see ]Image Settings[; ][]

[For Editing the text and setting text alignments, See ]BarItem Text[; ][]

[For changing the Paint Style, ][see ]PaintStyle[ topic. ]

[Appearance of the Text can be customized. See ]Foreground Settings[ for details.]

[] 

See Also

[] 

UpdateUIOnAppIdle property in UI Command Update Patterns topic,

[[Customize Dialog]{.UGHyperlink}]()[]{.UGHyperlink}

[]{#p867}[]{#_ToolBarListBarItem}3.5.4.1.2.2.8      ToolBarListBarItem

[] 

A **ToolbarListBarItem** is a ListBarItem that expands during runtime to automatically show the list of toolbars currently used in the application. The user can click on this list to show / hide the toolbars. A ToolBarListBarItem can be added to a ParentBarItem by a simple drag-and-drop similar to other bar items.

[] 

{border="0"}

**[]** 

Figure 759: Adding ToolbarListBarItem through the designer by using Customize Dialog Box

**[]** 

{border="0"}

***[]*** 

Figure 760: ToolbarListBarItems Displayed

[] 

Behavior Settings

**[]** 

DropDownBarItem supports all the behavior properties of BarItem.

**[]** 

Other Common properties

**[]** 

For setting images see [Image Settings];

For Editing the text and setting text alignments, see [BarItem Text];

For setting shortcuts for the bar items, see [Keyboard shortcuts] and

For changing the Paint Style, see [PaintStyle] topic.

Appearance of the Text can be customized. See [Foreground Settings] for details.

[] 

See Also

[] 

[UI Command Update Patterns]{.UGHyperlink}[,]{.UGHyperlink}

[[Customize Dialog]{.UGHyperlink}]()[]{.UGHyperlink}

[] 

3.5.4.1.2.2.9      TextBoxBarItem

[]{#p868}[] 

A TextBoxBarItem behaves like a normal windows textbox. It lets the end users to enter text in the text area at run time. You can also specify the text in **TextBoxValue** property. A TextBoxBarItem can be added to a ParentBarItem by a simple drag and drop similar to other bar items. Width of the TextBoxBarItem can be controlled using **MinWidth** property.

[] 


{border="0"} Note: Paint Style should be \"ImageAndText\" for the TextBoxBarItem to display TextBoxBarItem.Text.


[] 

{border="0"}

[] 

Figure 761: Adding TextBoxBarItems

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                    |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                   |
| [this][.textBoxBarItem1.MinWidth = 100;]                                                                                     |
|                                                                                                                                                                                                                   |
| [this][.textBoxBarItem1.PaintStyle = Syncfusion.Windows.Forms.Tools.XPMenus.[PaintStyle].ImageAndText;] |
|                                                                                                                                                                                                                   |
| [this][.textBoxBarItem1.Text = [\"Product Name\"];]                                                   |
|                                                                                                                                                                                                                   |
| [this][.textBoxBarItem1.TextBoxValue = [\"Essential Chart\"];]                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                              |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                 |
| [Me][.textBoxBarItem1.MinWidth = 100;]                                                                                     |
|                                                                                                                                                                                                                 |
| [Me][.textBoxBarItem1.PaintStyle = Syncfusion.Windows.Forms.Tools.XPMenus.[PaintStyle].ImageAndText;] |
|                                                                                                                                                                                                                 |
| [Me][.textBoxBarItem1.Text = [\"Product Name\"];]                                                   |
|                                                                                                                                                                                                                 |
| [Me][.textBoxBarItem1.TextBoxValue = [\"Essential Chart\"];]                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

***[]*** 

Figure 762: TextBoxBarItem

[] 

Behavior Settings

**[]** 

DropDownBarItem supports all the behavior properties of BarItem.

[] 

Other Common properties

**[]** 

[For setting images see ]Image Settings[; ][]

[For Editing the text and setting text alignments, See ]BarItem Text[; ][]

[For setting shortcuts for the bar items, see ]Keyboard shortcuts[ and ]

[For changing the Paint Style, ][see ]PaintStyle[ topic. ]

[Appearance of the Text can be customized. See ]Foreground Settings[ for details.]

[We can set banner text for the TextBoxBarItem. Refer ][BannerTextProvider Component](../../../../../../../../Documents%20and%20Settings/sindhujamj/Desktop/D2H/ui/windows/tools/Documents/Tools%20-%20Part%202.docx#BannerTextProviderComponent)[ topic for more details.]

[] 

See Also

[] 

UpdateUIOnAppIdle property in UI Command Update Patterns topic,

[Customize Dialog]()[]

###### []{#p869}[]{#_Customization_Options}3.5.4.1.2.3 Customization Options {#customization-options style="tab-stops: 0pt"}

 

[]{#p870}This section discusses the behavior settings common to all types of BarItem.

[] 

[] 

See Also

[] 

[[Types of Bar Items]{.UGHyperlink}]()[]{.UGHyperlink}

[]{#_Paint_Style}3.5.4.1.2.3.1      Paint Style

[] 

The MenuItem can be displayed as a TextOnly, ImageOnly or Image and Text using **PaintStyle** property.

[] 

{border="0"}

[] 

Figure 763: PaintStyle property Options

[] 


+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BarItem Property                  | Description                                                                                                                                                                  |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PaintStyle                        | Indicates the painting style of the bar item.                                                                                                                                |
|                                   |                                                                                                                                                                              |
|                                   |                                                                                                                                                                              |
|                                   |                                                                                                                                                                              |
|                                   | *Default* - Displays the style of it parents. In case of MainMenu, only text will be drawn, in other toolbars only image and in Dropdown menu, image and text will be drawn. |
|                                   |                                                                                                                                                                              |
|                                   | *TextOnly* - Displays only Text.                                                                                                                                             |
|                                   |                                                                                                                                                                              |
|                                   | *TextOnlyInMenus* - Image will be ignored when the BarItem is in a drop down menu.                                                                                           |
|                                   |                                                                                                                                                                              |
|                                   | *ImageAndText* - Both Image and Text will be drawn.                                                                                                                          |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                                     |
| [   ]                                                                                                                           |
|                                                                                                                                                                     |
| [this][.barItem4.PaintStyle = [PaintStyle].ImageAndText;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                        |
|                                                                                                                                           |
| []                                                                                                    |
|                                                                                                                                           |
| [Me][.barItem4.PaintStyle = PaintStyle.ImageAndText] |
+-------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 764: PaintStyle = \"Text\"

[] 

{border="0"}

**[]** 

Figure 765: PaintStyle = \"ImageAndText\"

**[]** 

See Also

[] 

[[Types of Bar Items]{.UGHyperlink}]()[]{.UGHyperlink}

[]{#p871}[]{#_Keyboard_Shortcut}3.5.4.1.2.3.2      Keyboard Shortcut

[] 

Keyboard support can be assigned for each BarItem using **BarItem.Shortcut** property of the particular bar item. A customized text can be specified in the place of shortcut key using **ShortcutText** property.

[] 

{border="0"}

**[]** 

Figure 766: Property Grid Displaying ShortCut with options and ShortcutText

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                       |
|                                                                                                                                                                      |
| **[]**                                                                                                             |
|                                                                                                                                                                      |
| [this][.barItem4.Shortcut=System.Windows.Forms.Shortcut.CtrlX;]                 |
|                                                                                                                                                                      |
| [this][.dropDownBarItem2.ShortcutText = [\"Cut\"];     ] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                              |
|                                                                                                                                                                 |
| **[]**                                                                                                        |
|                                                                                                                                                                 |
| [Me][.barItem4.Shortcut=System.Windows.Forms.Shortcut.CtrlX]               |
|                                                                                                                                                                 |
| [this][.dropDownBarItem2.ShortcutText = [\"Cut\"];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 767: BarItem with Keyboard Shortcut

**[]** 

See Also

[] 

[[Types of Bar Items]{.UGHyperlink}]()[]{.UGHyperlink}

[] 

[]{#p872}3.5.4.1.2.3.3      Image Settings

[] 

The properties which let you set images for the menu items are as follows.

[] 


  ------------------ ------------------------------------------
  BarItem Property   Description
  Image              Default image displayed in the bar item.
  ImageIndex         Image index of the image.
  ImageList          Indicates the ImageList.
  ------------------ ------------------------------------------


[] 

By selecting the imagelist using **Imagelist** property and choosing the index of the image through **ImageIndex** property, we can display images. The images can also be directly set by using the **Image** property.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                              |
| [this][.barItem2.Image = ((Syncfusion.Windows.Forms.Tools.XPMenus.[ImageExt])(resources.GetObject([\"barItem2.Image\"])));] |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [this][.barItem2.ImageList = [this].imageList1;]                                                                                                   |
|                                                                                                                                                                                                                                                              |
| [this][.barItem2.ImageIndex = 2;]                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                     |
| [Me][.barItem2.Image = [DirectCast]((resources.GetObject([\"barItem2.Image\"])), Syncfusion.Windows.Forms.Tools.XPMenus.ImageExt)] |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| [this][.barItem2.ImageList = [this].imageList1;]                                                                                                          |
|                                                                                                                                                                                                                                                                     |
| [this][.barItem2.ImageIndex = 2;]                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Images for Highlighted and Disabled Menu Items

[] 

A BarItem can be enabled or disabled **Enabled** property. Images for disabled (Enabled - False) or enabled (Enabled - True) bar items can be specified in **DisabledImage** or **HighlightedImage** properties.

**[]** 

**DisabledImageList, DisabledImageIndex** or **HighlightedImageList, HighlightedImageIndex** properties can also be used instead.

[] 


  --------------------------- -------------------------------------------------------------------------------
  BarItem Property            Description
  DisabledImage               Sets image for disabled bar item, when Enabled = false.
  DisabledImageList           ImageList for the disabled bar items.
  DisabledImageIndex          ImageIndex for the disabled bar item.
  DisabledLargeImageList      ImageList for the disabled bar item when BarManager is in LargeIcons mode.
  HighlightedImage            Sets image for highlighted bar item, the bar item is enabled.
  HighlightedImageList        ImageList for the highlighted bar item.
  HighlightedImageIndex       ImageIndex for the highlighted bar item.
  HighlightedLargeImageList   ImageList for the highlighted bar item when BarManager is in LargeIcons mode.
  --------------------------- -------------------------------------------------------------------------------


[] 

{border="0"}

[] 

Figure 768: Enabled, Highlighted and Disabled BarItems with Images

**[]** 

{border="0"}

[] 

Figure 769: Menus with Large Icons

*[]* 

Setting images for bar items when it is pressed

[] 

You can set the image for the bar item when it is pressed. You need to associate the corresponding ImageList to the **PressedImageList** property of bar item and you can set the image index using **PressedImageIndex** property. Similarly you can associate ImageListAdv with **PressedImageListAdv** property.

[] 


{border="0"} Note: It is required to set image to Baritem before it is pressed.


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                          |
|                                                                                                                                                                         |
| **[]**                                                                                                                |
|                                                                                                                                                                         |
| [this][.barItem1.Image = image;]                                                   |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| [this][.barItem1.PressedImageIndex = 0;]                                           |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| [this][.barItem1.PressedImageListAdv = [this].imageListAdv1;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                 |
|                                                                                                                                                                    |
| **[]**                                                                                                           |
|                                                                                                                                                                    |
| [Me][.barItem1.Image = image]                                                 |
|                                                                                                                                                                    |
| []                                                                                                                             |
|                                                                                                                                                                    |
| [Me][.barItem1.PressedImageIndex = 0]                                         |
|                                                                                                                                                                    |
| []                                                                                                                             |
|                                                                                                                                                                    |
| [Me][.barItem1.PressedImageListAdv = [Me].imageListAdv1] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[[Types of Bar Items]{.UGHyperlink}]()[]{.UGHyperlink}

[[]]{.UGHyperlink} 

[]{#p873}[]{#_BarItem_Text}3.5.4.1.2.3.4      BarItem Text

[] 

Text for a bar item can be edited through **Text** property. Alignment of text can be specified in **TextAlignment** property.

[] 


+-----------------------------------+---------------------------------------+
| ParentBarItem Property            | Description                           |
+-----------------------------------+---------------------------------------+
| Text                              | Sets text for the Bar item.           |
+-----------------------------------+---------------------------------------+
| TextAlignment                     | Sets the text alignment. Options are, |
|                                   |                                       |
|                                   |                                       |
|                                   |                                       |
|                                   | *Near, (Default)*                     |
|                                   |                                       |
|                                   | *Far,*                                |
|                                   |                                       |
|                                   | *Center*                              |
+-----------------------------------+---------------------------------------+


**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                            |
| **[]**                                                                                                                                                   |
|                                                                                                                                                                                                            |
| [this][.barItem2.Text = [\"Center\"];]                                                         |
|                                                                                                                                                                                                            |
| [this][.barItem2.TextAlignment = Syncfusion.Windows.Forms.Tools.XPMenus.[TextAlignment].Center;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                       |
|                                                                                                                                                                                                          |
| **[]**                                                                                                                                                 |
|                                                                                                                                                                                                          |
| [Me][.barItem2.Text = [\"Center\"]]                                                          |
|                                                                                                                                                                                                          |
| [Me][.barItem2.TextAlignment = Syncfusion.Windows.Forms.Tools.XPMenus.[TextAlignment].Center] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 770: Text & Text Alignment Property

**[]** 


{border="0"} Note: We can also change the text color for the Baritems using MenuColors.SelTextColor property.


**[]** 

See Also

[] 

[[Types of Bar Items]{.UGHyperlink}]()[]{.UGHyperlink}

[] 

3.5.4.1.2.3.5      Foreground Settings

[]{#p874}[] 

Foreground of the bar item text can be controlled using the below properties.

**[]** 


  ------------------------- ---------------------------------------
  BarItem Property          Description
  CustomActiveTextColor     Sets the text color in active mode.
  CustomDisabledTextColor   Sets the text color in disabled mode.
  CustomNormalTextColor     Sets the text color in normal mode.
  CustomTextFont            Sets the text font.
  ------------------------- ---------------------------------------


**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                     |
| [this][.barItem4.CustomActiveTextColor = System.Drawing.[Color].OrangeRed;]                                                                                                               |
|                                                                                                                                                                                                                                                                                                     |
| [this][.barItem5.CustomDisabledTextColor = System.Drawing.[Color].DeepSkyBlue;]                                                                                                           |
|                                                                                                                                                                                                                                                                                                     |
| [this][.barItem6.CustomNormalTextColor = System.Drawing.[Color].Magenta;]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                     |
| [this][.barItem4.CustomTextFont = [new] System.Drawing.[Font]([\"Verdana\"], 8.25F, System.Drawing.[FontStyle].Bold);]   |
|                                                                                                                                                                                                                                                                                                     |
| [this][.barItem5.CustomTextFont = [new] System.Drawing.[Font]([\"Verdana\"], 8.25F, System.Drawing.[FontStyle].Italic);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                  |
| [Me][.barItem4.CustomActiveTextColor = System.Drawing.[Color].OrangeRed]                                                                                                               |
|                                                                                                                                                                                                                                                                                                  |
| [Me][.barItem5.CustomDisabledTextColor = System.Drawing.[Color].DeepSkyBlue]                                                                                                           |
|                                                                                                                                                                                                                                                                                                  |
| [Me][.barItem6.CustomNormalTextColor = System.Drawing.[Color].Magenta]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                  |
| [Me][.barItem4.CustomTextFont = [New] System.Drawing.[Font]([\"Verdana\"], 8.25F, System.Drawing.[FontStyle].Bold)]   |
|                                                                                                                                                                                                                                                                                                  |
| [Me][.barItem5.CustomTextFont = [New] System.Drawing.[Font]([\"Verdana\"], 8.25F, System.Drawing.[FontStyle].Italic)] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

[] 

Figure 771: Doc1(Highlighted, Bold, Red color); Doc2(Disabled, Italic, DeepSkyBlue); Doc3(Enabled, Magenta color)

**[]** 

See Also

[] 

[[Types of Bar Items]{.UGHyperlink}]()[]{.UGHyperlink}

[] 

[]{#p875}3.5.4.1.2.3.6      ToolTip

[] 

ToolTip for the BarItems can be enabled using **BarItem.ShowTooltips** property, which can be edited using **BarItem.Tooltip** property.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                                     |
| **[]**                                                                                                            |
|                                                                                                                                                                     |
| [this][.dropDownBarItem2.ShowTooltip = [true];]           |
|                                                                                                                                                                     |
| [this][.dropDownBarItem2.Tooltip = [\"Pick a color\"];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                               |
|                                                                                                                                                                  |
| **[]**                                                                                                         |
|                                                                                                                                                                  |
| [Me][.dropDownBarItem2.ShowTooltip = [True]]           |
|                                                                                                                                                                  |
| [Me][.dropDownBarItem2.Tooltip = [\"Pick a color\"]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 772: Tooltip displayed for a DropDownBarItem

**[]** 


{border="0"} Note:[ ]We can control the display of tooltips for the bar items, only when the form is active, using the below BarManager property.


**[]** 


  -------------------------------- ------------------------------------------------------------------------------------------
  BarManager Property              Description
  BarItemActiveFormCheckOverride   Specifies whether bar items should check for active form before displaying the tooltips.
  -------------------------------- ------------------------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                   |
|                                                                                                                                                                                  |
| **[]**                                                                                                                         |
|                                                                                                                                                                                  |
| [this][.mainFrameBarManager1.BarItemActiveFormCheckOverride = [true];] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                            |
|                                                                                                                                                                               |
| **[]**                                                                                                                      |
|                                                                                                                                                                               |
| [Me][.mainFrameBarManager1.BarItemActiveFormCheckOverride = [True]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

