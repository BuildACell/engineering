from opentrons import robot, containers, instruments

# This protocol sets up a T4 ligase reaction in a PCR strip.

# Configure the robot

#  Layout:
#    A     B       C      D      E
#  3 p200                        p10
#  2               pcr           p10
#  1       reagt          trash  p10
#

p10s_tipracks = [containers.load('tiprack-10ul', 'E3')]
p10_tipracks = [containers.load('tiprack-10ul', 'E2')]
p200_tipracks = [containers.load('tiprack-200ul', 'A3')]

pcr = containers.load('96-PCR-tall', 'C2')

# Reagents should be laid out: ddH2O, mastermix, DNA, forward_primer
reagents = containers.load('tube-rack-2ml', 'B1')
ddH2O = reagents['A1']
ligase_buffer = reagents['B1']
ligase = reagents['C1']

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

p10 = instruments.Pipette(
    axis='a',
    max_volume=10,
    min_volume=0.5,
    tip_racks=p10_tipracks,
    trash_container=trash,
    channels=8,
    name='p10-8'
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

# Go higher between wells
robot.arc_height=20

SOURCE = pcr.rows('1')
DEST = pcr.rows('2')

p200.distribute(16, ddH2O, DEST, touch_tip=True, disposal_vol=5)
p10s.distribute(2, ligase_buffer, DEST, touch_tip=True, new_tip="always")
p10s.distribute(1, ligase, DEST, touch_tip=True, blow_out=True, new_tip="always")
# p10.transfer(1, SOURCE, DEST, touch_tip=True, new_tip="always", blow_out=True)

p10.pick_up_tip()
p10.aspirate(1, SOURCE)
robot.home('z')
import time; time.sleep(5)
p10.dispense(DEST)
p10.blow_out()
p10.touch_tip()
p10.drop_tip()

robot.home()

for c in robot.commands():
    print(c)
