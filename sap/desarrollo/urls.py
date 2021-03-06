from django.conf.urls import patterns, url
from desarrollo.views import desarrollo_view, ver_fases_view, ver_items_view
from desarrollo.views import calcular_costo_view, crear_solicitud_view, solicitudes_proyecto_view, analizar_solicitud_view, solicitudes_usuario_view, visualizar_solicitud_view, cancelar_solicitud_view, finalizar_proyecto_view, historial_item_view, visualizar_version_item_view
from desarrollo.views import fases_proyecto_view
from desarrollo.views import roles_fase_view, fase_agregar_rol_view, fase_confirmacion_agregar_rol_view, fase_quitar_rol_view
from desarrollo.views import tipos_item_fase_view
from desarrollo.views import crear_tipo_item_view, modificar_tipo_item_view, eliminar_tipo_item_view, visualizar_tipo_item_view
from desarrollo.views import tipos_atributo_tipo_item_view, agregar_tipo_atributo_view, confirmacion_agregar_tipo_atributo_view, quitar_tipo_atributo_view
from desarrollo.views import iniciar_fase_view
from desarrollo.views import finalizar_fase_view
from desarrollo.views import items_fase_view
from desarrollo.views import crear_item_view, modificar_item_view, eliminar_item_view, visualizar_item_view, validar_item_view, aprobar_item_view, desaprobar_item_view, revivir_item_view, confirmacion_revivir_item_view, calcular_impacto_view
from desarrollo.views import relaciones_item_view, agregar_relacion_view, confirmacion_agregar_relacion_view, quitar_relacion_view
from desarrollo.views import lineas_base_fase_view, crear_linea_base_view, visualizar_linea_base_view, cerrar_linea_base_view
from desarrollo.views import items_linea_base_view, linea_base_agregar_item_view,linea_base_confirmacion_agregar_item_view, linea_base_quitar_item_view
from desarrollo.views import versiones_item_view, confirmacion_reversionar_item_view
from desarrollo.views import reporte_proyecto_view, reporte_cambios_view

urlpatterns = patterns('',
    url(r'^desarrollo/$', desarrollo_view, name="vista_desarrollo"),
    url(r'^desarrollo/ver_fases/proyecto/(?P<id_proyecto>\d+)/$', ver_fases_view, name="vista_ver_fases"),
    url(r'^desarrollo/ver_items/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', ver_items_view, name="vista_ver_items"),
    url(r'^desarrollo/solicitudes/proyecto/(?P<id_proyecto>\d+)/$', solicitudes_proyecto_view, name="vista_solicitudes_proyecto"),
    url(r'^desarrollo/solicitudes/analizar_solicitud/(?P<id_solicitud>\d+)/proyecto/(?P<id_proyecto>\d+)/$', analizar_solicitud_view, name="vista_analizar_solicitud"),
    url(r'^desarrollo/solicitudes/(?P<id_solicitud>\d+)/historial_item/(?P<id_item>\d+)/proyecto/(?P<id_proyecto>\d+)/$', historial_item_view, name="vista_historial_item"),
    url(r'^desarrollo/solicitudes/(?P<id_solicitud>\d+)/historial_item/(?P<id_item>\d+)/version/(?P<version>\d+)/proyecto/(?P<id_proyecto>\d+)/$', visualizar_version_item_view, name="vista_visualizar_version_item"),
    url(r'^desarrollo/crear_solicitud/item/(?P<id_item>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', crear_solicitud_view, name="vista_crear_solicitud"),
    url(r'^desarrollo/solicitudes/usuario/(?P<id_usuario>\d+)/proyecto/(?P<id_proyecto>\d+)/$', solicitudes_usuario_view, name="vista_solicitudes_usuario"),
    url(r'^desarrollo/solicitudes/visualizar_solicitud/(?P<id_solicitud>\d+)/proyecto/(?P<id_proyecto>\d+)/$', visualizar_solicitud_view, name="vista_visualizar_solicitud"),
    url(r'^desarrollo/solicitudes/cancelar_solicitud/(?P<id_solicitud>\d+)/proyecto/(?P<id_proyecto>\d+)/$', cancelar_solicitud_view, name="vista_cancelar_solicitud"),
    url(r'^desarrollo/calcular_costo/proyecto/(?P<id_proyecto>\d+)/$', calcular_costo_view, name="vista_calcular_costo"),
    url(r'^desarrollo/finalizar_proyecto/(?P<id_proyecto>\d+)/$', finalizar_proyecto_view, name="vista_finalizar_proyecto"),
    url(r'^desarrollo/fases/proyecto/(?P<id_proyecto>\d+)/$', fases_proyecto_view, name="vista_desarrollo_fases_proyecto"),
    url(r'^desarrollo/fases/roles/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', roles_fase_view, name="vista_roles_fase"),
    url(r'^desarrollo/fases/agregar_rol/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', fase_agregar_rol_view, name="vista_fase_agregar_rol"),
    url(r'^desarrollo/fases/confirmacion_agregar_rol/(?P<id_rol>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', fase_confirmacion_agregar_rol_view, name="vista_confirmacion_fase_agregar_rol"),
    url(r'^desarrollo/fases/quitar_rol/(?P<id_rol>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', fase_quitar_rol_view, name="vista_fase_quitar_rol"),
    url(r'^desarrollo/fases/tipos_item/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', tipos_item_fase_view, name="vista_tipos_item_fase"),
    url(r'^desarrollo/fases/tipos_item/crear_tipo_item/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', crear_tipo_item_view, name="vista_crear_tipo_item"),  
    url(r'^desarrollo/fases/tipos_item/modificar_tipo_item/(?P<id_tipo_item>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', modificar_tipo_item_view, name="vista_modificar_tipo_item"),
    url(r'^desarrollo/fases/tipos_item/eliminar_tipo_item/(?P<id_tipo_item>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', eliminar_tipo_item_view, name="vista_eliminar_tipo_item"),
    url(r'^desarrollo/fases/tipos_item/tipo_item/(?P<id_tipo_item>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', visualizar_tipo_item_view, name="vista_visualizar_tipo_item"),
    url(r'^desarrollo/fases/tipos_item/tipos_atributo/tipo_item/(?P<id_tipo_item>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', tipos_atributo_tipo_item_view, name="vista_tipos_atributo_tipo_item"),
    url(r'^desarrollo/fases/tipos_item/agregar_tipo_atributo/tipo_item/(?P<id_tipo_item>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', agregar_tipo_atributo_view, name="vista_agregar_tipo_atributo"),
    url(r'^desarrollo/fases/tipos_item/confirmacion_agregar_tipo_atributo/(?P<id_tipo_atributo>\d+)/tipo_item/(?P<id_tipo_item>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', confirmacion_agregar_tipo_atributo_view, name="vista_confirmacion_agregar_tipo_atributo"),
    url(r'^desarrollo/fases/tipos_item/quitar_tipo_atributo/(?P<id_tipo_atributo>\d+)/tipo_item/(?P<id_tipo_item>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', quitar_tipo_atributo_view, name="vista_quitar_tipo_atributo"),
    url(r'^desarrollo/fases/iniciar_fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', iniciar_fase_view, name="vista_iniciar_fase"),
    url(r'^desarrollo/fases/items/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', items_fase_view, name="vista_items_fase"),
    url(r'^desarrollo/fases/items/crear_item/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', crear_item_view, name="vista_crear_item"),
    url(r'^desarrollo/fases/items/modificar_item/(?P<id_item>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', modificar_item_view, name="vista_modificar_item"),
    url(r'^desarrollo/fases/items/eliminar_item/(?P<id_item>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', eliminar_item_view, name="vista_eliminar_item"),
    url(r'^desarrollo/fases/items/item/(?P<id_item>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', visualizar_item_view, name="vista_visualizar_item"),
    url(r'^desarrollo/fases/items/validar_item/(?P<id_item>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', validar_item_view, name="vista_validar_item"),
    url(r'^desarrollo/fases/items/aprobar_item/(?P<id_item>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', aprobar_item_view, name="vista_aprobar_item"),
    url(r'^desarrollo/fases/items/desaprobar_item/(?P<id_item>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', desaprobar_item_view, name="vista_desaprobar_item"),
    url(r'^desarrollo/fases/items/calcular_impacto/(?P<id_item>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', calcular_impacto_view, name="vista_calcular_impacto"),
    url(r'^desarrollo/fases/items/revivir_item/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', revivir_item_view, name="vista_revivir_item"),
    url(r'^desarrollo/fases/items/confirmacion_revivir_item/(?P<id_item>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', confirmacion_revivir_item_view, name="vista_confirmacion_revivir_item"),
    url(r'^desarrollo/fases/items/relaciones/item/(?P<id_item>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', relaciones_item_view, name="vista_relaciones_item"),
    url(r'^desarrollo/fases/items/agregar_relacion/item/(?P<id_item>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', agregar_relacion_view, name="vista_agregar_relacion"),
    url(r'^desarrollo/fases/items/confirmacion_agregar_relacion/(?P<eleccion>\d+)/(?P<id_relacion>\d+)/item/(?P<id_item>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', confirmacion_agregar_relacion_view, name="vista_confirmacion_agregar_relacion"),
    url(r'^desarrollo/fases/items/quitar_relacion/(?P<eleccion>\d+)/(?P<id_relacion>\d+)/item/(?P<id_item>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', quitar_relacion_view, name="vista_quitar_relacion"),
    url(r'^desarrollo/fases/items/versiones/item/(?P<id_item>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', versiones_item_view, name="vista_versiones_item"),
    url(r'^desarrollo/fases/items/confirmacion_reversionar_item/(?P<id_reversion>\d+)/item/(?P<id_item>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', confirmacion_reversionar_item_view, name="vista_confirmacion_reversionar_item"),
    url(r'^desarrollo/fases/finalizar_fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', finalizar_fase_view, name="vista_finalizar_fase"),
    url(r'^desarrollo/fases/lineas_base/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', lineas_base_fase_view, name="vista_lineas_base_fase"),
    url(r'^desarrollo/fases/lineas_base/crear_linea_base/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', crear_linea_base_view, name="vista_crear_linea_base"),
    url(r'^desarrollo/fases/lineas_base/linea_base/(?P<id_linea_base>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', visualizar_linea_base_view, name="vista_visualizar_linea_base"),
    url(r'^desarrollo/lineas_base/items/linea_base/(?P<id_linea_base>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', items_linea_base_view, name="vista_items_linea_base"),
    url(r'^desarrollo/lineas_base/agregar_item/linea_base/(?P<id_linea_base>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', linea_base_agregar_item_view, name="vista_linea_base_agregar_item"),
    url(r'^desarrollo/lineas_base/confirmacion_agregar_item/(?P<id_item>\d+)/linea_base/(?P<id_linea_base>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', linea_base_confirmacion_agregar_item_view, name="vista_confirmacion_linea_base_agregar_item"),
    url(r'^desarrollo/lineas_base/quitar_item/(?P<id_item>\d+)/linea_base/(?P<id_linea_base>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', linea_base_quitar_item_view, name="vista_linea_base_quitar_item"),
    url(r'^desarrollo/lineas_base/cerrar_linea_base/(?P<id_linea_base>\d+)/fase/(?P<id_fase>\d+)/proyecto/(?P<id_proyecto>\d+)/$', cerrar_linea_base_view, name="vista_cerrar_linea_base"),
    url(r'^desarrollo/reporte_proyecto/(?P<id_proyecto>\d+)/$', reporte_proyecto_view, name='vista_reporte_proyecto'),
    url(r'^desarrollo/reporte_cambios/(?P<id_proyecto>\d+)/$', reporte_cambios_view, name='vista_reporte_cambios'),
)
