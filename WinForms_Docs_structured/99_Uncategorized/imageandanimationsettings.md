---
title: imageandanimationsettings.md
original_path: WinForms_Docs/99_Uncategorized/imageandanimationsettings.md
created_at: 2025-08-05
---






##### Image and Animation Settings {#image-and-animation-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This section demonstrates how to set a splash image and how to display it with animation.

[] 

**Splash Image**

[] 

The splash image can be displayed by setting the property given below.

[] 


  ------------------------ --------------------------------------------------------------------------
  SplashControl Property   Description
  SplashImage              The image for displaying as the background of the default splash screen.
  ------------------------ --------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [this][.splashControl1.SplashImage = ((System.Drawing.[Image])(resources.GetObject([\"splashControl1.SplashImage\"])));] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [Me][.splashControl1.SplashImage = [CType]((resources.GetObject([\"splashControl1.SplashImage\"])), System.Drawing.Image)] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 988: Splash Image

[] 

Animation

[] 

When animation is set for the splash image, by default, the splash image will be drawn from left to right.

[] 


  ------------------------ --------------------------------------------------------------------------------------
  SplashControl Property   Description
  ShowAnimation            Indicates whether the splash image should occur on the screen in an animated manner.
  ShowAsTopMost            Specifies if the splash screen is to be displayed as the topmost window.
  SplashImage              The image for displaying as the background of the default splash screen.
  TransparentColor         Gets / sets the color to be used to make the splash image transparent.
  ------------------------ --------------------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [this][.splashControl1.ShowAnimation = [true];]                                                                                                 |
|                                                                                                                                                                                                                                                           |
| [this][.splashControl1.ShowAsTopMost = [false];]                                                                                                |
|                                                                                                                                                                                                                                                           |
| [this][.splashControl1.SplashImage = ((System.Drawing.[Image])(resources.GetObject([\"splashControl1.SplashImage\"])));] |
|                                                                                                                                                                                                                                                           |
| [this][.splashControl1.TransparentColor = System.Drawing.[Color].White;]                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [Me][.splashControl1.ShowAnimation = [True]]                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [Me][.splashControl1.ShowAsTopMost = [False]]                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [Me][.splashControl1.SplashImage = [CType]((resources.GetObject([\"splashControl1.SplashImage\"])), System.Drawing.Image)] |
|                                                                                                                                                                                                                                                             |
| [Me][.splashControl1.TransparentColor = System.Drawing.Color.White]                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

