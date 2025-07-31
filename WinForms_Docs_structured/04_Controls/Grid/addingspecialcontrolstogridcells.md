---
title: addingspecialcontrolstogridcells.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\addingspecialcontrolstogridcells.md
created_at: 2025-07-03
---






#### Adding Special Controls to Grid Cells {#adding-special-controls-to-grid-cells style="tab-stops: 0pt"}

[] 

The **GridStyleInfo** property, **CellType**, lets you add special controls such as a check box or a combo box to a grid cell. Since the CellType is a member of GridStyleInfo, you can use it on a cell basis, row basis, column basis, or on a table basis, simply by setting this CellType property on the appropriate style. If you want the entire grid to be a combo box, then you simply have to set the grid\'s **CellValue** property to use combo boxes. You can derive your own controls to implement additional cell types. For more details, see [deriving a cell control]{.UGHyperlink}.

[] 

Following table lists the cell types that are supported in Essential Grid.

[] 


  ------------------- ----------------------------------------------------------------------------
  Grid Cell Control   Description
  Check Box           Displays a check box in the cell.
  Color Edit          Displays a color selection and allows editing color choices.
  Combo Box           Displays a combo box in the cell.
  Control             Displays a System.Windows.Forms.Control in a cell.
  Currency Edit       Displays a currency value and allows editing of it.
  Formula Cell        Displays calculation from a formula entered in the cell.
  Grid List Control   Displays a multicolumn list control as a drop down.
  Header              Displays cells as grid header cells with static text.
  Masked Edit         Uses a mask to control values entered into the cell.
  Month Calendar      Displays a DateTime value and allows editing of it.
  Numeric Up Down     Displays numeric text that can be edited or modified with spinner buttons.
  Progress Bar        Displays a ProgressBar control in a cell.
  Push Button         Displays a button in the cell that the user can click.
  Rich Text           Displays rich text in the cell and allows editing while in a drop down.
  Slider              Displays a slider control in a cell.
  Static              Displays text in the cell that cannot be edited.
  Text Box            Displays text in the cell that can be edited.
  ------------------- ----------------------------------------------------------------------------


 

[]{#p50} 

 

More:





































