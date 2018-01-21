from cms.wizards.wizard_base import Wizard
from cms.wizards.wizard_pool import wizard_pool

from .forms import PictureWizardForm


class PictureWizard(Wizard):
    pass

picture_wizard = PictureWizard(
    title="Picture",
    weight=200,  # determines the ordering of wizards in the Create dialog
    form=PictureWizardForm,
    description="Create a new Picture",
)

wizard_pool.register(picture_wizard)
