"""Django urlpatterns declaration for nautobot_templates_interface app."""

from nautobot.apps.urls import NautobotUIViewSetRouter

from nautobot_templates_interface import views

router = NautobotUIViewSetRouter()
router.register("dot1qtemplate", views.Dot1qTemplateUIViewSet)
#router.register("dot1qtemplate", views.Dot1qTemplateUIViewSet, basename='dot1qtemplate_viewset')
#router.register("dot1qtemplate_detail", views.Dot1qTemplateDetailView, basename='dot1qtemplate_detail')

urlpatterns = router.urls
