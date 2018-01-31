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
# target_primers = containers.load('tube-rack-2ml', 'B1')

# Reagents should be laid out: ddH2O, mastermix, DNA, forward_primer
# The second through fifth rows of the reagent rack are primers.
reagents = containers.load('tube-rack-2ml', 'B1')
ddH2O = reagents['A1']
mastermix = reagents['B1']
vector = reagents['C1']
forward_primer = reagents['D1']
target_primers = reagents[4:]

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

NUM_PRIMERS = 7
TEMPLATE_CONC = 0.8 # ng/ul

dna_volume = 5 / TEMPLATE_CONC
water_volume = 25 - 2.5 - 12.5 - dna_volume

print(dest[:NUM_PRIMERS])
print(dest[:NUM_PRIMERS].bottom())

# p200.distribute(12.5, mastermix, dest[:NUM_PRIMERS], touch_tip=True, disposal_vol=5)
# p200.distribute(water_volume, ddH2O, dest[:NUM_PRIMERS], touch_tip=True)
p10s.distribute(dna_volume, vector, dest[:NUM_PRIMERS], touch_tip=True, new_tip="always")
p10s.distribute(1.25, forward_primer, dest[:NUM_PRIMERS], touch_tip=True, new_tip="always")

p10s.transfer(1.25, target_primers[:NUM_PRIMERS], dest[:NUM_PRIMERS], touch_tip=True, new_tip="always")

for c in robot.commands():
    print(c)
