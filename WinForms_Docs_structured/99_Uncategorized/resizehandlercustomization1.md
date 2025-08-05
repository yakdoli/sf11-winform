---
title: resizehandlercustomization1.md
original_path: WinForms_Docs/99_Uncategorized/resizehandlercustomization1.md
created_at: 2025-08-05
---








  









### Resize Handler Customization {#resize-handler-customization style="tab-stops: 0pt"}

This feature provides different styles for Resize Handler. This enables you to customize the complete look and feel of the eight resize handler.

 

Use Case Scenarios

The appearance of the Resizer Handler can be effectively changed by applying different styles to the Thumb, using the Resize Handler Customization. 

 

Creating Custom Style for Resize Handler

The Resize Handler consists of eight Resizer Thumbs. You can set different styles to a ResizerThumb by using the Resize Handler Properties.

 

Follow the below steps to create custom styles for Resize Handler.

Step1: Creating Style for ResizerThumb

Prepare styles with template for each ResizerThumb.

     

[·      ]Through XAML.

The following code illustrates how to create the style for ResizerThumb

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      [\<][Style ][x][:][Key][=\"TopLeftCornerResizerThump\"] [ TargetType][=\"syncfusion:ResizerThumb\" \>]]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      [   ][\<][Setter][ Property][=\"SnapsToDevicePixels\"][ Value][=\"True\"/\>]]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      [   ][\<][Setter][ Property][=\"OverridesDefaultStyle\"][ Value][=\"true\"/\>]]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      [   ][\<][Setter][ Property][=\"IsTabStop\"][ Value][=\"false\"/\>]]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      [   ][\<][Setter][ Property][=\"Focusable\"][ Value][=\"false\"/\>]]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      [   ][\<][Setter][ Property][=\"Height\"][ Value][=\"15\"/\>]]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      [   ][\<][Setter][ Property][=\"Width\"][ Value][=\"15\"/\>]]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      [   ][\<][Setter][ Property][=\"Cursor\"][ Value][=\"SizeNWSE\"/\>]]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      [   ][\<][Setter][ Property][=\"Margin\"][ Value][=\"-3 -3 0 0\"/\>]]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      [   ][\<][Setter][ Property][=\"VerticalAlignment\"][ Value][=\"Top\"/\>]]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      [   ][\<][Setter][ Property][=\"HorizontalAlignment\"][ Value][=\"Left\"/\>]]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      [    ][\<][Setter][ Property][=\"Template\"\>]]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      [    ][\<][Setter.Value][\>]]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      [      ][\<][ControlTemplate][ TargetType][=\"syncfusion:ResizerThumb\"\>]]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      [         ][\<][Grid][\>]]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      [          ][\<][Rectangle][ HorizontalAlignment][=\"Stretch\" ][Margin][=\"{][TemplateBinding][ Margin][}\"]]                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      ][         [   VerticalAlignment][=\"{][TemplateBinding][ VerticalAlignment][}\" ][StrokeDashCap][=\"Flat\"                                       ][     ]             [     ]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      [            Cursor][=\"{][TemplateBinding][ Cursor][}\" ][x][:][Name][=\"PART_ReseizerThumb3\" ][Stroke][=\"Blue\"]]                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                  StrokeStartLineCap][=\"Round\" ][StrokeThickness][=\"5\"/\>][]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      [          ][\<][Rectangle][ HorizontalAlignment][=\"{][TemplateBinding][ HorizontalAlignment][}\"]]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [               [   VerticalAlignment][=\"Stretch\"][ Cursor][=\"{][TemplateBinding][ Cursor][}\" ][Stroke][=\"Blue\"]]                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      ][            [x][:][Name][=\"PART_ReseizerThumb2\"] [ StrokeDashCap][=\"Flat\"][ StrokeThickness][=\"5\"][      ]]                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      [            StrokeStartLineCap][=\"Round\"][ Margin][=\"{][TemplateBinding][ Margin][}\"/\>]]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      [           ][\</][Grid][\>]]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      [         ][\</][ControlTemplate][\>]]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      [     ][\</][Setter.Value][\>]]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      ][  ][\</][Setter][\>]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][Style][\>][]                                                                                                                                                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Step2:  Assign the Style to Node

[·      ]Through XAML.

 

The following code illustrates how to assign the Resize Handler Style to Node

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [      ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [      \<][Style][ TargetType][=\"syncfusion:Node\"\>]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [      \<][Setter][ Property][=\"TopResizer\"][ Value][=\"{][StaticResource][ [ TopResizerThump][}\"/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [      [\<][Setter][ Property][=\"LeftResizer\"][ Value][=\"{][StaticResource][ LeftResizerThump][}\"/\>]]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [      [\<][Setter][ Property][=\"RightResizer\"][ Value][=\"{][StaticResource][ RightResizerThump][}\"/\>]]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [      [\<][Setter][ Property][=\"BottomResizer\"][ Value][=\"{][StaticResource][ BottomResizerThump][}\"/\>]]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [      [\<][Setter][ Property][=\"TopLeftCornerResizer\"][ Value][=\"{][StaticResource ][TopLeftCornerResizerThump][}\"/\>]]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [      [\<][Setter][ Property][=\"TopRightCornerResizer\"] [Value][=\"{][StaticResource][ TopRightCornerResizerThump][}\"/\>]]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [      [\<][Setter][ Property][=\"BottomLeftCornerResizer\"][ Value][=\"{][StaticResource][ BottomLeftCornerResizerThump][}\"/\>]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [      \<][Setter][ Property][=\"BottomRightCornerResizer\"][ [Value][=\"{][StaticResource][ BottomRightCornerResizerThump][}\"/\>]]                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\</][Style][\>][]                                                                                                                                                                                                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[·      ]Through Code behind\[C#\]

 

The following code illustrates how to assign the Resize Handler Style to Node

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[ ]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [Node][ n = shape [as] [Node]; ][]                                                |
|                                                                                                                                                                                                                                                                            |
| [n.TopResizer = [this.]Resources\[[\"TopResizerThump\"]\] [as] [Style];][]            |
|                                                                                                                                                                                                                                                                            |
| [n.LeftResizer =[this].Resources\[[\"LeftResizerThump\"]\] [as] [Style];]                                                                 |
|                                                                                                                                                                                                                                                                            |
| [n.RightResizer =[this].Resources\[[\"RightResizerThump\"]\] [as] [Style];]                                                               |
|                                                                                                                                                                                                                                                                            |
| [n.BottomResizer =[this].Resources\[[\"BottomResizerThump\"]\] [as] [Style];]                                                             |
|                                                                                                                                                                                                                                                                            |
| [n.TopLeftCornerResizer =[this].Resources\[[\"TopLeftCornerResizerThump\"]\] [as] [Style];]                                               |
|                                                                                                                                                                                                                                                                            |
| [n.TopRightCornerResizer =[this].Resources\[[\"TopRightCornerResizerThump\"]\] [as] [Style];]                                             |
|                                                                                                                                                                                                                                                                            |
| [n.BottomLeftCornerResizer =[this].Resources\[[\"BottomLeftCornerResizerThump\"]\] [as] [Style];]                                         |
|                                                                                                                                                                                                                                                                            |
| [n.BottomRightCornerResizer =[this].Resources\[[\"BottomRightCornerResizerThump\"]\] [as] [Style];][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[ ]                                                                                                           |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                                 |
| [Dim][ n [As] [Node] = [TryCast](Shape, [Node])] |
|                                                                                                                                                                                                                                 |
| [n.TopResizer = [TryCast](Me.Resources(\"TopResizerThump\"), Style)]                                                                                                   |
|                                                                                                                                                                                                                                 |
| [n.LeftResizer =TryCast(Me.Resources(\"LeftResizerThump\"), Style)]                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [n.RightResizer =TryCast(Me.Resources(\"RightResizerThump\"), Style)]                                                                                                                       |
|                                                                                                                                                                                                                                 |
| [n.BottomResizer =TryCast(Me.Resources(\"BottomResizerThump\"), Style)]                                                                                                                     |
|                                                                                                                                                                                                                                 |
| [n.TopLeftCornerResizer =TryCast(Me.Resources(\"TopLeftCornerResizerThump\"), Style)]                                                                                                       |
|                                                                                                                                                                                                                                 |
| [n.TopRightCornerResizer =TryCast(Me.Resources(\"TopRightCornerResizerThump\"), Style)]                                                                                                     |
|                                                                                                                                                                                                                                 |
| [n.BottomLeftCornerResizer =TryCast(Me.Resources(\"BottomLeftCornerResizerThump\"), Style)]                                                                                                 |
|                                                                                                                                                                                                                                 |
| [n.BottomRightCornerResizer =TryCast(Me.Resources(\"BottomRightCornerResizerThump\"), Style)][]                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Setting ResizerThumb Template as null

ResizerThumb will not be visible When the ResizerThumb Template value as Null

 

The following code illustrates how to set the ResizerThumb Template to Null

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XMAL\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [      \<][Style][ x][:][Key][=\"TopResizerThump\"][ TargetType][=\"syncfusion:ResizerThumb\"\>][ ][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [      [       \<][Setter][ Property][=\"Template\"][ Value][=\"{][x][:][Null][}\"\>]]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [      ][       ][\</][Setter][\>]                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\</][Style][\>][]                                                                                                                                                                                                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Following is a sample screenshot of customized resizer that has only four corners.

{border="0"}

Figure 49:Custom Style

 

Tables for Properties, Methods, and Events

 

Properties

 

Table 27: ResizeHandler Property/ies Table


  -------------------- --------------------------------------------------------------------- --------------------- --------------------------------- ------------------------------
  Property             Description                                                            Type                 Data Type                         Reference links
  TopResizer           Gets or sets a value of TopResizer Style for Resize Handler           Dependency property   Style[]   No[]
  BottomResizer        Gets or sets a value of BottomResizer Style for Resize Handler        Dependency property   Style                             No
  LeftResizer          Gets or sets a value of LeftResizer Style for  Resize Handler         Dependency property   Style                             No
  RightResizer         Gets or sets a value of RightResizer Style for Resize Handle          Dependency property   Style                             No
  TopLeftResizer       Gets or sets a value of TopLeftResizer Style for Resize Handler       Dependency property   Style                             No
  TopRightResizer      Gets or sets a value of TopRightResizer Style for Resize Handler      Dependency property   Style                             No
  BottomLeftResizer    Gets or sets a value of BottomLeftResizer Style for  Resize Handler   Dependency property   Style                             No
  BottomRightResizer   Gets or sets a value of BottomRightResizer Style for Resize Handler   Dependency property   Style                             No
  -------------------- --------------------------------------------------------------------- --------------------- --------------------------------- ------------------------------


 

Sample Link

To view sample,

1.   Open the WPF sample browser from the dashboard.

2.   Navigate to WPF Diagram -\> Editable Diagram-\>ResizerCustomization Demo

[] 

 

[]{#related-topics}

