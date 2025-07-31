---
title: symbolpalettecustomization.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\symbolpalettecustomization.md
created_at: 2025-07-03
---








  









### [Symbol Palette Customization] {#symbol-palette-customization style="tab-stops: 0pt"}

[This feature allows you to customize the appearance of the symbol palette in the diagram page to suit any application. Several properties have been provided in the **SymbolPalette** class to enable this.]

 

Use Case Scenario

This feature allows users to[ change the following:]

[·      ][Border color of the palette]

[·      ][Background color of the palette from which you can pick the symbols]

[·      ][Selection color of a group name when the cursor hovers over it]

[·      ][Foreground color of a group]

[·      ][Item selector color, etc.]

 

Appearance and Structure

The following figure gives you an idea as to which parts of the symbol palette can be customized using this feature:

{border="0"}

Figure 134: Customized Symbol Palette

 

Where do I find the installed samples?

To view a sample:

1.   Open the Essential Diagram sample browser from the dashboard. (Refer to the Samples and Location chapter.)

2.   Navigate to **Getting Started** \> **SymbolPalette Customization Demo**.

 

Properties

+------------------------------------+----------------------------------------------------------------------------+---------------------+--------------------------------+----------------------------------------+
| Property                           | Description                                                                | Type of Property    | Value it Accepts               | Dependencies                           |
+------------------------------------+----------------------------------------------------------------------------+---------------------+--------------------------------+----------------------------------------+
| Background                         | Gets or sets the background color for the symbol palette.                  | Dependency property | String                         | No (This is not supported in SVG Mode) |
|                                    |                                                                            |                     |                                |                                        |
|                                    |                                                                            |                     |                                |                                        |
+------------------------------------+----------------------------------------------------------------------------+---------------------+--------------------------------+----------------------------------------+
| BorderColor                        | Gets or sets the border color for the symbol palette.                      | Dependency property | String                         | No (This is not supported in SVG Mode) |
|                                    |                                                                            |                     |                                |                                        |
|                                    |                                                                            |                     |                                |                                        |
+------------------------------------+----------------------------------------------------------------------------+---------------------+--------------------------------+----------------------------------------+
| SymbolPaletteGroupBackground       | Gets or sets the background color for the symbol palette group.            | Dependency property | String                         | No (This is not supported in SVG Mode) |
|                                    |                                                                            |                     |                                |                                        |
|                                    |                                                                            |                     |                                |                                        |
+------------------------------------+----------------------------------------------------------------------------+---------------------+--------------------------------+----------------------------------------+
| SymbolPaletteGroupForeground       | Gets or sets the foreground color for the symbol palette group.            | Dependency property | String[] | No (This is not supported in SVG Mode) |
|                                    |                                                                            |                     |                                |                                        |
|                                    |                                                                            |                     |                                |                                        |
+------------------------------------+----------------------------------------------------------------------------+---------------------+--------------------------------+----------------------------------------+
| SymbolPaletteGroupBorderColor      | Gets or sets the border color for the symbol palette group.                | Dependency property | String[] | No (This is not supported in SVG Mode) |
|                                    |                                                                            |                     |                                |                                        |
|                                    |                                                                            |                     |                                |                                        |
+------------------------------------+----------------------------------------------------------------------------+---------------------+--------------------------------+----------------------------------------+
| SymbolPaletteGroupHoverBackground  | Gets or sets the mouse-over background color for the symbol palette group. | Dependency property | String[] | No (This is not supported in SVG Mode) |
|                                    |                                                                            |                     |                                |                                        |
|                                    |                                                                            |                     |                                |                                        |
+------------------------------------+----------------------------------------------------------------------------+---------------------+--------------------------------+----------------------------------------+
| SymbolPaletteGroupHoverForeground  | Gets or sets the mouse-over foreground color for the symbol palette group. | Dependency property | String[] | No (This is not supported in SVG Mode) |
|                                    |                                                                            |                     |                                |                                        |
|                                    |                                                                            |                     |                                |                                        |
+------------------------------------+----------------------------------------------------------------------------+---------------------+--------------------------------+----------------------------------------+
| SymbolPaletteGroupHoverBorderColor | Gets or sets the mouse-over border color for the symbol palette group.     | Dependency property | String[] | No (This is not supported in SVG Mode) |
|                                    |                                                                            |                     |                                |                                        |
|                                    |                                                                            |                     |                                |                                        |
+------------------------------------+----------------------------------------------------------------------------+---------------------+--------------------------------+----------------------------------------+
| ItemMouseOverBorderColor           | Gets or sets the mouse-over border color for the symbol palette item.      | Dependency property | String[] | No (This is not supported in SVG Mode) |
|                                    |                                                                            |                     |                                |                                        |
|                                    |                                                                            |                     |                                |                                        |
+------------------------------------+----------------------------------------------------------------------------+---------------------+--------------------------------+----------------------------------------+

 

More:





