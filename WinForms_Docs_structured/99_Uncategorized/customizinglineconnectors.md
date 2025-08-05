---
title: customizinglineconnectors.md
original_path: WinForms_Docs/99_Uncategorized/customizinglineconnectors.md
created_at: 2025-08-05
---








  









### Customizing Line Connectors {#customizing-line-connectors style="tab-stops: 0pt"}

The lineconnector can be customized by using the following properties:

 

Properties

  ---------------------------------------------------------- ------------------------------------------------------------------------------------ ------------------ ---------------
  Property Name                                              Description                                                                          Value it Accepts   Default Value
  LineColor                                                  Used to change the color of the line/connector.                                      String             Black
  LineWidth                                                  Used to change the width of the line/connector.                                      Double             1
  [HeadDecoratorHeight]                Used to change the height of the line/connector head decorator shape.                Double             8
  [HeadDecoratorWidth]                 Used to change the width of the line/connector head decorator shape.                 Double             8
  [HeadDecoratorBackground]            Used to change the background color of the line/connector head decorator shape.      String             Black
  [HeadDecoratorBorderColor]           Used to change the border color of the line/connector headdecorator shape.           String             Black
  [HeadDecoratorSelectorBackground]    Used to change the background color of the line/connector head decorator selector.   String             Gray
  [HeadDecoratorSelectorBorderColor]   Used to change the border color of the line/connector head decorator selector.       String             Black
  [TailDecoratorBackground]            Used to change the background color of the line/connector tail decorator shape.      String             Black
  [TailDecoratorBorderColor]           Used to change the border color of the line/connector tail decorator shape.          String             Black
  [TailDecoratorSelectorBackground]    Used to change the background color of the line/connector tail decorator selector.   String             Gray
  [TailDecoratorSelectorBorderColor]   Used to change the border color of the line/connector tail decorator selector.       String             Black
  [TailDecoratorHeight]                Used to change the height of the line/connector tail decorator shape.                Double             8
  [TailDecoratorWidth]                 Used to change the width of the line/connector tail decorator shape.                 Double             8
  ---------------------------------------------------------- ------------------------------------------------------------------------------------ ------------------ ---------------

 

The following code can be used to customize the line connector. 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**[]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                              |
| [             LineConnector][ lineConnector = [new] [LineConnector]()]                                                |
|                                                                                                                                                                                                                                                                                              |
| [            {]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                              |
| [                Name=name,]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                              |
| [                HeadNode = headNode,]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                              |
| [                TailNode = tailNode,]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                              |
| [                ConnectorType = [ConnectorType].Beizer,]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                              |
|                    LineColor = "green",                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                              |
| [                LineWidth = 2,]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                              |
| [                HeadDecoratorHeight=14,]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                              |
| [                HeadDecoratorWidth=14,]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                              |
| [                HeadDecoratorBackground=][\"red\"][,]                            |
|                                                                                                                                                                                                                                                                                              |
| [                HeadDecoratorBorderColor=][\"black\"][,]                         |
|                                                                                                                                                                                                                                                                                              |
| [                HeadDecoratorSelectorBackground=][\"gold\"][,]                   |
|                                                                                                                                                                                                                                                                                              |
| [                HeadDecoratorSelectorBorderColor = ][\"black\"][,  ]             |
|                                                                                                                                                                                                                                                                                              |
| [                TailDecoratorBackground=][\"blue\"][,]                           |
|                                                                                                                                                                                                                                                                                              |
| [                TailDecoratorBorderColor=][\"black\"][,]                         |
|                                                                                                                                                                                                                                                                                              |
| [                TailDecoratorSelectorBackground = ][\"gold\"][,]                 |
|                                                                                                                                                                                                                                                                                              |
| [                TailDecoratorSelectorBorderColor=][\"black\"][,                ] |
|                                                                                                                                                                                                                                                                                              |
| [                TailDecoratorHeight=14,]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                              |
| [                TailDecoratorWidth=14]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                              |
| [            };]                                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 72: Connector Customization

[]{#related-topics}

