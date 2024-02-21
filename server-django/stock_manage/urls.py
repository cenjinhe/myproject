from django.urls import include, path
from stock_manage import views, views_baostock, views_trend, views_recommend


urlpatterns = [
    # views
    path('getStockList/', views.getStockList),
    path('getRawDataList/', views.getRawDataList),
    path('getRawDataDict/', views.getRawDataDict),
    path('updateStockList/', views.updateStockList),
    path('updateStatus/', views.updateStatus),
    path('deleteStockRecord/', views.deleteStockRecord),
    # views_baostock
    path('update_history_data_single/', views_baostock.update_history_data_single),
    path('update_history_data_all/', views_baostock.update_history_data_all),
    # views_trend
    path('getUpTrendDataList/', views_trend.getUpTrendDataList),
    path('postUpdateTrendStatus/', views_trend.postUpdateTrendStatus),
    # views_recommend
    path('postUpdateStockRecommend/', views_recommend.postUpdateStockRecommend),
]
