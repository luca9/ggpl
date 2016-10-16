from pyplasm import T, CUBOID, STRUCT

def createSpace(beamDimensions,
                pillarDimensions,
                pillarsDistances,
                interstoryHeights):



    bx, bz = beamDimensions
    px, py = pillarDimensions

    floors = []

    for height in interstoryHeights:
        pillar = CUBOID([px, py, height])
        beams = []
        pillars = [pillar]
        beamWidth = 0


        for i in range(0, len(pillarsDistances) - 1):
            distance = pillarsDistances[i]
            beamWidth += distance + py
            beams += [CUBOID([bx, beamWidth, bz]), T(2)(beamWidth)]
            pillars += [T(2)(distance + py), pillar]
            beamWidth = 0

        distance = pillarsDistances[-1]

        beams.append(CUBOID([bx, distance + py + (py/2.0) + beamWidth, bz]))

        # last pillar
        pillars += [T(2)(distance + py), pillar]

        floors += [STRUCT(pillars), T(3)(height), STRUCT(beams), T(3)(bz)]

    return STRUCT(floors)
