# F1-style Christmas Tree Racer — product spec for the supplier

Concept: like the classic train that runs under the Christmas tree, but a modern open-wheel (F1-style) race cars that runs on a track **mounted on the tree itself**: one turn climbing around the tree, one turn coming back down, endlessly.

No licensed teams, no logos, no sponsor decals, no numbers. Liveries in the colours of current F1 cars (red/black, papaya/black, navy/red-yellow, silver/teal).

## 1. How the car stays on the track (it must never fly off)
It is a **slot-car system** (the same principle as Scalextric / Carrera), plus a magnet:

1. **Guide slot + guide blade.** The track has a narrow slot running down the middle. Under the car's nose there is a pivoting guide blade (a thin vertical fin, about 8 mm deep) that sits inside the slot. The car is physically locked to the line of the track and steers itself through every curve.
2. **Magnet traction.** A neodymium magnet under the chassis is pulled down onto the steel power rails of the track. That keeps the car pressed to the track in the banked curve at full speed, so it does not tip over or jump out of the slot.
3. **Banked curves + guard wall.** All curves are banked inward by about 5°. Every curve has a low clear guard wall on its outer edge (about 15 mm high) as a last safety barrier.
4. **Speed limiter.** The power box caps the maximum voltage so that the top speed is safe on the downhill spiral and in the crossovers. There is no "turbo" that can throw the car out.

## 2. Power
- Two thin steel rails run on each side of the slot and carry low-voltage DC (12 V max) from a wall adapter to the power box.
- Two small copper braids (contact brushes) on each side of the guide blade pick up the current. A small DC motor drives the rear axle.
- **Handheld controller:** a trigger speed controller with a cable, or optionally wireless 2.4 GHz.
- **Auto mode:** a switch on the power box makes the car run on its own at a constant slow "display" speed, like the Christmas train.
- **LED lights:** small LEDs in the car (front-wing light strip and a red rear rain light), powered from the rails.
- Low voltage only. Child-safe: 8+ with adult setup.

## 3. Track layout on the tree (one endless loop: up around the tree, then down around the tree)
The car climbs one full turn around the tree, crosses over at the back, comes down one full turn around the tree, crosses back and starts again. Single lane, one continuous closed circuit, no switches, and the track never touches itself. All dimensions below are checked in `schema_traseu.py`, which draws `schema-traseu.png`.

- The track follows the cone of the tree. The radius gets smaller as the track goes up, so it always sits just outside the branch tips.
- **Up spiral (outer lane):** about 320° around the tree. Radius 62 cm at the bottom down to 50 cm at the top, about 8 cm outside the branch tips. Climbs 35 cm, from 50 cm to 85 cm above the floor. Length about 2.95 m, grade 12%.
- **Down spiral (inner lane):** about 320° around the tree. Always 15 cm inside the outer lane: radius 47 cm at the bottom down to 35 cm at the top, about 7 cm into the branch tips. Descends 35 cm. Length about 2.17 m, grade 16.4% downhill.
- At the front of the tree both lanes pass side by side at the same height, 15 cm apart centre to centre (5 cm between the lane edges), like a two-lane road. They never touch.
- **Top crossover (85 cm) and bottom crossover (50 cm):** two S-bends at the back of the tree, each over 60° of the circle, about 48 cm long, shifting the lane by 15 cm (bend radius about 36 cm). The top S passes 35 cm above the bottom S.
- Lane 100 mm wide (the car is 60 mm wide). Curves are banked 5° inward. Clear guard lip on the outer edges.
- Pieces: outer climbing curves, inner descending curves and 2 S-crossovers, each with a factory-set slope and radius (numbered for assembly). Pieces snap together with tabs. Rails connect through metal joiners.
- One car runs the loop. A second car can follow it on the same lane. Speed is limited for the downhill.

## 4. Mounting
- **2 trunk collar clamps** (black, adjustable, fit trunks / centre poles of 2–5 cm), one at about 50 cm and one at about 85 cm, clamped to the trunk.
- **6 support arms per collar** (black, adjustable length and height) go out radially. Each arm has two track holders, outer and inner lane, that clip under the track and set its height on the spiral.
- **Clear branch clips** only stabilise the track against the branches.
- Total weight of track + cars well under 2.5 kg. Fits artificial and real trees from 6 to 7.5 ft. Assembly is tool-free, about 15 minutes.

## 5. In the box
1 car (extra cars and colours sold separately) · about 12 outer climbing curves + about 12 inner descending curves + 2 S-crossovers · 2 trunk collars + 12 support arms · branch clips · 1 power box with speed limiter and auto mode · 1 handheld controller · wall adapter · spare guide blades + spare brushes · instructions.

## 6. Car
- Scale 1:32: 160 mm long, 60 mm wide. Modern F1 shape: halo, multi-element front wing, big rear wing, slick tyres.
- Body: ABS plastic. Chassis: plastic with the magnet pocket, motor pod and guide-blade mount.
- Liveries without any logos or text: red/black, papaya/black, navy/red-yellow, silver/teal.

## 7. Questions for the supplier
- Unit cost of the car and of the full set at MOQ.
- Can they make the up/down spiral (dimensions in section 3 and in schema-traseu.png) with numbered, fixed-slope curve pieces?
- How much does the full set weigh?
- Certifications for the US (CPSC / ASTM F963, FCC if wireless).
- Shipping to the USA: time and cost.

## 8. Key dimensions (from schema_traseu.py)
| Part | Size |
|---|---|
| Up spiral (outer lane) | radius 62 → 50 cm, climbs 50 → 85 cm above the floor, 2.95 m long, 12% |
| Down spiral (inner lane) | radius 47 → 35 cm (15 cm inside the outer lane), 2.17 m long, 16.4% |
| S-crossovers | 2, at the back of the tree, 60° each, about 48 cm long, 35 cm apart vertically |
| Lane width | 100 mm, slot in the centre, 2 steel rails |
| Outer guard lip | 15 mm high, clear |
| Car | 160 × 60 mm, 1:32 |
| Trunk collar | fits Ø 20–50 mm |
| Support arms | 6 per collar, adjustable 30–60 cm, 2 holders each (outer + inner lane) |
| Box | about 60 × 40 × 15 cm |
