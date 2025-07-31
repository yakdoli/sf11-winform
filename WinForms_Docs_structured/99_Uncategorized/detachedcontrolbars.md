---
title: detachedcontrolbars.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\detachedcontrolbars.md
created_at: 2025-07-03
---






##### Detached ControlBars {#detached-controlbars style="tab-stops: 0pt"}

[] 

**ControlBars** in Essential Tools XP Menus framework enables application developers to add dockable / floatable controls to their form\'s toolbar layout. A common example of a **ControlBar** is the task pane window found in the Microsoft Office 2003 product suite.

 

A ControlBar is a full-featured docking container that can host any control and be docked along the border of the host form or floated as a top-level window. ControlBars, however, differ from traditional docking windows by adopting the characteristic layout behavior of a toolbar rather than that of a classic dockable control.

 

{border="0"}

[] 

Figure 794: Dockable ControlBar

**[]** 

See also

**[]** 

[How to dock the ControlBars to any edge of the host form?]{.UGHyperlink}[]{.UGHyperlink}

###### []{#_ControlBar_Client_Controls}3.5.4.2.2.1 ControlBar Client Controls {#controlbar-client-controls style="tab-stops: 0pt"}

[] 

A ControlBar is capable of hosting two controls.

[] 

[·      ]A **main control** that occupies the ControlBar\'s client region.

[·      ]A **CaptionControl** that is displayed within the ControlBar\'s caption region.

[] 

While just about any **System.Windows.Forms.Control** instance can be used as the ControlBar\'s main client, the caption control position is normally occupied by single line controls such as a toolbar, text box or combo box.

[] 

{border="0"}

**[]** 

Figure 795: ControlBar highlighted with Client Control

**[]** 

{border="0"}

**[]** 

Figure 796: ControlBar highlighted with Caption Control

**[]** 

Dropping a control onto the ControlBar automatically sets it as the ControlBar\'s main client. To assign the caption control, drop the control onto the ControlBar and using the Properties window, set the bar\'s **CaptionControl** property to refer that control. Doing so will reposition and resize the control to occupy the bar\'s caption region. Height of the ControlBar caption bar can be specified in **ControlBarCaptionHeight** property. Default height is 25.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                     |
|                                                                                                                                                                    |
| **[]**                                                                                                           |
|                                                                                                                                                                    |
| [this][.controlBar1.CaptionControl = [this].xpToolBar1;] |
|                                                                                                                                                                    |
| [this][.controlBar1.ControlBarCaptionHeight = 30;]                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                            |
|                                                                                                                                                               |
| **[]**                                                                                                      |
|                                                                                                                                                               |
| [Me][.controlBar1.CaptionControl = [Me].xpToolBar1] |
|                                                                                                                                                               |
| [Me][.controlBar1.ControlBarCaptionHeight = 30]                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[ControlBar Properties]{.UGHyperlink}[]{.UGHyperlink}

[Adding Different Pages To Control Bar]{.UGHyperlink}[]{.UGHyperlink}

[How to dock the ControlBars to any edge of the host form?]{.UGHyperlink}[]{.UGHyperlink}

[] 

 

 

###### []{#_ControlBar_Properties}3.5.4.2.2.2 ControlBar Properties {#controlbar-properties style="tab-stops: 0pt"}

**[]** 

Appearance Properties

**[]** 


+-----------------------------------+---------------------------------------------------------------------+
| ControlBar Property               | Description                                                         |
+-----------------------------------+---------------------------------------------------------------------+
| BackColor                         | Sets the back color for the XPToolbar.                              |
+-----------------------------------+---------------------------------------------------------------------+
| BackgroundImage                   | Sets the background image for the XPToolbar.                        |
+-----------------------------------+---------------------------------------------------------------------+
| BackgroundImagelayout             | Specifies the layout of the image.                                  |
|                                   |                                                                     |
|                                   | Title, Center, Stretch, Zoom are the option. Default value is Tile. |
+-----------------------------------+---------------------------------------------------------------------+
| ChevronColor                      | Sets color of the chevron.                                          |
+-----------------------------------+---------------------------------------------------------------------+
| Font                              | Sets the font style for the text.                                   |
+-----------------------------------+---------------------------------------------------------------------+
| ForeColor                         | Sets the foreground color of the text.                              |
+-----------------------------------+---------------------------------------------------------------------+
| Text                              | Sets the control\'s text.                                           |
+-----------------------------------+---------------------------------------------------------------------+


**[]** 

Behavior Properties

**[]** 


  --------------------- -------------------------------------------------------------------------------
  ControlBar Property   Description
  AllowedDockBorders    Specifies dock border sides in which command bar can be docked from floating.
  AlwaysLeadingEdge     Docks the CommandBar permanently to the leading edge of the dock border.
  AlwaysTrailingEdge    Docks the CommandBar permanently to the trailing edge of the dock border.
  CaptionControl        Specifies the control that represents the caption of the control bar.
  DisableDocking        Disables docking ability of the CommandBar.
  DisableFloating       Disables floating ability of the CommandBar.
  --------------------- -------------------------------------------------------------------------------


[] 

Hide / Show

[] 


  --------------------- -------------------------------------------------------------------
  ControlBar Property   Description
  HideCloseButton       Hides Close button for the floating CommandBar, when set to true.
  HideDropDownButton    Shows / Hides the dropdown button.
  HideGripper           Shows / Hides the drag gripper.
  --------------------- -------------------------------------------------------------------


**[]** 

Popup for the DropDown

[] 


  --------------------- ---------------------------------------------------------------------------------------------
  ControlBar Property   Description
  PopupContainer        Indicates the PopupContainer control that is displayed when the dropdown button is clicked.
  PopupMenu             Indicates the Popup menu on clicking the dropdown button.
  --------------------- ---------------------------------------------------------------------------------------------


[] 

See Also

[] 

[[ControlBar Client Controls]{.UGHyperlink}]()[, ]{.UGHyperlink}

[Adding Different Pages To Control Bar]{.UGHyperlink}[]{.UGHyperlink}

[How to dock the ControlBars to any edge of the host form?]{.UGHyperlink}[]{.UGHyperlink}

[[]]{.UGHyperlink} 

[[]]{.UGHyperlink} 

 

###### []{#_Adding_Different_Pages}3.5.4.2.2.3 Adding Different Pages To Control Bar {#adding-different-pages-to-control-bar style="tab-stops: 0pt"}

[] 

Adding and Removing ControlBars

**[]** 

The MainFrameBarManager\'s **Add Detached ControlBar**[ ]design-time verb, available through the Properties window, facilitates the addition of ControlBars to the design form. The XP Menus design-time is fully WYSIWYG and the bar layout can be designed by simply dragging and docking or floating each ControlBar at the desired location. Upon saving the design form, the ControlBar state information is serialized by the BarManager as a part of the form\'s resource file along with the rest of the menu/toolbar layout.

 

Follow the steps below to add different pages to the control bar.

[] 

{border="0"}

[] 

Figure 797: Add Detached ControlBar Design-Time Verb

[] 


{border="0"} Note: Control Bar can also be added by clicking the verb in the properties window.


[] 

{border="0"}

***[]*** 

Figure 798: Add Detached ControlBar Verb

[] 

 The resulted screen shot displays controlbar in the designer.

[] 

{border="0"}

***[]*** 

Figure 799: ControlBar displayed in the Designer

[] 

[·      ]Now add **XPToolbar** to the control bar.

[·      ]Add panel to the control bar.

[·      ]Add CardLayout over the panel to add different pages.

[] 

While dropping out **CardLayout** onto the panel, the layout designer window will open, asking whether to make panel1 as container control. Click \'Yes\' and continue.

[] 

{border="0"}

***[]*** 

Figure 800: Panel1 set as the Layout Manager\'s Container Control

[] 

[·      ]You can add multiple panels to the control bar.

[·      ]Select the card using the **SelectedCard** property in the CardLayout Property window.

[] 

{border="0"}

[] 

Figure 801: CardLayout property Window

[] 

[·      ]In the selected card, add XPTaskBar to the control bar and right-click it to add XPTaskBarBox to add Items.

[] 

{border="0"}

[] 

Figure 802: Add TaskBox to the control bar using Verbs

[] 

The resultant form is as follows.

[] 

{border="0"}

[] 

Figure 803: Control bar with TaskBarBox Added

 

[·      ]Inside XPTaskbarBox, you can insert link labels, ComboBoxAdv controls like in the following screen shot.

[] 

{border="0"}

***[]*** 

Figure 804: Inserting controls inside the XPTaskBarBox 

[] 

At Run Time

**[]** 

Include the following code snippet in the Click event of a BarItem to view the next page of a card.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                               |
| [this][.cardlayoutmanager1.][next][();] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                            |
| [Me][.cardlayoutmanager1.][next][()] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

A sample which demonstrates adding control bar is available in the below sample installation location.

[] 

..\\My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Menus Package\\ControlBars

[] 

See Also

**[]** 

[[ControlBar Client Controls]{.UGHyperlink}]()[, ]{.UGHyperlink}

[[Adding Different Pages To Control Bar]{.UGHyperlink}]()[]{.UGHyperlink}

[How to dock the ControlBars to any edge of the host form]{.UGHyperlink}[]{.UGHyperlink}

[] 

 

[]{#related-topics}

