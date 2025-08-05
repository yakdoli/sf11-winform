---
title: features54.md
original_path: WinForms_Docs/02_Concepts/features54.md
created_at: 2025-08-05
---








  









### Features {#features style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

**[]** 

Office2007 Controls Features

**[]** 

RibbonControlAdv

[] 

[·      ]**OfficeMenuButton -** The RibbonControlAdv comes with the Office MenuButton with desired image. The visibility of this OfficeMenuButton can also be toggled during runtime. This OfficeMenuButton can have SuperToolTips associated with it. See [[ToolTips]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Tooltips).

 

[·      ]**OfficeMenuDropDown -** Similar to the Office2007 UI, the RibbonControlAdv can have [[OfficeMenuDropDown]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_MenuButton_Drop_Down) with both the Main and Auxiliary panels.

 

[·      ]**Quick Access ToolBar -** [[Quick Access ToolBar]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Quick_Access_Toolbar) can host items in it to make a more easy and efficient access to the items. The RibbonControlAdv supports full customization of Quick Access ToolBar at runtime.

 

[·      ]**Ribbon Panel  -** The [[RibbonPanel]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Ribbon_Panel) can have various tabitems with the ability to scroll the tabs. The RibbonPanel can have three different states such as Expanded, Collapsed and floating state while expanded.

[] 

The TabItems in the RibbonPanel can auto align the controls when width of the RibbonControl is reduced.

[] 

{border="0"}

[] 

Figure 1283: : Ribbon Panel[]

[·      ]**RibbonForm -** The RibbonForm is exclusively designed to be used as a Form that hosts RibbonControlAdv. This supports all three color schemes.

 

[·      ]**ToolStripTabItems -** The TabItems can have a number of ToolStripEx which in turn can host various items in it. ToolStripTabItems can also host custom controls such as Grid, Treeview through ToolStrip.

 

[·      ]**Tab Group -** The RibbonControlAdv allows TabItems to be grouped together. The TabGroups can have colors set and this color will also be applied for the corresponding TabPanel.

[] 

{border="0"}

[] 

Figure 1284: Tab Groups

**[]** 

[·      ]**GalleryItem -** Essential Tools RibbonControlAdv provides options to add a collection of items and store them into a gallery. The GalleryItem comes with a standard and a Compact scrollbars type. It supports all the three color schemes (Blue, Silver and Black).

[·      ]Option to merge RibbonPanel of child form with the RibbonPanel in parent form RibbonControlAdv. See [[Ribbon Merging]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Ribbon_Merging).

[] 

{border="0"}

***[]*** 

Figure 1285: Ribbon Merging Support

[] 

[·      ]Super accelerator support for Office Menu button. This is discussed in [Customization] topic.

[] 

{border="0"}

***[]*** 

Figure 1286: Super Accelerator Support Illustrated

[] 

[·      ]Multiline text support for all Text and ToolTip properties.

[·      ]Support to display the gallery items one row at a time when it was invoked by the collapsed ToolStripEx.

[] 

[{border="0"}][]

[] 

Figure 1287: Gallery Items displayed in a Single Row

[] 

[·      ]Collection related properties MainItems and QuickItems to the RibbonControlAdv Header to access items collection.

[·      ]AllowCollapse property to restrict the Ribbon Panel from collapsing.

[·      ]Events **RibbonControlAdv.BeforeCustomizeDropDownPopup** and **RibbonControlAdv.AfterCustomizeDropDownPopup** that occurs before/after DropDown of QuickItemsDropDownButton is shown.

[·      ]Events like RibbonControlAdv.Header.QuickItems.BeforeAddItem and RibbonControlAdv.Header.QuickItems.BeforeRemoveItem that occurs before ToolStripItem is added/removed from the QuickAccessPanel collection.

[·      ]RibbonControlAdv.SelectedTabItemChanged that occurs when selected ToolStripTabItem has changed.

[·      ]Method RibbonControlAdv.ShowCustomizeDialog that shows QuickItems customizing dialog.

[·      ]Checkbox item option with Tristate behavior in the ToolStripEx items collection.

[·      ]RadioButton item option in the ToolStripEx items collection.

[·      ]Ability to define the color scheme for the RibbonControlAdv, RibbonForm, StatusStripEx and Office2007Form.

[·      ][[Tooltip]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_ToolTips_1) features included for ToolStripEx in this new version.

[·      ]New ToolStrip item, [[ComboBoxEx]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_ComboBoxEx) is added, which has Office 2007 look and feel and resizable dropdown height feature at run time.

[] 

Office2007 Form

 

[[Office2007 Form]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Office2007_Form) which does not have any dependency in RibbonControlAdv is now available in Essential suite. It supports all three color schemes, help button, Right To left feature everything similar to the normal form with the Office2007 look and feel.

 

New property UseOffice2007SchemeBackColor is added, which lets you use the Office2007 scheme color, as the back color for the [[Office2007Form]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Office2007_Form).

 

MiniToolBar

 

[[MiniToolBar]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_MiniToolBar) control which is available in the Essential Tools will appear when the user selects a text. It gives options to customize the selected text.

[] 

Added ability to associate MiniToolBar to any control with a [[AssociatedControl]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Creating_MiniToolBar)[ ]property.[]

[] 

StatusStripEx

**[]** 

It can be docked to the bottom of the Form. It can hold controls like TrackBarEx, ProgressBar, StatusStripButton. See [[StatusStripEx]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_StatusStripEx)[.]

[Custom colors] can be applied to StatusStripEx.

[] 

[{border="0"}][]

[] 

Figure 1288: Custom Color applied to StatusStripEx

[] 

ScrollersFrame

**[]** 

[[ScrollersFrame]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_ScrollersFrame) is a new control that attaches scrollbars to any control, that is added to the form. This supports all three color schemes.

[] 

[[Custom colors]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Visual_Styles_1)[ ]{.UGHyperlink}can be applied to ScrollerFrame.

[] 

{border="0"}

***[]*** 

***[]*** 

***[]*** 

Figure 1289: Custom Color applied to ScrollerFrame

[] 

ContextMenuStripEx

**[]** 

[[ContextMenuStripEx]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_ContextMenuStripEx)[ ]control that appears on right clicking during runtime, has numerous advanced features.[]

[] 

[·      ]RightToLeft support for the items in the ContextMenuStripEx.

[·      ]The shadow of the ContextMenuStripEx can be made visible or hidden.

[·      ]It supports Office2007 color schemes.

[·      ]It can have a header associated with it.

[] 

TrackBarEx

**[]** 

[·      ]This control allows the user to slide between minimum value and maximum value specified through a pointer. See [[[TrackBarEx]]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_TrackBarEx).

[·      ]Orientation property for the TrackBarEx with options vertical and horizontal. This is discussed [[[here]]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_TrackBar_Appearance).

[·      ]Scroll Event is added to the TrackBarEx control.

[] 

SuperToolTip

 

Essential Tools has come up with a new control known as the [[Super ToolTip]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_SuperToolTip) which, enables the user to give tooltip information using this control with an  appealing look and feel.

The SuperToolTip can have three segments, Header, body and Footer to display the content. The superToolTip control supports high level customization of the SuperTooltip Look and Feel through properties for colors, Images and Text.

 

SuperAccelerator

 

With this component users can accelerate the click event of items by using a Single key stroke without mouse hover on it. This control have options to customize the look and feel of the Key tips. See [[Super Accelerator]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Super_Accelerator).

[] 

Quick Access Toolbar

[] 

Office2007 form look and feel for QAT dialog.

[] 

{border="0"}

[] 

***[]*** 

Figure 1290: Office2007 Look and Feel for QAT Dialog Box

 

More:

























