def enterData(modules, num_days, module_name):
    days = []

    for day in range(1, num_days + 1):
        activities = []
        num_activities = int(
            input(
                "Enter number of activities for Day {} of {}: ".format(day, module_name)
            )
        )
        for activity in range(1, num_activities + 1):
            activity_name = input(
                "Enter name of activity {} for Day {} of {}: ".format(
                    activity, day, module_name
                )
            )
            activities.append(activity_name)

        day_data = {"day{}".format(day): activities}
        days.append(day_data)

    module = {module_name: days}
    modules.append(module)
