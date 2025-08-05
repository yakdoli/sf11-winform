---
title: slideshoweffects.md
original_path: WinForms_Docs/99_Uncategorized/slideshoweffects.md
created_at: 2025-08-05
---






##### Slideshow Effects {#slideshow-effects style="tab-stops: 0pt"}

[] 

The slide show can be created by setting **RotationType** to **SlideShow**. For the slide shows, transition effects can be applied when an item is shown or hidden by setting the **HideEffect** and **ShowEffect** properties to the style transition options.

[] 


+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
|                                   |                                                                                                                                               |
|                                   |                                                                                                                                               |
| Property                          | Description                                                                                                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| HideEffect                        | Specifies the transition slide effect to be used while hiding the slides. Default value is \'None\'. The options included are as follows:     |
|                                   |                                                                                                                                               |
|                                   | [·      ]Fade                                                                                                    |
|                                   |                                                                                                                                               |
|                                   | [·      ]Dissolve                                                                                                |
|                                   |                                                                                                                                               |
|                                   | [·      ]GradientWipe                                                                                            |
|                                   |                                                                                                                                               |
|                                   | [·      ]Pixelate                                                                                                |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ShowEffect                        | Specifies the transition slide effect to be used while displaying the slides. Default value is \'None\'. The options included are as follows: |
|                                   |                                                                                                                                               |
|                                   | [·      ]Fade                                                                                                    |
|                                   |                                                                                                                                               |
|                                   | [·      ]Dissolve                                                                                                |
|                                   |                                                                                                                                               |
|                                   | [·      ]GradientWipe                                                                                            |
|                                   |                                                                                                                                               |
|                                   | [·      ]Pixelate                                                                                                |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+


[] 

If we specify both **HideEffect** and **ShowEffect** properties as **None**, then the slides will be displayed one by one without any style transitions.

The time interval of hide effect and show effect can be specified using the **HideEffectDuration** and **ShowEffectDuration** properties. These two properties will accept the time interval as milliseconds. By default the duration will be set to **1000** **milliseconds**.

[] 


  -------------------- ----------------------------------------
  Property             Description
  HideEffectDuration   Specifies the duration of hide effect.
  ShowEffectDuration   Specifies the duration of show effect.
  -------------------- ----------------------------------------


[] 

The below screenshot displays the Pixelate and Dissolve slide effects when the image is shown and hidden respectively.

[] 

{border="0"}{border="0"}

**[]** 

Figure 347: Pixelate             Figure 348: Dissolve

**[]** 

These effects can be set programmatically as follows.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\] ]**                                                          |
|                                                                                                                                          |
| []                                                                      |
|                                                                                                                                          |
| [Rotator1.HideEffect=Syncfusion.Web.UI.WebControls.Tools.SlideShowEffects.Dissolve;] |
|                                                                                                                                          |
| [Rotator1.ShowEffect=Syncfusion.Web.UI.WebControls.Tools.SlideShowEffects.Pixelate;] |
+------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\] ]**                                                                                                                                      |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                  |
|                                                                                                                                                                                                                      |
| [Private][ Rotator1.HideEffect = Syncfusion.Web.UI.WebControls.Tools.SlideShowEffects.Dissolve] |
|                                                                                                                                                                                                                      |
| [Private][ Rotator1.ShowEffect = Syncfusion.Web.UI.WebControls.Tools.SlideShowEffects.Pixelate] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


[{border="0"}]Note: This slideshow feature requires Microsoft® Internet Explorer 5.5 or later.


 

[]{#related-topics}

