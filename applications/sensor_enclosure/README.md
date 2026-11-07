# Sensor Enclosure — Mechanical CAD

## Overview

This project demonstrates the mechanical design of an enclosure for a small sensor PCB using FreeCAD.

The goal is to create a parametric 3D model and a technical drawing suitable for documenting the enclosure geometry.

## Design Specifications

| Parameter | Value |
|---|---|
| PCB dimensions | 50 × 30 mm |
| External enclosure dimensions | 58 × 38 × 20 mm |
| Internal cavity dimensions | 54 × 34 × 18 mm |
| Wall thickness | 2 mm |
| Bottom thickness | 2 mm |
| PCB clearance | 2 mm per side |
| PCB supports | 4 cylindrical standoffs |
| Standoff diameter | 4 mm |
| Standoff height | 3 mm |
| Connector opening | 8 × 5 mm |

The standoffs are positioned symmetrically at X = ±22 mm and Y = ±12 mm.

## Tools

- FreeCAD 1.1.4
- Part Design Workbench
- Sketcher Workbench
- TechDraw Workbench

## Design Process

1. Created a fully constrained rectangular sketch.
2. Extruded the sketch using Pad.
3. Created the enclosure cavity using Pocket.
4. Added four cylindrical PCB supports.
5. Created a rectangular connector opening.
6. Generated orthographic projections using TechDraw.
7. Added dimensional annotations and exported the drawing to PDF.

## Files

- `sensor_enclosure.FCStd` — Parametric FreeCAD model.
- `sensor_enclosure_drawing.pdf` — Technical drawing with orthographic projections and dimensions.

## Engineering Considerations

- Clearance is required for reliable PCB installation.
- PCB supports provide space underneath the circuit board.
- Parametric constraints allow dimensions to be modified without rebuilding the entire model.
- The connector opening must be adapted to the dimensions of the actual connector.

This is a conceptual enclosure model. A production-ready design would additionally require a lid, a PCB retention mechanism, manufacturing tolerances, and physical fit verification.

## Learning Outcomes

- Understanding parametric mechanical CAD.
- Applying geometric and dimensional constraints.
- Using additive and subtractive modeling operations.
- Designing mechanical features for electronic assemblies.
- Creating technical drawings from 3D models.
