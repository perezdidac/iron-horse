from train import EngineConsist, ElectroDieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="shoebox",
        base_numeric_id=280,
        name="Shoebox",
        role="express",
        role_child_branch_num=-1,
        power=950,  # yes it's quite low power initially eh
        power_by_railtype={"RAIL": 950, "ELRL": 2300},
        random_reverse=True,
        pantograph_type="z-shaped-single",
        gen=4,
        intro_date_offset=3,  # introduce later than gen epoch by design
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_CREAM", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectroDieselEngineUnit,
        weight=67,
        vehicle_length=8,
        effect_offsets=[(2, 0)],
        spriterow_num=0,
    )

    consist.description = (
        """This one can go on electric or diesel. Madder than a box of frogs."""
    )
    consist.foamer_facts = """BR Class 73, Class 71/74, proposed Class 75"""

    return consist
