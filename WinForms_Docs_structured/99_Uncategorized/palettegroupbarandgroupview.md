---
title: palettegroupbarandgroupview.md
original_path: WinForms_Docs/99_Uncategorized/palettegroupbarandgroupview.md
created_at: 2025-08-05
---








  









### Palette Groupbar And GroupView {#palette-groupbar-and-groupview style="tab-stops: 0pt"}

[] 

The Palette Groupbar control provides a way for users to drag-and-drop the symbols onto a diagram. It is based on the Syncfusion Essential Tools GroupBar control. Each symbol palette loaded in the PaletteGroupBar occupies a panel that can be selected by a bar button. The bar button is labeled with the name of the symbol palette. The symbols in the palette are shown as icons that can be dragged and dropped onto the diagram. This control allows users to add symbols to a palette, and save or load the palette whenever necessary. It provides a way to classify and maintain the symbols.

 

The PaletteGroupView control provides an easy way to serialize a symbol palette to and from the resource file of a form. At the design-time, users can attach a symbol palette to a PaletteGroupView control in a form. Selecting the PaletteGroupView, and clicking the **Palette** property in the Visual Studio .NET properties window, opens a standard **Open File** dialog, which allows the user to select a symbol palette file that has been created using the Symbol Designer.

 

The properties of the PaletteGroupBar and GroupView with their descriptions are given in the below table.

[] 


  ----------------------- ---------------------------------------------------------------------------------------------------------------
  Property                Description
  BackColor               Sets the background color of the component.
  BorderStyle             Sets the border style to FixedSingle, Fixed3D or None.
  Collapsed               Indicates whether the GroupBar is collapsed.
  CollapsedText           Sets the text for the collapsed client area of the GroupBar.
  CollapsedWidth          Specifies the width of the collapsed GroupBar.
  CollapseImage           Image of the collapsed button in the expanded state.
  DrawClientBorder        Indicates whether border is drawn around the GroupBar\'s client window.
  ExpandImage             Sets image of the collapse button.
  FlatLook                Indicates whether control is displayed with a flat look.
  Font                    Sets font style for text in the control.
  ForeColor               Sets fore color of the display text in the component.
  GroupBarItemCursor      Cursor that is to be displayed when the mouse pointer is over the GroupBarItems.
  Office2007Theme         Sets the (blue, black or silver) office theme used for drawing the control.
  PopupClientSize         Sets the initial size of the pop-up for GroupBar client.
  PopupResizeMode         Gets / sets the pop-up resize mode.
  ShowPopupGripper        Boolean value indicating whether to show GroupBarItem\'s popup gripper.
  Text                    Text associated with the control.
  TextAlign               Alignment of the text set through Text property.
  ThemesEnabled           Specifies whether control should be themed.
  VisualStyle             Visual style for drawing the control. Styles are Default, OfficeXP, Office2003, VS2005 and Office2007.
  AllowCollapse           Indicates whether GroupBar can be collapsed.
  AnimatedSelection       Indicates whether animated selection is enabled.
  BarHighlight            Indicates whether GroupBar item is highlighted on mouse hovering over a GroupBar Item.
  EditMode                This property determines whether the symbols from the palette can be dragged and dropped onto the Diagram.
  Enabled                 Indicates whether component is enabled.
  ExpandButtonToolTip     Sets tooltip for Collapse button, when the control is collapsed.
  GroupBarItemHeight      Height of the GroupBarItems.
  MinimizeButtonToolTip   ToolTip for collapse button when control is expanded.
  NavigationPaneToolTip   ToolTip for navigation pane.
  PopupAutoClose          Indicates whether pop-up is closed after clicking an item.
  SelectedItem            Index of the selected GroupBarItem.
  StackedMode             Indicates whether GroupBarItem is stacked.
  Visible                 Sets the visibility of the GroupBar control.
  GroupBarItems           GroupBarItem collection in the control.
  ShowChevron             Indicates if chevron button of the navigation panel should be displayed when required.
  ShowItemImageInHeader   Gets / sets a value indicating whether the selected item\'s image is shown in the header in Stacked GroupBar.
  Palette                 Indicates the loaded palette is in palette view.
  ----------------------- ---------------------------------------------------------------------------------------------------------------


[] 


  ------------- -----------------------------------------------------
  Method        Description
  LoadPalette   Loads given Symbol Palette to the PaletteGroupView.
  ------------- -----------------------------------------------------


[\
\
][]

The important events of the PaletteGroupBar and GroupView with their descriptions are given in the below table.

[] 


  -------------------------- ---------------------------------------------------------------------------------------------------
  Event                      Description
  Click                      Occurs when component is clicked.
  DoubleClick                Occurs when the component is double-clicked.
  GroupViewItemHighlighted   Event fired when an item in the GroupView control is highlighted.
  GroupViewItemSelected      Event fired when an item in the GroupView control is selected.
  GroupViewItemReordered     Event fired after the GroupView control items have been reordered by a drag--and--drop operation.
  GroupViewItemRenamed       Event fired after an in-place rename operation.
  ShowContextMenu Event      Event fired when the right mouse button is clicked over the control.
  -------------------------- ---------------------------------------------------------------------------------------------------


[] 

Programmatically, the properties can be set as follows.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [paletteGroupBar1.AllowDrop = [true];]                                                                                                                                             |
|                                                                                                                                                                                                                                             |
| [paletteGroupBar1.Controls.Add(paletteGroupView1);]                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [paletteGroupBar1.Controls.Add(paletteGroupView2);]                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [paletteGroupBar1.Dock = System.Windows.Forms.[DockStyle].Left;]                                                                                                                   |
|                                                                                                                                                                                                                                             |
| [paletteGroupBar1.EditMode = [false];]                                                                                                                                             |
|                                                                                                                                                                                                                                             |
| [paletteGroupBar1.GroupBarItems.AddRange([new] Syncfusion.Windows.Forms.Tools.GroupBarItem\[\]                                                 { groupBarItem1, groupBarItem2 });] |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [paletteGroupBar1.Location = [new] System.Drawing.Point(0, 0);]                                                                                                                    |
|                                                                                                                                                                                                                                             |
| [paletteGroupBar1.Name = [\"paletteGroupBar1\"];]                                                                                                                                |
|                                                                                                                                                                                                                                             |
| [paletteGroupBar1.SelectedItem = 1;]                                                                                                                                                                    |
|                                                                                                                                                                                                                                             |
| [paletteGroupBar1.Size = [new] System.Drawing.Size(114, 477);]                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [paletteGroupBar1.TabIndex = 1;]                                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [paletteGroupBar1.Text = [\"Symbol Palette\"];]                                                                                                                                  |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [groupBarItem1.Client = paletteGroupView1;]                                                                                                                                                             |
|                                                                                                                                                                                                                                             |
| [groupBarItem1.Text = [\"Basic Shapes\"];]                                                                                                                                       |
|                                                                                                                                                                                                                                             |
| [groupBarItem2.Client = paletteGroupView2;]                                                                                                                                                             |
|                                                                                                                                                                                                                                             |
| [groupBarItem2.Text = [\"ElectricalSymbols\"];]                                                                                                                                  |
|                                                                                                                                                                                                                                             |
| [paletteGroupView1.ButtonView = [true];]                                                                                                                                           |
|                                                                                                                                                                                                                                             |
| [paletteGroupView1.Location = [new] System.Drawing.Point(2, 24);]                                                                                                                  |
|                                                                                                                                                                                                                                             |
| [paletteGroupView1.Name = [\"paletteGroupView1\"];]                                                                                                                              |
|                                                                                                                                                                                                                                             |
| [paletteGroupView1.Size = [new] System.Drawing.Size(71, 0);]                                                                                                                       |
|                                                                                                                                                                                                                                             |
| [paletteGroupView1.TabIndex = 0;]                                                                                                                                                                       |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [paletteGroupView1.Text = [\"paletteGroupView1\"];]                                                                                                                              |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [paletteGroupView1.LoadPalette]                                                                                                                                                                         |
|                                                                                                                                                                                                                                             |
| [([@\"..\\..\\..\\..\\..\\..\\..\\..\\..\\Common\\Data\\Diagram\\BasicShapes.edp\"]);]                                                                                           |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [paletteGroupView2.LoadPalette]                                                                                                                                                                         |
|                                                                                                                                                                                                                                             |
| [([@\"..\\..\\..\\..\\..\\..\\..\\..\\..\\Common\\Data\\Diagram\\ElectricalSymbols.edp\"]);]                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                         |
|                                                                                                                                                                                        |
| []                                                                                                                                    |
|                                                                                                                                                                                        |
| [paletteGroupBar1.AllowDrop = [True]]                                                                                         |
|                                                                                                                                                                                        |
| [paletteGroupBar1.Controls.Add(paletteGroupView1)]                                                                                                 |
|                                                                                                                                                                                        |
| [paletteGroupBar1.Controls.Add(paletteGroupView2)]                                                                                                 |
|                                                                                                                                                                                        |
| [paletteGroupBar1.Dock = System.Windows.Forms.DockStyle.Left]                                                                                      |
|                                                                                                                                                                                        |
| [paletteGroupBar1.EditMode = [False]]                                                                                         |
|                                                                                                                                                                                        |
| [paletteGroupBar1.GroupBarItems.AddRange([New] Syncfusion.Windows.Forms.Tools.GroupBarItem() {groupBarItem1, groupBarItem2})] |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
|                                                                                                                                                                                        |
| [paletteGroupBar1.Location = [New] System.Drawing.Point(0, 0)]                                                                |
|                                                                                                                                                                                        |
| [paletteGroupBar1.Name = [\"paletteGroupBar1\"]]                                                                            |
|                                                                                                                                                                                        |
| [paletteGroupBar1.SelectedItem = 1]                                                                                                                |
|                                                                                                                                                                                        |
| [paletteGroupBar1.Size = [New] System.Drawing.Size(114, 477)]                                                                 |
|                                                                                                                                                                                        |
| [paletteGroupBar1.TabIndex = 1]                                                                                                                    |
|                                                                                                                                                                                        |
| [paletteGroupBar1.Text = [\"Symbol Palette\"]]                                                                              |
|                                                                                                                                                                                        |
| []                                                                                                                                  |
|                                                                                                                                                                                        |
| [groupBarItem1.Client = paletteGroupView1]                                                                                                         |
|                                                                                                                                                                                        |
| [groupBarItem1.Text = [\"Basic Shapes\"]]                                                                                   |
|                                                                                                                                                                                        |
| [groupBarItem2.Client = paletteGroupView2]                                                                                                         |
|                                                                                                                                                                                        |
| [groupBarItem2.Text = [\"ElectricalSymbols\"]]                                                                              |
|                                                                                                                                                                                        |
| [paletteGroupView1.ButtonView = [True]]                                                                                       |
|                                                                                                                                                                                        |
| [paletteGroupView1.Location = [New] System.Drawing.Point(2, 24)]                                                              |
|                                                                                                                                                                                        |
| [paletteGroupView1.Name = [\"paletteGroupView1\"]]                                                                          |
|                                                                                                                                                                                        |
| [paletteGroupView1.Size = [New] System.Drawing.Size(71, 0)]                                                                   |
|                                                                                                                                                                                        |
| [paletteGroupView1.TabIndex = 0]                                                                                                                   |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
|                                                                                                                                                                                        |
| [paletteGroupView1.Text = [\"paletteGroupView1\"]]                                                                          |
|                                                                                                                                                                                        |
| []                                                                                                                                  |
|                                                                                                                                                                                        |
| [paletteGroupView1.LoadPalette([\"..\\..\\..\\..\\..\\..\\..\\..\\..\\Common\\Data\\Diagram\\BasicShapes.edp\"])]           |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
|                                                                                                                                                                                        |
| [paletteGroupView2.LoadPalette([\"..\\..\\..\\..\\..\\..\\..\\..\\..\\Common\\Data\\Diagram\\ElectricalSymbols.edp\"])]     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Dynamically add Symbol Palette into PaletteGroupBar

[] 

You can add Symbol Palettes into PaletteGroupBar by means of deserializing the palette (\*.edp) file dynamically. The PaletteGroupBar control supports **PaletteGroupBar1.AddPalette()** method in order to add a palette into the PaletteGroupBar.

[] 

Follow the steps given below for adding symbol palette into PaletteGroupBar:

[] 

1.   Add OpenFileDialog control into form.

6\.

2.   Set the **Filter** property of OpenFileDialog as,

7\.

3.   Essential Diagram Palettes\|\*.edp\|Visio Stencils\|\*.vss; \*.vsx\|Visio Drawings(Shapes only)\|\*.vsd; \*.vdx\|All files\|\*.\*

8\.

4.   Add the following lines of code to your button click event.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                              |
|                                                                                                                                                                             |
| []                                                                                                                         |
|                                                                                                                                                                             |
| [if][ (openPaletteDialog.ShowDialog([this]) == DialogResult.OK)]  |
|                                                                                                                                                                             |
| [{]                                                                                                                                     |
|                                                                                                                                                                             |
| [    SymbolPalette curSymbolPalette;]                                                                                                   |
|                                                                                                                                                                             |
| [    FileStream iStream;]                                                                                                               |
|                                                                                                                                                                             |
| [    [string] strFileName = openPaletteDialog.FileName;]                                                           |
|                                                                                                                                                                             |
| [    RegexOptions options = RegexOptions.IgnoreCase \| RegexOptions.RightToLeft;]                                                       |
|                                                                                                                                                                             |
| [    Match match = Regex.Match(strFileName, [\".vss\|.vsx\|.vsd\|.vdx\"], options);]                            |
|                                                                                                                                                                             |
| [    [if] (match.Success)]                                                                                         |
|                                                                                                                                                                             |
| [    {]                                                                                                                                 |
|                                                                                                                                                                             |
| [        VisioStencilConverter converter = [new] VisioStencilConverter(strFileName, [this]);] |
|                                                                                                                                                                             |
| [        converter.ShowProgressDialog = [true];]                                                                   |
|                                                                                                                                                                             |
| [        curSymbolPalette = converter.Convert();]                                                                                       |
|                                                                                                                                                                             |
| [        [if] (curSymbolPalette != [null])]                                                   |
|                                                                                                                                                                             |
| [            PaletteGroupBar1.AddPalette(curSymbolPalette);]                                                                            |
|                                                                                                                                                                             |
| [    }]                                                                                                                                 |
|                                                                                                                                                                             |
| [    [else]]                                                                                                       |
|                                                                                                                                                                             |
| [    {]                                                                                                                                 |
|                                                                                                                                                                             |
| [        [try]]                                                                                                    |
|                                                                                                                                                                             |
| [        {]                                                                                                                             |
|                                                                                                                                                                             |
| [            iStream = [new] FileStream(strFileName, FileMode.Open, FileAccess.Read);]                             |
|                                                                                                                                                                             |
| []                                                                                                                                      |
|                                                                                                                                                                             |
| [            [// Deserialize  the Binary format]]                                                                 |
|                                                                                                                                                                             |
| [            IFormatter formatter = [new] BinaryFormatter();]                                                      |
|                                                                                                                                                                             |
| [            [AppDomain].CurrentDomain.AssemblyResolve +=]                                                      |
|                                                                                                                                                                             |
| [                      [new] [ResolveEventHandler](DiagramBaseAssembly.AssemblyResolver);] |
|                                                                                                                                                                             |
| [            curSymbolPalette = (SymbolPalette)formatter.Deserialize(iStream);]                                                         |
|                                                                                                                                                                             |
| [            PaletteGroupBar1.AddPalette(curSymbolPalette);]                                                                            |
|                                                                                                                                                                             |
| [        }]                                                                                                                             |
|                                                                                                                                                                             |
| [        [catch] ([Exception] se)]                                                         |
|                                                                                                                                                                             |
| [        {]                                                                                                                             |
|                                                                                                                                                                             |
| [            MessageBox.Show([this], se.Message);]                                                                 |
|                                                                                                                                                                             |
| [        }]                                                                                                                             |
|                                                                                                                                                                             |
| [        [finally]]                                                                                                |
|                                                                                                                                                                             |
| [        {]                                                                                                                             |
|                                                                                                                                                                             |
| [            iStream.Close();]                                                                                                          |
|                                                                                                                                                                             |
| [        }]                                                                                                                             |
|                                                                                                                                                                             |
| [    }]                                                                                                                                 |
|                                                                                                                                                                             |
| [}]                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Saving the active Palette

[] 

You can save the current active palette of PaletteGroupBar window by means of serializing the palette (.edp) file. The **PaletteGroupBar.CurrentSymbolPalette** property returns the currently selected symbol palette.

[] 

Follow the steps given below for saving current symbol palette

[] 

1.   Add SaveFileDialog control into form.

2.   Set the **Filter** property of SaveFileDialog as

9\.      Essential Diagram Palettes\|\*.edp\|All files\|\*.\*

3.   Add the following lines of code to your button click event.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                             |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [if][ (savePaletteDialog.ShowDialog([this]) == DialogResult.OK)] |
|                                                                                                                                                                            |
| [{]                                                                                                                                    |
|                                                                                                                                                                            |
| [    SymbolPalette symbolPalette = PaletteGroupBar1.CurrentSymbolPalette;]                                                             |
|                                                                                                                                                                            |
| [    [string] strSavePath = savePaletteDialog.FileName;]                                                          |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [    [if] (symbolPalette != [null])]                                                         |
|                                                                                                                                                                            |
| [    {]                                                                                                                                |
|                                                                                                                                                                            |
| [        FileStream fStream = [new] FileStream(strSavePath, FileMode.OpenOrCreate, FileAccess.Write);]            |
|                                                                                                                                                                            |
| [        BinaryFormatter formatter = [new] BinaryFormatter();]                                                    |
|                                                                                                                                                                            |
| [        formatter.Serialize(fStream, symbolPalette);]                                                                                 |
|                                                                                                                                                                            |
| [        fStream.Close();]                                                                                                             |
|                                                                                                                                                                            |
| [    }]                                                                                                                                |
|                                                                                                                                                                            |
| [}]                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 40: Palette GroupBar and Palette GroupView

 

[]{#p23} 

 

[]{#related-topics}

