---
title: 3dannotation.md
original_path: WinForms_Docs/99_Uncategorized/3dannotation.md
created_at: 2025-08-05
---






##### 3D Annotation {#d-annotation style="tab-stops: 0pt"}

 

3D Annotations are the means by which 3D artwork is represented in a PDF document. Essential PDF can embed the 3D files (u3d) in PDF files. It provides a way to interact with the user by using the mouse and keyboard.

 

You can control the annotation with the help of the following classes.

 

[·      ]Pdf3DAnnotation

[·      ]Pdf3DView

[·      ]Pdf3DProjection

[·      ]Pdf3DActivation

[·      ]Pdf3DBackground

[·      ]Pdf3DRenderMode

[·      ]Pdf3DLighting

[·      ]Pdf3DCrossSection

 

**Pdf3DAnnotation**

 

Pdf3DAnnotation specifies parameters to be applied to the virtual camera associated with a 3D annotation. These parameters include orientation and position of the camera, details regarding the projection of camera coordinates onto the target coordinate system of the annotation, and a description of the background on which the artwork is to be drawn.

 

The following code example illustrates how to embed a 3D file.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                           |
| [// Pdf 3D Annotation]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                           |
| [Pdf3DAnnotation][ annotation = [new]  [Pdf3DAnnotation]([new] [RectangleF](10, 270, 270, 150), [@\"..\\..\\Data\\box.u3d\"]);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [\' Pdf 3D Annotation]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ annotation [As] Syncfusion.Pdf.Interactive.Pdf3DAnnotation = [New] Syncfusion.Pdf.Interactive.Pdf3DAnnotation([New] RectangleF(10, 270, 270, 150), [\"..\\..\\Data\\box.u3d\"])] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Pdf3DView**

 

Pdf3DView class specifies parameters to be applied to the virtual camera associated with a 3D annotation. These parameters include orientation and position of the camera, details regarding the projection of camera coordinates onto the target coordinate system of the annotation, and a description of the background on which the artwork is to be drawn.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                |
| []                                                                                                                         |
|                                                                                                                                                                                |
| [// Pdf 3D View]                                                                                                             |
|                                                                                                                                                                                |
| [Pdf3DView][ view = [new] [Pdf3DView]();] |
|                                                                                                                                                                                |
| [view.ExternalName = [\"Default View\"];            ]                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                                      |
| [\' Pdf 3D View]                                                                                                                                                                   |
|                                                                                                                                                                                                                                      |
| [Dim][ view [As] Syncfusion.Pdf.Interactive.Pdf3DView = [New] Syncfusion.Pdf.Interactive.Pdf3DView()] |
|                                                                                                                                                                                                                                      |
| [view.ExternalName = [\"Default View\"]]                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Pdf3DProjection**

 

Pdf3DProjection defines the mapping of 3D camera coordinates onto the target coordinate system of the annotation. Using this class, you can specify the type of Projection which determines how objects are projected onto the near plane and scaled. The possible values are **Orthographic** projection and **Perspective** projection.

 

Pdf3DProjection supports both near and far clipping. This type of clipping defines a near plane and far plane. Objects or parts of objects that are beyond the far plane or closer to the camera than the near plane, are not drawn.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                 |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [Pdf3DView][ view = [new] [Pdf3DView]();]                   |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [Pdf3DProjection][ projection = [new] [Pdf3DProjection]();] |
|                                                                                                                                                                                                  |
| [projection.ProjectionType = [Pdf3DProjectionType].Perspective;]                                                                     |
|                                                                                                                                                                                                  |
| [projection.FieldOfView = 10;]                                                                                                                               |
|                                                                                                                                                                                                  |
| [projection.ClipStyle = [Pdf3DProjectionClipStyle].ExplicitNearFar;]                                                                 |
|                                                                                                                                                                                                  |
| [projection.NearClipDistance = 10;]                                                                                                                          |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [view.Projection = projection;]                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [Dim][ view [As] Syncfusion.Pdf.Interactive.Pdf3DView = [New] Syncfusion.Pdf.Interactive.Pdf3DView()]                   |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [Dim][ projection [As] Syncfusion.Pdf.Interactive.Pdf3DProjection = [New] Syncfusion.Pdf.Interactive.Pdf3DProjection()] |
|                                                                                                                                                                                                                                                        |
| [projection.ProjectionType = Pdf3DProjectionType.Perspective]                                                                                                                                                      |
|                                                                                                                                                                                                                                                        |
| [projection.FieldOfView = 10]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                        |
| [projection.ClipStyle = Pdf3DProjectionClipStyle.ExplicitNearFar]                                                                                                                                                  |
|                                                                                                                                                                                                                                                        |
| [projection.NearClipDistance = 10]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [view.Projection = projection]                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: You can set the near or far distance by using the NearClipDistance property. If you want to set the clipping distance explicitly, you have to set the ClipStyle property to ExplicitNearFar.


 

Pdf3DActivation

 

Pdf3DActivation class determines when a 3D annotation is active or when it is inactive. 3D artwork is activated in one of the following three states with the help of Pdf3DActivationMode class.

[] 

[·      ]**ExplicitActivation**-Initial state of the annotation is deactivated. If you want to activate the annotation by clicking it, then you can use the explicit annotation.

[·      ]**PageOpen**-Annotation is activated while opening the pdf document page

[·      ]**PageVisible**-Annotation is activated when the page is visible

 

You can show or hide the toolbar by using the **ShowToolbar** property.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                 |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [// Creating instance for Pdf3DActivation class]                                                                                               |
|                                                                                                                                                                                                  |
| [Pdf3DActivation][ activation = [new] [Pdf3DActivation]();] |
|                                                                                                                                                                                                  |
| []                                                                                                                                             |
|                                                                                                                                                                                                  |
| [// Setting Activation Mode as PageVisible]                                                                                                    |
|                                                                                                                                                                                                  |
| [activation.ActivationMode = [Pdf3DActivationMode].PageVisible;]                                                                     |
|                                                                                                                                                                                                  |
| []                                                                                                                                             |
|                                                                                                                                                                                                  |
| [// Showing the Toolbar]                                                                                                                       |
|                                                                                                                                                                                                  |
| [activation.ShowToolbar = [true];]                                                                                                      |
|                                                                                                                                                                                                  |
| []                                                                                                                                             |
|                                                                                                                                                                                                  |
| [// Setting Deactivation Mode as PageVisible]                                                                                                  |
|                                                                                                                                                                                                  |
| [activation.DeactivationMode = [Pdf3DDeactivationMode].ExplicitDeactivation;]                                                        |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [// Assigning the Activation to the Pdf3DAnnotation]                                                                                           |
|                                                                                                                                                                                                  |
| [annotation.Activation = activation;]                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [\' Creating instance for Pdf3DActivation class]                                                                                                                                                     |
|                                                                                                                                                                                                                                                        |
| [Dim][ activation [As] Syncfusion.Pdf.Interactive.Pdf3DActivation = [New] Syncfusion.Pdf.Interactive.Pdf3DActivation()] |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [\' Setting Activation Mode as PageVisible]                                                                                                                                                          |
|                                                                                                                                                                                                                                                        |
| [activation.ActivationMode = Pdf3DActivationMode.PageVisible]                                                                                                                                                      |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [\' Showing the Toolbar]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                        |
| [activation.ShowToolbar = [True]]                                                                                                                                                             |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [\' Setting Deactivation Mode as PageVisible]                                                                                                                                                        |
|                                                                                                                                                                                                                                                        |
| [activation.DeactivationMode = Pdf3DDeactivationMode.ExplicitDeactivation]                                                                                                                                         |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [\' Assigning the Activation to the Pdf3DAnnotation]                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [annotation.Activation = activation]                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: You can also set the deactivation mode by using the Pdf3DDeactivationMode class.


 

**Pdf3DBackground**

 

Pdf3DBackground defines the background over which the 3D artwork is to be drawn. You can apply background color to the entire annotation by enabling the **ApplyToEntireAnnotation** property. If set to ***False***, the background should apply only to the rectangle that is specified by the 3D view box of the annotation. Default value is ***False***.

 

The following code example illustrates this.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [PdfColor][ color = [new] [PdfColor]([Color].Silver);] |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [Pdf3DBackground][ background = [new] [Pdf3DBackground]();]                    |
|                                                                                                                                                                                                                     |
| [background.Color = color;]                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| [background.ApplyToEntireAnnotation = [true];]                                                                                                             |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [// Setting Background color to current view.]                                                                                                                    |
|                                                                                                                                                                                                                     |
| [view.Background = background;]                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [Dim][ color [As] Syncfusion.Pdf.Graphics.PdfColor = [New] Syncfusion.Pdf.Graphics.PdfColor(color.Silver)]              |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [Dim][ background [As] Syncfusion.Pdf.Interactive.Pdf3DBackground = [New] Syncfusion.Pdf.Interactive.Pdf3DBackground()] |
|                                                                                                                                                                                                                                                        |
| [background.Color = color]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                        |
| [background.ApplyToEntireAnnotation = [True]]                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                        |
| [\' Setting Background color to current view.]                                                                                                                                                       |
|                                                                                                                                                                                                                                                        |
| [view.Background = background]                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Pdf3DRenderMode

[] 

You can specify the rendering style for the 3D artwork by using the Pdf3DRenderMode class. For example, surfaces may be filled with opaque colors, they may be stroked as a \"wireframe\", or the artwork may be rendered with special lighting effects.

 

The following are the rendering styles supported by the Pdf3DRenderMode class.

[] 

[·      ]Solid

[·      ]SolidWireframe

[·      ]Transparent

[·      ]TransparentWireframe

[·      ]BoundingBox

[·      ]TansparentBoundingBox

[·      ]TransparentBoundingBoxOutline

[·      ]Wireframe

[·      ]ShadedWireframe

[·      ]HiddenWireframe

[·      ]Vertices

[·      ]ShadedVertices

[·      ]Illustration

[·      ]SolidOutline

[·      ]ShadedIllustration

 

Apart from using the Style property, you can also change the rendering style by using the following properties.

 

[·      ]**AuxilaryColor**: PdfColor name that specifies the auxiliary color to be used when rendering the 3D image. The first entry in the array is a color space; the subsequent entries are values specifying color values in that color space.

[·      ]**FaceColor**: PdfColor name that specifies the face color to be used when rendering the 3D image. This entry is relevant only when the Style property is set to Illustration.

[·      ]**Opacity**: Number specifying the opacity of the added transparency applied by some render modes using a standard additive blend. Default value is ***0.5***.

[·      ]**CreaseValue**: Number specifying the angle in degrees to be used as the crease value while determining silhouette edges. Default value is ***45***.

 

The following code example illustrates this.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                 |
|                                                                                                                                                                                                  |
| []                                                                                                                                           |
|                                                                                                                                                                                                  |
| [Pdf3DRendermode][ rendermode = [new] [Pdf3DRendermode]();] |
|                                                                                                                                                                                                  |
| [rendermode.Style = [Pdf3DRenderStyle].Solid;]                                                                                       |
|                                                                                                                                                                                                  |
| [view.RenderMode = renderMode;]                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [Dim][ rendermode [As] Syncfusion.Pdf.Interactive.Pdf3DRendermode = [New] Syncfusion.Pdf.Interactive.Pdf3DRendermode()] |
|                                                                                                                                                                                                                                                        |
| [rendermode.Style = Pdf3DRenderStyle.Solid]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                        |
| [view.RenderMode = renderMode]                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Pdf3DLighting

 

Pdf3DLighting class specifies the lighting to be applied to the 3D artwork. The following lighting effects are supported by the Pdf3DLighting class.

[] 

[·      ]Artwork

[·      ]None

[·      ]White

[·      ]Day

[·      ]Night

[·      ]Hard

[·      ]Primary

[·      ]Blue

[·      ]Red

[·      ]Cube

[·      ]CAD

[·      ]Headlamp

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [Pdf3DLighting][ lighting = [new] [Pdf3DLighting]();] |
|                                                                                                                                                                                                                            |
| [lighting.Style = [Pdf3DLightingStyle].CAD;]                                                                                                   |
|                                                                                                                                                                                                                            |
| [view.LightingScheme = lightingScheme;]                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                  |
| [Dim][ lighting [As] Syncfusion.Pdf.Interactive.Pdf3DLighting = [New] Syncfusion.Pdf.Interactive.Pdf3DLighting()] |
|                                                                                                                                                                                                                                                  |
| [lighting.Style = Pdf3DLightingStyle.CAD]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                  |
| [view.LightingScheme = lightingScheme]                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Pdf3DCrossSection

 

Pdf3DCrossSection specifies how a portion of the 3D artwork is clipped for the purpose of showing artwork cross sections. The following code example illustrates this.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                   |
|                                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                                    |
| [Pdf3DCrossSection][ csection = [new] [Pdf3DCrossSection]();] |
|                                                                                                                                                                                                    |
| [csection.IntersectionColor = color;]                                                                                                                          |
|                                                                                                                                                                                                    |
| [csection.IntersectionIsVisible = 50;]                                                                                                                         |
|                                                                                                                                                                                                    |
| [view.CrossSections = csection;]                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                          |
| [Dim][ csection [As] Syncfusion.Pdf.Interactive.Pdf3DCrossSection = [New] Syncfusion.Pdf.Interactive.Pdf3DCrossSection()] |
|                                                                                                                                                                                                                                                          |
| [csection.IntersectionColor = color]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                          |
| [csection.IntersectionIsVisible = 50]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                          |
| [view.CrossSections = csection]                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#related-topics}

