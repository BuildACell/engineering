from opentrons import robot, containers, instruments

# Configure the robot

#  Layout:
#    A     B       C      D      E
#  3 p200                        p10
#  2               dest          p10
#  1       reagt          trash  p10
#

p10s_tipracks = [containers.load('tiprack-10ul', 'E3')]
p200_tipracks = [containers.load('tiprack-200ul', 'A3')]

dest = containers.load('96-PCR-tall', 'C2')
cells = containers.load('tube-rack-2ml', 'B1')
trash = containers.load('point', 'D1', 'holywastedplasticbatman')

p10s = instruments.Pipette(
    axis='a',
    max_volume=10,
    min_volume=0.5,
    tip_racks=p10s_tipracks,
    trash_container=trash,
    channels=1,
    name='p10-8s'
)

p200 = instruments.Pipette(
    axis='b',
    max_volume=200,
    min_volume=20,
    tip_racks=p200_tipracks,
    trash_container=trash,
    channels=1,
    name='p200-1'
)

ALIQUOT_VOL = 50 # ul
NUM_ALIQUOTS = 32

p200.distribute(ALIQUOT_VOL, cells['A1'], dest[:NUM_ALIQUOTS], touch_tip=True, disposal_vol=0)
p200.drop_tip()

for c in robot.commands():
    print(c)
