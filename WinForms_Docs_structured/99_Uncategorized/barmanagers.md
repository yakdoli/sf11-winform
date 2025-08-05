---
title: barmanagers.md
original_path: WinForms_Docs/99_Uncategorized/barmanagers.md
created_at: 2025-08-05
---






##### BarManagers {#barmanagers style="tab-stops: 0pt"}

[] 

There are two kinds of BarManagers.

[] 

[·      ]MainFrameBarManager

[·      ]ChildFrameBarManager

[] 

The MainFrameBarManager is associated with a **MDI container form** in the MDI scenario or with the top-level form in a single document scenario.

 

The ChildFrameBarManager should be associated with a **MDIChild** in the MDI scenario.

 

These two classes are derived from the BarManager and hence will be referred as such when discussing features common to both these classes.

 


{border="0"} Note: At run-time, a ChildFrameBarManager does not show the menus and toolbars inside a child form. It is merely a place holder for the menus and toolbars during design-time, which will be merged into the main form\'s menus during run-time.


[] 

BarManagers come with full design-time support and lets users add menus and toolbars and fill them with items, all without writing a single line of code. The Customize dialog facilitates customization of the menus. It is available to the developer during design-time and to the end user during runtime.

[] 

{border="0"}

 

Figure 773: MainFrameBarManager at Design Time

**[]** 

{border="0"}

**[]** 

Figure 774: ChildFrameBarManager at Design Time

**[]** 

See Also

**[]** 

[MainFrameBarManager Properties]{.UGHyperlink}[,]{.UGHyperlink}

[ChildFrameBarManager Properties]{.UGHyperlink}[, ]{.UGHyperlink}[MDI Child Forms]{.UGHyperlink}[]{.UGHyperlink}

[Detached CommandBar]{.UGHyperlink}[, ]{.UGHyperlink}[Detached ControlBars]{.UGHyperlink}[]{.UGHyperlink}

###### []{#p877}[]{#_MainFrameBarManager_Property}3.5.4.1.3.1 MainFrameBarManager Property {#mainframebarmanager-property style="tab-stops: 0pt"}

[] 

Image Settings

[] 


  ------------------------- ------------------------------------------------------------------------------------------
  BarManager Property       Description
  DisabledImageList         The ImageList to which the BarItems refer to, when disabled.
  DisabledLargeImageList    The ImageList to which the BarItems refer to, when disabled and uses LargeIcons mode.
  HighlightImageList        The ImageList to which the BarItems refer to, when highlighted.
  HighlightLargeImageList   The ImageList to which the BarItems refer to, when highlighted and uses LargeIcons mode.
  ImageList                 ImageList that bar items refer to when in small icons mode.
  LargeIcons                Enables or disables LargeIcons mode for items in the toolbar.
  LargeImageList            The ImageList to which the BarItems refer to, when in LargeIcons mode.
  ------------------------- ------------------------------------------------------------------------------------------


 

Foreground and Style Settings

**[]** 


  --------------------- ---------------------------------------------------------------
  BarManager Property   Description
  Font                  Sets font style for the bar items.
  Style                 Sets the common visual style for the toolbars and main menus.
  Themes Enabled        Specify whether to apply themes.
  --------------------- ---------------------------------------------------------------


**[]** 

Data Settings

**[]** 


  --------------------- -------------------------------------------------------------------------------
  BarManager Property   Description
  Bars                  Invokes the Customize dialog - Toolbar tab indicating the collection of Bars.
  Categories            Lists the categories defined in this bar manager.
  --------------------- -------------------------------------------------------------------------------


**[]** 

Misc Properties

**[]** 


  ------------------------ --------------------------------------------------------------------------------------------
  BarManager Property      Description
  ActivateFormFromBar      Indicates if activating menu should activate parent form also.
  PopupCloseTimer          Indicates the delay in milliseconds before the displayed dropdown on toolbar, gets closed.
  ShowHighlightRectangle   Indicates whether to highlight bar items when moving mouse over it.
  ------------------------ --------------------------------------------------------------------------------------------


**[]** 

Shadow Settings

**[]** 


  --------------------- ---------------------------------------------------------
  BarManager Property   Description
  ShowDropShadow        Indicates whether to show shadow for BarItem\'s images.
  ShowShadow            Indicates whether to show shadows for popups.
  --------------------- ---------------------------------------------------------


[] 


{border="0"} Note: The properties related to the partial menus concept is discussed in ParentBarItem.


[] 

Tooltip Settings

[] 


{border="0"} Note: We can control the display of tooltips for the bar items, only when the form is active, using the below BarManager.BarItemActiveFormCheckOverride property.


[] 

See Also

[] 

[Toolbar State Persistence]{.UGHyperlink}[,]{.UGHyperlink}

[ParentBarItem]{.UGHyperlink}[,]{.UGHyperlink}

[Tooltip]{.UGHyperlink}[]{.UGHyperlink}

###### []{#_ChildFrameBarManager_Properties}3.5.4.1.3.2 ChildFrameBarManager Properties {#childframebarmanager-properties style="tab-stops: 0pt"}

[]{#p878} 

Image Settings

[] 


  ------------------------- ------------------------------------------------------------------------------------------
  BarManager Property       Description
  DisabledImageList         The ImageList to which the BarItems refer to, when disabled.
  DisabledLargeImageList    The ImageList to which the BarItems refer to, when disabled and uses LargeIcons mode.
  HighlightImageList        The ImageList to which the BarItems refer to, when highlighted.
  HighlightLargeImageList   The ImageList to which the BarItems refer to, when highlighted and uses LargeIcons mode.
  ImageList                 ImageList that bar items refer to when in small icons mode.
  LargeImageList            The ImageList to which the BarItems refer to, when in LargeIcons mode.
  ------------------------- ------------------------------------------------------------------------------------------


**[]** 

Style Settings

**[]** 


  --------------------- ---------------------------------------------------------------
  BarManager Property   Description
  Style                 Sets the common visual style for the toolbars and main menus.
  --------------------- ---------------------------------------------------------------


**[]** 

Data Settings

**[]** 


  --------------------- -------------------------------------------------------------------------------
  BarManager Property   Description
  Bars                  Invokes the Customize dialog - Toolbar tab indicating the collection of Bars.
  Categories            Lists the categories defined in this bar manager.
  --------------------- -------------------------------------------------------------------------------


**[]** 

Shadow and Highlight Rectangle Settings

**[]** 


  ------------------------ ---------------------------------------------------------------------
  BarManager Property      Description
  ShowDropShadow           Indicates whether to show shadow for BarItem\'s images.
  ShowHighlightRectangle   Indicates whether to highlight bar items when moving mouse over it.
  ShowShadow               Indicates whether to show shadows for popups.
  ------------------------ ---------------------------------------------------------------------


[]{#related-topics}

