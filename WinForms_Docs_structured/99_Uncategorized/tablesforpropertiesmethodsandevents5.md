---
title: tablesforpropertiesmethodsandevents5.md
original_path: WinForms_Docs/99_Uncategorized/tablesforpropertiesmethodsandevents5.md
created_at: 2025-08-05
---








  









### Tables for Properties, Methods, and Events {#tables-for-properties-methods-and-events style="tab-stops: 0pt"}

Properties

 


+--------------------------------------------------+-------------------------------------------------------------------+-------------------------------------+-------------------------------------------+-------------------------------------------------+-------------------------------------------------+
| Name                                             | Description                                                       | Type of property                    | Data type                                 | Value it accepts                                | Dependency                                      |
+--------------------------------------------------+-------------------------------------------------------------------+-------------------------------------+-------------------------------------------+-------------------------------------------------+-------------------------------------------------+
| AllowKeyboardNavigation[ ] | Used to enable KeyboardNavigation.[]        | [Server side] | Boolean[]           | true/false[ ]             | [NA ]                     |
+--------------------------------------------------+-------------------------------------------------------------------+-------------------------------------+-------------------------------------------+-------------------------------------------------+-------------------------------------------------+
| KeyConfigurator[]          | Used to customize all keyboard shortcuts.[] | [Server side] | [KeyConfigurator] | KeyConfigurator object[ ] | AllowKeyboardNavigation[] |
|                                                  |                                                                   |                                     |                                           |                                                 |                                                 |
|                                                  |                                                                   |                                     | []                  | []                        |                                                 |
+--------------------------------------------------+-------------------------------------------------------------------+-------------------------------------+-------------------------------------------+-------------------------------------------------+-------------------------------------------------+


**[]** 


  Name                    Description                                                              Type of property                      Data Type                                                Value it accepts                                                              Dependency
  ----------------------- ------------------------------------------------------------------------ ------------------------------------- -------------------------------------------------------- ----------------------------------------------------------------------------- -------------------------------------------------
  FocusKey                Used to set the Keyboard shortcut for FocusKey[]   [Server side]   [Keys][]   [[Keys options]]{.underline}                             AllowKeyboardNavigation[]
  FirstCellSelection      Used to set the Keyboard shortcut for FirstCellSelection                 [Server side]   [Keys]                           [[Keys options]]{.underline}                             AllowKeyboardNavigation[]
  LastCellSelection       Used to set the Keyboard shortcut for LastCellSelection                  [Server side]   [Keys]                           [[Keys options]]{.underline}[]   AllowKeyboardNavigation[]
  FirstRowSelection       Used to set the Keyboard shortcut for FirstRowSelection                  [Server side]   [Keys]                           [[Keys options]]{.underline}[]   AllowKeyboardNavigation[]
  LastRowSelection        Used to set the Keyboard shortcut for LastRowSelection                   [Server side]   [Keys]                           [[Keys options]]{.underline}[]   AllowKeyboardNavigation[]
  InsertRecord            Used to set the Keyboard shortcut for InsertRecord                       [Server side]   [Keys]                           [[Keys options]]{.underline}[]   AllowKeyboardNavigation[]
  DeleteRecord            Used to set the Keyboard shortcut for DeleteRecord                       [Server side]   [Keys]                           [[Keys options]]{.underline}[]   AllowKeyboardNavigation[]
  EditRecord              Used to set the Keyboard shortcut for EditRecord                         [Server side]   [Keys]                           [[Keys options]]{.underline}[]   AllowKeyboardNavigation[]
  SaveRequest             Used to set the Keyboard shortcut for SaveRequest                        [Server side]   [Keys]                           [[Keys options]]{.underline}[]   AllowKeyboardNavigation[]
  CancelRequest           Used to set the Keyboard shortcut for CancelRequest                      [Server side]   [Keys]                           [[Keys options]]{.underline}[]   AllowKeyboardNavigation[]
  ExportToExcel           Used to set the Keyboard shortcut for ExportToExcel                      [Server side]   [Keys]                           [[Keys options]]{.underline}[]   AllowKeyboardNavigation[]
  NextPage                Used to set the Keyboard shortcut for  the NextPage                      [Server side]   [Keys]                           [[Keys options]]{.underline}[]   AllowKeyboardNavigation[]
  PreviousPage            Used to set the Keyboard shortcut for the  PreviousPage                  [Server side]   [Keys]                           [[Keys options]]{.underline}[]   AllowKeyboardNavigation[]
  NextPager               Used to set the Keyboard shortcut for NextPager                          [Server side]   [Keys]                           [[Keys options]]{.underline}[]   AllowKeyboardNavigation[]
  PreviousPager           Used to set the Keyboard shortcut for PreviousPager                      [Server side]   [Keys]                           [[Keys options]]{.underline}[]   AllowKeyboardNavigation[]
  LastPage                Used to set the Keyboard shortcut for the LastPage                       [Server side]   [Keys]                           [[Keys options]]{.underline}[]   AllowKeyboardNavigation[]
  FirstPage               Used to set the Keyboard shortcut for the FirstPage                      [Server side]   [Keys]                           [[Keys options]]{.underline}[]   AllowKeyboardNavigation[]
  SelectedGroupExpand     Used to set the Keyboard shortcut for SelectedGroupExpand                [Server side]   [Keys]                           [[Keys options]]{.underline}[]   AllowKeyboardNavigation[]
  TotalGroupExpand        Used to set the Keyboard shortcut for TotalGroupExpand                   [Server side]   [Keys]                           [[Keys options]]{.underline}[]   AllowKeyboardNavigation[]
  SelectedGroupCollapse   Used to set the Keyboard shortcut for SelectedGroupCollapse              [Server side]   [Keys]                           [[Keys options]]{.underline}[]   AllowKeyboardNavigation[]
  TotalGroupCollapse      Used to set the Keyboard shortcut for TotalGroupCollapse                 [Server side]   [Keys]                           [[Keys options]]{.underline}[]   AllowKeyboardNavigation[]


 

[]{#_Keys_Enumerable_Options}Keys Enumerable Options

The following options are present under the Keys Enumerable:

[·      ]Keys.Home

[·      ]Keys.End

[·      ]Keys.CtrlPlusHome

[·      ]Keys.CtrlPlusEnd

[·      ]Keys.PgUp

[·      ]Keys.PgDn

[·      ]Keys.Insert

[·      ]Keys.Delete

[·      ]Keys.Enter

[·      ]Keys.Esc

[·      ]Keys.F2

[·      ]Keys.CtrlPlusAltPlusF

[·      ]Keys.AltPlusHome

[·      ]Keys.AltPlusEnd

[·      ]Keys.AltPlusPgUp

[·      ]Keys.AltPlusPgDn

[·      ]Keys.AltPlusInsert

[·      ]Keys.AltPlusDelete

[·      ]Keys.AltPlusEnter

[·      ]Keys.AltPlusEsc

[·      ]Keys.CtrlPlusAltPlusHome

[·      ]Keys.CtrlPlusAltPlusEnd

[·      ]Keys.CtrlPlusAltPlusPgUp

[·      ]Keys.CtrlPlusAltPlusPgDn

[·      ]Keys.CtrlPlusAltPlusInsert

[·      ]Keys.CtrlPlusAltPlusDelete

[·      ]Keys.CtrlPlusAltPlusEnter

[·      ]Keys.CtrlPlusAltPlusEsc

[·      ]Keys.AltPlusA

[·      ]...

[·      ]Keys.AltPlusZ

[·      ]Keys.CtrlPlusAltPlusA

[·      ]...

[·      ]Keys.CtrlPlusAltPlusZ

[·      ]Keys.AltPlusUpArrow

[·      ]Keys.CtrlPlusAltPlusUpArrow

[·      ]Keys.AltPlusDownArrow

[·      ]Keys.CtrlPlusAltPlusDownArrow

[] 

Sample Link

To use the Keyboard Interface demo:

1.   Select the **Product Showcase** option from the accordion on the left side of the sample browser.

2.   Select the **Keyboard Interface** demo.

 

[]{#related-topics}

