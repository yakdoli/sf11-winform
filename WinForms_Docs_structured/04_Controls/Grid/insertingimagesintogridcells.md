---
title: insertingimagesintogridcells.md
original_path: WinForms_Docs/04_Controls/Grid/insertingimagesintogridcells.md
created_at: 2025-08-05
---






#### Inserting Images into Grid Cells {#inserting-images-into-grid-cells style="tab-stops: 0pt"}

Grid provides inherent support to add images into grid cells. There are two possible ways to achieve this.

 

[·      ]Style.Image property---Used to insert an image alongside the text in the grid cells.

[·      ]Style.ImageList property---It serves the same purpose as the Image property, points to a collection of images and lets you share the same ImageSource for a group of cells. Once you have selected the images by using the ImageList property, you must set the ImageIndex property for individual cells, to indicate the specific image (from the ImageList) to be inserted into the cell.

**[]** 


{border="0"}Note: If you use both Image and ImageList properties, then the most recent property applied will be considered.


 

The following code example illustrates how to use these properties.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                               |
| [// Using Vector Images.]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                               |
| [ResourceDictionary][ dictionary = [new] [ResourceDictionary]();]                                                                        |
|                                                                                                                                                                                                                                                                               |
| [dictionary.Source = [new] [Uri](vectorImgSrcUri, [UriKind].RelativeOrAbsolute);]                                                                                    |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [ObservableCollection][\<[Image]\> imgList = [new] [ObservableCollection]\<[Image]\>();] |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [// Loading ImageList.]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                               |
| [foreach][ ([string] key [in] dictionary.Keys)]                                                                                                |
|                                                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [   [Image] img = [new] [Image]();]                                                                                                                                  |
|                                                                                                                                                                                                                                                                               |
| [   img.Source = ([DrawingImage])dictionary\[[\"Technology\"]\];]                                                                                                                         |
|                                                                                                                                                                                                                                                                               |
| [   imgList.Add(img);   ]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [// Setting ImageList.]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                               |
| [grid.Model.TableStyle.ImageList = imgList;]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                               |
| [// Image property setting.]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                               |
| [grid.Model\[0, 2\].Text = [\"Technology\"];]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                               |
| [Image][ img = [new] [Image]();]                                                                                                         |
|                                                                                                                                                                                                                                                                               |
| [img.Source = [new] [BitmapImage]([new] [Uri]([\"Technology.png\"], [UriKind].Absolute));]      |
|                                                                                                                                                                                                                                                                               |
| [grid.Model\[0, 2\].Image = img;]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [// Setting ImageIndex.]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                               |
| [grid.Model\[1, 2\].Text = [\"Business\"];]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [grid.Model\[1, 2\].ImageIndex = 0;]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                               |
| [grid.Model\[2, 2\].Text = [\"Software\"];]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [grid.Model\[2, 2\].ImageIndex = 1;]                                                                                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following output is generated using the code above.

 

{border="0"}

Figure 44: Text Image Cell

 

 

[]{#related-topics}

