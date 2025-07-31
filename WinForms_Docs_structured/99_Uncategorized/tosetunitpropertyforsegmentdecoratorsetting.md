---
title: tosetunitpropertyforsegmentdecoratorsetting.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\tosetunitpropertyforsegmentdecoratorsetting.md
created_at: 2025-07-03
---






##### To set unit property for Segment decorator setting {#to-set-unit-property-for-segment-decorator-setting style="tab-stops: 0pt"}

LineUnit property is used to access the following:

 

[·      ]**AbsoluteFraction:** the fraction values (double value between 0 to 1) entered are considered from the particular segment's StartPointPosition

[·      ]**RelativeFraction:**  the fraction values (double value between 0 to 1) entered are considered from the previous DecoratorShape position

[·      ]**AbsoluteValue:** the pixel values (double) entered are considered from the particular segment's StartPointPosition

[·      ]**RelativeValue:** the pixel values (double) entered are considered from the previous DecoratorShape position

 

Through XAML

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][syncfusion][:][LineConnector.SegmentDecoratorSettings][\>][]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [   \<][syncfusion][:][SegmentDecoratorSettings][ Unit][=\"RelativeFraction\"\>]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [      \<][syncfusion][:][SegmentDecoratorSettings.SegmentDecorator][\>][]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [         ][\<][syncfusion][:][CollectionExt][\>]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [          ][\<][syncfusion][:][SegmentDecorator][ DecoratorOffset][=\"0.2\"][ DecoratorShape][=\"Arrow\" /\>]  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [          ][\<][syncfusion][:][SegmentDecorator][ DecoratorOffset][=\"0.5\"][ DecoratorShape][=\"Diamond\"/\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [         ][\</][syncfusion][:][CollectionExt][\>]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [      \</][syncfusion][:][SegmentDecoratorSettings.SegmentDecorator][\>][ ][]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [     ][\</][syncfusion][:][SegmentDecoratorSettings][\>][]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\</][syncfusion][:][LineConnector.SegmentDecoratorSettings][\>]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Through code behind \[c#\]

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                             |
|                                                                                                                                                                                                              |
| [           SegmentDecorator][ decorator1=[new] [SegmentDecorator] ();] |
|                                                                                                                                                                                                              |
| [            decorator1.DecoratorOffset=0.2;]                                                                                                                            |
|                                                                                                                                                                                                              |
| [            decorator1.DecoratorShape=Syncfusion.Windows.Diagram.[DecoratorShape].Arrow;]                                                       |
|                                                                                                                                                                                                              |
| [              [SegmentDecorator] decorator2=[new] [SegmentDecorator] ();]                          |
|                                                                                                                                                                                                              |
| [            decorator2.DecoratorOffset=0.5;]                                                                                                                            |
|                                                                                                                                                                                                              |
| [            decorator2.DecoratorShape=Syncfusion.Windows.Diagram.[DecoratorShape].Diamond;]                                                     |
|                                                                                                                                                                                                              |
| [            ]                                                                                                                                                           |
|                                                                                                                                                                                                              |
| [            [CollectionExt] collection=[new] [CollectionExt] ();]                                  |
|                                                                                                                                                                                                              |
| [            collection.Add(decorator1);]                                                                                                                                |
|                                                                                                                                                                                                              |
| [            collection.Add(decorator2);]                                                                                                                                |
|                                                                                                                                                                                                              |
| [            ]                                                                                                                                                           |
|                                                                                                                                                                                                              |
| [            [SegmentDecoratorSettings] decoratorsettings = [new] [SegmentDecoratorSettings]();]    |
|                                                                                                                                                                                                              |
| [            decoratorsettings.Unit = [LineUnit].RelativeFraction;]                                                                              |
|                                                                                                                                                                                                              |
| [            decoratorsettings.SegmentDecorator = collection;]                                                                                                           |
|                                                                                                                                                                                                              |
| [            line.SegmentDecoratorSettings = decoratorsettings;][]                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

