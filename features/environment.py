def before_scenario(context, scenario):
    print("Starting--------------------------->" + scenario.name)

def after_scenario(context, scenario):
    print("Completed--------------------------->" + scenario.name)