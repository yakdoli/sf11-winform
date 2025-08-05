---
title: howtogenerateathumbnailimageofadiagram.md
original_path: WinForms_Docs/04_Controls/Diagram/howtogenerateathumbnailimageofadiagram.md
created_at: 2025-08-05
---








  









## How To Generate a Thumbnail Image Of a Diagram {#how-to-generate-a-thumbnail-image-of-a-diagram style="tab-stops: 0pt"}

[] 

To display a thumbnail image of the diagram, follow the below given steps.

 

1.   Generate a Bitmap image of the diagram.

 

2.   Use the **GetThumbnailImage** method of the **Image** class to generate a thumbnail, and set it as the image of the picture box in which you want to display the thumbnail.

[] 

The following code illustrates this.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                      |
| [public][ [bool] ThumbnailCallback()]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [return][ [false];]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| [//Generate Thumbnail and set it to be image of the PictureBox]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                      |
| [Image][.[GetThumbnailImageAbort] myCallback = [new] [Image].[GetThumbnailImageAbort](ThumbnailCallback); ] |
|                                                                                                                                                                                                                                                                                      |
| [this][.pictureBox1.Image = ([Bitmap]) diagramimage.GetThumbnailImage(150,75,myCallback, [IntPtr].Zero);]                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [Public][ [Function] ThumbnailCallback() [As] [Boolean]]                                |
|                                                                                                                                                                                                                                             |
| [Return][ [False]]                                                                                                                |
|                                                                                                                                                                                                                                             |
| [End][ [Function]]                                                                                                                |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                             |
| [\'Generate Thumbnail and set it to be image of the PictureBox]                                                                                                                           |
|                                                                                                                                                                                                                                             |
| [Dim][ myCallback [As] Image.GetThumbnailImageAbort = [New] Image.GetThumbnailImageAbort(ThumbnailCallback)] |
|                                                                                                                                                                                                                                             |
| [Me][.pictureBox1.Image = [CType](diagramimage.GetThumbnailImage(150,75,myCallback, IntPtr.Zero), Bitmap)]                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p85} 

[]{#related-topics}

