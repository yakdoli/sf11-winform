---
title: howtoanimatethenodesinthediagram.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Diagram\howtoanimatethenodesinthediagram.md
created_at: 2025-07-03
---








  









### How to animate the nodes in the diagram? {#how-to-animate-the-nodes-in-the-diagram style="tab-stops: 0pt"}

[] 

We can perform many kinds of animations on nodes by using the double animation. Rotation and Translation are some of the basic operations performed on the nodes. We can use double animation to perform these operations on the node in a specific pattern.

 

To rotate a node, the following code can be used:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                    |
| [Node][ node = [new] [Node]([Guid].NewGuid(), [\"Node\"]);]   |
|                                                                                                                                                                                                                                                    |
| [            node.Shape = [Shapes].FlowChart_Decision;]                                                                                                                                |
|                                                                                                                                                                                                                                                    |
| [            node.Level = 0;]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                    |
| [            node.Width = 150;]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                    |
| [            node.Height = 50;]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                    |
| [            node.OffsetX = 40;]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                    |
| [            node.OffsetY = 100;]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                    |
| [            node.Content = [\"Node\"];]                                                                                                                                               |
|                                                                                                                                                                                                                                                    |
| [            node.Level = 0;]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                    |
| [DoubleAnimation][ nodeanimation = [new] [DoubleAnimation]();]                                                |
|                                                                                                                                                                                                                                                    |
| [            nodeanimation.From = 0;]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                    |
| [            nodeanimation.To = 360;]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                    |
| [            nodeanimation.Duration = [new] [Duration]([new] [TimeSpan](0, 0, 0, 0, 500));]                          |
|                                                                                                                                                                                                                                                    |
| [            nodeanimation.RepeatBehavior = [new] [RepeatBehavior](5);]                                                                                           |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [            [RotateTransform] rt = [new] [RotateTransform]();]                                                                           |
|                                                                                                                                                                                                                                                    |
| [            node.RenderTransform = rt;]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| [            node.RenderTransformOrigin = [new] [Point](.5, .5);]                                                                                                 |
|                                                                                                                                                                                                                                                    |
| [            [Storyboard].SetTarget(nodeanimation, rt);]                                                                                                                               |
|                                                                                                                                                                                                                                                    |
| [            [Storyboard].SetTargetProperty(nodeanimation, [new] [PropertyPath]([\"(RotateTransform.Angle)\"]));] |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [            [Storyboard] storyBoard = [new] [Storyboard]();]                                                                             |
|                                                                                                                                                                                                                                                    |
| [            storyBoard.Children.Add(nodeanimation);]                                                                                                                                                          |
|                                                                                                                                                                                                                                                    |
| [            storyBoard.Begin();]                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                         |
| [    Dim][ node [As] [New] [Node]([Guid].NewGuid(), [\"Node\"])] |
|                                                                                                                                                                                                                                                                         |
| [                  node.Shape = Shapes.FlowChart_Decision]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| [                  node.Level = 0]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [                  node.Width = 150]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                         |
| [                  node.Height = 50]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                         |
| [                  node.OffsetX = 40]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                         |
| [                  node.OffsetY = 100]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| [                  node.Content = \"Node\"]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                         |
| [                  node.Level = 0]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [    [Dim] nodeanimation [As] [New] [DoubleAnimation]()]                                                                                     |
|                                                                                                                                                                                                                                                                         |
| [                  nodeanimation.From = 0]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| [                  nodeanimation.To = 360]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| [                  nodeanimation.Duration = [New] Duration(New TimeSpan(0, 0, 0, 0, 500))]                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| [                  nodeanimation.RepeatBehavior = [New] RepeatBehavior(5)]                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [    [Dim] rt [As] [New] [RotateTransform]()]                                                                                                |
|                                                                                                                                                                                                                                                                         |
| [                  node.RenderTransform = rt]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                         |
| [                  node.RenderTransformOrigin = [New] Point(.5,.5)]                                                                                                                                            |
|                                                                                                                                                                                                                                                                         |
| [                  Storyboard.SetTarget(nodeanimation, rt)]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                         |
| [                  Storyboard.SetTargetProperty(nodeanimation, [New] PropertyPath(\"(RotateTransform.Angle)\"))]                                                                                               |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [    [Dim] storyBoard [As] [New] [Storyboard]()]                                                                                             |
|                                                                                                                                                                                                                                                                         |
| [                  storyBoard.Children.Add(nodeanimation)]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| [                  storyBoard.Begin()][]                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

To translate a node with respect to the x-axis, the TranslateTransform can be applied.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [DoubleAnimation][ nodeanimation = [new] [DoubleAnimation]();]                       |
|                                                                                                                                                                                                                           |
| [            nodeanimation.From = 40;]                                                                                                                                                |
|                                                                                                                                                                                                                           |
| [            nodeanimation.To = 400;]                                                                                                                                                 |
|                                                                                                                                                                                                                           |
| [            nodeanimation.Duration = [new] [Duration]([new] [TimeSpan](0, 0, 0, 0, 500));] |
|                                                                                                                                                                                                                           |
| [            nodeanimation.RepeatBehavior = [new] [RepeatBehavior](5);]                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                              |
|                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                             |
| [Dim][ nodeanimation [As] [New] [DoubleAnimation]()] |
|                                                                                                                                                                                                             |
| [                  nodeanimation.From = 40]                                                                                                                             |
|                                                                                                                                                                                                             |
| [                  nodeanimation.To = 400]                                                                                                                              |
|                                                                                                                                                                                                             |
| [                  nodeanimation.Duration = [New] Duration(New TimeSpan(0, 0, 0, 0, 500))]                                                         |
|                                                                                                                                                                                                             |
| [                  nodeanimation.RepeatBehavior = [New] RepeatBehavior(5)]                                                                         |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Once we have created the double animation, we can then apply it to the node, which we want to translate in the following way:

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [Node][ node = [new] [Node]([Guid].NewGuid(), [\"Node\"]);]  |
|                                                                                                                                                                                                                                                   |
| [            node.Shape = [Shapes].FlowChart_Decision;]                                                                                                                               |
|                                                                                                                                                                                                                                                   |
| [            node.Level = 0;]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                   |
| [            node.Width = 150;]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                   |
| [            node.Height = 50;]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                   |
| [            node.OffsetX = 40;]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [            node.OffsetY = 100;]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                   |
| [            node.Content = [\"Node\"];]                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [            node.Level = 0;]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                   |
| [            [DoubleAnimation] nodeanimation = [new] [DoubleAnimation]();]                                                               |
|                                                                                                                                                                                                                                                   |
| [            nodeanimation.From = 40;]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                   |
| [            nodeanimation.To = 400;]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                   |
| [            nodeanimation.Duration = [new] [Duration]([new] [TimeSpan](0, 0, 0, 0, 500));]                         |
|                                                                                                                                                                                                                                                   |
| [            nodeanimation.RepeatBehavior = [new] [RepeatBehavior](5);]                                                                                          |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [            [TranslateTransform] tt = [new] [TranslateTransform]();]                                                                    |
|                                                                                                                                                                                                                                                   |
| [            node.RenderTransform = tt;]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [            node.RenderTransformOrigin = [new] [Point](.5, .5);]                                                                                                |
|                                                                                                                                                                                                                                                   |
| [            [Storyboard].SetTarget(nodeanimation, tt);]                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [            [Storyboard].SetTargetProperty(nodeanimation, [new] [PropertyPath]([\"(TranslateTransform.X)\"]));] |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [            [Storyboard] storyBoard = [new] [Storyboard]();]                                                                            |
|                                                                                                                                                                                                                                                   |
| [            storyBoard.Children.Add(nodeanimation);]                                                                                                                                                         |
|                                                                                                                                                                                                                                                   |
| [            storyBoard.Begin();]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                         |
| [    Dim][ node [As] [New] [Node]([Guid].NewGuid(), [\"Node\"])] |
|                                                                                                                                                                                                                                                                         |
| [                  node.Shape = Shapes.FlowChart_Decision]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| [                  node.Level = 0]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [                  node.Width = 150]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                         |
| [                  node.Height = 50]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                         |
| [                  node.OffsetX = 40]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                         |
| [                  node.OffsetY = 100]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| [                  node.Content = \"Node\"]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                         |
| [                  node.Level = 0]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [    ]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| [Dim][ nodeanimation [As] [New] [DoubleAnimation]()]                                                             |
|                                                                                                                                                                                                                                                                         |
| [                  nodeanimation.From = 40]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                         |
| [                  nodeanimation.To = 400]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| [                  nodeanimation.Duration = [New] Duration(New TimeSpan(0, 0, 0, 0, 500))]                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| [                  nodeanimation.RepeatBehavior = [New] RepeatBehavior(5)]                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [    [Dim] tt [As] [New] [TranslateTransform]()]                                                                                             |
|                                                                                                                                                                                                                                                                         |
| [                  node.RenderTransform = tt]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                         |
| [                  node.RenderTransformOrigin = [New] Point(.5,.5)]                                                                                                                                            |
|                                                                                                                                                                                                                                                                         |
| [                  Storyboard.SetTarget(nodeanimation, tt)]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                         |
| [                  Storyboard.SetTargetProperty(nodeanimation, [New] PropertyPath(\"(TranslateTransform.X)\"))]                                                                                                |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [    [Dim] storyBoard [As] [New] [Storyboard]()]                                                                                             |
|                                                                                                                                                                                                                                                                         |
| [                  storyBoard.Children.Add(nodeanimation)]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| [                  storyBoard.Begin()]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

 

 

 

 

 

 

 

 

 

 

                                                                         

[]{#related-topics}

