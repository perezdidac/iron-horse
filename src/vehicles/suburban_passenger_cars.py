from train import PassengerSuburbanCarConsist, PaxSuburbanCar


def main():
    # --------------- pony NG----------------------------------------------------------------------
    consist = PassengerSuburbanCarConsist(
        roster_id="pony",
        base_numeric_id=770,
        gen=1,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxSuburbanCar, chassis="4_axle_ng_16px")

    # no gen 2 for NG, straight to gen 3

    consist = PassengerSuburbanCarConsist(
        roster_id="pony",
        base_numeric_id=800,
        gen=3,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxSuburbanCar, chassis="4_axle_ng_16px")

    consist = PassengerSuburbanCarConsist(
        roster_id="pony",
        base_numeric_id=860,
        gen=4,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxSuburbanCar, chassis="4_axle_ng_16px")

    # --------------- pony ----------------------------------------------------------------------

    consist = PassengerSuburbanCarConsist(
        roster_id="pony",
        base_numeric_id=3300,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxSuburbanCar, chassis="3_axle_solid_express_16px")

    consist = PassengerSuburbanCarConsist(
        roster_id="pony", base_numeric_id=740, gen=1, subtype="B", sprites_complete=True
    )

    consist.add_unit(type=PaxSuburbanCar, chassis="4_axle_solid_express_24px")

    consist = PassengerSuburbanCarConsist(
        roster_id="pony",
        base_numeric_id=3310,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxSuburbanCar, chassis="3_axle_solid_express_16px")

    consist = PassengerSuburbanCarConsist(
        roster_id="pony", base_numeric_id=750, gen=2, subtype="B", sprites_complete=True
    )

    consist.add_unit(type=PaxSuburbanCar, chassis="4_axle_solid_express_24px")

    consist = PassengerSuburbanCarConsist(
        roster_id="pony",
        base_numeric_id=3290,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxSuburbanCar, chassis="3_axle_solid_express_16px")

    consist = PassengerSuburbanCarConsist(
        roster_id="pony", base_numeric_id=760, gen=3, subtype="B", sprites_complete=True
    )

    consist.add_unit(type=PaxSuburbanCar, chassis="4_axle_solid_express_24px")

    consist = PassengerSuburbanCarConsist(
        roster_id="pony",
        base_numeric_id=4570,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxSuburbanCar, chassis="4_axle_solid_express_32px")

    consist = PassengerSuburbanCarConsist(
        roster_id="pony",
        base_numeric_id=3110,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxSuburbanCar, chassis="4_axle_solid_express_24px")

    consist = PassengerSuburbanCarConsist(
        roster_id="pony",
        base_numeric_id=3260,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxSuburbanCar, chassis="4_axle_solid_express_32px")

    consist = PassengerSuburbanCarConsist(
        roster_id="pony",
        base_numeric_id=3100,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxSuburbanCar, chassis="4_axle_solid_express_24px")

    consist = PassengerSuburbanCarConsist(
        roster_id="pony",
        base_numeric_id=3280,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxSuburbanCar, chassis="4_axle_solid_express_32px")

    # gen 6 broadly same as gen 5, but new liveries (any other difference?)

    consist = PassengerSuburbanCarConsist(
        roster_id="pony",
        base_numeric_id=1580,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxSuburbanCar, chassis="4_axle_solid_express_24px")

    consist = PassengerSuburbanCarConsist(
        roster_id="pony",
        base_numeric_id=3270,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxSuburbanCar, chassis="4_axle_solid_express_32px")
