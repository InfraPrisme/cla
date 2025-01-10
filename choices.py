from nautobot.core.choices import ChoiceSet

""" Class for all feature type value """
class InterfaceFeatureTypeChoices(ChoiceSet):
    """ All type value """
    TYPE_BOOLEAN = "boolean"
    TYPE_SELECT = "select"

    """ Set the tuple choises var with the specific value and the displayed text in the field """
    CHOICES = (
        (TYPE_BOOLEAN, "Boolean (True/False/None)"),
        (TYPE_SELECT, "Selection"),
    )
    