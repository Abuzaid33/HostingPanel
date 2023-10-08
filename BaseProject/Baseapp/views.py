from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')    
def home_view(request):
    return render(request, 'home.html')



def analytics(request):
    return render(request, 'dashboard-analytics.html')

def projects(request):
    return render(request, 'dashboard-projects.html')

def crm(request):
    return render(request, 'dashboard-crm.html')

def e_wallet(request):
    return render(request, 'dashboard-wallet.html')


def calendar_view(request):
    return render(request, 'apps-calendar.html')

def chat_view(request):
    return render(request, 'apps-chat.html')


def projects_view(request):
    return render(request, 'crm-projects.html')

def orders_list_view(request):
    return render(request, 'crm-orders-list.html')

def clients_view(request):
    return render(request, 'crm-clients.html')

def management_view(request):
    return render(request, 'crm-management.html')


def ecommerce_products(request):
    return render(request, 'apps-ecommerce-products.html')

def ecommerce_products_details(request):
    return render(request, 'apps-ecommerce-products-details.html')

def ecommerce_orders(request):
    return render(request, 'apps-ecommerce-orders.html')

def ecommerce_orders_details(request):
    return render(request, 'apps-ecommerce-orders-details.html')

def ecommerce_customers(request):
    return render(request, 'apps-ecommerce-customers.html')

def ecommerce_shopping_cart(request):
    return render(request, 'apps-ecommerce-shopping-cart.html')

def ecommerce_checkout(request):
    return render(request, 'apps-ecommerce-checkout.html')

def ecommerce_sellers(request):
    return render(request, 'apps-ecommerce-sellers.html')

def email_inbox(request):
    return render(request, 'apps-email-inbox.html')

def email_read(request):
    return render(request, 'apps-email-read.html')

def projects_list(request):
    return render(request, 'apps-projects-list.html')

def projects_details(request):
    return render(request, 'apps-projects-details.html')

def projects_gantt(request):
    return render(request, 'apps-projects-gantt.html')

def projects_add(request):
    return render(request, 'apps-projects-add.html')

def social_feed(request):
    return render(request, 'apps-social-feed.html')

def tasks_list(request):
    return render(request, 'apps-tasks.html')

def tasks_details(request):
    return render(request, 'apps-tasks-details.html')

def kanban_board(request):
    return render(request, 'apps-kanban.html')

def file_manager(request):
    return render(request, 'apps-file-manager.html')



def pages_profile(request):
    return render(request, 'pages-profile.html')

def pages_profile_2(request):
    return render(request, 'pages-profile-2.html')

def pages_invoice(request):
    return render(request, 'pages-invoice.html')

def pages_faq(request):
    return render(request, 'pages-faq.html')

def pages_pricing(request):
    return render(request, 'pages-pricing.html')

def pages_maintenance(request):
    return render(request, 'pages-maintenance.html')

def pages_login(request):
    return render(request, 'pages-login.html')

def pages_login_2(request):
    return render(request, 'pages-login-2.html')

def pages_register(request):
    return render(request, 'pages-register.html')

def pages_register_2(request):
    return render(request, 'pages-register-2.html')

def pages_logout(request):
    return render(request, 'pages-logout.html')

# Add views for other pages as needed
def pages_logout_2(request):
    return render(request, 'pages-logout-2.html')

def pages_recover_password(request):
    return render(request, 'pages-recoverpw.html')

def pages_recover_password_2(request):
    return render(request, 'pages-recoverpw-2.html')

def pages_lock_screen(request):
    return render(request, 'pages-lock-screen.html')

def pages_lock_screen_2(request):
    return render(request, 'pages-lock-screen-2.html')

def pages_confirm_mail(request):
    return render(request, 'pages-confirm-mail.html')

def pages_confirm_mail_2(request):
    return render(request, 'pages-confirm-mail-2.html')

def pages_starter(request):
    return render(request, 'pages-starter.html')

def pages_preloader(request):
    return render(request, 'pages-preloader.html')

def pages_timeline(request):
    return render(request, 'pages-timeline.html')

def pages_404(request):
    return render(request, 'pages-404.html')

def pages_404_alt(request):
    return render(request, 'pages-404-alt.html')

def pages_500(request):
    return render(request, 'pages-500.html')

def landing(request):
    return render(request, 'landing.html')


def layouts_horizontal(request):
    return render(request, 'layouts-horizontal.html')

def layouts_detached(request):
    return render(request, 'layouts-detached.html')

def layouts_full(request):
    return render(request, 'layouts-full.html')

def layouts_fullscreen(request):
    return render(request, 'layouts-fullscreen.html')

def layouts_hover(request):
    return render(request, 'layouts-hover.html')

def layouts_compact(request):
    return render(request, 'layouts-compact.html')

def layouts_icon_view(request):
    return render(request, 'layouts-icon-view.html')


def ui_accordions(request):
    return render(request, 'ui-accordions.html')

def ui_alerts(request):
    return render(request, 'ui-alerts.html')

def ui_avatars(request):
    return render(request, 'ui-avatars.html')

def ui_badges(request):
    return render(request, 'ui-badges.html')

def ui_breadcrumb(request):
    return render(request, 'ui-breadcrumb.html')

def ui_buttons(request):
    return render(request, 'ui-buttons.html')

def ui_cards(request):
    return render(request, 'ui-cards.html')

def ui_carousel(request):
    return render(request, 'ui-carousel.html')

def ui_dropdowns(request):
    return render(request, 'ui-dropdowns.html')

def ui_embed_video(request):
    return render(request, 'ui-embed-video.html')

def ui_grid(request):
    return render(request, 'ui-grid.html')

def ui_list_group(request):
    return render(request, 'ui-list-group.html')

def ui_modals(request):
    return render(request, 'ui-modals.html')

def ui_notifications(request):
    return render(request, 'ui-notifications.html')

def ui_offcanvas(request):
    return render(request, 'ui-offcanvas.html')

def ui_placeholders(request):
    return render(request, 'ui-placeholders.html')

def ui_pagination(request):
    return render(request, 'ui-pagination.html')

def ui_popovers(request):
    return render(request, 'ui-popovers.html')

def ui_progress(request):
    return render(request, 'ui-progress.html')

def ui_ribbons(request):
    return render(request, 'ui-ribbons.html')

def ui_spinners(request):
    return render(request, 'ui-spinners.html')

def ui_tabs(request):
    return render(request, 'ui-tabs.html')

def ui_tooltips(request):
    return render(request, 'ui-tooltips.html')

def ui_links(request):
    return render(request, 'ui-links.html')

def ui_typography(request):
    return render(request, 'ui-typography.html')

def ui_utilities(request):
    return render(request, 'ui-utilities.html')

# Extended UI Views
def extended_dragula(request):
    return render(request, 'extended-dragula.html')

def extended_range_slider(request):
    return render(request, 'extended-range-slider.html')

def extended_ratings(request):
    return render(request, 'extended-ratings.html')

def extended_scrollbar(request):
    return render(request, 'extended-scrollbar.html')

def extended_scrollspy(request):
    return render(request, 'extended-scrollspy.html')

def extended_treeview(request):
    return render(request, 'extended-treeview.html')


def widgets_view(request):
    return render(request, 'widgets.html')    


def icons_remixicons(request):
    return render(request, 'icons-remixicons.html')

def icons_mdi(request):
    return render(request, 'icons-mdi.html')

def icons_unicons(request):
    return render(request, 'icons-unicons.html')

# Charts Views
def charts_apex_area(request):
    return render(request, 'charts-apex-area.html')

def charts_apex_bar(request):
    return render(request, 'charts-apex-bar.html')

def charts_apex_bubble(request):
    return render(request, 'charts-apex-bubble.html')

def charts_apex_candlestick(request):
    return render(request, 'charts-apex-candlestick.html')

def charts_apex_column(request):
    return render(request, 'charts-apex-column.html')

def charts_apex_heatmap(request):
    return render(request, 'charts-apex-heatmap.html')

def charts_apex_line(request):
    return render(request, 'charts-apex-line.html')

def charts_apex_mixed(request):
    return render(request, 'charts-apex-mixed.html')

def charts_apex_timeline(request):
    return render(request, 'charts-apex-timeline.html')

def charts_apex_boxplot(request):
    return render(request, 'charts-apex-boxplot.html')

def charts_apex_treemap(request):
    return render(request, 'charts-apex-treemap.html')

def charts_apex_pie(request):
    return render(request, 'charts-apex-pie.html')

def charts_apex_radar(request):
    return render(request, 'charts-apex-radar.html')

def charts_apex_radialbar(request):
    return render(request, 'charts-apex-radialbar.html')

def charts_apex_scatter(request):
    return render(request, 'charts-apex-scatter.html')

def charts_apex_polar_area(request):
    return render(request, 'charts-apex-polar-area.html')

def charts_apex_sparklines(request):
    return render(request, 'charts-apex-sparklines.html')

def charts_chartjs_area(request):
    return render(request, 'charts-chartjs-area.html')

def charts_chartjs_bar(request):
    return render(request, 'charts-chartjs-bar.html')

def charts_chartjs_line(request):
    return render(request, 'charts-chartjs-line.html')

def charts_chartjs_other(request):
    return render(request, 'charts-chartjs-other.html')

def charts_brite(request):
    return render(request, 'charts-brite.html')

def charts_sparkline(request):
    return render(request, 'charts-sparkline.html')

# Forms Views
def form_elements(request):
    return render(request, 'form-elements.html')

def form_advanced(request):
    return render(request, 'form-advanced.html')

def form_validation(request):
    return render(request, 'form-validation.html')

def form_wizard(request):
    return render(request, 'form-wizard.html')

def form_fileuploads(request):
    return render(request, 'form-fileuploads.html')

def form_editors(request):
    return render(request, 'form-editors.html')

# Tables Views
def tables_basic(request):
    return render(request, 'tables-basic.html')

def tables_datatable(request):
    return render(request, 'tables-datatable.html')

# Maps Views
def maps_google(request):
    return render(request, 'maps-google.html')

def maps_vector(request):
    return render(request, 'maps-vector.html')


