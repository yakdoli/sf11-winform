---
title: decoratorshapes.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\decoratorshapes.md
created_at: 2025-07-03
---








  









### Decorator Shapes {#decorator-shapes style="tab-stops: 0pt"}

[] 

Head and tail decorator shape properties provide an option to add arrows and to customize these arrows. End point decorators can be provided for all types of connectors. There are a number of shapes available for head and tail decorators.

 

Properties\
\

+--------------------+-----------------------------------------------------------------------+----------------------+------------------------+---------------------------------------------------+
| Property           | Description                                                           | Type of the property | Value it accepts       | Any other dependencies/ sub properties associated |
+====================+=======================================================================+======================+========================+===================================================+
| HeadDecoratorShape | Gets or sets the head decorator shape of the connection.              | CLR Property         | DecoratorShape.None    | No                                                |
|                    |                                                                       |                      |                        |                                                   |
|                    | Four values namely None, Arrow , Diamond and Circle can be specified. |                      | DecoratorShape.Arrow   |                                                   |
|                    |                                                                       |                      |                        |                                                   |
|                    | Default value: HeadDecoratorShape.None                                |                      | DecoratorShape.Diamond |                                                   |
|                    |                                                                       |                      |                        |                                                   |
|                    |                                                                       |                      | DecoratorShape.Circle  |                                                   |
+--------------------+-----------------------------------------------------------------------+----------------------+------------------------+---------------------------------------------------+
| TailDecoratorShape | Gets or sets the head decorator shape of the connection.              | CLR Property         | DecoratorShape.None    | No                                                |
|                    |                                                                       |                      |                        |                                                   |
|                    | Four values namely None, Arrow , Diamond and Circle can be specified. |                      | DecoratorShape.Arrow   |                                                   |
|                    |                                                                       |                      |                        |                                                   |
|                    | Default value: TailDecoratorShape.Arrow                               |                      | DecoratorShape.Diamond |                                                   |
|                    |                                                                       |                      |                        |                                                   |
|                    |                                                                       |                      | DecoratorShape.Circle  |                                                   |
+--------------------+-----------------------------------------------------------------------+----------------------+------------------------+---------------------------------------------------+
| HeadDecoratorStyle | Provides customization option for the head decorator shape.           | CLR Property         | DecoratorStyle         | No                                                |
+--------------------+-----------------------------------------------------------------------+----------------------+------------------------+---------------------------------------------------+
| TailDecoratorStyle | Provides customization option for the tail decorator shape.           | CLR Property         | DecoratorStyle         | No                                                |
+--------------------+-----------------------------------------------------------------------+----------------------+------------------------+---------------------------------------------------+

 

[] 

Arrow settings can be changed using HeadDecoratorShape and TailDecoratorShape properties. Both head and tail decorators consist of the same set of properties that allow one to customize the settings as required.

[] 

Types of decorator shapes

[] 

[·      ]Arrow

[·      ]Diamond

[·      ]Circle

**[]** 

The following code shows the setting of these properties.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [LineConnector][ l1 = [new] [LineConnector]();] |
|                                                                                                                                                                                      |
| [l1.HeadNode = n1;]                                                                                                                              |
|                                                                                                                                                                                      |
| [l1.TailNode = n2;]                                                                                                                              |
|                                                                                                                                                                                      |
| [l1.ConnectorType = [ConnectorType].Bezier;]                                                                             |
|                                                                                                                                                                                      |
| [l1.HeadDecoratorShape = [DecoratorShape].Diamond;]                                                                      |
|                                                                                                                                                                                      |
| [l1.TailDecoratorShape = [DecoratorShape].Circle;]                                                                       |
|                                                                                                                                                                                      |
| [diagramModel.Connections.Add(l1); ]                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [Dim][ l1 [As] [New] [LineConnector]()] |
|                                                                                                                                                                                                |
| [l1.HeadNode = n1]                                                                                                                                         |
|                                                                                                                                                                                                |
| [l1.TailNode = n2]                                                                                                                                         |
|                                                                                                                                                                                                |
| [l1.ConnectorType = ConnectorType.Bezier]                                                                                                                  |
|                                                                                                                                                                                                |
| [l1.HeadDecoratorShape = DecoratorShape.Diamond]                                                                                                           |
|                                                                                                                                                                                                |
| [l1.TailDecoratorShape = DecoratorShape.Circle]                                                                                                            |
|                                                                                                                                                                                                |
| [diagramModel.Connections.Add(l1)][]                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 65: Decorator Shapes**[]**

 

[]{#p42} 

[]{#related-topics}

