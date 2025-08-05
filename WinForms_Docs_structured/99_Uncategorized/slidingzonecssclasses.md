---
title: slidingzonecssclasses.md
original_path: WinForms_Docs/99_Uncategorized/slidingzonecssclasses.md
created_at: 2025-08-05
---






##### SlidingZone CSS Classes {#slidingzone-css-classes style="tab-stops: 0pt"}

[] 

Using this feature, we can add custom styles to Splitter control through external cascading style sheets.

[] 

[·      ]The CSS folder contains style settings for different themes, one file for each theme.

[·      ]In aspx, a CSS style gets associated with the corresponding control\'s style.

[] 

CSS Classes

[] 

We can add our own styles to the following CSS classes to change the entire look and feel of the control.

[] 

[·      ]Splitter

[·      ]SplitterBar_Default

[·      ]SplitterBar_Hover

[·      ]SplitterBar_Resize

[·      ]SplitterBar_ResizeError

[·      ]Sliding Zone

[·      ]SlidingPanel_CollapseHeader

[·      ]SlidingPanel_CollapseHeader_Hover

[·      ]SlidingPanel_ExpandHeader

[·      ]SlidingPanel_ExpandHeader_Hover

[·      ]SlidingPane_ResizeBar

[·      ]SlidingPane_ResizeBar_Hover

[·      ]SlidingPane_ResizeBar_Resize

[·      ]SlidingPane_ResizeBar_ResizeError

[·      ]SlidingPane

[] 

+--------------------------------------------------------------------------------+
| [/\*Splitter css setting\*/] |
|                                                                                |
| []                           |
|                                                                                |
| [Splitter]                                 |
|                                                                                |
| [{]                                        |
|                                                                                |
| [      border:1px solid #9D5806;]          |
|                                                                                |
| [      background-color: #FDFCFB;]         |
|                                                                                |
| [}]                                        |
+--------------------------------------------------------------------------------+

**[]** 

Property

[] 

In order to apply the styles from the custom css file to the control, we need to set the **CustomCSSClass** property.

[] 

  -----------------------------------------------------------------------------------------------
  [CustomCSSClass = "css/Splitter_style.css"]
  -----------------------------------------------------------------------------------------------

 

[]{#related-topics}

