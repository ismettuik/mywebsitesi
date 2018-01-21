from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms_dynamic_carousel.models import PicturePluginModel
from django.utils.translation import ugettext as _
from dynamic_carousel.models import Picture


@plugin_pool.register_plugin  # register the plugin
class PicturePluginPublisher(CMSPluginBase):
    model = PicturePluginModel  # model where plugin data are saved
    module = _("Picture")
    name = _("Dynamic Carousel plugin")  # name of the plugin in the interface
    render_template = "cms_dynamic_carousel/dycarousel_list.html"

    def render(self, context, instance, placeholder):
        instance.pictures = Picture.objects.all().order_by('-upload_date')
        context.update({'instance': instance})
        return context


