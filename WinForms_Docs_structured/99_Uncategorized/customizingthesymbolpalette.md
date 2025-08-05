---
title: customizingthesymbolpalette.md
original_path: WinForms_Docs/99_Uncategorized/customizingthesymbolpalette.md
created_at: 2025-08-05
---








  









### Customizing the Symbol Palette {#customizing-the-symbol-palette style="tab-stops: 0pt"}

[] 

The appearance of the symbol palette can be customized to suit any application. Several properties have been provided in the **SymbolPalette** class to enable its customization.

 

The following properties can be used to customize the Symbol Palette in your application.\
\

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| Property                          | Description                                                                                        | Type of the property | Value it accepts | Any other dependencies/ sub properties associated |
+===================================+====================================================================================================+======================+==================+===================================================+
| Background                        | Specifies the background color of the Symbol Palette.                                              | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default color is *Beige*.                                                                      |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| BorderThickness                   | Gets or sets the border thickness of the Symbol Palette.                                           | Dependency property  | Thickness        | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default value is 1.                                                                            |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| BorderBrush                       | Specifies the border color of the Symbol Palette.                                                  | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default color is *Brown*.                                                                      |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| SymbolPaletteGroupBackground      | Specifies the background color of the Symbol Palette Group.                                        | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default color is *Bisque*.                                                                     |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| SymbolPaletteGroupForeground      | Specifies the foreground color of the Symbol Palette Group.                                        | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default color is *SaddleBrown.*                                                                |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| SymbolPaletteGroupBorderBrush     | Specifies the border color of the Symbol Palette Group.                                            | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default color is *Chocolate.*                                                                  |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| ItemBorderThickness               | Gets or sets the border thickness of the Symbol Palette Item.                                      | Dependency property  | Thickness        | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default value is 1.                                                                            |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| ItemCornerRadius                  | Gets or sets the corner radius of the Symbol Palette Item.                                         | Dependency property  | CornerRadius     | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default value is 2.                                                                            |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| ItemMouseOverBorderBrush          | Specifies the border color of the Symbol Palette Item over which the mouse pointer rests.          | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default value is *Orange*.                                                                     |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| ItemCheckedBorderBrush            | Specifies the border color of the Symbol Palette Item that is selected.                            | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default value is *Red*.                                                                        |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| ItemCheckedMouseOverBorderBrush   | Specifies the border color of the selected Symbol Palette Item over which the mouse pointer rests. | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default value is *Green*.                                                                      |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| FilterSelectorBackground          | Specifies the background color of the Symbol Palette Filter.                                       | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default value is *Chocolate*.                                                                  |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| FilterSelectorForeground          | Specifies the foreground color of the Symbol Palette Filter.                                       | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default value is *DarkSlateGray*.                                                              |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| FilterSelectorBorderThickness     | Gets or sets the border thickness of the Symbol Palette Filter                                     | Dependency property  | Thickness        | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default value is (0,0,0,1).                                                                    |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| FilterSelectorMouseOverForeground | Specifies the foreground color of the Symbol Palette Filter over which the mouse pointer rests.    | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default value is *OldLace*.                                                                    |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| FilterSelectorBorderBrush         | Specifies the border color of the Symbol Palette Filter                                            | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default value is *Chocolate*.                                                                  |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| PopUpBackground                   | Specifies the background color of the Symbol Palette PopUp.                                        | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default value is *WhiteSmoke*.                                                                 |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| PopUpForeground                   | Specifies the foreground color of the Symbol Palette PopUp.                                        | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default value is *DarkSlateGray*.                                                              |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| PopUpBorderThickness              | Gets or sets the border thickness of the Symbol Palette PopUp.                                     | Dependency property  | Thickness        | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default value is (0,1,1,1).                                                                    |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| PopUpMouseOverBrush               | Specifies the background color of the Symbol Palette PopUp Item over which the mouse pointer rests | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default value is *LightSalmon*.                                                                |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| PopUpBorderBrush                  | Specifies the border color of the Symbol Palette PopUp.                                            | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default value is *Chocolate*.                                                                  |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| PopUpLeftColumnBackground         | Specifies the background color of the Check Box Column in the Symbol Palette PopUp                 | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default value is *LightGray*.                                                                  |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| CheckerBackground                 | Specifies the the background color of the Check Boxes in the Symbol Palette PopUp                  | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default value is *Bisque*.                                                                     |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| CheckerBorderBrush                | Specifies the the border color of the Check Boxes in the Symbol Palette Pop Up.                    | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default value is *DarkSlateGray.*                                                              |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| CheckerTickBrush                  | Specifies the Tick color of the selected Check Box in the Symbol Palette PopUp                     | Dependency property  | Brush            | No                                                |
|                                   |                                                                                                    |                      |                  |                                                   |
|                                   | The default value is *DarkSlateGray.*                                                              |                      |                  |                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+


[] 

The following code example illustrates the setting of the Symbol Palette properties.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                      |
| [DiagramControl][ diagramControl = [new] [DiagramControl](); diagramControl.SymbolPalette.BorderThickness = [new] [Thickness](2);]                 |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.BorderBrush = [Brushes].MidnightBlue;]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.Background = [Brushes].Blue; diagramControl.SymbolPalette.SymbolPaletteGroupBackground = [Brushes].DarkBlue; diagramControl.SymbolPalette.SymbolPaletteGroupForeground = [Brushes].White;] |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.SymbolPaletteGroupBorderBrush = [Brushes].SlateBlue;]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.FilterSelectorBackground = [Brushes].SkyBlue; diagramControl.SymbolPalette.FilterSelectorForeground = [Brushes].White;]                                                                                            |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.FilterSelectorBorderBrush = [Brushes].Blue; diagramControl.SymbolPalette.FilterSelectorBorderThickness = [new] [Thickness](0);]                                                               |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.CheckerTickBrush = [Brushes].White;]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.CheckerBorderBrush = [Brushes].MidnightBlue;]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.CheckerBackground = [Brushes].LightBlue; diagramControl.SymbolPalette.PopUpItemMouseOverBrush = [Brushes].CornflowerBlue;]                                                                                         |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.PopUpBorderBrush = [Brushes].MidnightBlue;]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                      |
| [diagramControl.SymbolPalette.ItemBorderThickness = [new] [Thickness](2);]                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                              |
|                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                             |
| [Dim][ diagramControl [As] [New] [DiagramControl]()] |
|                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.BorderThickness = [New] Thickness(2)]                                                                                |
|                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.BorderBrush = Brushes.MidnightBlue]                                                                                                       |
|                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.Background = Brushes.Blue]                                                                                                                |
|                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.SymbolPaletteGroupBackground = Brushes.DarkBlue]                                                                                          |
|                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.SymbolPaletteGroupForeground = Brushes.White]                                                                                             |
|                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.SymbolPaletteGroupBorderBrush = Brushes.SlateBlue]                                                                                        |
|                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.FilterSelectorBackground = Brushes.SkyBlue]                                                                                               |
|                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.FilterSelectorForeground = Brushes.White]                                                                                                 |
|                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.FilterSelectorBorderBrush = Brushes.Blue]                                                                                                 |
|                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.FilterSelectorBorderThickness = [New] Thickness(0)]                                                                  |
|                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.CheckerTickBrush = Brushes.White]                                                                                                         |
|                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.CheckerBorderBrush = Brushes.MidnightBlue]                                                                                                |
|                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.CheckerBackground = Brushes.LightBlue]                                                                                                    |
|                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.PopUpItemMouseOverBrush = Brushes.CornflowerBlue]                                                                                         |
|                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.PopUpBorderBrush = Brushes.MidnightBlue]                                                                                                  |
|                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.ItemBorderThickness = [New] Thickness(2)][]                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following screen shot illustrates the various customization options that are available for the Symbol Palette Item, Group and Filter Selector.

[] 

{border="0"}

Figure 156: Symbol Palette Item, Group and Filter Selector Customization Properties**[]**

The following screen shot illustrates the various customization options available for the Symbol Palette PopUp.

[] 

{border="0"}

Figure 157: Symbol Palette PopUp Customization Properties[]{#p98}

 

[]{#related-topics}

