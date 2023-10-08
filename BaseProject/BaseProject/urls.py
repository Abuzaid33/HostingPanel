from django.contrib import admin
from django.urls import path,include
from Baseapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_view, name='home'),
    path('', include('Authentication.urls')),



    path('dashboard-analytics.html', views.analytics, name='analytics'),
    path('dashboard-projects.html', views.projects, name='projects'),
    path('dashboard-crm.html', views.crm, name='crm'),
    path('dashboard-wallet.html', views.e_wallet, name='e_wallet'),

    path('apps-calendar.html', views.calendar_view, name='calendar'),
    path('apps-chat.html', views.chat_view, name='chat'),

    path('crm-projects.html', views.projects_view, name='projects'),
    path('crm-orders-list.html', views.orders_list_view, name='orders_list'),
    path('crm-clients.html', views.clients_view, name='clients'),
    path('crm-management.html', views.management_view, name='management'),

    path('apps-ecommerce-products.html', views.ecommerce_products, name='ecommerce_products'),
    path('apps-ecommerce-products-details.html', views.ecommerce_products_details, name='ecommerce_products_details'),
    path('apps-ecommerce-orders.html', views.ecommerce_orders, name='ecommerce_orders'),
    path('apps-ecommerce-orders-details.html', views.ecommerce_orders_details, name='ecommerce_orders_details'),
    path('apps-ecommerce-customers.html', views.ecommerce_customers, name='ecommerce_customers'),
    path('apps-ecommerce-shopping-cart.html', views.ecommerce_shopping_cart, name='ecommerce_shopping_cart'),
    path('apps-ecommerce-checkout.html', views.ecommerce_checkout, name='ecommerce_checkout'),
    path('apps-ecommerce-sellers.html', views.ecommerce_sellers, name='ecommerce_sellers'),
    path('apps-email-inbox.html', views.email_inbox, name='email_inbox'),
    path('apps-email-read.html', views.email_read, name='email_read'),
    path('apps-projects-list.html', views.projects_list, name='projects_list'),
    path('apps-projects-details.html', views.projects_details, name='projects_details'),
    path('apps-projects-gantt.html', views.projects_gantt, name='projects_gantt'),
    path('apps-projects-add.html', views.projects_add, name='projects_add'),
    path('apps-social-feed.html', views.social_feed, name='social_feed'),
    path('apps-tasks.html', views.tasks_list, name='tasks_list'),
    path('apps-tasks-details.html', views.tasks_details, name='tasks_details'),
    path('apps-kanban.html', views.kanban_board, name='kanban_board'),
    path('apps-file-manager.html', views.file_manager, name='file_manager'),

    path('pages-profile.html/', views.pages_profile, name='pages_profile'),
    path('pages-profile-2.html/', views.pages_profile_2, name='pages_profile_2'),
    path('pages-invoice.html/', views.pages_invoice, name='pages_invoice'),
    path('pages-faq.html/', views.pages_faq, name='pages_faq'),
    path('pages-pricing.html/', views.pages_pricing, name='pages_pricing'),
    path('pages-maintenance.html/', views.pages_maintenance, name='pages_maintenance'),
    path('pages-login.html/', views.pages_login, name='pages_login'),
    path('pages-login-2.html/', views.pages_login_2, name='pages_login_2'),
    path('pages-register.html/', views.pages_register, name='pages_register'),
    path('pages-register-2.html/', views.pages_register_2, name='pages_register_2'),
    path('pages-logout.html/', views.pages_logout, name='pages_logout'),
    path('pages-logout-2.html/', views.pages_logout_2, name='pages_logout_2'), 
    path('pages-recoverpw.html/', views.pages_recover_password, name='pages_recover_password'),  
    path('pages-recoverpw-2.html/', views.pages_recover_password_2, name='pages_recover_password_2'),  
    path('pages-lock-screen.html/', views.pages_lock_screen, name='pages_lock_screen'),  
    path('pages-lock-screen-2.html/', views.pages_lock_screen_2, name='pages_lock_screen_2'),  
    path('pages-confirm-mail.html/', views.pages_confirm_mail, name='pages_confirm_mail'), 
    path('pages-confirm-mail-2.html/', views.pages_confirm_mail_2, name='pages_confirm_mail_2'), 
    path('pages-starter.html/', views.pages_starter, name='pages_starter'), 
    path('pages-preloader.html/', views.pages_preloader, name='pages_preloader'), 
    path('pages-timeline.html/', views.pages_timeline, name='pages_timeline'), 
    path('pages-404.html/', views.pages_404, name='pages_404'),
    path('pages-404-alt.html/', views.pages_404_alt, name='pages_404_alt'),
    path('pages-500.html/', views.pages_500, name='pages_500'),
    path('landing.html/', views.landing, name='landing'),
    
    path('layouts-horizontal.html/', views.layouts_horizontal, name='layouts_horizontal'),
    path('layouts-detached.html/', views.layouts_detached, name='layouts_detached'),
    path('layouts-full.html/', views.layouts_full, name='layouts_full'),
    path('layouts-fullscreen.html/', views.layouts_fullscreen, name='layouts_fullscreen'),
    path('layouts-hover.html/', views.layouts_hover, name='layouts_hover'),
    path('layouts-compact.html/', views.layouts_compact, name='layouts_compact'),
    path('layouts-icon-view.html/', views.layouts_icon_view, name='layouts_icon_view'),


    path('ui-accordions.html/', views.ui_accordions, name='ui_accordions'),
    path('ui-alerts.html/', views.ui_alerts, name='ui_alerts'),
    path('ui-avatars.html/', views.ui_avatars, name='ui_avatars'),
    path('ui-badges.html/', views.ui_badges, name='ui_badges'),
    path('ui-breadcrumb.html/', views.ui_breadcrumb, name='ui_breadcrumb'),
    path('ui-buttons.html/', views.ui_buttons, name='ui_buttons'),
    path('ui-cards.html/', views.ui_cards, name='ui_cards'),
    path('ui-carousel.html/', views.ui_carousel, name='ui_carousel'),
    path('ui-dropdowns.html/', views.ui_dropdowns, name='ui_dropdowns'),
    path('ui-embed-video.html/', views.ui_embed_video, name='ui_embed_video'),
    path('ui-grid.html/', views.ui_grid, name='ui_grid'),
    path('ui-list-group.html/', views.ui_list_group, name='ui_list_group'),
    path('ui-modals.html/', views.ui_modals, name='ui_modals'),
    path('ui-notifications.html/', views.ui_notifications, name='ui_notifications'),
    path('ui-offcanvas.html/', views.ui_offcanvas, name='ui_offcanvas'),
    path('ui-placeholders.html/', views.ui_placeholders, name='ui_placeholders'),
    path('ui-pagination.html/', views.ui_pagination, name='ui_pagination'),
    path('ui-popovers.html/', views.ui_popovers, name='ui_popovers'),
    path('ui-progress.html/', views.ui_progress, name='ui_progress'),
    path('ui-ribbons.html/', views.ui_ribbons, name='ui_ribbons'),
    path('ui-spinners.html/', views.ui_spinners, name='ui_spinners'),
    path('ui-tabs.html/', views.ui_tabs, name='ui_tabs'),
    path('ui-tooltips.html/', views.ui_tooltips, name='ui_tooltips'),
    path('ui-links.html/', views.ui_links, name='ui_links'),
    path('ui-typography.html/', views.ui_typography, name='ui_typography'),
    path('ui-utilities.html/', views.ui_utilities, name='ui_utilities'),

    # Extended UI URLs
    path('extended-dragula.html/', views.extended_dragula, name='extended_dragula'),
    path('extended-range-slider.html/', views.extended_range_slider, name='extended_range_slider'),
    path('extended-ratings.html/', views.extended_ratings, name='extended_ratings'),
    path('extended-scrollbar.html/', views.extended_scrollbar, name='extended_scrollbar'),
    path('extended-scrollspy.html/', views.extended_scrollspy, name='extended_scrollspy'),
    path('extended-treeview.html/', views.extended_treeview, name='extended_treeview'),

    path('icons-remixicons.html/', views.icons_remixicons, name='icons_remixicons'),
    path('icons-mdi.html/', views.icons_mdi, name='icons_mdi'),
    path('icons-unicons.html/', views.icons_unicons, name='icons_unicons'),

    # Charts URLs
    path('charts-apex-area.html/', views.charts_apex_area, name='charts_apex_area'),
    path('charts-apex-bar.html/', views.charts_apex_bar, name='charts_apex_bar'),
    path('charts-apex-bubble.html/', views.charts_apex_bubble, name='charts_apex_bubble'),
    path('charts-apex-candlestick.html/', views.charts_apex_candlestick, name='charts_apex_candlestick'),
    path('charts-apex-column.html/', views.charts_apex_column, name='charts_apex_column'),
    path('charts-apex-heatmap.html/', views.charts_apex_heatmap, name='charts_apex_heatmap'),
    path('charts-apex-line.html/', views.charts_apex_line, name='charts_apex_line'),
    path('charts-apex-mixed.html/', views.charts_apex_mixed, name='charts_apex_mixed'),
    path('charts-apex-timeline.html/', views.charts_apex_timeline, name='charts_apex_timeline'),
    path('charts-apex-boxplot.html/', views.charts_apex_boxplot, name='charts_apex_boxplot'),
    path('charts-apex-treemap.html/', views.charts_apex_treemap, name='charts_apex_treemap'),
    path('charts-apex-pie.html/', views.charts_apex_pie, name='charts_apex_pie'),
    path('charts-apex-radar.html/', views.charts_apex_radar, name='charts_apex_radar'),
    path('charts-apex-radialbar.html/', views.charts_apex_radialbar, name='charts_apex_radialbar'),
    path('charts-apex-scatter.html/', views.charts_apex_scatter, name='charts_apex_scatter'),
    path('charts-apex-polar-area.html/', views.charts_apex_polar_area, name='charts_apex_polar_area'),
    path('charts-apex-sparklines.html/', views.charts_apex_sparklines, name='charts_apex_sparklines'),
    path('charts-chartjs-area.html/', views.charts_chartjs_area, name='charts_chartjs_area'),
    path('charts-chartjs-bar.html/', views.charts_chartjs_bar, name='charts_chartjs_bar'),
    path('charts-chartjs-line.html/', views.charts_chartjs_line, name='charts_chartjs_line'),
    path('charts-chartjs-other.html/', views.charts_chartjs_other, name='charts_chartjs_other'),
    path('charts-brite.html/', views.charts_brite, name='charts_brite'),
    path('charts-sparkline.html/', views.charts_sparkline, name='charts_sparkline'),

    # Forms URLs
    path('form-elements.html/', views.form_elements, name='form_elements'),
    path('form-advanced.html/', views.form_advanced, name='form_advanced'),
    path('form-validation.html/', views.form_validation, name='form_validation'),
    path('form-wizard.html/', views.form_wizard, name='form_wizard'),
    path('form-fileuploads.html/', views.form_fileuploads, name='form_fileuploads'),
    path('form-editors.html/', views.form_editors, name='form_editors'),

    # Tables URLs
    path('tables-basic.html/', views.tables_basic, name='tables_basic'),
    path('tables-datatable.html/', views.tables_datatable, name='tables_datatable'),

    # Maps URLs
    path('maps-google.html/', views.maps_google, name='maps_google'),
    path('maps-vector.html/', views.maps_vector, name='maps_vector'),



    path('widgets.html', views.widgets_view, name='widgets'),
    
    
    
    
]
