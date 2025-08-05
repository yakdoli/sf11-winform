---
title: addingthroughc5.md
original_path: WinForms_Docs/99_Uncategorized/addingthroughc5.md
created_at: 2025-08-05
---






#### Adding through C# {#adding-through-c style="tab-stops: 0pt"}

Follow the below steps to add the Carousel control by using VisualStudio.

1.   Open Visual Studio. On the File menu, select **New -\> Project**. This opens the New Project Dialog box.

 

{border="0"}

Figure 105: Open New Project

 

2.   In the Project Dialog window, select **WPF Application** and in the name field type the name of the project, and then click **OK**.

 

3.   Add the following reference with the sample project.

**Syncfusion.Shared.Wpf.dll**

 

4.   Click and open the C# file and add the Carousel control to your application.

[] 

The below code shows how the Carousel control can be added to an application:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                             |
|                                                                                                                                              |
| []                                                                                                       |
|                                                                                                                                              |
| [Carousel][ carousel = [new] [Carousel]();\ |
| carousel.Items.Add([new] [CarouselItem]() { Content = [\"1\"] });\      |
| carousel.Items.Add([new] [CarouselItem]() { Content = [\"2\"] });\      |
| carousel.Items.Add([new] [CarouselItem]() { Content = [\"3\"] });\      |
| carousel.Items.Add([new] [CarouselItem]() { Content = [\"4\"] });\      |
| carousel.Items.Add([new] [CarouselItem]() { Content = [\"5\"] });\      |
| [this].LayoutRoot.Children.Add(carousel);]                                          |
|                                                                                                                                              |
| []                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

