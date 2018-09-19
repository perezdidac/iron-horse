from train import PassengerEngineMetroConsist, MetroUnit

consist = PassengerEngineMetroConsist(id='serpentine',
                                      base_numeric_id=460,
                                      name='Serpentine',
                                      role='pax_metro',
                                      power=600,
                                      type_base_buy_cost_points=40,  # dibble buy cost for game balance
                                      gen=1,
                                      sprites_complete=True)

# should be 4 units not 2, would look nicer short, but eh, painting
consist.add_unit(type=MetroUnit,
                 weight=40,
                 vehicle_length=8,
                 capacity=120,
                 chassis='railcar',
                 repeat=2)
