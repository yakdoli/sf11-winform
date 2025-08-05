---
title: animatethedodesinthediagram.md
original_path: WinForms_Docs/04_Controls/Diagram/animatethedodesinthediagram.md
created_at: 2025-08-05
---








  









### Animate the Dodes in the Diagram {#animate-the-dodes-in-the-diagram style="tab-stops: 0pt"}

You can perform many kinds of animations on nodes by using the double animation. Rotation and Translation are some of the basic operations performed on the nodes. You can use double animation to perform these operations on the node in a specific pattern.

[] 

To rotate a node, the following code can be used.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                |
|                                                                                                                                                                                                               |
| []                                                                                                                                                          |
|                                                                                                                                                                                                               |
| [DoubleAnimation][ nodeanimation = [new] [DoubleAnimation]();]           |
|                                                                                                                                                                                                               |
| [nodeanimation.From = 0;]                                                                                                                                                 |
|                                                                                                                                                                                                               |
| [nodeanimation.To = 360;]                                                                                                                                                 |
|                                                                                                                                                                                                               |
| [nodeanimation.Duration = [new] [Duration]([new] [TimeSpan](0, 0, 0, 0, 500));] |
|                                                                                                                                                                                                               |
| [nodeanimation.RepeatBehavior = [new] [RepeatBehavior](15);]                                                                 |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [RotateTransform][ rt = [new] [RotateTransform]();]                      |
|                                                                                                                                                                                                               |
| [nodeObj.RenderTransform = rt;]                                                                                                                                           |
|                                                                                                                                                                                                               |
| [nodeObj.RenderTransformOrigin = [new] [Point](.5, .5);]                                                                     |
|                                                                                                                                                                                                               |
| [rt.BeginAnimation([RotateTransform].AngleProperty, nodeanimation);]                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                   |
|                                                                                                                                                                                                  |
| []                                                                                                                                             |
|                                                                                                                                                                                                  |
| [Dim][ nodeanimation [As] [New] DoubleAnimation()]                |
|                                                                                                                                                                                                  |
| [nodeanimation.From = 0]                                                                                                                                     |
|                                                                                                                                                                                                  |
| [nodeanimation.To = 360]                                                                                                                                     |
|                                                                                                                                                                                                  |
| [nodeanimation.Duration = [New] Duration(New TimeSpan(0, 0, 0, 0, 500))]                                                                |
|                                                                                                                                                                                                  |
| [nodeanimation.RepeatBehavior = [New] RepeatBehavior(15)]                                                                               |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [Dim][ rt [As] [New] [RotateTransform]()] |
|                                                                                                                                                                                                  |
| [nodeObj.RenderTransform = rt]                                                                                                                               |
|                                                                                                                                                                                                  |
| [nodeObj.RenderTransformOrigin = [New] Point(.5,.5)]                                                                                    |
|                                                                                                                                                                                                  |
| [rt.BeginAnimation(RotateTransform.AngleProperty, nodeanimation)][]                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

To translate a node with respect to the x-axis, the TranslateTransform can be applied.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                |
|                                                                                                                                                                                                               |
| []                                                                                                                                                          |
|                                                                                                                                                                                                               |
| [DoubleAnimation][ nodeanimation = [new] [DoubleAnimation]();]           |
|                                                                                                                                                                                                               |
| [nodeanimation.From = 500;]                                                                                                                                               |
|                                                                                                                                                                                                               |
| [nodeanimation.To = 0;]                                                                                                                                                   |
|                                                                                                                                                                                                               |
| [nodeanimation.Duration = [new] [Duration]([new] [TimeSpan](0, 0, 0, 0, 500));] |
|                                                                                                                                                                                                               |
| [nodeanimation.RepeatBehavior = [new] [RepeatBehavior](1);]                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                    |
|                                                                                                                                                                                   |
| []                                                                                                                              |
|                                                                                                                                                                                   |
| [Dim][ nodeanimation [As] [New] DoubleAnimation()] |
|                                                                                                                                                                                   |
| [nodeanimation.From = 500]                                                                                                                    |
|                                                                                                                                                                                   |
| [nodeanimation.To = 0]                                                                                                                        |
|                                                                                                                                                                                   |
| [nodeanimation.Duration = [New] Duration(New TimeSpan(0, 0, 0, 0, 500))]                                                 |
|                                                                                                                                                                                   |
| [nodeanimation.RepeatBehavior = [New] RepeatBehavior(1)][]                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Once you have created the double animation, you can then apply it to the node which we want to translate in the following way.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                |
|                                                                                                                                                                                                               |
| []                                                                                                                                                          |
|                                                                                                                                                                                                               |
| [DoubleAnimation][ nodeanimation = [new] [DoubleAnimation]();]           |
|                                                                                                                                                                                                               |
| [nodeanimation.From = 500;]                                                                                                                                               |
|                                                                                                                                                                                                               |
| [nodeanimation.To = 0;]                                                                                                                                                   |
|                                                                                                                                                                                                               |
| [nodeanimation.Duration = [new] [Duration]([new] [TimeSpan](0, 0, 0, 0, 500));] |
|                                                                                                                                                                                                               |
| [nodeanimation.RepeatBehavior = [new] [RepeatBehavior](1);]                                                                  |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [TranslateTransform][ rt = [new] [TranslateTransform]();]                |
|                                                                                                                                                                                                               |
| [nodeObj.RenderTransform = rt;]                                                                                                                                           |
|                                                                                                                                                                                                               |
| [rt.BeginAnimation([TranslateTransform].XProperty, nodeanimation);]                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                      |
|                                                                                                                                                                                                     |
| []                                                                                                                                                |
|                                                                                                                                                                                                     |
| [Dim][ nodeanimation [As] [New] DoubleAnimation()]                   |
|                                                                                                                                                                                                     |
| [nodeanimation.From = 500]                                                                                                                                      |
|                                                                                                                                                                                                     |
| [nodeanimation.To = 0]                                                                                                                                          |
|                                                                                                                                                                                                     |
| [nodeanimation.Duration = [New] Duration(New TimeSpan(0, 0, 0, 0, 500))]                                                                   |
|                                                                                                                                                                                                     |
| [nodeanimation.RepeatBehavior = [New] RepeatBehavior(1)]                                                                                   |
|                                                                                                                                                                                                     |
| []                                                                                                                                                              |
|                                                                                                                                                                                                     |
| [Dim][ rt [As] [New] [TranslateTransform]()] |
|                                                                                                                                                                                                     |
| [nodeObj.RenderTransform = rt]                                                                                                                                  |
|                                                                                                                                                                                                     |
| [rt.BeginAnimation(TranslateTransform.XProperty, nodeanimation)][]                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

