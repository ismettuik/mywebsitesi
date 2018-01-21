from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from duyuru_cms.models import TekDuyuruPluginModel, CokDuyuruPluginModel
from django.utils.translation import ugettext as _
from duyuru.models import Duyuru

@plugin_pool.register_plugin  # register the plugin
class TekDuyuruPluginPublisher(CMSPluginBase):
    model = TekDuyuruPluginModel  # model where plugin data are saved
    module = _("DuyuruTek")
    name = _("Tek Duyuru Plugin")  # name of the plugin in the interface
    render_template = "duyuru_cms/duyuru_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


@plugin_pool.register_plugin  # register the plugin
class CokDuyuruPluginPublisher(CMSPluginBase):
    model = CokDuyuruPluginModel  # model where plugin data are saved
    module = _("DuyuruCok")
    name = _("Cok Duyuru Plugin")  # name of the plugin in the interface
    render_template = "duyuru_cms/duyuru_plugin.html"

    def render(self, context, instance, placeholder):
        instance.duyurular = Duyuru.objects.filter(yayinlansinmi = 'E').order_by('-eklenme_tarihi')
        context.update({'instance': instance})
        return context
