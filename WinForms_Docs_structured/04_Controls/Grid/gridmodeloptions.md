---
title: gridmodeloptions.md
original_path: WinForms_Docs/04_Controls/Grid/gridmodeloptions.md
created_at: 2025-08-05
---






#### Grid Model Options {#grid-model-options style="tab-stops: 0pt"}

This section provides information on how to write syntax for the following GridModel Options:

[·      ]ActivateCurrentCellBehavior

[·      ]AllowScrollCurrentCellInView

[·      ]AlphaBlendSelectionColor

[·      ]ClickedOnDisabledCellBehavior

[·      ]ShowCurrentCellBorderBehavior

[·      ]DefaultGridBorderStyle

 

Activating Current Cell Behavior

 

The following code illustrates how to activate current cell behavior:

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [this][.gridGroupingControl1.ActivateCurrentCellBehavior = [GridCellActivateAction].SelectAll;]
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 

Allow scroll for Current cell view

The following code illustrates how to allow scroll for current cell view:

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [this][.gridGroupingControl1.AllowScrollCurrentCellInView = [GridScrollCurrentCellReason].Activate;]
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 

Alpha Blend Selection Color

The following code illustrates how to [select alpha blend selection color: ]

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [this][.gridGroupingControl1.AlphaBlendSelectionColor = [Color].Red;]
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 

ClickedOnDisabledCellBehavior

The following code illustrates how to define the current cell behavior when disabled cell is clicked:

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [this][.gridGroupingControl1.ClickedOnDisabledCellBehavior = [GridClickedOnDisabledCellBehavior].Default;]
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 

Show Current Cell Border Behavior

The following code illustrates how to show current cell border behavior:

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [this][.gridGroupingControl1.ShowCurrentCellBorderBehavior = [GridShowCurrentCellBorder].HideAlways;]
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 

Default Grid Border Style

The following code illustrates how to set default grid border style:

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [this][.gridGroupingControl1.DefaultGridBorderStyle = [GridBorderStyle].None;]
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 

 

[]{#related-topics}

