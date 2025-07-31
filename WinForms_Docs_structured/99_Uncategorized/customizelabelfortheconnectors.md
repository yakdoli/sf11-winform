---
title: customizelabelfortheconnectors.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\customizelabelfortheconnectors.md
created_at: 2025-07-03
---








  









### Customize Label for the Connectors {#customize-label-for-the-connectors style="tab-stops: 0pt"}

The labels of the connectors are customized by the following properties, i.e. the user can specify the font color of the label. Also, several other customization properties have been added for the labels. These are tabulated below:

Properties

  Property           Description                                                                            Type of the Property   Value it Accepts   Any Other Dependencies/Sub-Properties Associated
  ------------------ -------------------------------------------------------------------------------------- ---------------------- ------------------ --------------------------------------------------
  LabelFontColor     Gets or sets the color of the label. The default value is black.                       Server side            String             No
  LabelFontFamily    Gets or sets the font family of the label. The default value is Arial.                 Server side            FontFamily         No
  LabelFontSize      Gets or sets the font size of the label. The default value is 11.                      Server side            Double             No
  LabelBackground    Gets or sets the background of the label. The default value is Transparent.            Server side            string             No (This is not supported in SVG Mode)
  LabelBorderColor   Gets or sets the border color of the label. The default value is Transparent.          Server side            String             No (This is not supported in SVG Mode)
  LabelBorderWidth   Gets or sets the border width of the label. The default value is Transparent.          Server side            Int                No (This is not supported in SVG Mode)
  LabelWidth         Gets or sets the width of the label. The default value is the node's width.            Server side            Double             No (This is not supported in SVG Mode)
  LabelHeight        Gets or sets the height of the label. The default value is the  node's label height.   Server side            Double             No (This is not supported in SVG Mode)

[] 

The following code snippet illustrates the implementation of the properties mentioned in the table above.

More:







